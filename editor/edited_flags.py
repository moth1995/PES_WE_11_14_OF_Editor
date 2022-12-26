from .pes_stat import Stat


class EditedFlags:
    def __init__(self, player):
        self.name_edited = Stat(player, 3, 0, 1, "Name Edited")
        self.callname_edited = Stat(player, 3, 2, 1, "Callname Edited")
        self.shirt_name_edited = Stat(player, 3, 1, 1, "Shirt Name Edited")
        self.ability_edited = Stat(player, 40, 5, 1, "Ability Edited")
        self.appearance_edited = Stat(player, 66, 6, 1, "Appearance Edited")
        
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



