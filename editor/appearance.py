from editor.utils.constants import BODY_TYPES, BODY_TYPES_VALUES
from .pes_stat import Stat

class Appearance:
    def __init__(self, player):
        # Player appearence settings
        # Head
        
        # Face menu
        self.face = Stat(player, 55, 0, 3, "Face", 5)
        """
        if self.face_type == 0:
            self.face_type = "BUILD"
        elif self.face_type == 1:
            self.face_type = "PRESET SPECIAL"
        elif self.face_type == 2:
            self.face_type = "PRESET NORMAL"
        else:
            self.face_type = "ERROR"
        """
        self.skin_colour = Stat(player, 68, 0, 0x7, "Skin Colour", "{stat} + 1 if {normalize} else {stat} - 1", 1, 6)# + 1
        self.head_height = Stat(player, 43, 4, 15, "Head height", "{stat} - 7 if {normalize} else {stat} + 7", -7, 7)# - 7
        self.head_width = Stat(player, 44, 0, 15, "Head width", "{stat} - 7 if {normalize} else {stat} + 7", -7, 7)# - 7
        self.face_idx = Stat(player, 53, 4, 4095, "Face ID", "{stat} + 1 if {normalize} else {stat} - 1", 1, 4096)# + 1
        #self.head_ov_pos = Stat(player, 124-48,5, 7, "Head overall position") - 3
        
        # Brows menu
        #self.brows_type = Stat(player, 119-48, 5, 31, "Brows type") + 1
        #self.brows_angle = (Stat(player, 119-48, 2, 7, "Brown angle") - 3)*-1
        #self.brows_height = (Stat(player, 118-48, 4, 7, "Brown height") - 3)*-1
        #self.brows_spacing = (Stat(player, 118-48, 7, 7, "Brown spacing") - 3)*-1
        
        # Eyes menu
        #self.eyes_type = Stat(player, 116-48, 3, 31, "Eyes type") + 1
        #self.eyes_position = (Stat(player, 117-48, 0, 7, "Eye Position")-3)*-1
        #self.eyes_angle = (Stat(player, 117-48, 3, 7, "Eye Angle") -3)*-1
        #self.eyes_lenght = (Stat(player, 117-48, 6, 7, "Eye Length") -3)*-1
        #self.eyes_widxth = (Stat(player, 118-48, 1, 7, "Eye Widxth") -3)*-1
        #self.eyes_c1 = Stat(player, 94-48, 9, 3, "Eyes colour 1") + 1
        #self.eyes_c2 = Stat(player, 95-48, 3, 15, "Eyes colour 2")
        """
        if self.eyes_c2 == 0:
            self.eyes_c2 = "BLACK 1"
        elif self.eyes_c2 == 1:
            self.eyes_c2 = "BLACK 2"
        elif self.eyes_c2 == 2:
            self.eyes_c2 = "DARK GREY 1"
        elif self.eyes_c2 == 3:
            self.eyes_c2 = "DARK GREY 2"
        elif self.eyes_c2 == 4:
            self.eyes_c2 = "BROWN 1"
        elif self.eyes_c2 == 5:
            self.eyes_c2 = "BROWN 2"
        elif self.eyes_c2 == 6:
            self.eyes_c2 = "LIGHT BLUE 1"
        elif self.eyes_c2 == 7:
            self.eyes_c2 = "LIGHT BLUE 2"
        elif self.eyes_c2 == 8:
            self.eyes_c2 = "BLUE 1"
        elif self.eyes_c2 == 9:
            self.eyes_c2 = "BLUE 2"
        elif self.eyes_c2 == 10:
            self.eyes_c2 = "GREEN 1"
        elif self.eyes_c2 == 11:
            self.eyes_c2 = "GREEN 2"
        else:
            self.eyes_c2 = "ERROR"
        """
        # Nose menu
        #self.nose_type = Stat(player,121-48, 0, 7, "Nose type") + 1
        #self.nose_height = (Stat(player,121-48, 6, 7, "Nose height") - 3)*-1
        #self.nose_widxth = (Stat(player,121-48, 3, 7, "Nose widxth") - 3)*-1
        
        # Cheeks menu
        #self.cheecks_type = Stat(player,120-48, 2, 7, "cheeks type") + 1
        #self.cheecks_shape = (Stat(player,120-48, 5, 7, "cheecks shape") - 3)*-1
        
        # Mouth menu
        #self.mouth_type = Stat(player,122-48, 1, 31, "mouth type") + 1
        #self.mouth_size = (Stat(player,123-48, 1, 7, "mouth type") - 3)*-1
        #self.mouth_position = (Stat(player,122-48, 6, 7, "mouth position") - 3)*-1
        
        # Jaw menu
        #self.jaw_type = Stat(player,123-48, 4, 7, "Jaw type") + 1
        #self.jaw_chin = (Stat(player,123-48, 7, 7, "Jaw chin") - 3)*-1
        #self.jaw_widxth = (Stat(player,124-48, 2, 7, "Jaw widxth") - 3)*-1

        # Hair menu
        # The variable below will get the Hairstyle idx but we have to return many other variables such a hair type, shape, front, volume, darkness and bandana
        # Millions thanks to Pato_lucas18 for this code who save me from doom
        
        self.hair =  Stat(player, 45, 0, 4095, "Hairstyle ID", "{stat} + 1 if {normalize} else {stat} - 1", 1, 4096)# + 1
        self.special_hairstyles_2 =  Stat(player, 52, 6, 1, "Special Hairstyles 2", 6)
        """
        # Bald
        if 0 <= self.hair <= 3:
            self.hair_type = "BALD"
            self.hair_shape = self.hair + 1
            self.hair_front = 1
            self.hair_volume = 1
            self.hair_darkness = 1
            self.hair_bandana = 1
        # Buzz cut
        elif 4 <= self.hair <= 83:
            self.hair_type = "BUZZ CUT"
            self.hair_shape = 1
            self.hair_front = 1
            self.hair_volume = 1
            self.hair_darkness = 0
            self.hair_bandana = 1
            for c in range(4, self.hair + 1):
                self.hair_darkness += 1
                if self.hair_darkness == 5:
                    self.hair_darkness = 1
                    self.hair_front += 1
                    if self.hair_front == 6:
                        self.hair_front = 1
                        self.hair_shape += 1
        # Very short 1
        elif 84 <= self.hair <= 107:
            self.hair_type = "VERY SHORT 1"
            self.hair_shape = 1
            self.hair_front = 0
            self.hair_volume = 1
            self.hair_darkness = 1
            self.hair_bandana = 1
            for c in range(84, self.hair +1 ):
                self.hair_front += 1
                if self.hair_front == 7:
                    self.hair_front = 1
                    self.hair_shape += 1
        # Very short 2
        elif 108 <= self.hair <= 152:
            self.hair_type = "VERY SHORT 2"
            self.hair_front = 0
            self.hair_volume = 1
            self.hair_darkness = 1
            self.hair_bandana = 1
            if self.hair >= 138:
                self.hair_shape = 4
                for c in range(138, self.hair + 1):
                    self.hair_front += 1
                    if self.hair_front == 6:
                        self.hair_front = 1
                        self.hair_shape += 1
            else:
                self.hair_shape = 1
                for c in range(108, self.hair + 1):
                    self.hair_front += 1
                    if self.hair_front == 11:
                        self.hair_front = 1
                        self.hair_shape += 1
        # Straight 1
        elif 153 <= self.hair <= 560:
            self.hair_type = "STRAIGHT 1"
            self.hair_shape = 1
            self.hair_front = 1
            self.hair_volume = 1
            self.hair_darkness = 1
            self.hair_bandana = 0
            for c in range(153, self.hair + 1):
                self.hair_bandana += 1
                if self.hair_bandana > 3 :
                    self.hair_volume += 1
                    self.hair_bandana = 1
                    if self.hair_volume == 4 :
                        self.hair_front += 1
                        self.hair_volume = 1
                        if self.hair_front == 17 :
                            self.hair_shape += 1
                            self.hair_front = 1
                    if self.hair_front >= 10:
                        self.hair_bandana = 4
        # Straight 2
        elif 561 <= self.hair <= 659:
            self.hair_type = "STRAIGHT 2"
            self.hair_shape = 1
            self.hair_front = 1
            self.hair_volume = 1
            self.hair_darkness = 1
            self.hair_bandana = 0
            for c in range(561, self.hair + 1):
                self.hair_bandana += 1
                if self.hair_bandana > 3:
                    self.hair_volume += 1
                    self.hair_bandana = 1
                    if self.hair_volume == 4:
                        self.hair_front += 1
                        self.hair_volume = 1
                        if self.hair_front == 8:
                            self.hair_shape += 1
                            self.hair_front = 1
                    if self.hair_front >= 3:
                        self.hair_bandana = 4
        # Curly 1
        elif 660 <= self.hair <= 863:
            self.hair_type = "CURLY 1"
            self.hair_shape = 1
            self.hair_front = 1
            self.hair_volume = 1
            self.hair_darkness = 1
            self.hair_bandana = 0
            for c in range(660, self.hair + 1):
                self.hair_bandana += 1
                if self.hair_bandana > 3 :
                    self.hair_volume += 1
                    self.hair_bandana = 1
                    if self.hair_volume == 4 :
                        self.hair_front += 1
                        self.hair_volume = 1
                        if self.hair_front == 8 :
                            self.hair_shape += 1
                            self.hair_front = 1
                    if self.hair_front >= 6:
                        self.hair_bandana = 4
        # Curly 2
        elif 864 <= self.hair <= 911:
            self.hair_type = "CURLY 2"
            self.hair_shape = 1
            self.hair_front = 1
            self.hair_volume = 0
            self.hair_darkness = 1
            self.hair_bandana = 1
            for c in range(864, self.hair + 1):
                self.hair_volume += 1
                if self.hair_volume == 3 :
                    self.hair_front += 1
                    self.hair_volume = 1
                    if self.hair_front == 7 :
                        self.hair_shape += 1
                        self.hair_front = 1
        # Ponytail 1
        elif 912 <= self.hair <= 947:
            self.hair_type = "PONYTAIL 1"
            self.hair_shape = 1
            self.hair_front = 1
            self.hair_volume = 0
            self.hair_darkness = 1
            self.hair_bandana = 1
            for c in range(912, self.hair + 1):
                self.hair_volume += 1
                if self.hair_volume == 4 :
                    self.hair_front += 1
                    self.hair_volume = 1
                    if self.hair_front == 5:
                        self.hair_shape += 1
                        self.hair_front = 1
        # Ponytail 2
        elif 948 <= self.hair <= 983:
            self.hair_type = "PONYTAIL 2"
            self.hair_shape = 1
            self.hair_front = 1
            self.hair_volume = 0
            self.hair_darkness = 1
            self.hair_bandana = 1
            for c in range(948, self.hair + 1):
                self.hair_volume += 1
                if self.hair_volume == 4 :
                    self.hair_front += 1
                    self.hair_volume = 1
                    if self.hair_front == 5:
                        self.hair_shape += 1
                        self.hair_front = 1
        # Dreadlocks
        elif 984 <= self.hair <= 1007:
            self.hair_type = "DREADLOCKS"
            self.hair_shape = 1
            self.hair_front = 1
            self.hair_volume = 0
            self.hair_darkness = 1
            self.hair_bandana = 1
            for c in range(984, self.hair + 1):
                self.hair_volume += 1
                if self.hair_volume == 3 :
                    self.hair_front += 1
                    self.hair_volume = 1
                    if self.hair_front == 5 :
                        self.hair_shape += 1
                        self.hair_front = 1
        # Pulled back
        elif 1008 <= self.hair <= 1025:
            self.hair_type = "PULLED BACK"
            self.hair_shape = 1
            self.hair_front = 0
            self.hair_volume = 1
            self.hair_darkness = 1
            self.hair_bandana = 1
            for c in range(1008, self.hair + 1):
                self.hair_front += 1
                if self.hair_front == 7:
                    self.hair_shape += 1
                    self.hair_front = 1
        # Special hair
        elif 1026 <= self.hair <= 2047:
            self.hair_type = "SPECIAL HAIRSTYLES"
            self.hair_shape = self.hair - 1025
            self.hair_front = 1
            self.hair_volume = 1
            self.hair_darkness = 1
            self.hair_bandana = 1        
        # Another case that should not happen... just to return a value :)
        else:
            self.hair_type = "OUT OF RANGE ERROR"
            self.hair_shape = self.hair
            self.hair_front = 1
            self.hair_volume = 1
            self.hair_darkness = 1
            self.hair_bandana = 1
        """
        # Hair colour menu
        #self.hair_colour_config = Stat(player, 94-48, 3, 63, "hair colour config") + 1
        #self.hair_rgb_r = (Stat(player, 102-48, 5, 63, "hair colour rgb R") - 63)*-1
        #self.hair_rgb_g = (Stat(player, 103-48, 3, 63, "hair colour rgb G") - 63)*-1
        #self.hair_rgb_b = (Stat(player, 104-48, 1, 63, "hair colour rgb B") - 63)*-1
        
        """
        # Hair bandana menu
        if self.hair_bandana==4:
            self.hair_bandana=1
        self.hair_bandana-=1
        """
        #self.hair_bandana_colour = Stat(player,109-48, 2, 7, "bandana colour") + 1
        # Cap menu
        #self.cap = Stat(player, 98-48, 6, 1, "cap")
        #self.cap_colour = Stat(player, 114-48, 3, 7, "cap colour") + 1
        # Facial hair menu
        #self.facial_hair_type = Stat(player,95-48, 7, 127, "facial hair")
        #self.facial_hair_colour = Stat(player,97-48, 0, 63, "facial hair colour") + 1
        # Sunglasses menu
        #self.sunglasses = Stat(player,97-48, 6, 3, "Sun glasses type")
        #self.sunglasses_colour = Stat(player,114-48, 0, 7, "Sun glasses colour") + 1
        
        # Physical settings
        self.height = Stat(player, 41, 0, 63, "Height", "{stat} + 148 if {normalize} else {stat} - 148", min = 148, max = 220)# + 148
        self.weight = Stat(player, 42, 0, 127, "Weight", min = 1, max = 123)

        self.neck_length = Stat(player, 57, 8, 15, "Neck Length", "{stat} - 7 if {normalize} else {stat} + 7", -7, 7)
        self.neck_width = Stat(player, 44, 4, 15, "Neck Width", "{stat} - 7 if {normalize} else {stat} + 7", -7, 7)
        self.shoulder_height = Stat(player, 61, 4, 15, "Shoulder Height", "{stat} - 7 if {normalize} else {stat} + 7", -7, 7)
        self.shoulder_width = Stat(player, 62, 0, 15, "Shoulder Width", "{stat} - 7 if {normalize} else {stat} + 7", -7, 7)
        self.chest_measu = Stat(player, 57, 12, 15, "Chest Measurement", "{stat} - 7 if {normalize} else {stat} + 7", -7, 7)
        self.waist_circumference = Stat(player, 58, 12, 15, "Waist Circumferemce", "{stat} - 7 if {normalize} else {stat} + 7", -7, 7)
        self.arm_circumference = Stat(player, 58, 8, 15, "Arm Circumferemce", "{stat} - 7 if {normalize} else {stat} + 7", -7, 7)
        self.leg_circumference = Stat(player, 59, 8, 15, "Leg Circumference", "{stat} - 7 if {normalize} else {stat} + 7", -7, 7)
        self.calf_circumference = Stat(player, 59, 12, 15, "Calf Circumferemce", "{stat} - 7 if {normalize} else {stat} + 7", -7, 7)
        self.leg_length = Stat(player, 60, 8, 15, "Leg Length", "{stat} - 7 if {normalize} else {stat} + 7", -7, 7)

        # Boots/Accesories
        """
        self.boot_type = Stat(player, 99-48, 9, 15, "boot type")
        self.boot_colour = Stat(player, 99-48, 13, 3, "boot COLOUR") + 1 
        self.neck_warm = Stat(player,98-48, 0, 1, "Neck Warmer")
        self.necklace_type = Stat(player,98-48, 1, 3, "Necklace type")
        self.necklace_colour = Stat(player,98-48, 3, 7, "Necklace colour") + 1
        self.wistband = Stat(player,98-48, 7, 3, "wistband")
        self.wistband_colour = Stat(player,99-48, 1, 7, "wistband colour") + 1
        self.friend_brace =  Stat(player,99-48, 3, 4, "friendship bracelate")
        self.friend_brace_colour =  Stat(player,99-48, 6, 7, "friendship bracelate colour") + 1
        self.gloves = Stat(player,104-48, 7, 1, "Gloves")
        self.finger_band = Stat(player,109-48, 0, 3, "Finger Band")
        self.shirt = Stat(player,92-48, 7, 1, "Shirt")
        self.sleeves =  Stat(player,96-48, 6, 3, "Sleeves")
        self.under_short =  Stat(player,100-48, 76, 1, "under short")
        self.under_short_colour =  Stat(player,101-48, 0, 7, "under short colour") + 1
        self.socks =  Stat(player,105-48, 0, 3, "Socks") + 1
        self.tape =  Stat(player,102-48, 4, 1, "Tape")
        """

    @property
    def body_parameters(self):
        return (
            self.neck_length, 
            self.neck_width, 
            self.shoulder_height, 
            self.shoulder_width, 
            self.chest_measu, 
            self.waist_circumference, 
            self.arm_circumference,
            self.leg_circumference, 
            self.calf_circumference, 
            self.leg_length,
        )

    @body_parameters.setter
    def body_parameters(self, values:'tuple[int]'):
        for i, body_parameter in enumerate(values):
            self.body_parameters[i].set_value(body_parameter)

    @property
    def body_type(self):
        body_parameters_vals = tuple(body_parameter() for body_parameter in self.body_parameters)
        return (
            BODY_TYPES[
                BODY_TYPES_VALUES.index(body_parameters_vals)
            ] 
            if body_parameters_vals in BODY_TYPES_VALUES
            else
            BODY_TYPES[-1]
        )

    def __iter__(self):
        """
        Returns an iterable object with all class attributes

        Returns:
            any: iterable object with all class attributes
        """
        keys = list(self.__dict__.keys())
        values =list(self.__dict__.values())
        return iter([values[i] for i in range(len(keys)) if not keys[i].startswith('__')])
    
    def __call__(self):
        return [appearance() for appearance in self.__iter__()]
