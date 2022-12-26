import itertools
import os
import subprocess
from pathlib import Path
from enum import Enum, auto

from editor.pes_stat import Stat

from .utils.constants import *

from .option_file_data import (
    OF_BYTE_LENGTH,
    OF_BLOCK,
    OF_BLOCK_SIZE,
    OF_KEY,
)

from .club import Club
from .logo import Logo
from .player import Player
from .leagues import League
from .stadiums import Stadium
from .shop import Shop
from .teams import Team
from .images import PNG
from .kits import Kits

from .utils.common_functions import bytes_to_int, zero_fill_right_shift, resource_path


class OptionFile:
    #of_byte_length = OF_BYTE_LENGTH
    #of_block = OF_BLOCK
    #of_block_size = OF_BLOCK_SIZE
    of_key = OF_KEY

    def __init__(self, file_location, config):
        self.file_location = file_location
        self.data = bytearray()
        self.file_name = ""
        self.extension = ""
        self.header_data = bytearray()
        self.config = config
        self.encrypted = self.config['option_file_data']['ENCRYPTED']
        self.of_byte_length = self.config['option_file_data']['OF_BYTE_LENGTH']
        self.of_block = self.config['option_file_data']['OF_BLOCK']
        self.of_block_size = self.config['option_file_data']['OF_BLOCK_SIZE']
        self.nations = self.config['NATIONS']
        self.read_option_file()
        Player.start_address = self.config['option_file_data']['OF_BLOCK'][4]
        Player.start_address_edited = self.config['option_file_data']['OF_BLOCK'][3]
        Player.total_edit = int(self.config['option_file_data']['OF_BLOCK_SIZE'][3] / Player.size)
        Player.total_players = int(self.config['option_file_data']['OF_BLOCK_SIZE'][4] / Player.size)
        # To avoid a possible crash in case it is set to 0 we will load the total of players as first unused until is loaded properly
        Player.first_unused = self.config['Player']['First Unused'] if self.config['Player']['First Unused'] else Player.total_players

        Player.first_ml_old = Player.first_unused - Player.total_ml_old
        Player.first_ml_youth = Player.first_ml_old - Player.total_ml_youth
        Player.first_shop = Player.first_ml_youth - Player.total_shop
        Player.first_ml_default = Player.first_shop - Player.total_ml_default

        Club.start_address = self.config['option_file_data']['OF_BLOCK'][6]
        Club.size = self.config['Club']['Size']
        Club.total = int(self.config['option_file_data']['OF_BLOCK_SIZE'][6] / Club.size)
        #print(Club.total)
        Club.max_abbr_name_size = self.config['Club']['Max Abbr Name Size']
        Club.first_emblem = self.config['Club']['First Emblem']
        Club.first_club_emblem = self.config['Club']['First Club Emblem']
        Club.stadium_offset = Club.size - 7
        Club.color1_offset = Club.size - 16
        Club.emblem_offset = Club.size - 28
        Club.flag_style_offset = Club.size - 18
        Club.supp_color_offset = Club.size - 8
        Stadium.TOTAL = self.config['Stadiums']['Total']
        Stadium.MAX_LEN = self.config['Stadiums']['Max Lenght']
        Stadium.START_ADDRESS = self.config['option_file_data']['OF_BLOCK'][2]
        Stadium.SW_ADDR = Stadium.START_ADDRESS + (Stadium.MAX_LEN * Stadium.TOTAL)
        Stadium.END_ADDR = Stadium.SW_ADDR + Stadium.TOTAL
        League.TOTAL = self.config['Leagues']['Total']
        League.START_ADDRESS = Stadium.END_ADDR + Stadium.MAX_LEN + 1
        Team.total_nations = self.config['Teams']['Total Nations']
        Team.total_classic = self.config['Teams']['Total Classic']
        Team.total_clubs = Club.total
        Team.total_j_nations = self.config['Teams']['Total J Nations']
        Team.total_j_clubs = self.config['Teams']['Total J Clubs']
        Team.total_players_in_nations = self.config['Teams']['Max Players In Nations']
        Team.total_players_in_clubs = self.config['Teams']['Max Players In Clubs']
        Team.separator_size = self.config['Teams']['Separator Size']
        Team.dorsal_start_address = self.config['option_file_data']['OF_BLOCK'][5]
        Player.first_classic_player = Team.total_players_in_nations * (Team.total_nations - Team.total_classic) + 1
        Player.last_classic_player = Player.first_classic_player + Team.total_players_in_nations * (Team.total_classic)
        Kits.start_address = self.config['option_file_data']['OF_BLOCK'][7]
        Kits.size_nation = self.config['Kits']['Nation Kit Data Size']
        Kits.size_club = self.config['Kits']['Club Kit Data Size']
        Kits.kit_data_size = self.config["Kits"]["Kit Data Size"]
        Kits.total = Club.total + Team.total_nations + Team.total_classic
        Kits.start_address_club = Kits.start_address + ((Kits.total - Club.total) * Kits.size_nation)
        Kits.end_address = Kits.start_address_club + (Club.total) * Kits.size_club
        Stat.growth_types_early = self.config["GROWTH TYPES"]["EARLY"]
        Stat.growth_types_early_lasting = self.config["GROWTH TYPES"]["EARLY LASTING"]
        Stat.growth_types_standard = self.config["GROWTH TYPES"]["STANDARD"]
        Stat.growth_types_standard_lasting = self.config["GROWTH TYPES"]["STANDARD LASTING"]
        Stat.growth_types_late = self.config["GROWTH TYPES"]["LATE"]
        Stat.growth_types_late_lasting = self.config["GROWTH TYPES"]["LATE LASTING"]

        #print(Kits.end_address)
        #print(Team.total_teams_slots())
        
        Logo.start_address = Kits.end_address
        Shop.HAS_BG = self.config['Shop']['Has Background Selector']
        Shop.TOTAL_BGS = self.config['Shop']['Total Backgrounds']
        Shop.POINTS_OFFSET_2 = self.config['Shop']['Points Offset']

        import time
        start_time = time.time()

        self.set_clubs()
        self.set_clubs_names()
        self.set_logos()
        self.set_players()
        self.set_players_names()
        self.set_edited_players()
        self.set_edited_players_names()
        self.set_teams()
        self.set_leagues()
        self.set_leagues_names()
        self.set_stadiums()
        self.set_stadiums_names()
        self.set_shop()
        self.set_free_agents()
        #print("--- %s seconds ---" % (time.time() - start_time))


    @property
    def teams_names(self):       
        if Team.total_classic == 0:
            classic_teams_names = []
        else:
            classic_teams_names = self.config['CLASSIC TEAMS']


        japan_n_team_names = ["<Japan National %d>" % (i + 1) for i in range(Team.total_j_nations)]
        japan_c_team_names = ["<Japan Club %d>" % (i + 1) for i in range(Team.total_j_clubs)]
        

        return self.nations[:Team.total_nations] + classic_teams_names + japan_n_team_names + EDITED_TEAM_NAMES + self.clubs_names + japan_c_team_names + ML_TEAM_NAME + SHOP_TEAM_NAMES + ML_TEAM_NAMES_EXTRAS

    def set_teams(self):
        self.teams = [Team(self, i) for i in range(Team.total_slots_cm())]
        

    def set_free_agents(self):
        first_club = Team.total_nations + Team.total_j_nations + Team.total_classic + int(Player.total_edit / Team.total_players_in_nations)
        last_club = first_club + Club.total

        for i, team in enumerate(self.teams):
            if team.is_national_team:
                for j, player in enumerate(team.players):
                    if player is not None:
                        player.free_agent = True
                    if player is not None and player.national_id is None and player.national_dorsal is None:
                        player.national_id = i
                        player.national_dorsal = team.dorsals[j]
            elif first_club <= team.idx < last_club :
                for j, player in enumerate(team.players):
                    if player is not None:
                        player.free_agent = False
                        player.club_id = i
                        player.club_dorsal = team.dorsals[j]
            else:
                for j, player in enumerate(team.players):
                    if player is not None:
                        player.free_agent = True
                    if player is not None and player.club_id is None and player.club_dorsal is None:
                        player.club_id = i
                        player.club_dorsal = team.dorsals[j]


    def read_option_file(self):
        """
        Decrypt supplied file and set OF data.
        """
        of_file = open(self.file_location, "rb")
        file_name = Path(of_file.name).stem
        extension = Path(of_file.name).suffix
        folder = Path(of_file.name).resolve().parents[0]
        file_size = os.stat(of_file.name).st_size
        self.file_name = file_name
        self.extension = extension
        self.folder = folder
        file_contents = bytearray(of_file.read())
        of_file.close()
        

        if self.extension == ".psu":
            self.header_data, self.data = file_contents[:file_size - self.of_byte_length], file_contents[file_size - self.of_byte_length:]
            game_identifier = self.header_data[64:64+19].decode('utf-8')

        elif self.extension == ".xps":
            self.header_data, self.data = file_contents[:file_size - self.of_byte_length -4], file_contents[file_size - self.of_byte_length-4:-4]
            #game_identifier = self.header_data[79:79+19].decode('utf-8')
            game_identifier = self.config['option_file_data']['Game Identifier'] # xps support but without gameid checking
        else:
            self.data = file_contents
            game_identifier = file_name
        if game_identifier != self.config['option_file_data']['Game Identifier'] and self.extension ==".psu":
            #print("game_identifier: %s"%game_identifier)
            #print("self.config: %s"%self.config['option_file_data']['Game Identifier'])
            raise ValueError("Invalid option file version")

        if self.of_byte_length != len(self.data):
            raise ValueError("Invalid option file, size doesn't match!")
        if self.encrypted:
            self.decrypt()

        return True

    def save_option_file(self, file_location=None):
        """
        Save OF data to supplied file.
        """
        file_location = self.file_location = file_location or self.file_location

        #self.data[49] = 1
        #self.data[50] = 1
        #self.data[5938] = 1
        #self.data[5939] = 1
        if self.encrypted:
            self.encrypt()
            self.checksums()

        of_file = open(file_location, "wb")

        if self.extension == ".psu":
            of_file.write(self.header_data)
            of_file.write(self.data)
        elif self.extension == ".xps":
            of_file.write(self.header_data)
            of_file.write(self.data)
            of_file.write(bytearray(4))
        else:
            of_file.write(self.data)
        
        of_file.close()

        self.decrypt()
        return True

    def decrypt(self):
        """
        Decrypt OF.
        """
        for i in range(1, len(self.of_block)):
            k = 0
            a = self.of_block[i]
            while True:
                if a + 4 > self.of_block[i] + self.of_block_size[i]:
                    break

                c = bytes_to_int(self.data, a)
                p = ((c - self.of_key[k]) + self.of_key[-1]) ^ self.of_key[-1]

                self.data[a] = p & 0x000000FF
                self.data[a + 1] = zero_fill_right_shift(p, 8) & 0x000000FF
                self.data[a + 2] = zero_fill_right_shift(p, 16) & 0x000000FF
                self.data[a + 3] = zero_fill_right_shift(p, 24) & 0x000000FF

                k += 1
                if k == len(self.of_key):
                    k = 0

                a += 4

    def encrypt(self):
        """
        Encrypt OF.
        """
        for i in range(1, len(self.of_block)):
            k = 0
            a = self.of_block[i]
            while True:
                if a + 4 > self.of_block[i] + self.of_block_size[i]:
                    break

                p = bytes_to_int(self.data, a)
                c = self.of_key[k] + ((p ^ self.of_key[-1]) - self.of_key[-1])

                self.data[a] = c & 0x000000FF
                self.data[a + 1] = zero_fill_right_shift(c, 8) & 0x000000FF
                self.data[a + 2] = zero_fill_right_shift(c, 16) & 0x000000FF
                self.data[a + 3] = zero_fill_right_shift(c, 24) & 0x000000FF

                k += 1
                if k == len(self.of_key):
                    k = 0

                a += 4

    def checksums(self):
        """
        Set checksums.
        """
        for i in range(0, len(self.of_block)):
            checksum = 0

            for a in range(
                self.of_block[i], self.of_block[i] + self.of_block_size[i], 4
            ):
                checksum += bytes_to_int(self.data, a)

            self.data[self.of_block[i] - 8] = checksum & 0x000000FF
            self.data[self.of_block[i] - 7] = (
                zero_fill_right_shift(checksum, 8) & 0x000000FF
            )
            self.data[self.of_block[i] - 6] = (
                zero_fill_right_shift(checksum, 16) & 0x000000FF
            )
            self.data[self.of_block[i] - 5] = (
                zero_fill_right_shift(checksum, 24) & 0x000000FF
            )

    def set_clubs(self):
        """
        Load all clubs from OF data and add to clubs list.
        """
        self.clubs = [Club(self, i) for i in range(Club.total)]
        #for i in range(Club.total):
            #club = Club(self, i)
            #self.clubs.append(club)

    def set_clubs_names(self):
        self.clubs_names = [club.name for club in self.clubs]

    def set_logos(self):
        """
        Load all logos from OF data and add to logos list.
        """
        self.logos = [Logo(self, i) for i in range(Logo.total)]
        self.logos_png = [PNG(logo) for logo in self.logos]
        self.logos_tk = [png.png_bytes_to_tk_img() for png in self.logos_png]
        """
        for i in range(Logo.total):
            logo = Logo(self, i)
            self.logos.append(logo)
            png = PNG(logo)
            self.logos_png.append(png)
            img_tk = png.png_bytes_to_tk_img()
            self.logos_tk.append(img_tk)
        """
    def set_players(self):
        """
        Load all players from OF data and add to players list.
        """
        self.players = [Player(self, i) for i in range(int(self.of_block_size[4] / 124))]

    def set_players_names(self):
        self.players_names = [player.name for player in self.players]

    def set_edited_players(self):
        """
        Load all edited players from OF data and add to edited players list.
        """
        self.edited_players = [Player(self, i) for i in range(Player.first_edited_id, Player.first_edited_id + Player.total_edit)]

    def set_edited_players_names(self):
        self.edited_players_names = [edited_player.name for edited_player in self.edited_players]

    def get_player_by_name(self, name:str):
        return self.players[self.players_names.index(name)] if name in self.players_names else self.edited_players[self.edited_players_names.index(name)]

    def get_player_by_idx(self, idx:int):
        return self.players[idx] if idx < Player.first_edited_id else self.edited_players[idx - Player.first_edited_id]

    def set_leagues(self):
        """
        Load all leagues from OF data and add to leagues list.
        """
        self.leagues = [League(self, i) for i in range(League.TOTAL)]

    def set_leagues_names(self):
        self.leagues_names = [league.name for league in self.leagues]

    def set_stadiums(self):
        """
        Load all leagues from OF data and add to leagues list.
        """
        self.stadiums = [Stadium(self, i) for i in range(Stadium.TOTAL)]

    def set_stadiums_names(self):
        self.stadiums_names = [stadium.name for stadium in self.stadiums]

    def set_shop(self):
        """
        Load Shop info and methods
        """
        self.shop = Shop(self)

