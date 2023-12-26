import unittest
from advent5pt1 import get_input, parse_input, start, get_seed_list, find_last_seed, get_blank_map_list, par_fill_map, fill_map, create_blank_maps, fill_in_maps


class TestAdventDay5pt1(unittest.TestCase):
    testInput = "day5input_test.txt"

    def test_create_blank_maps(self):
        length = 5
        parsed_input = {
            "seeds": [79, 14, 55, 13],
            "seed-to-soil": {"0": [50, 98, 2],
                            "1": [52, 50, 48]},
            "soil-to-fertilizer": {"0": [0, 15, 37],
                                    "1": [37, 52, 2],
                                    "2": [39, 0, 15]},
            "fertilizer-to-water": {"0": [49, 53, 8],
                                    "1": [0, 11, 42],
                                    "2": [42, 0, 7],
                                    "3": [57, 7, 4]}
                                    }
        answer = {
            "blank_soil_list": ["", "", "", "", ""],
            "blank_fertilizer_list": ["", "", "", "", ""],
            "blank_water_list": ["", "", "", "", ""]
                  }
        length_2 = 10
        parsed_input_2 = {
            "seeds": [79, 14, 55, 13],
            "seed-to-soil": {"0": [50, 98, 2],
                            "1": [52, 50, 48]},
            "soil-to-fertilizer": {"0": [0, 15, 37],
                                    "1": [37, 52, 2],
                                    "2": [39, 0, 15]},
            "fertilizer-to-water": {"0": [49, 53, 8],
                                    "1": [0, 11, 42],
                                    "2": [42, 0, 7],
                                    "3": [57, 7, 4]}
                                    }
        answer_2 = {
            "blank_soil_list": ["", "", "", "", "", "", "", "", "", ""],
            "blank_fertilizer_list": ["", "", "", "", "", "", "", "", "", ""],
            "blank_water_list": ["", "", "", "", "", "", "", "", "", ""]
                  }

        self.assertEqual(create_blank_maps(parsed_input, length), answer)
        self.assertEqual(create_blank_maps(parsed_input_2, length_2), answer_2)

    def test_fill_map(self):
        source = [0, 1, 2, 3, 4, 5, 6]
        par_fill_map = [["", 2, "", 7, 8, 9, ""]]
        answer = [[0, 2, 2, 7, 8, 9, 6]]

        self.assertEqual(fill_map(source, par_fill_map), answer)

    def test_fill_in_maps(self): # TODO: write
        parsed_input = {"seeds": [0, 1, 2, 3, 4, 5, 6],
                        "seed-to-soil": {"0": [2, 1, 1],
                                         "1": [7, 3, 3]}}
        blank_map = {"blank_soil_map": ["", "", "", "", "", "", ""]}
        answer = {"soil": [[0, 2, 2, 7, 8, 9, 6]]}
        seed_list = [0, 1, 2, 3, 4, 5, 6]
        
        self.assertEqual(fill_in_maps(parsed_input, seed_list, blank_map), answer)

    def test_find_last_seed(self): # TODO: re-write to use only handwritten inputs
        answer = 100
        parsedInput = parse_input(get_input(self.testInput))

        self.assertEqual(find_last_seed(parsedInput), answer)

    def test_get_blank_map_list(self):
        answer = ["", "", "", "", ""]
        seed_len = 5
        answer_2 = [""]
        seed_len_2 = 1

        self.assertEqual(get_blank_map_list(seed_len), answer)
        self.assertEqual(get_blank_map_list(seed_len_2), answer_2)
  
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

    def test_get_seed_list(self):
        answer = [i for i in range(0, 100)]
        seed_list = get_seed_list(99)

        self.assertEqual(seed_list, answer)

    def test_par_fill_map(self):
        source = [1, 2, 3, 4, 5, 6]
        dest = ["", "", "", "", "", ""]
        rules = {"0": [2, 1, 1], "1": [7, 3, 3]}
        answer = [2, "", 7, 8, 9, ""]

        self.assertEqual(par_fill_map(source, dest, rules), answer)

    def test_parse_input(self):
        file = {
            "seeds": [79, 14, 55, 13],
            "seed-to-soil": {"0": [50, 98, 2],
                                  "1": [52, 50, 48]},
            "soil-to-fertilizer": {"0": [0, 15, 37],
                                        "1": [37, 52, 2],
                                        "2": [39, 0, 15]},
            "fertilizer-to-water": {"0": [49, 53, 8],
                                        "1": [0, 11, 42],
                                        "2": [42, 0, 7],
                                        "3": [57, 7, 4]},
            "water-to-light": {"0": [88, 18, 7],
                                   "1": [18, 25, 70]},
            "light-to-temperature": {"0": [45, 77, 23],
                                        "1": [81, 45, 19],
                                        "2": [68, 64, 13]},
            "temperature-to-humidity": {"0": [0, 69, 1],
                                            "1": [1, 0, 69]},
            "humidity-to-location":  {"0": [60, 56, 37],
                                          "1": [56, 93, 4]}
        }
        
        self.assertEqual(parse_input(get_input(self.testInput)), file)

    def test_start(self):
        answer = 35

        self.assertEqual(start(self.testInput), answer)


#########
# start #
#########
if __name__ == "__main__":
    unittest.main()