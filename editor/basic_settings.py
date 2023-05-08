from .pes_stat import Stat

class BasicSettings:
    def __init__(self,player):

        self.age = Stat(player, 66, 1, 0x1F, "Age", "{stat} + 15 if {normalize} else {stat} - 15", 15, 46)# +15
        self.stronger_foot = Stat(player, 5, 0, 1, "Stronger Foot", 0)
        self.injury = Stat(player, 33, 6, 3, "Injury", 3)
        self.style_of_dribble = Stat(player, 6, 0, 3, "Style of Dribble", "{stat} + 1 if {normalize} else {stat} - 1")# + 1
        self.free_kick_type = Stat(player, 5, 1, 15, "Free Kick Type", "{stat} + 1 if {normalize} else {stat} - 1")# + 1
        self.penalty_kick = Stat(player, 5, 5, 7, "Penalty Kick", "{stat} + 1 if {normalize} else {stat} - 1")# + 1
        self.drop_kick_style = Stat(player, 6, 2, 3, "Drop Kick Style", "{stat} + 1 if {normalize} else {stat} - 1")# + 1
        self.goal_celebration_1 = Stat(player, 36, 0, 127, "Goal Celebration 1")
        self.goal_celebration_2 = Stat(player, 37, 0, 127, "Goal Celebration 2")
        self.player_special_id = Stat(player, 38, 0, 0xff, "Player Special ID")
        self.growth_type= Stat(player, 39, 0, 0xff, "Growth type")

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
        """
        Make every object in the class callable

        Returns:
            _type_: _description_
        """
        return [basic_setting() for basic_setting in self.__iter__()]



