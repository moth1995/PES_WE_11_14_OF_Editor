from .utils.constants import *
class Stadium:

    TOTAL = 0
    START_ADDRESS = 0
    MAX_LEN = 0
    SW_ADDR = 0
    END_ADDR = 0

    def __init__(self,option_file, idx):
        self.idx = idx
        self.of = option_file
        self.get_name()

    @property
    def offset(self):
        return self.START_ADDRESS + self.idx * self.MAX_LEN

    def get_name(self):
        self.name = self.of.data[self.offset : self.offset + self.MAX_LEN].partition(b"\0")[0].decode(UTF_8,"ignore")

    def set_name(self, new_name):
        if 0 < len(new_name) < self.MAX_LEN:
            new_name = new_name[: self.MAX_LEN]
            stadium_name_bytes = [0] * self.MAX_LEN
            new_name_bytes = str.encode(new_name, UTF_8, "ignore")
            stadium_name_bytes[: len(new_name_bytes)] = new_name_bytes
            for i, byte in enumerate(stadium_name_bytes):
                self.of.data[self.offset + i] = byte
            self.of.data[self.SW_ADDR+self.idx] = 1
            self.get_name()
            self.of.set_stadiums_names()
            return "Stadium name changed!"
        else:
            raise ValueError("Stadium name can't be empty or bigger than 60 characters")



