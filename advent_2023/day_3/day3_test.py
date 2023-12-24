import unittest
from advent3pt1 import get_input, two_d_ify, test_num, find_max_column
from advent3pt2 import two_d_ify, find_gear, test_gear, find_gear_ratio, start as pt2start, find_num


class TestAdventDay3(unittest.TestCase):
    def test_find_gear(self):
        solution_1 = 467835
        engine_list_1 = two_d_ify(get_input("day3testInput.txt"))
        solution_2 = 2344 * 23
        engine_list_2 = two_d_ify(get_input("day3testInput2.txt"))

        self.assertEqual(find_gear(engine_list_1), solution_1)
        self.assertEqual(find_gear(engine_list_2), solution_2)

    def test_find_gear_ratio(self):
        engine_list = two_d_ify(get_input("day3testInput.txt"))
        valid_gear_1 = [1, 3]
        answer_1 = 16345 # 467 * 35
        valid_gear_2 = [8, 5]
        answer_2 = 451490 # 755 * 598
        engine_list_2 = two_d_ify(get_input("day3testInput2.txt"))
        valid_gear_3 = [1, 4]
        answer_3 = 2344 * 23

        self.assertEqual(find_gear_ratio(engine_list, valid_gear_1[0], valid_gear_1[1]), answer_1)
        self.assertEqual(find_gear_ratio(engine_list, valid_gear_2[0], valid_gear_2[1]), answer_2)
        self.assertEqual(find_gear_ratio(engine_list_2, valid_gear_3[0], valid_gear_3[1]), answer_3)

    def test_find_max_column(self):
        cols = 10
        engine_list = two_d_ify(get_input("day3testInput.txt"))
        max_col = find_max_column(engine_list)

        self.assertEqual(max_col, cols)

    def test_find_num(self):
        input_list = two_d_ify(get_input("day3testInput2.txt"))
        number_set1 = [-3, 4]
        number_set2 = [0, 2]

        self.assertEqual(find_num(input_list, 0, 3), number_set1)
        self.assertEqual(find_num(input_list, 0, 5), number_set2)

    def test_get_input(self):
        one_d_list = ["467..114..", "...*......", "..35..633.", "......#...", "617*......", ".....+.58.", "..592.....", "......755.", "...$.*....", ".664.598.."]

        self.assertEqual(get_input("day3testInput.txt"), one_d_list)

    def test_test_gear(self):
        engine_list = two_d_ify(get_input("day3testInput.txt"))
        gear = test_gear(engine_list, 1, 3)
        not_gear = test_gear(engine_list, 4, 3)

        engine_list_2 = two_d_ify(get_input("day3testInput2.txt"))
        gear_2 = test_gear(engine_list_2, 1, 4)
        
        self.assertTrue(gear)
        self.assertFalse(not_gear)

        self.assertTrue(gear_2)

    def test_test_num(self):
        self.assertTrue(test_num("5"))
        self.assertFalse(test_num("*"))

    def test_two_d_ify(self):
        two_d_list = [["4", "6", "7", ".", ".", "1", "1", "4", ".", "."],
                      [".", ".", ".", "*", ".", ".", ".", ".", ".", "."],
                      [".", ".", "3", "5", ".", ".", "6", "3", "3", "."],
                      [".", ".", ".", ".", ".", ".", "#", ".", ".", "."],
                      ["6", "1", "7", "*", ".", ".", ".", ".", ".", "."],
                      [".", ".", ".", ".", ".", "+", ".", "5", "8", "."],
                      [".", ".", "5", "9", "2", ".", ".", ".", ".", "."],
                      [".", ".", ".", ".", ".", ".", "7", "5", "5", "."],
                      [".", ".", ".", "$", ".", "*", ".", ".", ".", "."],
                      [".", "6", "6", "4", ".", "5", "9", "8", ".", "."]]

        self.assertEqual(two_d_ify(get_input("day3testInput.txt")), two_d_list)

    def test_start3pt2(self):
        answer = (467 * 35) + (755 * 598)
        self.assertEqual(pt2start("day3testInput.txt"), answer)

        answer_2 = 2344 * 23
        self.assertEqual(pt2start("day3testInput2.txt"), answer_2)

#########
# start #
#########
if __name__ == "__main__":
    unittest.main()
