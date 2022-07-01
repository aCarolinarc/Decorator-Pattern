from fighter import Fighter
from fighter_decorator import Fighter_Decorator


class Crown(Fighter_Decorator):
    def __init__(self, decorated_fighter: Fighter):
        self.fighter = decorated_fighter

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
