import struct

class FormationPlayer():
    def __init__(self, idx, of, address):
        self.idx = idx
        self.of = of
        self.address = address

    @property
    def x(self):
        return self.of[0]

    @property
    def y(self):
        return self.of[0]

    @property
    def role(self):
        return self.of[0]

    @property
    def defense(self):
        return self.of[0]

    @property
    def attack(self):
        return self.of[0]

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
        "Current",
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
        self.__strategy_idx = 0

    @property
    def start_address(self):    
        return self.team.formations_start_address

    @property    
    def address(self):
        return self.start_address + self.team.real_idx * self.size

    @property
    def coordinates_address(self):
        return self.address + 118 + self.strategy * self.alt_size

    @property
    def form_name(self):
        name = self.form_names[self.form_data.index(self.form_values)]
        return name


    @property
    def total(self):
        return self.team.total_nations + self.team.total_clubs

    @property
    def strategy(self):
        return self.__strategy_idx

    @strategy.setter
    def strategy(self, new_val:int):
        self.__strategy_idx = new_val
        
    @property
    def jobs(self):
        job_address = self.address + 111
        return struct.unpack("<%dB" % self.jobs_count, self.team.of.data[job_address: job_address + self.jobs_count])

    @jobs.setter
    def jobs(self, new_val:tuple):
        job_address = self.address + 111
        self.team.of.data[job_address: job_address + self.jobs_count] = struct.pack("<%dB" % self.jobs_count, *new_val)


    @property
    def form_values(self):
        val = struct.unpack(
            "<%dB"% self.form_data_len, 
            self.team.of.data[
                    self.coordinates_address
                :
                    self.coordinates_address + self.form_data_len
            ]
        )
        self.form_data[-1] = val
        return val

    @form_values.setter
    def form_values(self, new_val:tuple):
        self.team.of.data[
                self.coordinates_address 
            : 
                self.coordinates_address + self.form_data_len
        ] = struct.pack(
            "<%dB" % (self.form_data_len),
            *new_val,
        )
        self.form_data[-1] = new_val

    @property
    def roles(self):
        return [self.position_to_string(val) for val in self.form_values[(self.player_count -1) * 2 :]]



    def position_to_string(self, pos:int):
        if (pos <= 0):
            return "GK"
        elif (pos < 4 or (pos > 5 and pos < 8)):
            return "CB"
        elif (pos == 4):
            return "CWP"
        elif (pos == 5):
            return "CWP"
        elif (pos == 8):
            return "LB"
        elif (pos == 9):
            return "RB"
        elif (pos < 15):
            return "DMF"
        elif (pos == 15):
            return "LWB"
        elif (pos == 16):
            return "RWB"
        elif (pos < 22):
            return "CMF"
        elif (pos == 22):
            return "LMF"
        elif (pos == 23):
            return "RMF"
        elif (pos < 29):
            return "AMF"
        elif (pos == 29):
            return "LWF"
        elif (pos == 30):
            return "RWF"
        elif (pos < 36):
            return "SS"
        elif (pos < 41):
            return "CF"
        return "pos"
