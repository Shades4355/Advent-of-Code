import unittest
from advent3pt1 import get_input, two_d_ify, test_num
from advent3pt2 import two_d_ify, find_gear


class TestAdvent3pt2(unittest.TestCase):
    def test_get_input(self):
        prompt = ["467..114..", "...*......", "..35..633.", "......#...", "617*......", ".....+.58.", "..592.....", "......755.", "...$.*....", ".664.598.."]

        self.assertEqual(get_input("day3pt2testInput.txt"), prompt)

    def test_two_d_ify(self):
        two_d_list = [["4", "6", "7", ".", ".", "1", "1", "4", ".", "."], [".", ".", ".", "*", ".", ".", ".", ".", ".", "."], [".", ".", "3", "5", ".", ".", "6", "3", "3", "."], [".", ".", ".", ".", ".", ".", "#", ".", ".", "."], ["6", "1", "7", "*", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", "+", ".", "5", "8", "."], [".", ".", "5", "9", "2", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", "7", "5", "5", "."], [".", ".", ".", "$", ".", "*", ".", ".", ".", "."], [".", "6", "6", "4", ".", "5", "9", "8", ".", "."]]

        self.assertEqual(two_d_ify(get_input("day3pt2testInput.txt")), two_d_list)

    def test_find_gear(self):
        solution = 467835
        engine_list = two_d_ify(get_input("day3pt2testInput.txt"))

        self.assertEqual(find_gear(engine_list), solution)
    
    def test_test_num(self):
        self.assertTrue(test_num("5"))
        self.assertFalse(test_num("*"))


#########
# start #
#########
if __name__ == "__main__":
    unittest.main()
