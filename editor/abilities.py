from .pes_stat import Stat

class Abilities:
    def __init__(self, player):
        self.attack = Stat(player, 7, 0, 127, "Attack", None, 1, 99)
        self.defence = Stat(player, 8, 0, 127, "Defence", None, 1, 99)
        self.body_balance = Stat(player, 9, 0, 127, "Body Balance", None, 1, 99)
        self.stamina = Stat(player, 10, 0, 127, "Stamina", None, 1, 99)
        self.top_speed = Stat(player, 11, 0, 127, "Top Speed", None, 1, 99)
        self.acceleration = Stat(player, 12, 0, 127, "Acceleration", None, 1, 99)
        self.response = Stat(player, 13, 0, 127, "Response", None, 1, 99)
        self.agility = Stat(player, 14, 0, 127, "Agility", None, 1, 99)
        self.dribble_accuracy = Stat(player, 15, 0, 127, "Dribble Accuracy", None, 1, 99)
        self.dribble_speed = Stat(player, 16, 0, 127, "Dribble Speed", None, 1, 99)
        self.short_pass_accuracy = Stat(player, 17, 0, 127, "Short Pass Accuracy", None, 1, 99)
        self.short_pass_speed = Stat(player, 18, 0, 127, "Short Pass Speed", None, 1, 99)
        self.long_pass_accuracy = Stat(player, 19, 0, 127, "Long Pass Accuracy", None, 1, 99)
        self.long_pass_speed = Stat(player, 20, 0, 127, "Long Pass Speed", None, 1, 99)
        self.shot_accuracy = Stat(player, 21, 0, 127, "Shot Accuracy", None, 1, 99)
        self.shot_power = Stat(player, 22, 0, 127, "Shot Power", None, 1, 99)
        self.shot_technique = Stat(player, 23, 0, 127, "Shot Technique", None, 1, 99)
        self.free_kick_accuracy = Stat(player, 24, 0, 127, "Free Kick Accuracy", None, 1, 99)
        self.swerve = Stat(player, 25, 0, 127, "Swerve", None, 1, 99)
        self.heading = Stat(player, 26, 0, 127, "Heading", None, 1, 99)
        self.jump = Stat(player, 27, 0, 127, "Jump", None, 1, 99)
        self.technique = Stat(player, 29, 0, 127, "Technique", None, 1, 99)
        self.aggression = Stat(player, 30, 0, 127, "Aggression", None, 1, 99)
        self.mentality = Stat(player, 31, 0, 127, "Mentality", None, 1, 99)
        self.goal_keeping_skills = Stat(player, 32, 0, 127, "Goal Keeping Skills", None, 1, 99)
        self.team_work_ability = Stat(player, 28, 0, 127, "Team Work Ability", None, 1, 99)

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
        return [ability() for ability in self.__iter__()]

class Abilities_1_8:
    def __init__(self, player):
        self.consistency = Stat(player, 33, 0, 7, "Consistency", "{stat} + 1 if {normalize} else {stat} - 1", min=1, max=8)# + 1
        self.condition_fitness = Stat(player, 33, 8, 7, "Condition/Fitness", "{stat} + 1 if {normalize} else {stat} - 1", min=1, max=8)# + 1
        self.weak_foot_accuracy = Stat(player, 33, 11, 7, "Weak Foot Accuracy", "{stat} + 1 if {normalize} else {stat} - 1", min=1, max=8)# + 1
        self.weak_foot_frequency = Stat(player, 33, 3, 7, "Weak Foot Frequency", "{stat} + 1 if {normalize} else {stat} - 1", min=1, max=8)# + 1

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
        return [ability() for ability in self.__iter__()]

