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


def ist_straight_flush(hand):
    return ist_strasse(hand) and ist_flush(hand)


def ist_royal_flush(hand):
    royal_werte = ["10", "Bube", "Dame", "König", "Ass"]
    return ist_straight_flush(hand) and set([wert for farbe, wert in hand]) == set(royal_werte)


def ist_paar(hand):
    werte_in_hand = [wert for farbe, wert in hand]
    for wert in set(werte_in_hand):
        if werte_in_hand.count(wert) == 2:
            return True
    return False


def sind_zwei_paare(hand):
    werte_in_hand = [wert for farbe, wert in hand]
    for wert in set(werte_in_hand):
        if werte_in_hand.count(wert) == 2:
            andere_werte = set(werte_in_hand) - {wert}
            for anderer_wert in andere_werte:
                if werte_in_hand.count(anderer_wert) == 2:
                    return True
    return False


def ist_drilling(hand):
    werte_in_hand = [wert for farbe, wert in hand]
    for wert in set(werte_in_hand):
        if werte_in_hand.count(wert) == 3:
            return True
    return False


def ist_vierling(hand):
    werte_in_hand = [wert for farbe, wert in hand]
    for wert in set(werte_in_hand):
        if werte_in_hand.count(wert) == 4:
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


def karten_geben(karten, ergebnis):
    hand = random.choices(deck, k=karten)
    for karte in hand:
        print(f"{karte[0]} {karte[1]}")

    if ist_royal_flush(hand):
        ergebnis["Royale_Flush"] += 1
    elif ist_straight_flush(hand):
        ergebnis["Straight_Flush"] += 1
    elif ist_vierling(hand):
        ergebnis["Vierling"] += 1
    elif ist_full_house(hand):
        ergebnis["Full House"] += 1
    elif ist_flush(hand):
        ergebnis["Flush"] += 1
    elif ist_strasse(hand):
        ergebnis["Strasse"] += 1
    elif ist_drilling(hand):
        ergebnis["Drilling"] += 1
    elif sind_zwei_paare(hand):
        ergebnis["Zwei Paare"] += 1
    elif ist_paar(hand):
        ergebnis["Paar"] += 1


def statistic(anz_spiele):
    spiele = anz_spiele

    ergebnisse = {
        "Paar": 0,
        "Zwei Paare": 0,
        "Drilling": 0,
        "Vierling": 0,
        "Full House": 0,
        "Flush": 0,
        "Straight_Flush": 0,
        "Royale_Flush": 0,
        "Strasse": 0
    }

    for _ in range(spiele):
        karten_geben(5, ergebnisse)

    for key, value in ergebnisse.items():
        prozentsatz = (value / anz_spiele) * 100
        print(f"{key}: {prozentsatz:.6f} %")


if __name__ == '__main__':
    statistic(1000000)
