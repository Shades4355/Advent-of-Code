import unittest
from advent6pt1 import get_input, start as start_pt1

class TestAdventDay6(unittest.TestCase):
    test_data = "day6input_test.txt"

    def test_get_input(self):
        file = get_input(self.test_data)
        answer = {
            "Time": [7, 15, 30],
            "Distance": [9, 40, 200]
        }

        self.assertEqual(file, answer)

    def test_start_pt1(self):
        answer = 288

        self.assertEqual(start_pt1(self.test_data), answer)


#########
# start #
#########
if __name__ == "__main__":
    unittest.main()