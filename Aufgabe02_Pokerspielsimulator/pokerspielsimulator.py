import random

farben = ["Herz", "Karo", "Kreuz", "Pik"]
werte = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Bube", "Dame", "König", "Ass"]

deck = [(farbe, wert) for farbe in farben for wert in werte]


def ist_flush(hand):
    symbole = [karte[0] for karte in hand]
    return len(set(symbole)) == 1


def ist_strasse(hand):
    werte_in_hand = [wert for farbe, wert in hand]
    sortierte_werte = sorted(werte_in_hand, key=lambda x: werte.index(x))
    for i in range(len(sortierte_werte) - 1):
        if werte.index(sortierte_werte[i]) + 1 != werte.index(sortierte_werte[i + 1]):
            return False
    return True


def ist_paar(hand):
    werte_in_hand = [wert for farbe, wert in hand]
    for wert in set(werte_in_hand):
        if werte_in_hand.count(wert) >= 2:
            return True
    return False


def sind_zwei_paare(hand):
    werte_in_hand = [wert for farbe, wert in hand]
    for wert in set(werte_in_hand):
        if werte_in_hand.count(wert) >= 2:
            andere_werte = set(werte_in_hand) - {wert}
            for anderer_wert in andere_werte:
                if werte_in_hand.count(anderer_wert) >= 2:
                    return True
    return False


def ist_drilling(hand):
    werte_in_hand = [wert for farbe, wert in hand]
    for wert in set(werte_in_hand):
        if werte_in_hand.count(wert) >= 3:
            return True
    return False


def ist_vierling(hand):
    werte_in_hand = [wert for farbe, wert in hand]
    for wert in set(werte_in_hand):
        if werte_in_hand.count(wert) >= 4:
            return True
    return False


def ist_full_house(hand):
    werte_in_hand = [wert for farbe, wert in hand]
    for wert in set(werte_in_hand):
        if werte_in_hand.count(wert) == 3:
            andere_werte = set(werte_in_hand) - {wert}
            for anderer_wert in andere_werte:
                if werte_in_hand.count(anderer_wert) == 2:
                    return True
    return False


def karten_geben(karten):
    hand = random.choices(deck, k=karten)
    for karte in hand:
        print(f"{karte[0]} {karte[1]}")
    if ist_paar(hand):
        ergebnisse["Paar"] += 1
    if sind_zwei_paare(hand):
        ergebnisse["Zwei Paare"] += 1
    if ist_drilling(hand):
        ergebnisse["Drilling"] += 1
    if ist_vierling(hand):
        ergebnisse["Vierling"] += 1
    if ist_full_house(hand):
        ergebnisse["Full House"] += 1
    if ist_flush(hand):
        ergebnisse["Flush"] += 1
    if ist_strasse(hand):
        ergebnisse["Strasse"] += 1
    # print(" ")
    # print("Paar:", ist_paar(hand))
    # print(" ")
    # print("Zwei Paare:", sind_zwei_paare(hand))
    # print(" ")
    # print("Drilling:", ist_drilling(hand))
    # print(" ")
    # print("Vierling:", ist_vierling(hand))
    # print(" ")
    # print("Full House:", ist_full_house(hand))
    # print(" ")
    # print("Flush:", ist_flush(hand))
    # print(" ")
    # print("Strasse:", ist_strasse(hand))
    # print(" ")


if __name__ == '__main__':
    spiele = 100000

    ergebnisse = {
        "Paar": 0,
        "Zwei Paare": 0,
        "Drilling": 0,
        "Vierling": 0,
        "Full House": 0,
        "Flush": 0,
        "Strasse": 0
    }

    for _ in range(spiele):
        karten_geben(5)

    gesamtkombinationen = spiele

    for key, value in ergebnisse.items():
        prozentsatz = (value / gesamtkombinationen) * 100
        print(f"{key}: {prozentsatz:.2f}%")
