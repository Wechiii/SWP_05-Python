class Spieler:
    def __init__(self, name):
        self.name = name

    def gewaehlte_option(self):
        while True:
            try:
                # Spielerwahl abfragen
                option = int(input(
                    f"{self.name}, bitte wähle eine Option: (1)Schere, (2)Stein, (3)Papier, (4)Echse, (5)Spock: "))

                if option in range(1, 6):
                    return option
                else:
                    print("Ungültige Eingabe: Bitte wähle eine Zahl zwischen 1 und 5.")
            except ValueError:
                print("Ungültige Eingabe: Bitte wähle eine Zahl zwischen 1 und 5.")