import unittest
from advent7pt1 import start as start_pt1, get_input, find_hand_type

class TestAdventDay7(unittest.TestCase):
    test_input = "day7input_test.txt"

    def test_find_hand_type(self):
        def test_one_pair(self):
            hand = {
                    "hand": "32T3K",
                    "wager": 765,
                    "hand type": "",
                    "ranking": 0
            }
            answer = "One Pair"

            return self.assertEqual(find_hand_type(hand), answer)
        
        def test_three_of_a_kind(self):
            hand = {
                "hand": "T55J5",
                "wager": 684,
                "hand type": "",
                "ranking": 0
            }
            answer = "Three of a Kind"

            return self.assertEqual(find_hand_type(hand), answer)

        def test_two_pair(self):
            hand = {
                "hand": "KK677",
                "wager": 28,
                "hand type": "",
                "ranking": 0
            }
            answer = "Two Pair"

            return self.assertEqual(find_hand_type(hand), answer)

        def test_full_house(self):
            hand = {
                "hand": "KKKJJ"
            }
            answer = "Full House"

            return self.assertEqual(find_hand_type(hand), answer)

        def test_five_of_a_kind(self):
            hand = {
                "hand": "AAAAA"
            }
            answer = "Five of a Kind"

            return self.assertEqual(find_hand_type(hand), answer)

        def test_four_of_a_kind(self):
            hand = {
                "hand": "2222Q"
            }
            answer = "Four of a Kind"

            return self.assertEqual(find_hand_type(hand), answer)

        def test_high_card(self):
            hand = {
                "hand": "12345"
            }
            answer = "High Card"

            return self.assertEqual(find_hand_type(hand), answer)
        
        test_five_of_a_kind(self)
        test_four_of_a_kind(self)
        test_full_house(self)
        test_three_of_a_kind(self)
        test_two_pair(self)
        test_one_pair(self)
        test_high_card(self)
        
        


    def test_get_input(self):
        answer = {
            "hand 1": {
                "hand": "32T3K",
                "wager": 765,
                "hand type": "",
                "ranking": 0
            },
            "hand 2": {
                "hand": "T55J5",
                "wager": 684,
                "hand type": "",
                "ranking": 0
            },
            "hand 3": {
                "hand": "KK677",
                "wager": 28,
                "hand type": "",
                "ranking": 0
            },
            "hand 4": {
                "hand": "KTJJT",
                "wager": 220,
                "hand type": "",
                "ranking": 0
            },
            "hand 5": {
                "hand": "QQQJA",
                "wager": 483,
                "hand type": "",
                "ranking": 0
            }
        }
        file = get_input(self.test_input)

        self.assertEqual(file, answer)

    def test_start(self):
        def test_pt1(self):
            answer = 6440
            
            return self.assertEqual(start_pt1(self.test_input), answer)
        
        test_pt1(self)


#########
# start #
#########
if __name__ == "__main__":
    unittest.main()