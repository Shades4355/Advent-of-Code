import unittest
from advent6pt1 import get_input

class TestAdventDay6(unittest.TestCase):
    test_data = "day6input_test.txt"

    def test_get_input(self):
        file = get_input(self.test_data)
        answer = {
            "Time": [7, 15, 30],
            "Distance": [9, 40, 200]
        }

        self.assertEqual(file, answer)

#########
# start #
#########
if __name__ == "__main__":
    unittest.main()