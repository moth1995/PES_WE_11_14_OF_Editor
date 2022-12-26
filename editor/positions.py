from .pes_stat import Stat

class Position:
    def __init__(self, player):
        self.favored_side = Stat(player, 33, 14, 3, "Favored side", 0)
        self.registered_position = Stat(player, 6, 4, 15, "Registered position", 7)
        self.GK = Stat(player, 7, 7, 1, "Goak Keeper (GK)")
        self.CWP = Stat(player, 7, 15, 1, "Sweeper (CWP)")
        self.CB = Stat(player, 9, 7, 1, "Centre Back (CB)")
        self.SB = Stat(player, 9, 15, 1, "Side Back (SB)")
        self.DM = Stat(player, 11, 7, 1, "Defensive Midfielder (DMF)")
        self.WB = Stat(player, 11, 15, 1, "Wing Back (WB)")
        self.CM = Stat(player, 13, 7, 1, "Centre Midfielder (CMF)")
        self.SM = Stat(player, 13, 15, 1, "Side Midfielder (SMF)")
        self.AM = Stat(player, 15, 7, 1, "Attacking Midfielder (AMF)")
        self.WG = Stat(player, 15, 15, 1, "Wing Forward (WF)")
        self.SS = Stat(player, 17, 7, 1, "Second Striker (SS)")
        self.CF = Stat(player, 17, 15, 1, "Centre Forward (CF)")

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
        return [position() for position in self.__iter__()]



