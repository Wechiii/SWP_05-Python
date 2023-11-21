import sys
import unittest
from pokerspielsimulator import ist_paar, sind_zwei_paare, ist_drilling, \
    ist_strasse, ist_flush, ist_full_house, ist_vierling, ist_straight_flush, ist_royal_flush


class TestPokerSpiel(unittest.TestCase):
    def setUp(self):
        self.gespeicherter_stdout = sys.stdout

    def tearDown(self):
        sys.stdout = self.gespeicherter_stdout

    def test_ist_paar(self):
        hand = [("Herz", "Ass"), ("Karo", "Ass"), ("Pik", "7"), ("Kreuz", "3"), ("Herz", "5")]
        self.assertTrue(ist_paar(hand))

    def test_sind_zwei_paare_nicht(self):
        hand = [("Herz", "Ass"), ("Karo", "König"), ("Pik", "7"), ("Kreuz", "7"), ("Herz", "5")]
        self.assertFalse(sind_zwei_paare(hand))

    def test_ist_drilling_nicht(self):
        hand = [("Herz", "Ass"), ("Karo", "König"), ("Pik", "7"), ("Kreuz", "7"), ("Herz", "5")]
        self.assertFalse(ist_drilling(hand))

    def test_ist_strasse(self):
        hand = [("Herz", "7"), ("Karo", "8"), ("Pik", "9"), ("Kreuz", "10"), ("Herz", "Bube")]
        self.assertTrue(ist_strasse(hand))

    def test_ist_flush(self):
        hand = [("Herz", "7"), ("Herz", "8"), ("Herz", "9"), ("Herz", "König"), ("Herz", "Bube")]
        self.assertTrue(ist_flush(hand))

    def test_ist_full_house_nicht(self):
        hand = [("Herz", "Ass"), ("Karo", "Ass"), ("Pik", "7"), ("Kreuz", "7"), ("Herz", "5")]
        self.assertFalse(ist_full_house(hand))

    def test_ist_vierling(self):
        hand = [("Herz", "Ass"), ("Karo", "Ass"), ("Pik", "Ass"), ("Kreuz", "Ass"), ("Herz", "7")]
        self.assertTrue(ist_vierling(hand))

    def test_ist_straight_flush(self):
        hand = [("Herz", "7"), ("Herz", "8"), ("Herz", "9"), ("Herz", "10"), ("Herz", "Bube")]
        self.assertTrue(ist_straight_flush(hand))

    def test_ist_royal_flush(self):
        hand = [("Herz", "10"), ("Herz", "Bube"), ("Herz", "Dame"), ("Herz", "König"), ("Herz", "Ass")]
        self.assertTrue(ist_royal_flush(hand))


if __name__ == '__main__':
    unittest.main()
