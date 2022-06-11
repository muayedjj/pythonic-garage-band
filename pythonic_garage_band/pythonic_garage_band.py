"""
This is a program designed to define some data types/structures meant
to be used to construct bands with names and members, given that the
occupations of said members are, for now:
    Guitarist, lead
    Drummer, very cool
    Bassist, impressive
    For experimenting purposes, a band called MJS93 has been initiated
    Have fun ^^
"""
from abc import ABC


class Musician(ABC):
    """
    The base class of our band as per LAB: 04 instructions on canvas
    """
    def __init__(self, name):
        self.name = name


class Band:
    """
    Our MJS93 band members, (a list of instances)
    Attributes:
        name, members
    """
    instances = []

    def __init__(self, name, members=None):
        if members is None:
            members = []
        self.name = name
        self.members = members
        Band.instances.append(self)

    def play_solos(self):
        solo_engs = []
        for musician in self.members:
            solo_engs.append(musician.play_solo())
        return solo_engs

    @classmethod
    def to_list(cls):
        return cls.instances


class Guitarist(Musician):
    """
    The lead of our musicians, Muayad XD
    """
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f"My name is {self.name} and I play guitar"

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"

    @staticmethod
    def get_instrument():
        return "guitar"

    @staticmethod
    def play_solo():
        return "face melting guitar solo"


class Drummer(Musician):
    """
    The coolest and baddest musician/instance in the great band of ours
    Child of: Class Musician
    Proposed member: Any Electrical Engineer in Jordan (other than me ofc)
    """
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f"My name is {self.name} and I play drums"

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"

    @staticmethod
    def get_instrument():
        return "drums"

    @staticmethod
    def play_solo():
        return "rattle boom crash"


class Bassist(Musician):
    """
    The last of our musician/instance
    Child of: Class Musician
    They will probably be a civil engineer
    """
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f"My name is {self.name} and I play bass"

    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"

    @staticmethod
    def get_instrument():
        return "bass"

    @staticmethod
    def play_solo():
        return "bom bom buh bom"


if __name__ == "__main__":
    muayad = Guitarist('Muayed')
    elec_eng = Drummer('Poor EE')
    civil_eng = Bassist('A CE')

    engineers = Band('MJS93', [muayad, elec_eng, civil_eng])

    print(str(muayad))
    print(repr(muayad))
    print(f'We are {engineers.name}, we are {engineers.members}. We are all engineers (unfortunately)')
