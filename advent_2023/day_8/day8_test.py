import unittest
from advent8pt1 import start as start_pt1, get_input, parse_input, follow_directions


class TestDay8(unittest.TestCase):
    test_data1 = "day8input_test.txt"
    test_data2 = "day8input_test2.txt"

    def test_follow_directions(self):
        def test_1(self):
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

            return self.assertEqual(follow_directions(file), answer)
        
        def test_2(self):
            file = {"directions": ["L", "L", "R"],
                    "start": "AAA",
                    "AAA": ["BBB", "BBB"],
                    "BBB": ["AAA", "ZZZ"],
                    "ZZZ": ["ZZZ", "ZZZ"]}
            answer = 6

            return self.assertEqual(follow_directions(file), answer)
        
        test_1(self)
        test_2(self)

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
        file = ["LLR\n", "\n", "AAA = (BBB, BBB)\n", "BBB = (AAA, ZZZ)\n", "ZZZ = (ZZZ, ZZZ)"]
        answer = {"directions": ["L", "L", "R"],
                  "start": "AAA",
                  "AAA": ["BBB", "BBB"],
                  "BBB": ["AAA", "ZZZ"],
                  "ZZZ": ["ZZZ", "ZZZ"]}

        self.assertEqual(parse_input(file), answer)

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


#########
# Start #
#########
if __name__ == "__main__":
    unittest.main()