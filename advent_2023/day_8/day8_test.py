import unittest
from advent8pt1 import start as start_pt1, get_input, parse_input as parse_input_pt1, follow_directions as follow_directions_pt1
from advent8pt2 import start as start_pt2, parse_input as parse_input_pt2, follow_directions as follow_directions_pt2, all_end_in_z


class TestDay8(unittest.TestCase):
    test_data1 = "day8input_test.txt"
    test_data2 = "day8input_test2.txt"
    test_data3 = "day8input_test3.txt"

    def test_all_end_in_z(self):
        def test_true_1(self):
            '''test for True outcome with 3 placement values'''
            placement = ["ZZZ", "WJZ", "HSZ"]

            return self.assertTrue(all_end_in_z(placement))
        
        def test_true_2(self):
            '''tests for True outcome with only 1 placement value1'''
            placement = ["YPZ"]

            return self.assertTrue(all_end_in_z(placement))
        
        def test_false_1(self):
            '''Tests for a False outcome with 3rd value not ending in "Z"'''
            placement = ["ZZZ", "WJZ", "AAA"]

            return self.assertFalse(all_end_in_z(placement))
        
        def test_false_2(self):
            '''Tests for a False outcome with 2nd value not ending in "Z"'''
            placement = ["ZZZ", "WJY", "AAZ"]

            return self.assertFalse(all_end_in_z(placement))
        
        def test_false_3(self):
            '''Tests for a False outcome with 2nd & 3rd values not ending in "Z"'''
            placement = ["ZZZ", "WJU", "AAA"]

            return self.assertFalse(all_end_in_z(placement))
        
        def test_false_4(self):
            '''Tests for a False outcome with no values ending in "Z"'''
            placement = ["ZZA", "WJU", "AAA"]

            return self.assertFalse(all_end_in_z(placement))

        test_true_1(self)
        test_true_2(self)
        test_false_1(self)
        test_false_2(self)
        test_false_3(self)
        test_false_4(self)

    def test_follow_directions(self):
        def test_1(self):
            '''Tests follow_directions_pt1'''
            file = {
                "directions": ["R", "L"],
                "start": "AAA",
                "AAA": ["BBB", "CCC"],
                "BBB": ["DDD", "EEE"],
                "CCC": ["ZZZ", "GGG"],
                "DDD": ["DDD", "DDD"],
                "EEE": ["EEE", "EEE"],
                "GGG": ["GGG", "GGG"],
                "ZZZ": ["ZZZ", "ZZZ"]
            }
            answer = 2

            return self.assertEqual(follow_directions_pt1(file), answer)
        def test_2(self):
            '''Tests follow_directions_pt1'''
            file = {"directions": ["L", "L", "R"],
                    "start": "AAA",
                    "AAA": ["BBB", "BBB"],
                    "BBB": ["AAA", "ZZZ"],
                    "ZZZ": ["ZZZ", "ZZZ"]}
            answer = 6

            return self.assertEqual(follow_directions_pt1(file), answer)

        def test_3(self):
            '''Tests follow_directions_pt1'''
            file = {
                "directions": ["R", "L"],
                "start": "AAA",
                "AAA": ["BBB", "CCC"],
                "BBB": ["DDD", "EEE"],
                "CCC": ["ZZZ", "GGG"],
                "DDD": ["DDD", "DDD"],
                "EEE": ["EEE", "EEE"],
                "GGG": ["GGG", "GGG"],
                "ZZZ": ["AAA", "BBB"]
            }
            answer = 2

            return self.assertEqual(follow_directions_pt1(file), answer)
        def test_4(self):
            '''Tests follow_directions_pt2'''
            file = {
                "directions": ["L", "R"],
                "start": ["11A", "22A"],
                "11A": ["11B", "XXX"],
                "11B": ["XXX", "11Z"],
                "11Z": ["11B", "XXX"],
                "22A": ["22B", "XXX"],
                "22B": ["22C", "22C"],
                "22C": ["22Z", "22Z"],
                "22Z": ["22B", "22B"],
                "XXX": ["XXX", "XXX"]
            }
            answer = 6

            return self.assertEqual(follow_directions_pt2(file), answer)

        test_1(self)
        test_2(self)
        test_3(self)
        test_4(self)

    def test_get_input(self):
        def test_1(self):
            file1 = self.test_data1
            answer = ["RL\n", "\n", "AAA = (BBB, CCC)\n", "BBB = (DDD, EEE)\n", "CCC = (ZZZ, GGG)\n", "DDD = (DDD, DDD)\n", "EEE = (EEE, EEE)\n", "GGG = (GGG, GGG)\n", "ZZZ = (ZZZ, ZZZ)"]

            return self.assertEqual(get_input(file1), answer)
        
        def test_2(self):
            file2 = self.test_data2
            answer = ["LLR\n", "\n", "AAA = (BBB, BBB)\n", "BBB = (AAA, ZZZ)\n", "ZZZ = (ZZZ, ZZZ)"]

            return self.assertEqual(get_input(file2), answer)

        test_1(self)
        test_2(self)

    def test_parse_input(self):
        def test_1(self):
            '''Tests parse_input_pt1'''
            file = ["LLR\n", "\n", "AAA = (BBB, BBB)\n", "BBB = (AAA, ZZZ)\n", "ZZZ = (ZZZ, ZZZ)"]
            answer = {"directions": ["L", "L", "R"],
                  "start": "AAA",
                  "AAA": ["BBB", "BBB"],
                  "BBB": ["AAA", "ZZZ"],
                  "ZZZ": ["ZZZ", "ZZZ"]}

            return self.assertEqual(parse_input_pt1(file), answer)
        
        def test_2(self):
            '''Tests parse_input_pt2'''
            file = ["LR\n", "\n", "11A = (11B, XXX)\n", "11B = (XXX, 11Z)\n", "11Z = (11B, XXX)\n", "22A = (22B, XXX)\n", "22B = (22C, 22C\n", "22C = (22Z, 22Z)\n", "22Z = (22B, 22B)\n", "XXX = (XXX, XXX)"]
            answer = {
                "directions": ["L", "R"],
                "start": ["11A", "22A"],
                "11A": ["11B", "XXX"],
                "11B": ["XXX", "11Z"],
                "11Z": ["11B", "XXX"],
                "22A": ["22B", "XXX"],
                "22B": ["22C", "22C"],
                "22C": ["22Z", "22Z"],
                "22Z": ["22B", "22B"],
                "XXX": ["XXX", "XXX"]
            }

            return self.assertEqual(parse_input_pt2(file), answer)

        test_1(self)
        test_2(self)

    def test_start_pt1(self):
        def test_1(self):
            file1 = self.test_data1
            answer = 2

            return self.assertEqual(start_pt1(file1), answer)
    
        def test_2(self):
            file2 = self.test_data2
            answer = 6

            return self.assertEqual(start_pt1(file2), answer)
        
        test_1(self)
        test_2(self)

    def test_start_pt2(self):
        file = self.test_data3
        answer = 6

        self.assertEqual(start_pt2(file), answer)

#########
# Start #
#########
if __name__ == "__main__":
    unittest.main()