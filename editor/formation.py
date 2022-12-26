import struct


class Formation():
    start_address = 0
    total = 0
    size = 364
    alt_size = 82

    jobs_count = 6
    settings_count = 4
    player_count = 11
    min_club_size = player_count + 5

    form_names = [
        "4-4-2",
        "4-3-1-2",
        "4-4-1-1",
        "4-2-1-3",
        "4-5-1",
        "4-1-2-3",
        "4-3-3",
        "4-3-2-1",
        "3-4-1-2",
        "3-3-2-2",
        "3-4-3",
        "5-4-1",
        "Default",
    ]

    form_data = [
        (
            9, 63, 9, 41, 12, 87, 12, 17, 26, 77, 26, 61, 26, 43, 26, 
            27, 43, 66, 43, 38, 0, 7, 1, 9, 8, 20, 21, 17, 18,40, 36,
        ),
        (
            9, 63, 9, 41, 12, 87, 12, 17, 18, 52, 26, 70, 26, 34, 34,
            52, 43, 66, 43, 38, 0, 7, 1, 9, 8, 12, 21, 17, 26,40, 36,
        ),
        (
            9, 63, 9, 41, 12, 87, 12, 17, 18, 61, 18, 43, 29, 80, 29, 
            24, 32, 52, 43, 52, 0, 7, 1, 9, 8, 14, 10, 23, 22,26, 38,
        ),
        (
            9, 63, 9, 41, 12, 87, 12, 17, 18, 61, 18, 43, 32, 52, 43, 
            72, 43, 32, 43, 52, 0, 7, 1, 9, 8, 14, 10, 26, 30,29, 38,
        ),
        (
            9, 63, 9, 41, 12, 87, 12, 17, 18, 52, 29, 61, 29, 43, 31, 
            80, 31, 24, 43, 52, 0, 7, 1, 9, 8, 12, 21, 17, 23,22, 38,
        ),
        (
            9, 63, 9, 41, 12, 87, 12, 17, 18, 52, 32, 70, 32, 34, 43, 
            72, 43, 32, 43, 52, 0, 7, 1, 9, 8, 12, 28, 24, 30,29, 38,
        ),
        (
            9, 63, 9, 41, 12, 87, 12, 17, 26, 77, 26, 52, 26, 27, 43, 
            72, 43, 32, 43, 52, 0, 7, 1, 9, 8, 21, 19, 17, 30,29, 38,
        ),
        (
            9, 63, 9, 41, 12, 87, 12, 17, 22, 77, 22, 52, 22, 27, 34, 
            70, 34, 34, 43, 52, 0, 7, 1, 9, 8, 21, 19, 17, 28,24, 38,
        ),
        (
            9, 72, 9, 52, 9, 32, 18, 61, 18, 43, 24, 80, 24, 24, 32, 
            52, 43, 66, 43, 38, 0, 7, 3, 1, 14, 10, 16, 15, 26,40, 36,
        ),
        (
            9, 72, 9, 52, 9, 32, 18, 52, 24, 80, 24, 24, 32, 61, 32, 
            43, 43, 66, 43, 38, 0, 7, 3, 1, 12, 16, 15, 28, 24,40, 36,
        ),
        (
            9, 72, 9, 52, 9, 32, 24, 80, 24, 24, 22, 61, 22, 43, 43, 
            72, 43, 32, 43, 52, 0, 7, 3, 1, 16, 15, 21, 17, 30,29, 38,
        ),
        (
            9, 72, 9, 52, 9, 32, 12, 87, 12, 17, 18, 61, 18, 43, 31, 
            80, 31, 24, 43, 52, 0, 7, 3, 1, 9, 8, 14, 10, 23,22, 38
        ),
        # this is for the default formation
        (
            
        ),
    ]
    
    form_data_len = (len(form_data[0]))

    def __init__(self, team):
        self.team = team
    
    @property    
    def address(self):
        return self.start_address + self.team.real_idx * self.size

    @property
    def start_address(self):    
        return self.team.formations_start_address
    
    @property
    def total(self):
        return self.team.total_nations + self.team.total_clubs

    @property
    def coordinates_address(self):
        return self.address + 118

    @property
    def form_values(self):
        val = struct.unpack("%dB"% self.form_data_len, self.team.of.data[self.coordinates_address: self.coordinates_address + self.form_data_len])
        self.form_data[-1] = val
        return val
    
    @property
    def form_name(self):
        name = self.form_names[self.form_data.index(self.form_values)]
        return name