from fighter import Fighter


class Yoshi(Fighter):
    def __init__(self):
        self.hp = 175
        self.atq = 47
        self.df = 40
        self.vld = 63

    def get_hp(self):
        return self.hp

    def get_atq(self):
        return self.atq

    def get_def(self):
        return self.df

    def get_vld(self):
        return self.vld

    def get_comp(self):
        pass

    def compute_damage(self):
        pass