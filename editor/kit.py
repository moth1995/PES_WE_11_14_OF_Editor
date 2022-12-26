import struct
from .utils import common_functions, rgb_to_hex, hex_to_rgb, zero_fill_right_shift
from .utils.constants import *

class Kit:
    def __init__(self, data:bytearray):
        """
        Se inicializa la clase recibiendo un bytearray y se inicializan los parametros para el kit
        """
        self.data = data

    @property
    def font_shirt(self):
        """
        Carga la configuracion de nombre en la camiseta que tiene por default el kit
        """
        return OFF_ON[self.data[54]]

    @font_shirt.setter
    def font_shirt(self, new_value:str):
        """
        Actualiza la configuracion de nombre en la camiseta en el kit
        """
        if new_value not in OFF_ON:
            raise ValueError("Value not allowed")
        self.data[54] = OFF_ON.index(new_value)

    @property
    def font_curve(self):
        return FONT_CURVE[self.data[56]]

    @font_curve.setter
    def font_curve(self, new_value:int):
        """
        """
        if new_value not in FONT_CURVE:
            raise ValueError("Value not allowed")
        self.data[56] = FONT_CURVE.index(new_value)

    @property
    def front_number(self):
        """
        """
        return OFF_ON[self.data[58]]

    @front_number.setter
    def front_number(self, new_value:int):
        """
        """
        if new_value not in OFF_ON:
            raise ValueError("Value not allowed")
        self.data[58] = OFF_ON.index(new_value)

    @property
    def short_number(self):
        """
        """
        return OFF_LEFT_RIGHT[self.data[59]]

    @short_number.setter
    def short_number(self, new_value:int):
        """
        """
        if new_value not in OFF_LEFT_RIGHT:
            raise ValueError("Value not allowed")
        self.data[59] = OFF_LEFT_RIGHT.index(new_value)

    @property
    def overlay(self):
        """
        Carga el overlay que tiene por default el kit
        """
        return self.data[61]

    @overlay.setter
    def overlay(self, new_value:int):
        """
        Actualiza el model en el kit
        """
        min_value = 0
        max_value = 14
        if common_functions.check_value(min_value,new_value,max_value):
            self.data[61] = new_value
        else:
            raise ValueError(f"Overlay must be between {min_value} and {max_value}")

    @property
    def posc_overlay_y(self):
        return self.data[63]

    @posc_overlay_y.setter
    def posc_overlay_y(self, new_value:int):
        """
        """
        min_value = 0
        max_value = 10
        
        if common_functions.check_value(min_value,new_value,max_value):
            self.data[63] = new_value
        else:
            raise ValueError(f"Overlay y coordinate must be between {min_value} and {max_value}")
    @property
    def y_posc_num_back(self):
        """
        """
        return self.data[67]

    @y_posc_num_back.setter
    def y_posc_num_back(self, new_value:int):
        """
        """
        min_value = 0
        max_value = 18
        if common_functions.check_value(min_value,new_value,max_value):
            self.data[67] = new_value
        else:
            raise ValueError(f"Back number x coordinate must be between {min_value} and {max_value}")

    @property
    def number_size_back(self):
        """
        """
        return self.data[68]

    @number_size_back.setter
    def number_size_back(self, new_value:int):
        """
        """
        min_value = 0
        max_value = 31
        if common_functions.check_value(min_value,new_value,max_value):
            self.data[68] = new_value
        else:
            raise ValueError(f"Number size must be between {min_value} and {max_value}")

    @property
    def y_posc_front_num(self):
        """
        """
        return self.data[69]

    @y_posc_front_num.setter
    def y_posc_front_num(self, new_value:int):
        """
        """
        min_value = 0
        max_value = 29
        if common_functions.check_value(min_value,new_value,max_value):
            self.data[69] = new_value
        else:
            raise ValueError(f"Front number y coordinate must be between {min_value} and {max_value}")

    @property
    def x_posc_front_num(self):
        """
        """
        return self.data[70]

    @x_posc_front_num.setter
    def x_posc_front_num(self, new_value:int):
        """
        """
        min_value = 0
        max_value = 29
        if common_functions.check_value(min_value,new_value,max_value):
            self.data[70] = new_value
        else:
            raise ValueError(f"Front number x coordinate must be between {min_value} and {max_value}")

    @property    
    def front_number_size(self):
        """
        """
        return self.data[71]

    @front_number_size.setter
    def front_number_size(self, new_value:int):
        """
        """
        min_value = 0
        max_value = 22
        if common_functions.check_value(min_value,new_value,max_value):
            self.data[71] = new_value
        else:
            raise ValueError(f"Front number size must be between {min_value} and {max_value}")

    @property
    def y_posc_short_number(self):
        """
        """
        return self.data[72]

    @y_posc_short_number.setter
    def y_posc_short_number(self, new_value:int):
        """
        """
        min_value = 0
        max_value = 19
        if common_functions.check_value(min_value,new_value,max_value):
            self.data[72] = new_value
        else:
            raise ValueError(f"Short number y coordinate must be between {min_value} and {max_value}")
    
    @property
    def x_posc_short_number(self):
        """
        """
        return self.data[73]

    @x_posc_short_number.setter
    def x_posc_short_number(self, new_value:int):
        """
        """
        min_value = 0
        max_value = 25
        if common_functions.check_value(min_value,new_value,max_value):
            self.data[73] = new_value
        else:
            raise ValueError(f"Short number x coordinate must be between {min_value} and {max_value}")

    @property
    def short_number_size(self):
        """
        """
        return self.data[74]

    @short_number_size.setter
    def short_number_size(self, new_value:int):
        """
        """
        min_value = 0
        max_value = 28 #18
        if common_functions.check_value(min_value,new_value,max_value):
            self.data[74] = new_value
        else:
            raise ValueError(f"Short size must be between {min_value} and {max_value}")

    @property
    def font_size(self):
        """
        """
        return self.data[76]

    @font_size.setter
    def font_size(self, new_value:int):
        """
        """
        min_value =0
        max_value = 30
        if common_functions.check_value(min_value,new_value,max_value):
            self.data[76] = new_value
        else:
            raise ValueError(f"font size must be between {min_value} and {max_value}")

    @property
    def license(self):
        """
        Lee y carga en la variable self.license el valor correcto
        """
        license = struct.unpack("<H",self.data[80:82])[0]
        return NO_YES[license] if license == 1 else NO_YES[0]

    @license.setter
    def license(self, new_val:str):
        """
        Recibe un string que puede ser Yes o No y actualiza el valor,
        en los bytes del kit y en la clase
        """
        new_val = 1 if new_val == "Yes" else 0xFFFF
        self.data[80:82] = struct.pack("<H", new_val)

    @property
    def model(self):
        """
        Carga el numero de model que tiene por default el kit
        """
        return self.data[82]

    @model.setter
    def model(self, new_value:int):
        """
        Actualiza el model en el kit
        """
        min_value = 0
        max_value = 0xFF
        if common_functions.check_value(min_value,new_value,max_value):
            self.data[82] = new_value
        else:
            raise ValueError(f"Model must be between {min_value} and {max_value}")

    @property
    def color_radar(self):
        """
        Carga el color del radar que tiene el kit por default
        """
        color_radar_r = self.get_value(0,8,31) * 8
        color_radar_g = self.get_value(1,5,31) * 8
        color_radar_b = self.get_value(1,10,31) * 8
        
        colors_radar_rgb = color_radar_r,color_radar_g,color_radar_b

        return rgb_to_hex(colors_radar_rgb)

    @color_radar.setter
    def color_radar(self, new_value):
        """
        hacer una funcion para validar los valores a pasar que esten entre 0 y 31 y que sea int
        actualizo el valor de rojo a 5
        """
        hex_rgb = hex_to_rgb(new_value)

        r = int(hex_rgb[0] / 8)
        g = int(hex_rgb[1] / 8)
        b = int(hex_rgb[2] / 8)

        self.set_value(0, 8, 31, r)
        self.set_value(1, 5, 31, g)
        self.set_value(1, 10, 31, b)
        
        #self.color_radar = new_value

    def get_value(self, offset, shift, mask):
        j = (self.data[offset]) << 8 | (self.data[(offset - 1)])
        j = zero_fill_right_shift(j,shift)
        j &= mask
        return j

    def set_value(self, offset, shift, mask, new_value):
        j = (self.data[offset]) << 8 | (self.data[(offset - 1)])
        k = 0xFFFF & (mask << shift ^ 0xFFFFFFFF)
        j &= k
        new_value &= mask
        new_value <<= shift
        new_value = j | new_value
        self.data[(offset - 1)] = (new_value & 0xFF)
        self.data[offset] = (zero_fill_right_shift(new_value,8))



