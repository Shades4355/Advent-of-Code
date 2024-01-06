import unittest
from advent6pt1 import get_input as get_input_pt1, start as start_pt1, run_race, find_shortest_press, find_longest_press
from advent6pt2 import get_input as get_input_pt2, start as start_pt2

class TestAdventDay6(unittest.TestCase):
    test_data = "day6input_test.txt"

    def test_find_longest_press(self):
        def test_1(self):
            time = 7
            distance = 9
            answer = 5

            return self.assertEqual(find_longest_press(time, distance), answer)
        
        def test_2(self):
            time = 15
            distance = 40
            answer = 11

            return self.assertEqual(find_longest_press(time, distance), answer)

        def test_3(self):
            time = 30
            distance = 200
            answer = 19

            return self.assertEqual(find_longest_press(time, distance), answer)

        test_1(self)
        test_2(self)
        test_3(self)

    def test_find_shortest_press(self):
        def test_1(self):
            time = 7
            distance = 9
            answer = 2

            return self.assertEqual(find_shortest_press(time, distance), answer)
        
        def test_2(self):
            time = 15
            distance = 40
            answer = 4

            return self.assertEqual(find_shortest_press(time, distance), answer)

        def test_3(self):
            time = 30
            distance = 200
            answer = 11

            return self.assertEqual(find_shortest_press(time, distance), answer)

        test_1(self)
        test_2(self)
        test_3(self)

    def test_get_input(self):
        def test_pt1(self):
            file = get_input_pt1(self.test_data)
            answer = {
                "Time": [7, 15, 30],
                "Distance": [9, 40, 200]
            }

            return self.assertEqual(file, answer)

        def test_pt2(self):
            file = get_input_pt2(self.test_data)
            answer = {
                "Time": 71530,
                "Distance": 940200
            }

            return self.assertEqual(file, answer)

        test_pt1(self)
        test_pt2(self)

    def test_run_race(self):
        def test_1(self):
            time = 7
            distance = 9
            answer = 4

            return self.assertEqual(run_race(time, distance), answer)
        
        def test_2(self):
            time = 15
            distance = 40
            answer = 8

            return self.assertEqual(run_race(time, distance), answer)

        def test_3(self):
            time = 30
            distance = 200
            answer = 9

            return self.assertEqual(run_race(time, distance), answer)

        test_1(self)
        test_2(self)
        test_3(self)

    def test_start(self):
        def test_pt1(self):
            answer = 288

            return self.assertEqual(start_pt1(self.test_data), answer)
        
        def test_pt2(self):
            answer = 71503

            return self.assertEqual(start_pt2(self.test_data), answer)

        test_pt1(self)
        test_pt2(self)


#########
# start #
#########
if __name__ == "__main__":
    unittest.main()