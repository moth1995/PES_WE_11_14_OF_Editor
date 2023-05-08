import struct
from editor.club import Club

class Emblem:
    total_128 = 50
    idx_table_adr = 0 #option_file_data.OF_BLOCK[8] + 4
    empty_idx_value = 0x99

    #837628 + 160

    #startaddb = 837788 + (5184 * 50)
    #The emblem image with and height (64px x 64px).
    width = 64
    height = 64
    #The hi-res indexed-color image format (8 bits-per-pixel).
    bpp_128 = 8
    #The low-res indexed-color image format (4 bits-per-pixel).
    bpp_16 = 4
    #A hi-res club emblem data record length (5184 bytes).
    size_128 = 5184
    #A low-res club emblem data record length (2176 bytes).
    size_16 = 2176
    palette_size_16 = 1 << bpp_16
    palette_size_128 = 1 << bpp_128
    palette_pes_size_16 = bpp_16 * palette_size_16
    palette_pes_size_128 = bpp_128 * palette_size_128

    #total_16 = total_128 * 2
    #total = total_128 + total_16
    #idx_table_size = 2 + total + 8
    #start_address = idx_table_adr + idx_table_size

    @property
    def total_16(self):
        return self.total_128 * 2
    
    @property
    def total(self):
        return self.total_128 + self.total_16

    @property
    def idx_table_size(self):
        return 2 + self.total + 8

    @property
    def start_address(self):
        return self.idx_table_adr + self.idx_table_size

    def getOffset128(self, slot):
        if 0 > slot >= self.total_128:
            raise ValueError("slot#", slot)
        return self.start_address + slot * self.size_128

    def getOffset16(self, slot):
        if 0 > slot >= self.total_16:
            raise ValueError("slot#", slot)
        return self.start_address + (self.total_128 - 1) * self.size_128 - int(slot / 2) * self.size_128 + (slot % 2) * self.size_16

    def get128(self, of, slot, opaque, small):
        if (None == of):
            raise ValueError("of")
        return self.getOffset128(slot) + self.width
        #return Images.read(of.data, self.width, BPP128, adr, opaque, small ? 0.58f : 0f);

    def get16(self, of, slot, opaque, small):
        if (None == of):
            raise ValueError("of")
        return self.getOffset16(slot) + self.width
        #return Images.read(of.data, self.width, BPP16, adr, opaque, small ? 0.58f : 0f);

    # emblem index table: [hiCount] [lowCount] [..HighResTotal] [..LowResTotal]
    def getLocation(self, of, index):
        if (None == of):
            raise ValueError("of")
        if (index < 0 or index >= self.total):
            raise ValueError("index#", index)

        return self.getLocationInternal(of, index)

    def getLocationInternal(self, of, index):
        idx = of.data[self.idx_table_adr + 2 + index]
        return -1 if(idx == self.empty_idx_value) else idx

    def setLocation(self, of, index, location):
        if (None == of):
            raise ValueError("of")
        if (index < 0 or index >= self.total):
            raise ValueError("index#", index)
        self.setLocationInternal(of, index, location)

    def setLocationInternal(self, of, index, location):
        of.data[self.idx_table_adr + 2 + index] = location

    def set128(self, of, slot, image):
        if (None == of):
            raise ValueError("of")

        adr = self.getOffset128(slot)
        try:
            #Images.write(of.data, self.width, BPP128, adr + self.width, image);
            of.data[adr] = (None != image) # is used?

            if (slot == self.count128(of)) :
                self.setCount128(of, slot + 1)

                for i in range(self.total_128):
                    loc = self.getLocationInternal(of, i)
                    if (loc < 0 or loc >= self.total_128) :
                        self.setLocationInternal(of, i, slot)

                        id = Club.first_club_emblem + i;
                        self.of.data[adr + 4 : adr + 8] = struct.pack("<H",id)
                        break;
        except Exception as e :
            raise ValueError("Failed to save emblem 128:", e)
        return True
    

    def set16(self, of, slot, image) :
        if (None == of):
            raise ValueError("of")

        adr = self.getOffset16(slot)
        try:
            #Images.write(of.data, self.width, BPP128, adr + self.width, image);
            of.data[adr] = (None != image) # is used?

            if (slot == self.count16(of)) :
                self.setCount16(of, slot + 1)

                for i in range(self.total):
                    loc = self.getLocationInternal(of, i)
                    if (loc < self.total_128 or loc >= self.total) :
                        self.setLocationInternal(of, i, self.total_128 + slot)
                        id = Club.first_club_emblem + i
                        self.of.data[adr + 4 : adr + 8] = struct.pack("<H",id)
                        break;
        except Exception as e :
            raise ValueError("Failed to save emblem 16:", e)
        return True

    def count128(self,of):
        if (None == of):
            raise ValueError("of")
        return of.data[self.idx_table_adr]
    

    def setCount128(self, of, count):
        if (None == of):
            raise ValueError("of")
        of.data[self.idx_table_adr] = count
    

    def count16(self,of):
        if (None == of):
            raise ValueError("of")
        return of.data[self.idx_table_adr + 1]
    

    def setCount16(self, of, count):
        if (None == of):
            raise ValueError("of")
        of.data[self.idx_table_adr + 1] = count
    

    def getFree16(self, of):
        return self.total_16 - self.count16(of) - self.count128(of) * 2
    

    def getFree128(self, of):
        return self.total_128 - self.count128(of) - int((self.count16(of) + 1) / 2)

    def getImage(self, of, emblem):
        slot = self.getLocation(of, emblem)
        if (emblem < self.total_128):
            return self.get128(of, slot, False, False)
        
        return self.get16(of, slot - self.total_128, False, False)
    

    def deleteImage(self, of, emblem):
        slot = self.getLocation(of, emblem)
        if (emblem < self.total_128):
            if (slot < 0 or slot >= self.total_128):
                return
            self.delete128(of, slot)
        else:
            if (slot < self.total_128 or slot >= self.total) :
                return
            self.delete16(of, slot - self.total_128)
        
    

    """
    Image ID at 4th byte.
    """
    def getIndex(self, of, slot) :
        if (None == of):
            raise ValueError("of")
        if (slot < 0 or slot >= self.total):
            raise ValueError("slot#", slot)

        adr = self.getOffset128(slot) + 4 if (slot < self.total_128) else self.getOffset16(slot - self.total_128) + 4
        #id = Bits.toInt16(of.data, adr + 4);
        id = of.data[adr : adr + 2]
        # Try to fix incorrect emblem ID
        if (id < Club.first_club_emblem):
            # DEBUG
            print("Try to fix emblem#: ID: : -> :", slot, id, Club.first_club_emblem + slot)
            id = Club.first_club_emblem + slot;
            #Bits.toBytes(Bits.toInt16(id), of.data, adr + 4);
            of.data[adr : adr + 2] = id
        
        return id

    def delete16(self, of, slot):
        index = self.getIndex(of, slot + self.total_128)
        sourceIdx = index - Club.first_club_emblem

        self.setLocation(of, sourceIdx, self.empty_idx_value)
        #Clubs.unlinkEmblem(of, sourceIdx) # TODO

        newCount = self.count16(of) - 1
        source = self.getOffset16(newCount)
        if (slot != newCount):

            dest = self.getOffset16(slot);
            #System.arraycopy(of.data, source, of.data, dest, self.size_16); # TODO

            index = self.getIndex(of, slot + self.total_128);
            sourceIdx = index - Club.first_club_emblem;
            self.setLocation(of, sourceIdx, slot + self.total_128);
        

        #Arrays.fill(of.data, source, source + self.size_16, (byte) 0); # TODO
        self.setCount16(of, newCount);
    

    def delete128(self, of, slot):
        index = self.getIndex(of, slot)
        sourceIdx = index - Club.first_club_emblem

        self.setLocation(of, sourceIdx, self.empty_idx_value)
        #Clubs.unlinkEmblem(of, sourceIdx); # TODO

        newCount = self.count128(of) - 1
        source = self.getOffset128(newCount)
        if (slot != newCount):

            dest = self.getOffset128(slot)
            #System.arraycopy(of.data, source, of.data, dest, self.size_128); #TODO

            index = self.getIndex(of, slot)
            sourceIdx = index - Club.first_club_emblem
            self.setLocation(of, sourceIdx, slot)
        

        #Arrays.fill(of.data, source, source + self.size_128, (byte) 0); # TODO
        self.setCount128(of, newCount);
    
    '''
    def importData16(self, ofSource, slotSource, ofDest, slotDest):
        if (null == ofSource) :
            throw new NullArgumentException("ofSource");
        
        if (null == ofDest) :
            throw new NullArgumentException("ofDest");
        

        adrSource = getOffset16(slotSource);
        adrDest = getOffset16(slotDest);
        System.arraycopy(ofSource.data, adrSource + self.width,
                ofDest.data, adrDest + self.width, self.size_16 - self.width);

        cntDest = count16(ofDest);
        if (slotDest == cntDest) :
            ofDest.data[adrDest] = 1;# is used
            setCount16(ofDest, cntDest + 1);

            for (i = self.total_128; i < self.total; i++) :
                loc = getLocationInternal(ofDest, i);
                if (loc < self.total_128 or loc >= self.total) :
                    setLocationInternal(ofDest, i, self.total_128 + slotDest);

                    id = Club.first_club_emblem + i;
                    Bits.toBytes(Bits.toInt16(id), ofDest.data, adrDest + 4);
                    break;
                
            
        
    

    public static void importData128(ofSource, slotSource, ofDest, slotDest) :
        if (null == ofSource) :
            throw new NullArgumentException("ofSource");
        
        if (null == ofDest) :
            throw new NullArgumentException("ofDest");
        

        adrSource = getOffset128(slotSource);
        adrDest = getOffset128(slotDest);
        System.arraycopy(ofSource.data, adrSource + self.width,
                ofDest.data, adrDest + self.width, self.size_128 - self.width);

        cntDest = count128(ofDest);
        if (slotDest == cntDest) :
            ofDest.data[adrDest] = 1;# is used
            setCount128(ofDest, cntDest + 1);

            for (i = 0; i < self.total_128; i++) :
                loc = getLocationInternal(ofDest, i);
                if (loc < 0 or loc >= self.total_128) :
                    setLocationInternal(ofDest, i, slotDest);

                    id = Club.first_club_emblem + i;
                    Bits.toBytes(Bits.toInt16(id), ofDest.data, adrDest + 4);
                    break;
                
            
        
    
    '''
    def fixIndexesTable(self,of):
        n128 = self.count128(of)
        n16 = self.count16(of)
        print("Try to fix emblem indexes-table: : :", n128, n16)

        # i need to understand this someday
        self.highResIndexes = set(self.total_128);   
        self.lowResIndexes = set(self.total_16);

        # Fixes all invalid and duplicated emblem indexes
        isUpdated = False
        for i in range(self.total):
            location = self.getLocationInternal(of, i);
            if (location != -1) :

                if location < self.total_128 or location >= self.total:
                        #/*or lowResIndexes.contains(location)*/)
                    self.setLocationInternal(of, i, self.empty_idx_value)
                    isUpdated = True
                else:
                    self.lowResIndexes.add(location);
                    self.fixIdBasedOnIndex(of, i, location);
                
            
        

        # Fixes all duplicated and overwritten emblem indexes
        swapLocation = 0
        for i in range(self.total_128):
            location = self.getLocationInternal(of, i)
            if (location != -1):
                if (location < 0 or location >= self.total_128
                        or (self.lowResIndexes.size() + 2 * self.highResIndexes.size()) >= self.total_16# out of space
                        #/*or highResIndexes.contains(location)*/
                        # overwritten emblems
                        or self.lowResIndexes.contains(swapLocation = (self.total - 2 * (location + 1)))
                        or self.lowResIndexes.contains(swapLocation + 1)):
                    self.setLocationInternal(of, i, self.empty_idx_value)
                    isUpdated = True
                else :
                    self.highResIndexes.add(location);
                    self.fixIdBasedOnIndex(of, i, location);
                
            
        

        # Re-counts the number of emblems for each type
        if (n128 != self.highResIndexes.size()):
            self.setCount128(of, self.highResIndexes.size())
            isUpdated = True
        
        if (n16 != self.lowResIndexes.size()):
            self.setCount16(of, self.lowResIndexes.size())
            isUpdated = True
        

        if (isUpdated) :
            print("Fixed emblem indexes-table: : :", self.highResIndexes.size(), self.lowResIndexes.size())
        
        return isUpdated
    

    """
     * Fixes emblem ID based on it's index.
    """
    def fixIdBasedOnIndex(self, of, index, slot) :
        adr = self.getOffset128(slot) if (slot < self.total_128) else self.getOffset16(slot - self.total_128) + 4
        id = of.data[adr : adr + 2]

        expected = index + Club.first_club_emblem;
        if (id != expected) :
            #Bits.toBytes(Bits.toInt16(expected), of.data, adr + 4);
            of.data[adr : adr + 2] = expected # to bytes
            # DEBUG
            print("Fixed ID of emblem (: -> :) from : -> :", index, slot, id, expected);
            return True
        
        return False
    

