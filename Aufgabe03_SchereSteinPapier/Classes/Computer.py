from Spieler import Spieler

import random


class Computer(Spieler):
    def __init__(self, name="Computer"):
        super().__init__(name)

    def gewaehlte_option(self):
        return random.randint(1, 5)
