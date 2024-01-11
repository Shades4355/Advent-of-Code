import unittest
from advent9pt1 import start as start_pt1, get_input as get_input_pt1, parse_input as parse_input_pt1

class TestDay9(unittest.TestCase):
    test_data = "day9input_test.txt"

    def test_get_input_pt1(self):
        location = self.test_data
        answer = ["0 3 6 9 12 15",
                  "1 3 6 10 15 21",
                  "10 13 16 21 30 45"]
        
        self.assertEqual(get_input_pt1(location), answer)

    def test_parse_input_pt1(self):
        file = ["0 3 6 9 12 15",
                  "1 3 6 10 15 21",
                  "10 13 16 21 30 45"]
        answer = [[0, 3, 6, 9, 12, 15],
                  [1, 3, 6, 10, 15, 21],
                  [10, 13, 16, 21, 30, 45]]

        self.assertEqual(parse_input_pt1(file), answer)

    def test_start_pt1(self):
        file = self.test_data
        answer = 114

        self.assertEqual(start_pt1(file), answer)

#########
# Start #
#########
if __name__ == "__main__":
    unittest.main()