from fighter import Fighter


class Fox(Fighter):
    def __init__(self):
        self.hp = 340
        self.atq = 60
        self.df = 25
        self.vld = 70

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
