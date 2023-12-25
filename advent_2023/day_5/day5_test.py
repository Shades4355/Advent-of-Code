import unittest
from advent5pt1 import get_input, parse_input


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
        file = {
            "seeds": ["79", "14", "55", "13"],
            "seed-to-soil map": [["50", "98", "2"],
                                  ["52", "50", "48"]],
            "soil-to-fertilizer map": [["0", "15", "37"],
                                        [],
                                        []],
            "fertilizer-to-water map": [[],
                                        [],
                                        [],
                                        []],
            "water-to-light map": [[],
                                   []],
            "light-to-temperature map": [[],
                                        [],
                                        []],
            "temperature-to-humidity map": [[],
                                            []],
            "humidity-to-location map":  [[],
                                          []]
        }
        
        self.assertEqual(get_input(self.testInput), file)


#########
# start #
#########
if __name__ == "__main__":
    unittest.main()