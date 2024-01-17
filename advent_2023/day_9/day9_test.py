import unittest
from advent9pt1 import start as start_pt1, get_input as get_input_pt1, parse_input as parse_input_pt1, find_next_line, find_number

class TestDay9(unittest.TestCase):
    test_data = "day9input_test.txt"

    def test_find_next_line(self):
        def test_1(self):
            prompt = [2, 4, 5, 2, 6]
            answer = [False, [2, 1, -3, 4]]

            return self.assertEqual(find_next_line(prompt), answer)
        
        def test_2(self):
            prompt = [0, 0, 1, 0, 0]
            answer = [False, [0, 1, -1, 0]]

            return self.assertEqual(find_next_line(prompt), answer)
        
        def test_3(self):
            prompt = [1, 0, 0, 1]
            answer = [False, [-1, 0, 1]]

            return self.assertEqual(find_next_line(prompt), answer)
        
        def test_4(self):
            prompt = [7, 9]
            answer = [False, [2]]
            return self.assertEqual(find_next_line(prompt), answer)

        def test_5(self):
            prompt = [0, 0, 0, 0]
            answer = [True, [0, 0, 0]]

            return self.assertEqual(find_next_line(prompt), answer)
        
        def test_6(self):
            prompt = [0]
            answer = [True, []]
        
        # Tests for False return, plus new list
        test_1(self)
        test_2(self)
        test_3(self)
        test_4(self)

        # Tests for True return, plus a list of 0s
        test_5(self)
        test_6(self)

    def test_find_number(self):
        file = [[1, 5, 9, 19],
                [4, 7, 10],
                [3, 3],
                [0]]
        answer = 32

        self.assertEqual(find_number(file), answer)

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