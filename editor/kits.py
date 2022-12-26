from .kit import Kit

class Kits():
    start_address = 0
    size_nation = 0
    size_club = 0
    total = 0
    start_address_club = 0
    end_address = 0
    kit_data_size = 0

    def __init__(self, team):
        self.team = team
        self.__set_kit_collection()

    def __set_kit_collection(self):
        self.kits = [
            Kit(
                self.team.of.data[
                    self.address + self.kit_data_size * i  
                    : 
                    self.address + self.kit_data_size * i + self.kit_data_size
                ]
            )
            for i in range(4)
        ]

    def update_data(self):
        for i, kit in enumerate(self.kits):
            self.team.of.data[
                    self.address + self.kit_data_size * i  
                    : 
                    self.address + self.kit_data_size * i + self.kit_data_size
            ] = kit.data
        self.__set_kit_collection()


    @property
    def address(self):
        total_nat = self.team.total_nations + self.team.total_classic
        base = self.start_address if self.team.is_national_team else self.club_start_address
        idx = self.team.real_idx if self.team.is_national_team else self.team.real_idx - total_nat
        return base + idx * self.size 

    @property
    def club_start_address(self):
        return self.start_address + (self.team.total_nations + self.team.total_classic) * self.size_nation

    @property
    def size(self):
        return self.size_nation if self.team.is_national_team else self.size_club




