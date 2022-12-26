from .pes_stat import Stat

class SpecialAbilities:
    def __init__(self, player):
        self.dribbling = Stat(player, 21, 7, 1, "Dribbling")
        self.tactical_dribble = Stat(player, 21, 15, 1, "Tactical Dribble")
        self.positioning = Stat(player, 23, 7, 1, "Positioning")
        self.reaction = Stat(player, 23, 15, 1, "Reaction")
        self.playmaking = Stat(player, 25, 7, 1, "Playmaking")
        self.passing = Stat(player, 25, 15, 1, "Passing")
        self.scoring = Stat(player, 27, 7, 1, "Scoring")
        self.one_on_one_scoring = Stat(player, 27, 15, 1, "1-1 Scoring")
        self.post_player = Stat(player, 29, 7, 1, "Post Player")
        self.lines = Stat(player, 29, 15, 1, "Lines")
        self.middle_shooting = Stat(player, 31, 7, 1, "Middle Shooting")
        self.side = Stat(player, 31, 15, 1, "Side")
        self.centre = Stat(player, 19, 15, 1, "Centre")
        self.penalties = Stat(player, 19, 7, 1, "Penalties")
        self.one_touch_pass = Stat(player, 35, 0, 1, "1-Touch Pass")
        self.outside = Stat(player, 35, 1, 1, "Outside")
        self.marking = Stat(player, 35, 2, 1, "Marking")
        self.sliding_tackle = Stat(player, 35, 3, 1, "Sliding Tackle")
        self.covering = Stat(player, 35, 4, 1, "Covering")
        self.d_line_control = Stat(player, 35, 5, 1, "D-Line Control")
        self.penalty_stopper = Stat(player, 35, 6, 1, "Penalty Stopper")
        self.one_on_one_stopper = Stat(player, 35, 7, 1, "1-on-1 Stopper")
        self.long_throw = Stat(player, 37, 7, 1, "Long Throw")

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
        return [special_ability() for special_ability in self.__iter__()]




