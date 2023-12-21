import unittest
from advent3pt1 import get_input, two_d_ify, test_num
from advent3pt2 import two_d_ify, find_gear, test_gear, find_gear_ratio, start as pt2start


class TestAdvent3pt2(unittest.TestCase):
    def test_get_input(self):
        one_d_list = ["467..114..", "...*......", "..35..633.", "......#...", "617*......", ".....+.58.", "..592.....", "......755.", "...$.*....", ".664.598.."]

        self.assertEqual(get_input("day3testInput.txt"), one_d_list)

    def test_two_d_ify(self):
        two_d_list = [["4", "6", "7", ".", ".", "1", "1", "4", ".", "."], [".", ".", ".", "*", ".", ".", ".", ".", ".", "."], [".", ".", "3", "5", ".", ".", "6", "3", "3", "."], [".", ".", ".", ".", ".", ".", "#", ".", ".", "."], ["6", "1", "7", "*", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", "+", ".", "5", "8", "."], [".", ".", "5", "9", "2", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", "7", "5", "5", "."], [".", ".", ".", "$", ".", "*", ".", ".", ".", "."], [".", "6", "6", "4", ".", "5", "9", "8", ".", "."]]

        self.assertEqual(two_d_ify(get_input("day3testInput.txt")), two_d_list)

    def test_test_gear(self):
        engine_list = two_d_ify(get_input("day3testInput.txt"))
        gear = test_gear(engine_list, 1, 3)
        not_gear = test_gear(engine_list, 4, 3)
        
        self.assertTrue(gear)
        self.assertFalse(not_gear)

    def test_find_gear(self):
        solution = 467835
        engine_list = two_d_ify(get_input("day3testInput.txt"))

        self.assertEqual(find_gear(engine_list), solution)
    
    def test_test_num(self):
        self.assertTrue(test_num("5"))
        self.assertFalse(test_num("*"))

    def test_find_gear_ratio(self):
        engine_list = two_d_ify(get_input("day3testInput.txt"))
        valid_gear_1 = [1, 3]
        answer_1 = 16345 # 467 * 35
        valid_gear_2 = [8, 5]
        answer_2 = 451490 # 755 * 598

        self.assertEqual(find_gear_ratio(engine_list, valid_gear_1[0], valid_gear_1[1]), answer_1)
        self.assertEqual(find_gear_ratio(engine_list, valid_gear_2[0], valid_gear_2[1]), answer_2)

    def test_start(self):
        answer = 467835

        self.assertEqual(pt2start("day3testInput.txt"), answer)

#########
# start #
#########
if __name__ == "__main__":
    unittest.main()
