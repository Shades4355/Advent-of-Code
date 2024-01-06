import unittest
from advent7pt1 import start as start_pt1, get_input

class TestAdventDay7(unittest.TestCase):
    test_input = "day7input_test.txt"

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