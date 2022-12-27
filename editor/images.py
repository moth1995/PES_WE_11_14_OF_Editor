import struct
from PIL import Image, ImageTk
import io
import zlib

class PNG:
    PNG_SIGNATURE = bytearray([137, 80, 78, 71, 13, 10, 26, 10])
    IHDR_LENGTH = bytearray((13).to_bytes(4, byteorder='big', signed=False))
    IHDR = bytearray([73,72,68,82])
    PLTE = bytearray([80,76,84,69])
    TRNS = bytearray([116,82,78,83])
    IDAT = bytearray([73,68,65,84])
    IEND_LENGTH = bytearray(4)
    IEND = bytearray([73,69,78,68])
    iend_crc32 = bytearray(zlib.crc32(IEND).to_bytes(4, byteorder='big', signed=False))
    iend_chunk = IEND_LENGTH + IEND + iend_crc32
    TEXT = bytearray([116,69,88,116])
    keyword_author = 'Author'.encode('iso-8859-1')
    text_author = 'PES 5 Indie Team & Yerry11'.encode('iso-8859-1')
    keyword_software = 'Software'.encode('iso-8859-1')
    text_software = 'OF Team Editor'.encode('iso-8859-1')
    separator = bytearray(1)

    def __init__(self, pes_img, disable_alpha=False):
        self.pes_img = pes_img
        self.png_from_pes_img16(disable_alpha)

    def png_from_pes_img16(self, disable_alpha):
        """
        Returns a PNG image from a pes image
        """
        IHDR_DATA = (bytearray(self.pes_img.width.to_bytes(4, byteorder='big', signed=False)) 
        +  bytearray(self.pes_img.height.to_bytes(4, byteorder='big', signed=False)) 
        + bytearray([self.pes_img.bpp, 3, 0, 0, 0]))
        ihdr_crc32 = bytearray(zlib.crc32(self.IHDR + IHDR_DATA).to_bytes(4, byteorder='big', signed=False))
        ihdr_chunk = self.IHDR_LENGTH + self.IHDR + IHDR_DATA + ihdr_crc32
        palette_data = self.pes_palette_to_RGB()
        plte_lenght = bytearray(len(palette_data).to_bytes(4, byteorder='big', signed=False))
        plte_crc32 = bytearray(zlib.crc32(self.PLTE + palette_data).to_bytes(4, byteorder='big', signed=False))
        plt_chunk = plte_lenght + self.PLTE + palette_data + plte_crc32
        trns_data = self.pes_trns_to_alpha(disable_alpha)
        trns_lenght = bytearray(len(trns_data).to_bytes(4, byteorder='big', signed=False))
        trns_crc32 = bytearray(zlib.crc32(self.TRNS+trns_data).to_bytes(4, byteorder='big', signed=False))
        trns_chunk = trns_lenght + self.TRNS + trns_data + trns_crc32
        idat_data = self.pes_px_to_idat()
        idat_lenght = bytearray(len(idat_data).to_bytes(4, byteorder='big', signed=False))
        idat_crc32 = bytearray(zlib.crc32(self.IDAT + idat_data).to_bytes(4, byteorder='big', signed=False))
        idat_chunk = bytearray(idat_lenght + self.IDAT + idat_data + idat_crc32)
        author_data = bytearray(self.keyword_author + self.separator + self.text_author)
        author_lenght = bytearray(len(author_data).to_bytes(4, byteorder='big', signed=False))
        author_crc32 = bytearray(zlib.crc32(self.TEXT + author_data).to_bytes(4, byteorder='big', signed=False))
        author_chunk = bytearray(author_lenght + self.TEXT + author_data + author_crc32)

        software_data = bytearray(self.keyword_software + self.separator + self.text_software)
        software_lenght = bytearray(len(software_data).to_bytes(4, byteorder='big', signed=False))
        software_crc32 = bytearray(zlib.crc32(self.TEXT + software_data).to_bytes(4, byteorder='big', signed=False))
        software_chunk = bytearray(software_lenght + self.TEXT + software_data + software_crc32)

        self.png = self.PNG_SIGNATURE + ihdr_chunk + plt_chunk + trns_chunk + author_chunk + software_chunk + idat_chunk + self.iend_chunk

    def png_bytes_to_tk_img(self):
        return ImageTk.PhotoImage(Image.open(io.BytesIO(self.png)).convert("RGBA"))

    def pes_palette_to_RGB(self):
        palette_data = bytearray()
        for j in range(0, len(self.pes_img.pes_palette), 4):
            palette_data += self.pes_img.pes_palette[j : j + 3]
        return palette_data

    def pes_trns_to_alpha(self, disable_alpha:bool):
        trns_data = bytearray()
        for j in range(3, len(self.pes_img.pes_palette), 4):
            trns_data += self.pes_img.pes_palette[j : j + 1]
        if disable_alpha:
            trns_data = self.__disable_alpha(trns_data)

        return trns_data

    def __disable_alpha(self,trns_data):
        for i in range(0,len(trns_data),1): #Solo toma los bytes de transparencia
            value = trns_data[i]*2
            if value >= 256: #Si el valor es (mayor o igual a 256) se resta 1 al valor
                value = value-1
            elif value <= 0: #Si no el valor es (menor o igual al 0) se queda en 0
                value = 0
            trns_data[i] = value
        return trns_data


    def pes_px_to_idat(self):
        step = self.pes_img.width
        if step == 32:
            step = int(step / 2)
        idat_uncompress = bytearray()
        for j in range(0, len(self.pes_img.pes_idat), step):
            idat_uncompress += self.separator + self.pes_img.pes_idat[j : j + step]
        return bytearray(zlib.compress(idat_uncompress))

class PESImg:
    def __init__(self,):
        pass

    PES_IMAGE_SIGNATURE = bytearray([0x94, 0x72, 0x85, 0x29,])
    width = 0
    height = 0
    bpp = 8
    pes_idat = bytearray()
    pes_palette = bytearray()

    def from_bytes(self, pes_image_bytes:bytearray):
        print(type(pes_image_bytes))
        magic_number = pes_image_bytes[:4]
        if not self.__valid_PESImage(magic_number): 
            raise Exception("not valid PES IMAGE")
        size = struct.unpack("<I",pes_image_bytes[8:12])[0]
        pes_image_bytes = pes_image_bytes[:size]
        self.width = struct.unpack("<H",pes_image_bytes[20:22])[0]
        self.height = struct.unpack("<H",pes_image_bytes[22:24])[0]
        pes_palette_start = struct.unpack("<H",pes_image_bytes[18:20])[0]
        pes_idat_start = struct.unpack("<H",pes_image_bytes[16:18])[0]
        self.pes_palette = pes_image_bytes[pes_palette_start:pes_idat_start]
        self.pes_idat = pes_image_bytes[pes_idat_start:size]


    def from_png(self, png:bytearray):
        self.png = png
        self.pes_palette = bytearray()
        self.pes_idat = bytearray()
        if not self.png[ : 8] == PNG.PNG_SIGNATURE:
            raise TypeError("Not a PNG image")
        ihdr_start = self.png.find(PNG.IHDR) # we need to move 4 bytes from the identifier
        if ihdr_start == -1:
            raise TypeError("Not a valid PNG image")
        ihdr_start+=4
        ihdr_lenght = int.from_bytes(self.png[ihdr_start - 8 : ihdr_start - 4],'big', signed=False)
        ihdr = self.png[ihdr_start : ihdr_start + ihdr_lenght]
        self.width = int.from_bytes(ihdr[:4],'big',signed=False)
        self.height = int.from_bytes(ihdr[4:8],'big',signed=False)

        self.bpp = ihdr[8]
        self.palette_size = 1 << self.bpp
        self.palette_pes_size = self.bpp * self.palette_size

        color_type = ihdr[9]
        if color_type != 3:
            raise TypeError("Image is not indexed")

        plte_start = self.png.find(PNG.PLTE) # we need to move 4 bytes from the identifier
        if plte_start == -1:
            raise TypeError("Not a valid PNG image")
        plte_start+=4
        plte_lenght = int.from_bytes(self.png[plte_start - 8 : plte_start - 4],'big', signed=False)
        plte = png[plte_start : plte_start + plte_lenght]

        trns_start = self.png.find(PNG.TRNS) # we need to move 4 bytes from the identifier
        if trns_start == -1:
            raise TypeError("Not a valid PNG image")
        trns_start+=4
        trns_lenght = int.from_bytes(self.png[trns_start - 8 : trns_start - 4],'big', signed=False)
        trns = self.png[trns_start : trns_start + trns_lenght]

        idat_start = self.png.find(PNG.IDAT)# we need to move 4 bytes from the identifier
        if idat_start == -1:
            raise TypeError("Not a valid PNG image")
        idat_start+=4
        idat_lenght = int.from_bytes(self.png[idat_start - 8 : idat_start - 4],'big', signed=False)
        idat = zlib.decompress(self.png[idat_start : idat_start + idat_lenght])
        self.merge_trns_plte(trns,plte)
        self.idat_to_pes_px(idat)

    def merge_trns_plte(self,trns,plte):
        for x in range(len(trns)): 
            self.pes_palette += plte[3*x:3*x+3]+trns[1*x:1*x+1] #Se intercalan los colores y transparencias (3 bytes = 1 colors, 1 byte transparencia)

    def idat_to_pes_px(self,idat):
        step = self.width
        if step == 32:
            step = int(step / 2)
        for i in range(1, len(idat), step + 1):
            self.pes_idat += idat[ i : i + step]

    def __valid_PESImage(self,magic_number : bytearray):
        return magic_number == self.PES_IMAGE_SIGNATURE

    def bgr_to_bgri(self):
        for i in range(32,len(self.pes_palette),128):
            self.pes_palette[i:i+32], self.pes_palette[i+32:i+72] = self.pes_palette[i+32:i+72], self.pes_palette[i:i+32]
