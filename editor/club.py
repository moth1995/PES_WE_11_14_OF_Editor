from .utils import rgb_to_hex
from .utils.constants import *

class Club:
    start_address = 0
    size = 0
    total = 0
    j_league_extra_teams = 0
    max_name_size = 48
    max_abbr_name_size = 0
    stadium_offset = 0
    flag_style_offset = 0
    color1_offset = 0
    emblem_offset = 0
    first_emblem = 0
    # open with GGS the flg file which contains all the flags, go the first club emblem 
    # to define the value that goes into this variable will be club emblem -1 or quantity of nations + the difference
    first_club_emblem = 0
    supp_color_offset = max_name_size + max_abbr_name_size + 26

    def __init__(self, option_file, idx:int):
        self.option_file = option_file
        self.idx = idx
        
        self.set_addresses()
        self.set_name()
        self.set_abbr()
        self.set_stadium()
        self.set_emblem()
        self.set_color1()
        self.set_color2()
        self.set_flag()
        self.set_supp_color()

    def set_addresses(self):
        """
        Set the following club addresses:

        - Name
        """
        self.name_address = self.start_address + (self.idx * self.size)
        self.abbr_address = self.start_address + (self.idx * self.size) + self.max_name_size + 1
        self.name_edited_addr = self.name_address + 62
        self.stadium_address = self.start_address + (self.idx * self.size) + self.stadium_offset
        self.stadium_edited = self.stadium_offset + 2
        self.flag_address = self.start_address + (self.idx * self.size) + self.flag_style_offset
        self.color1_address = self.start_address + (self.idx * self.size) + self.color1_offset
        self.color2_address = self.start_address + (self.idx * self.size) + self.color1_offset + 4
        self.emblem_address = self.start_address + (self.idx * self.size) + self.emblem_offset
        self.emblem_edited_addr = self.emblem_address + 8
        self.supp_color_address = self.start_address + (self.idx * self.size) + self.supp_color_offset
        self.supp_c_edited_address = self.supp_color_address + 2

    def set_name(self):
        """
        Set club name from relevant OF data bytes.
        """
        name_byte_array = self.option_file.data[
            self.name_address : self.name_address + (self.max_name_size + 1)
        ]
        try:
            self.name = name_byte_array.partition(b"\0")[0].decode(UTF_8)
        except:
            self.name = f"<Encoding Error Team {self.idx + 64}>"

    def set_abbr(self):
        """
        Set club name from relevant OF data bytes.
        """
        abbr_byte_array = self.option_file.data[
            self.abbr_address : self.abbr_address + (self.max_abbr_name_size + 1)
        ]
        try:
            self.abbr = abbr_byte_array.partition(b"\0")[0].decode(UTF_8)
        except:
            self.abbr = f"<Encoding Error Team {self.idx + 64}>"

    def set_stadium(self):
        self.stadium = self.option_file.data[self.stadium_address]

    def set_flag(self):
        self.flag_style = self.option_file.data[self.flag_address]

    def set_emblem(self):
        self.emblem = int.from_bytes(self.option_file.data[self.emblem_address : self.emblem_address + 4], byteorder='little')

    def set_color1(self):
        self.color1 = rgb_to_hex([self.option_file.data[self.color1_address + i] for i in range(3)])

    def set_color2(self):
        self.color2 = rgb_to_hex([self.option_file.data[self.color2_address + i] for i in range(3)])

    def set_supp_color(self):
        supp_color = self.option_file.data[self.supp_color_address]
        self.supp_color_c1 = (supp_color & 0xf)
        self.supp_color_c2 = (supp_color >> 4)


    def update_name(self, name:str):
        """
        Update club name with the supplied value.
        """
        new_name = name[: self.max_name_size]

        club_name_bytes = [0] * (self.max_name_size + 1)
        new_name_bytes = str.encode(new_name,"utf-8")
        club_name_bytes[: len(new_name_bytes)] = new_name_bytes

        for i, byte in enumerate(club_name_bytes):
            self.option_file.data[self.name_address + i] = byte
        self.option_file.data[self.name_edited_addr] = 1
        self.set_name()
        self.option_file.set_clubs_names()

    def update_abbr(self, abbr:str):
        """
        Update club name with the supplied value.
        """
        new_abbr = abbr[: self.max_abbr_name_size]

        club_abbr_bytes = [0] * (self.max_abbr_name_size + 1)
        new_abbr_bytes = str.encode(new_abbr, UTF_8)
        club_abbr_bytes[: len(new_abbr_bytes)] = new_abbr_bytes

        for i, byte in enumerate(club_abbr_bytes):
            self.option_file.data[self.abbr_address + i] = byte

        self.set_abbr()

    def update_stadium(self, new_stadium:int):
        self.option_file.data[self.stadium_address] = new_stadium
        self.option_file.data[self.stadium_edited] = 1
        self.set_stadium()

    def update_flag(self, new_flag_style:int):
        self.option_file.data[self.flag_address] = new_flag_style
        self.set_flag

    def update_emblem(self, new_emblem:int):
        self.option_file.data[self.emblem_address] = new_emblem.to_bytes(4,"little")
        self.option_file.data[self.emblem_address + 4] = new_emblem.to_bytes(4,"little")
        # Flag to say that we edited this emblem
        self.option_file.data[self.emblem_edited_addr] = 1
        self.option_file.data[self.emblem_edited_addr + 1] = 1
        self.set_emblem()

    def update_color1(self,new_c1):
        for i in range(len(new_c1)):
            self.option_file.data[self.color1_address + i] = new_c1[i]
        self.set_color1()

    def update_color2(self,new_c2):
        for i in range(len(new_c2)):
            self.option_file.data[self.color2_address + i] = new_c2[i]
        self.set_color2()

    def update_supp_color(self, new_supp_c1, new_supp_c2):
        new_supp_color = (new_supp_c2 <<4) | new_supp_c1
        self.option_file.data[self.supp_color_address] = new_supp_color
        self.option_file.data[self.supp_c_edited_address] = 1
        self.set_supp_color()