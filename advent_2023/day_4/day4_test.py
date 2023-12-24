import unittest
from advent4pt1 import get_input, parse_card, read_scratchcard as read_scratchcard_pt1
from advent4pt2 import total_scratchcards, read_scratchcard as read_scratchcard_pt2


class TestAdventDay4(unittest.TestCase):
    testInput = "day4input_test.txt"

    def test_get_input(self):
        input_list = ["Card   1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53", "Card   2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19", "Card   3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1", "Card   4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83", "Card   5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36", "Card   6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"]

        self.assertEqual(get_input(self.testInput), input_list)

    def test_parse_card(self):
        scratchcard = {
            "Card 1": [
                ["41", "48", "83", "86", "17"], ["83", "86", "6", "31", "17", "9", "48", "53"]],
            "Card 2": [
                ["13", "32", "20", "16", "61"], ["61", "30", "68", "82", "17", "32", "24", "19"]],
            "Card 3": [
                ["1", "21", "53", "59", "44"],["69", "82", "63", "72", "16", "21", "14", "1"]],
            "Card 4": [
                ["41", "92", "73", "84", "69"], ["59", "84", "76", "51", "58", "5", "54", "83"]],
            "Card 5": [
                ["87", "83", "26", "28", "32"], ["88", "30", "70", "12", "93", "22", "82", "36"]],
            "Card 6": [
                ["31", "18", "13", "56", "72"], ["74", "77", "10", "23", "35", "67", "36", "11"]],}

        self.assertEqual(parse_card(get_input(self.testInput)), scratchcard)

    def test_read_scratchcard_pt1(self):
        total = 13

        self.assertEqual(read_scratchcard_pt1(parse_card(get_input(self.testInput))), total)

    def test_read_scratchcard_pt2(self):
        card_stack = parse_card(get_input(self.testInput))
        total_1 = 4
        total_2 = 2
        total_3 = 2

        self.assertEqual(read_scratchcard_pt2(card_stack['Card 1']), total_1)
        self.assertEqual(read_scratchcard_pt2(card_stack['Card 2']), total_2)
        self.assertEqual(read_scratchcard_pt2(card_stack['Card 3']), total_3)

    def test_total_scratchcards(self):
        total = 30
        scratchcard = parse_card(get_input(self.testInput))

        self.assertEqual(total_scratchcards(scratchcard), total)


#########
# start #
#########
if __name__ == "__main__":
    unittest.main()