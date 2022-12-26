from .utils.constants import *

class League:

    TOTAL = 0
    BASE_NAME_LEN = 20
    START_ADDRESS = 0
    MAX_LEN = 61
    SIZE = BASE_NAME_LEN + 1 + MAX_LEN + 2;

    def __init__(self,option_file, idx):
        self.idx = idx
        self.of = option_file
        self.get_name()

    @property
    def offset(self):
        return self.START_ADDRESS + self.idx * self.SIZE


    def get_name(self):
        self.name = self.of.data[self.offset + self.BASE_NAME_LEN + 1: self.offset + self.BASE_NAME_LEN + 1 + self.MAX_LEN].partition(b"\0")[0].decode(UTF_8,"ignore")

    def set_name(self, new_name):
        if 0 < len(new_name) < self.MAX_LEN:
            new_name = new_name[: self.MAX_LEN]
            league_name_bytes = [0] * self.MAX_LEN
            new_name_bytes = str.encode(new_name, UTF_8,"ignore")
            league_name_bytes[: len(new_name_bytes)] = new_name_bytes
            for i, byte in enumerate(league_name_bytes):
                self.of.data[self.offset + self.BASE_NAME_LEN + 1 + i] = byte
            self.get_name()
            self.of.set_leagues_names()
            return "League name changed!"
        else:
            raise ValueError("League name can't be empty or bigger than 60 characters")