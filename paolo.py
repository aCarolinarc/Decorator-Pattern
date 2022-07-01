from fighter import Fighter


class Paolo(Fighter):
    def __init__(self):
        self.hp = 250
        self.atq = 45
        self.df = 30
        self.vld = 75

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