from fighter import Fighter


class Blanca(Fighter):
    def __init__(self):
        self.hp = 200
        self.atq = 50
        self.df = 20
        self.vld = 80

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