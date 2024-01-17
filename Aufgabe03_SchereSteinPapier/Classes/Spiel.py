from Spieler import Spieler
from Computer import Computer


class Spiel:
    def __init__(self):
        self.spieler = Spieler("Spieler")
        self.computer = Computer()
        self.regeln = {
            1: ["Schere", "Echse"],
            2: ["Stein", "Echse"],
            3: ["Papier", "Spock"],
            4: ["Schere", "Spock"],
            5: ["Stein", "Papier"]
        }

    def kommentar(self, gewinner):
        if gewinner == 0:
            print("Unentschieden!")
        elif gewinner == 1:
            print(f"{self.spieler.name} gewinnt!")
        else:
            print(f"{self.computer.name} gewinnt!")

    def spiel(self):
        self.spieler_option = self.spieler.gewaehlte_option()
        self.computer_option = self.computer.gewaehlte_option()
        gewinner = 0
        if self.spieler_option == self.computer_option:
            gewinner = 0
        elif self.computer_option in self.regeln[self.spieler_option]:
            gewinner = 2
        else:
            gewinner = 1
        self.kommentar(gewinner)


if __name__ == "__main__":
    spiel = Spiel()
    while True:
        spiel.spiel()
        play_again = input("Noch eine Runde? (j)a/(n)ein: ")
        if play_again.lower() != "j":
            break
