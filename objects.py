from abc import ABC, abstractmethod

class RAM(ABC):
    def __init__(self) -> None:
        self.__ram_amount = 0
        self.__ram_type = ""

    @property
    def amount(self):
        return self.__ram_amount

    @amount.setter
    def amount(self, amount):
        self.__ram_amount = amount

    @property
    def type(self):
        return self.__ram_type

    @type.setter
    def type(self, type):
        self.__ram_type = type

    @abstractmethod
    def get_cost(self):
        raise NotImplementedError("You need to implement this method.")


class DDR4(RAM):
    def __init__(self, amount):
        super().__init__()
        self.amount = amount
        self.type = "DDR4"

    def get_cost(self):
        return self.amount * 10


class DDR6(RAM):
    def __init__(self, amount):
        super().__init__()
        self.amount = amount
        self.type = "DDR6"

    def get_cost(self):
        return self.amount * 12.5
