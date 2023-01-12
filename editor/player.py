from .edited_flags import EditedFlags
from .appearance import Appearance
from .special_abilities import SpecialAbilities
from .abilities import Abilities, Abilities_1_8
from .positions import Position
from .basic_settings import BasicSettings
from .pes_stat import Stat
from .utils.constants import *

class Player:
    start_address = 0
    start_address_edited = 0
    size = 124
    name_encoding = UTF_16_LE
    shirt_encoding = UTF_8
    max_name_size = 16
    name_bytes_length = 32
    shirt_name_bytes_length = 16
    
    total_players = 0
    total_ml_default = 28
    total_shop = 160
    total_ml_youth = 140
    total_ml_old = 10
    total_edit = 0

    first_classic_player = 0
    last_classic_player = 0
    first_ml_default = 0
    first_shop = 0
    first_ml_youth = 0
    first_ml_old = 0
    first_unused = 0
    first_edited_id = 32768
    
    free_agent = True
    national_id = None
    club_id = None
    national_dorsal = None
    club_dorsal = None


    def __init__(self,option_file, idx):
        self.idx = idx
        self.of = option_file
        self.set_name_from_bytes()
        self.set_shirt_name_from_bytes()
        self.callname = Stat(self, 1, 0, 0xffff, "Callname")
        self.nation = Stat(self, 65, 0, 127, "Nationality", 1)

    def init_stats(self):
        self.basic_settings = BasicSettings(self)
        self.position = Position(self)
        self.appearance = Appearance(self)
        self.abilities = Abilities(self)
        self.abilities_1_8 = Abilities_1_8(self)
        self.special_abilities = SpecialAbilities(self)
        self.edited_flags = EditedFlags(self)

    @property
    def club_team_name(self):
        return "Free Agent" if self.club_id is None else self.of.teams_names[self.club_id] 

    @property
    def national_team_name(self):
        return "Not Registered" if self.national_id is None else self.of.teams_names[self.national_id]

    @property
    def is_edit(self):
        """
        Return true if the player is an edit player.
        A player is deemed an edit player if its index number is greater than
        or equal to the first edit address.
        """
        return self.idx >= self.first_edited_id

    @property
    def is_unused(self):
        """
        Return true if the player is an unused player.
        A player is deemed an unused player if its index number is greater than
        or equal to the first unused address.
        """
        return self.idx >= self.first_unused


    @property
    def offset(self):
        """
        Return player offset.
        """
        return (
            self.idx * self.size
            if not self.is_edit
            else (self.idx - self.first_edited_id) * self.size
        )

    @property
    def address(self):
        """
        Return player address.
        """
        return (
            self.start_address + self.offset
            if not self.is_edit
            else self.start_address_edited + self.offset
        )


    def set_name_from_bytes(self):
        """
        Set player name from relevant OF data bytes.
        """
        name = "???"
        if (
            self.idx > 0
            and (self.idx <= self.total_players or self.idx >= self.first_edited_id)
            and self.idx < self.first_edited_id + self.total_edit
        ):
            all_name_bytes = self.of.data[self.address : self.address + self.name_bytes_length]
            try:
                name = all_name_bytes.decode(encoding=self.name_encoding,errors="replace").encode(encoding=self.shirt_encoding, errors="replace").partition(b"\0")[0].decode(encoding=self.shirt_encoding, errors="replace")
            except:
                name = f"Error (ID: {self.idx})"

            if not name:
                no_name_prefixes = {
                    self.first_edited_id: "Edited",
                    self.first_unused: "Unused",
                    1: "Unknown",
                }

                for address, address_prefix in no_name_prefixes.items():
                    if self.idx >= address:
                        prefix = address_prefix
                        break

                name = f"{prefix} ({self.idx})"

        self.__name = name

    @property
    def name(self):
        """
        Return player name.
        """
        return self.__name

    @name.setter
    def name(self, name):
        """
        Update player name with the supplied value.
        """
        new_name = name[: self.max_name_size]
        if (new_name == "Unknown (" + str(self.idx) + ")" 
            or new_name == "Edited (" + str(self.idx) + ")"
            or new_name == "Unused (" + str(self.idx) + ")" 
            or new_name == "Error (" + str(self.idx) + ")" 
            or new_name == ""):
            player_name_bytes=[0] * self.name_bytes_length
        else:
            player_name_bytes = [0] * self.name_bytes_length
            new_name_bytes = str.encode(new_name, self.name_encoding, errors="replace")
            player_name_bytes[: len(new_name_bytes)] = new_name_bytes

        for i, byte in enumerate(player_name_bytes):
            self.of.data[self.address + i] = byte

        self.__name = new_name

    def set_shirt_name_from_bytes(self):
        """
        Set player shirt name from relevant OF data bytes.
        """
        shirt_name_address = self.address + 32
        name_byte_array = self.of.data[
            shirt_name_address : shirt_name_address
            + self.shirt_name_bytes_length
        ]

        self.__shirt_name = name_byte_array.partition(b"\0")[0].decode(encoding=self.shirt_encoding, errors="replace")

    @property
    def shirt_name(self):
        """
        Return player shirt name.
        """
        return self.__shirt_name

    @shirt_name.setter
    def shirt_name(self, shirt_name:str):
        shirt_name_address = self.address + 32
        new_name = shirt_name[: self.max_name_size].upper()

        player_shirt_name_bytes = [0] * self.shirt_name_bytes_length
        new_name_bytes = str.encode(new_name, encoding=self.shirt_encoding, errors="replace")
        player_shirt_name_bytes[: len(new_name_bytes)] = new_name_bytes

        for i, byte in enumerate(player_shirt_name_bytes):
            self.of.data[shirt_name_address + i] = byte

        self.__shirt_name = new_name


