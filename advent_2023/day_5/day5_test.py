import unittest
from advent5pt1 import get_input, parse_input, start, get_seed_list, find_last_seed


class TestAdventDay5pt1(unittest.TestCase):
    testInput = "day5input_test.txt"

    def test_get_input(self):
        file = [
            "seeds: 79 14 55 13",
            "",
            "seed-to-soil map:",
            "50 98 2",
            "52 50 48",
            "",
            "soil-to-fertilizer map:",
            "0 15 37",
            "37 52 2",
            "39 0 15",
            "",
            "fertilizer-to-water map:",
            "49 53 8",
            "0 11 42",
            "42 0 7",
            "57 7 4",
            "",
            "water-to-light map:",
            "88 18 7",
            "18 25 70",
            "",
            "light-to-temperature map:",
            "45 77 23",
            "81 45 19",
            "68 64 13",
            "",
            "temperature-to-humidity map:",
            "0 69 1",
            "1 0 69",
            "",
            "humidity-to-location map:",
            "60 56 37",
            "56 93 4"
        ]

        self.assertEqual(get_input(self.testInput), file)

    def test_parse_input(self):
        self.maxDiff = 50
        file = {
            "seeds": [79, 14, 55, 13],
            "seed-to-soil map:": {"0": [50, 98, 2],
                                  "1": [52, 50, 48]},
            "soil-to-fertilizer map:": {"0": [0, 15, 37],
                                        "1": [37, 52, 2],
                                        "2": [39, 0, 15]},
            "fertilizer-to-water map:": {"0": [49, 53, 8],
                                        "1": [0, 11, 42],
                                        "2": [42, 0, 7],
                                        "3": [57, 7, 4]},
            "water-to-light map:": {"0": [88, 18, 7],
                                   "1": [18, 25, 70]},
            "light-to-temperature map:": {"0": [45, 77, 23],
                                        "1": [81, 45, 19],
                                        "2": [68, 64, 13]},
            "temperature-to-humidity map:": {"0": [0, 69, 1],
                                            "1": [1, 0, 69]},
            "humidity-to-location map:":  {"0": [60, 56, 37],
                                          "1": [56, 93, 4]}
        }
        
        self.assertEqual(parse_input(get_input(self.testInput)), file)

    def test_get_seed_list(self):
        answer = [i for i in range(0, 100)]
        parsedInput = parse_input(get_input(self.testInput))
        seed_list = get_seed_list(99)

        self.assertEqual(seed_list, answer)

    def test_find_last_seed(self):
        answer = 100
        parsedInput = parse_input(get_input(self.testInput))

        self.assertEqual(find_last_seed(parsedInput), answer)

    def test_start(self):
        answer = 35

        self.assertEqual(start(self.testInput), answer)


#########
# start #
#########
if __name__ == "__main__":
    unittest.main()