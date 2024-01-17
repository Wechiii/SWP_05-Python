import json

from Spieler import Spieler
from Computer import Computer


class Spiel:
    def __init__(self):
        self.spieler = Spieler(input("Bitte Name angeben:"))
        self.spieler2 = Spieler(None)
        self.computer = Computer()

        self.regeln = {
            1: [4, 3],  # Schere schlägt "Echse", "Papier"
            2: [4, 1],   # Stein schlägt "Echse", "Schere"
            3: [2, 5],  # Papier schlägt "Stein", "Spock"
            4: [3, 5],  # Echse schlägt "Papier", "Spock"
            5: [2, 1]   # Spock schlägt "Stein", "Schere"
        }

        self.computer_option = 0
        self.spieler2_option = 0

        self.siege = {self.spieler.name: 0, self.computer.name: 0}
        self.symbol = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}

        self.lade_daten()

    def speichere_daten(self):
        with open('../Data/spieldaten.json', 'w') as f:
            json.dump({'symbol': self.symbol}, f)

    def lade_daten(self):
        try:
            with open('spiel_data.json', 'r') as f:
                data = json.load(f)
                self.siege = data['siege']
                self.symbol = data['symbol']
        except FileNotFoundError:
            pass

    def kommentareSolo(self, gewinner):
        if gewinner == 0:
            print("Unentschieden!")
        elif gewinner == 1:
            self.siege[self.computer.name] += 1
            print(f"{self.computer.name} gewinnt!")
            print(f"{self.computer.name} hat {self.computer_option} gewählt")
        else:
            self.siege[self.spieler.name] += 1
            print(f"{self.spieler.name} gewinnt!")
            print(f"{self.computer.name} hat {self.computer_option} gewählt")

    def kommentareDuo(self, gewinner):
        if gewinner == 0:
            print("Unentschieden!")
        elif gewinner == 1:
            self.siege[self.spieler2.name] += 1
            print(f"{self.spieler2.name} gewinnt!")
        else:
            self.siege[self.spieler.name] += 1
            print(f"{self.spieler.name} gewinnt!")

    def spiel(self, modus):
        if modus == "s":

            spieler_option = self.spieler.gewaehlte_option()
            self.computer_option = self.computer.gewaehlte_option()

            gewinner = 0
            if spieler_option == self.computer_option:
                gewinner = 0
            elif spieler_option not in self.regeln[self.computer_option]:
                gewinner = 2
            else:
                gewinner = 1

            self.symbol[spieler_option] += 1

            self.kommentareSolo(gewinner)

        if modus == "d":

            self.spieler2 = Spieler(input("Bitte Name angeben:"))

            if self.spieler2.name not in self.siege.keys():
                self.siege.update({self.spieler2.name: 0})

            spieler_option = self.spieler.gewaehlte_option()
            self.spieler2_option = self.spieler2.gewaehlte_option()

            gewinner = 0
            if spieler_option == self.spieler2_option:
                gewinner = 0
            elif spieler_option not in self.regeln[self.spieler2_option]:
                gewinner = 2
            else:
                gewinner = 1

            self.symbol[spieler_option] += 1
            self.symbol[self.spieler2_option] += 1

            self.kommentareDuo(gewinner)

    def main(self):
        spielmodus = input("Bitte Spielmodus (s)olo oder (d)uo angeben: ")
        while True:
            self.spiel(spielmodus)

            self.speichere_daten()

            print(f"{self.spieler.name}'s Siege: {self.siege[self.spieler.name]}")

            if spielmodus == "s":
                print(f"{self.computer.name}'s Siege: {self.siege[self.computer.name]}")

            if spielmodus == "d":
                print(f"{self.spieler2.name}'s Siege: {self.siege[self.spieler2.name]}")

            print("Symbol count:")
            for symbol, count in spiel.symbol.items():
                print(f"{symbol}: {count}")

            play_again = input("Noch eine Runde? (j)a: ")
            if play_again.lower() != "j":
                break


if __name__ == "__main__":
    spiel = Spiel()
    spiel.main()
