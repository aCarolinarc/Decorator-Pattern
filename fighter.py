from abc import ABC, abstractmethod


class Fighter(metaclass=ABC):
    @abstractmethod
    def get_hp(self):
        pass

    @abstractmethod
    def get_atq(self):
        pass

    @abstractmethod
    def get_def(self):
        pass

    @abstractmethod
    def get_vld(self):
        pass

    @abstractmethod
    def get_comp(self):
        pass

    @abstractmethod
    def compute_damage(self):
        pass
