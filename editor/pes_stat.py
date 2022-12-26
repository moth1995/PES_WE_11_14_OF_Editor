from .utils.common_functions import zero_fill_right_shift
from .utils.constants import *
from .nationalities import get_nation, get_nation_idx

class Stat():
    
    start_address = 48
    growth_types_early = []
    growth_types_early_lasting = []
    growth_types_standard = []
    growth_types_standard_lasting = []
    growth_types_late = []
    growth_types_late_lasting = []

    def __init__(self, player,offset:int, shift:int, mask:int, name:str, type:int=None, min:int=None,max:int=None):
        #self.player.of = option_file
        self.player = player
        self.offset = offset
        self.shift = shift
        self.mask = mask
        self.name = name
        self.type = type
        self.min = min
        self.max = max

    @property
    def address(self):
        return self.player.address + self.start_address + self.offset

    def get_value(self):
        #i = self.player.start_address + 48 + self.player.idx * 124 + self.offset
        #if self.player.idx > self.player.total_players:
            #i = self.player.start_address_edited + 48 + (self.player.idx - self.player.first_edited_id) * 124 + self.offset
        j = (self.player.of.data[self.address]) << 8 | (self.player.of.data[(self.address - 1)])
        j = zero_fill_right_shift(j,self.shift)
        j &= self.mask
        if self.type is not None:
            j = self.normalize(j)
        return j

    def set_value(self, new_value):
        self.value_in_range(new_value)
        if self.type is not None:
            new_value = self.denormalize(new_value)
        #i = self.player.start_address + 48 + (self.player.idx * 124) + self.offset
        #if (self.player.idx > self.player.total_players):
            #i = self.player.start_address_edited + 48 + ((self.player.idx - self.player.first_edited_id) * 124) + self.offset
        j = (self.player.of.data[self.address]) << 8 | (self.player.of.data[(self.address - 1)])
        k = 0xFFFF & (self.mask << self.shift ^ 0xFFFFFFFF)
        j &= k
        new_value &= self.mask
        new_value <<= self.shift
        new_value = j | new_value
        self.player.of.data[(self.address - 1)] = (new_value & 0xFF)
        self.player.of.data[self.address] = (zero_fill_right_shift(new_value,8))

    def normalize(self,val:int):
        
        def foot_fav_side():
            return FOOT_FAV_SIDE[val]

        def nation():
            return get_nation(self.player.of.nations,val)

        def hair():
            return val

        def injury():
            return INJURY_VALUES[val]

        def eyes_colour_2():
            return EYES_COLOURS[val]

        def face_type():
            return FACE_TYPE[val]

        def yes_no():
            return NO_YES[val]

        def registered_position():
            return val - 1 if val > 0 else val
        
        def growth_type():
            return val
        
        if isinstance(self.type, str):
            return eval(self.type.format(stat=val, normalize=True))

        mycase = {
            0 : foot_fav_side,
            1 : nation,
            2 : hair,
            3 : injury,
            4 : eyes_colour_2,
            5 : face_type,
            6 : yes_no,
            7 : registered_position,
            8 : growth_type,
        }
        myfunc = mycase[self.type]
        return myfunc()

    def denormalize(self, val):
        def foot_fav_side():
            try:
                return FOOT_FAV_SIDE.index(val)
            except:
                raise ValueError("Value giving for %s on player id: %d was not found! Check again what you're entering" % (self.name, self.player.idx))

        def nation():
            return get_nation_idx(self.player.of.nations, val)

        def hair():
            try:
                return val
            except:
                raise ValueError("Value giving for %s on player id: %d was not found! Check again what you're entering" % (self.name, self.player.idx))

        def injury():
            try:
                return INJURY_VALUES.index(val)
            except:
                raise ValueError("Value giving for %s on player id: %d was not found! Check again what you're entering" % (self.name, self.player.idx))

        def eyes_colour_2():
            try:
                return EYES_COLOURS.index(val)
            except:
                raise ValueError("Value giving for %s on player id: %d was not found! Check again what you're entering" % (self.name, self.player.idx))

        def face_type():
            try:
                return FACE_TYPE.index(val)
            except:
                raise ValueError("Value giving for %s on player id: %d was not found! Check again what you're entering" % (self.name, self.player.idx))

        def yes_no():
            try:
                return NO_YES.index(val)
            except:
                raise ValueError("Value giving for %s on player id: %d was not found! Check again what you're entering" % (self.name, self.player.idx))

        def registered_position():
            return val + 1 if val > 0 else val
        
        def growth_type():
            if self.get_growth_type_name() == val:
                # if the growth type didn't changed we dont update it
                return self.get_value()
            else:
                return self.get_growth_type_value(val)

        if isinstance(self.type, str):
            return eval(self.type.format(stat=val, normalize=False))

        mycase = {
            0 : foot_fav_side,
            1 : nation,
            2 : hair,
            3 : injury,
            4 : eyes_colour_2,
            5 : face_type,
            6 : yes_no,
            7 : registered_position,
            8 : growth_type,
        }
        myfunc = mycase[self.type]
        return myfunc()

    def value_in_range(self, value:int):
        if self.min == None or self.max == None: return
        elif self.min <= value <= self.max: return True
        else: raise ValueError("Value out of allowed range for %s on player id: %d! Value: %d must be between %d and %d" % (self.name, self.player.idx, value, self.min, self.max))

    def get_growth_type_name(self, val:int=None):
        """
        Function to get the proper growth_type name by the decimal value

        Returns:
            str : growth type names could be "Early Peak", "Early/Lasting","Standard", "Std/Lasting", "Late peak", "Late/Lasting"
        """
        val = self.get_value() if val == None else val
        """
        if growth_types_early(val):
            return GROWTH_TYPE_NAMES[0]
        elif growth_types_early_lasting(val):
            return GROWTH_TYPE_NAMES[1]
        elif growth_types_standard(val):
            return GROWTH_TYPE_NAMES[2]
        elif growth_types_standard_lasting(val):
            return GROWTH_TYPE_NAMES[3]
        elif growth_types_late(val):
            return GROWTH_TYPE_NAMES[4]
        elif growth_types_late_lasting(val):
            return GROWTH_TYPE_NAMES[5]
        else:
            return GROWTH_TYPE_NAMES[2] # if it doesnt match with any case we just return standard
        """
        for i, growth_type_val in enumerate(self.growth_type_vals):
            if val in growth_type_val:
                growth_type_name = GROWTH_TYPE_NAMES[i]
                break
            else: growth_type_name = GROWTH_TYPE_NAMES[2] # if it doesnt match with any case we just return standard
        return growth_type_name

    def get_growth_type_value(self, name:str):
        return GROWTH_TYPE_DEFAULT_VALUES[GROWTH_TYPE_NAMES.index(name)]

    def __call__(self):
        return self.get_value()

    @property
    def growth_type_vals(self):
        return [
            self.growth_types_early, 
            self.growth_types_early_lasting, 
            self.growth_types_standard, 
            self.growth_types_standard_lasting,
            self.growth_types_late,
            self.growth_types_late_lasting,
        ]


