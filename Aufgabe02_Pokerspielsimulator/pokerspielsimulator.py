import random

farben = ["Herz", "Karo", "Kreuz", "Pik"]
werte = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Bube", "Dame", "König", "Ass"]

deck = [(farbe, wert) for farbe in farben for wert in werte]

def ist_flush(hand):


def ist_strasse(hand):


def ist_paar(hand):


def sind_zwei_paare(hand):


def ist_drilling(hand):


def ist_vierling(hand):


def ist_full_house(hand):


def karten_geben(karten):
    hand = random.choices(deck, k=karten)
    for karte in hand:
        print(f"{karte[0]} {karte[1]}")
        print(" ")
        print("Paar:", ist_paar(hand))
        print(" ")
        print("Zwei Paare:", sind_zwei_paare(hand))
        print(" ")
        print("Drilling:", ist_drilling(hand))
        print(" ")
        print("Vierling:", ist_vierling(hand))
        print(" ")
        print("Full House:", ist_full_house(hand))
        print(" ")


if __name__ == '__main__':
    karten_geben(5)

