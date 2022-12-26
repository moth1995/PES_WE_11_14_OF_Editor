import struct

from .kits import Kits
from .formation import Formation
from .player import Player


class Team:
    total_nations = 0
    total_classic = 0
    total_clubs = 0
    total_j_nations = 0
    total_j_clubs = 0
    total_players_in_nations = 23
    total_players_in_clubs = 32
    min_players = 16
    dorsal_start_address = 0
    separator_size = 0 # from pes 11 to pes 14 there was found a separator of size 1 between dorsals data and relink ids data
    total_ml_slots = 3
    
    def __init__(self, option_file, idx):
        self.of = option_file
        self.idx = idx
        self.get_dorsals_from_bytes()
        self.get_team_from_bytes()
        self.set_formation()
        self.set_kits()

    @classmethod
    def total_slots_cm(cls):
        return cls.total_nations  + cls.total_classic + cls.total_j_nations + int(Player.total_edit/cls.total_players_in_nations) + cls.total_clubs + cls.total_j_clubs + cls.total_ml_slots + int(Player.total_shop/cls.total_players_in_clubs)


    @property
    def is_national_team(self):
        return self.idx < self.total_national_slots

    @property
    def is_club(self):
        return self.real_idx < self.total_nations and self.real_idx is not None


    @property
    def total_national_slots(self):
        return self.total_nations  + self.total_classic + self.total_extra_nat_slot

    @property
    def total_extra_nat_slot(self):
        return self.total_j_nations + self.total_edit_teams
    
    @property
    def total_club_slots(self):
        return self.total_national_slots + self.total_clubs + self.total_extra_club_slot
    
    @property
    def total_extra_club_slot(self):
        return self.total_j_clubs + self.total_shop_teams + self.total_ml_slots
    
    @property
    def first_club_slot(self):
        return (self.total_nations + self.total_classic + self.total_j_nations) * self.total_players_in_nations + Player.total_edit

    @property
    def total_slots(self):
        return (self.total_clubs + self.total_j_clubs + self.total_ml_slots) * self.total_players_in_clubs + Player.total_shop

    @property
    def total_edit_teams(self):
        return int(Player.total_edit/self.total_players_in_nations)

    @property
    def total_shop_teams(self):
        return int(Player.total_shop/self.total_players_in_clubs)

    @property
    def real_idx(self):
        if self.idx < self.total_nations + self.total_classic:
            return self.idx
        elif self.idx < self.total_national_slots + self.total_clubs and not self.is_national_team:
            return self.idx - self.total_extra_nat_slot
        else:
            return None

    @property
    def max_players(self):
        return self.total_players_in_nations if self.is_national_team else self.total_players_in_clubs 


    ### for dorsals numbers in team

    @property
    def dorsal_address(self):
        return self.__national_dorsal_address() if self.is_national_team else self.__club_dorsal_address()

    @property
    def dorsal_size(self):
        return self.total_players_in_nations if self.is_national_team else self.total_players_in_clubs 

    def __national_dorsal_address(self):
        return self.dorsal_start_address + self.idx * self.dorsal_size
    
    def __club_dorsal_address(self):
        alt_idx = self.idx - (self.total_nations + self.total_classic + self.total_j_nations + self.total_edit_teams)
        return self.dorsal_start_address + self.first_club_slot + alt_idx * self.dorsal_size

    def get_dorsals_from_bytes(self):
        raw_values = struct.unpack("%dB" % self.max_players, self.of.data[self.dorsal_address : self.dorsal_address + self.dorsal_size])
        self.__dorsals = [dorsal + 1 if dorsal != 0xff else None for dorsal in raw_values]
        
    @property
    def dorsals(self):
        return self.__dorsals
    
    @dorsals.setter
    def dorsals(self, dorsals:list):
        # first we need to send all the none to the end but keeping the order
        
        dorsals = sorted(dorsals, key = lambda x: x is None)

        new_dorsals = [dorsal - 1 if dorsal is not None else 0xff for dorsal in dorsals]
        new_dorsals_bytes = struct.pack("%dB" % self.max_players, *new_dorsals)
        self.of.data[self.dorsal_address : self.dorsal_address + self.dorsal_size] = new_dorsals_bytes
        self.__dorsals = dorsals

    def set_random_dorsal(self, idx:int):
        self.dorsals[idx] = [x for x in range(1, 100) if x not in self.dorsals].__getitem__(0)

    ### for players registers in team

    @property
    def squad_start_address(self):
        return self.dorsal_start_address + self.first_club_slot + self.total_slots + self.separator_size

    @property
    def address(self):
        return self.__team_national_address() if self.is_national_team else self.__team_club_address()

    @property
    def team_size(self):
        return self.total_players_in_nations * 2 if self.is_national_team else self.total_players_in_clubs * 2

    def __team_national_address(self):
        return self.squad_start_address + self.idx * self.team_size 
    
    def __team_club_address(self):
        alt_idx = self.idx - (self.total_nations + self.total_classic + self.total_j_nations + self.total_edit_teams)
        return self.squad_start_address + self.first_club_slot * 2 + alt_idx * self.team_size


    def get_team_from_bytes(self):
        raw_values = struct.unpack("%dH" % self.max_players, self.of.data[self.address : self.address + self.team_size])
        self.__players = [self.of.get_player_by_idx(player_idx) if player_idx != 0x0000 else None for player_idx in raw_values]
        
    @property
    def players(self):
        return self.__players
    
    @players.setter
    def players(self, players:'list[Player]'):        
        if (
            (self.min_players > sum(x is not None for x in players)) and self.real_idx is not None
        ):
            raise Exception(f"You can't have less than {self.min_players} players in your team")

        # first we need to send all the none to the end but keeping the order
        
        players = sorted(players, key = lambda x: x is None)
        
        new_players_ids = [player.idx if player is not None else 0x0000 for player in players]
        new_new_players_ids_bytes = struct.pack("%dH" % self.max_players, *new_players_ids)
        self.of.data[self.address : self.address + self.team_size] = new_new_players_ids_bytes
        self.__players = players

    @property
    def total_available_slots(self):
        return sum(x is None for x in self.players)

    @property
    def current_players_in_team(self):
        return sum(x is not None for x in self.players)


    @property
    def formations_start_address(self):
        return self.squad_start_address + self.first_club_slot * 2 + self.total_slots * 2
    
    def set_formation(self):
        self.formation = Formation(self) if self.real_idx is not None else None

    def set_kits(self):
        self.kits = Kits(self) if self.real_idx is not None else None
