from .utils import zero_fill_right_shift

class Shop:
    BG_OFFSET = 5224
    HAS_BG = False
    TOTAL_BGS = 0
    POINTS_OFFSET_1 = 52
    POINTS_OFFSET_2 = 0

    def __init__(self,option_file):
        self.of = option_file
        self.get_points()
        self.get_background()

    def get_points(self):
        self.points = (self.of.data[self.POINTS_OFFSET_1 + 2] << 16) + (self.of.data[self.POINTS_OFFSET_1 + 1] << 8) + (self.of.data[self.POINTS_OFFSET_1])

    def set_points(self,new_points):
        if 0 <= new_points <= 99999:
            self.of.data[self.POINTS_OFFSET_1] = (new_points & 0xFF)
            self.of.data[self.POINTS_OFFSET_1 + 1] = zero_fill_right_shift((new_points & 0xFF00), 8)
            self.of.data[self.POINTS_OFFSET_1 + 2] = zero_fill_right_shift((new_points & 0xFF0000), 16)
            self.of.data[self.POINTS_OFFSET_2] = (new_points & 0xFF);
            self.of.data[self.POINTS_OFFSET_2 + 1] = zero_fill_right_shift((new_points & 0xFF00) , 8)
            self.of.data[self.POINTS_OFFSET_2 + 2] = zero_fill_right_shift((new_points & 0xFF0000) , 16)
            self.get_points()
        else:
            raise ValueError("Points value must be between 0 and 99999")

    def lock_shop(self):
        for i in range(5144,5170):
            self.of.data[i] = 0
        self.of.data[56] = 1
        return "Shop locked!"

    def unlock_shop(self):
        for i in range(20):
            self.of.data[5144 + i] = 255
        self.of.data[5164] = 254
        self.of.data[5165] = 255
        self.of.data[5166] = 255
        self.of.data[5167] = 127
        self.of.data[5168] = 15
        self.of.data[5169] = 63
        self.of.data[56] = 98
        return "Shop unlocked!"

    def get_background(self):
        self.bg = self.of.data[self.BG_OFFSET]

    def set_background(self, new_bg):
        if 0<=new_bg<= 62:
            self.of.data[self.BG_OFFSET] = new_bg
            self.get_background()
            return "Main Menu BG Changed!"
        else:
            raise ValueError("Out of range value")