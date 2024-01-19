import unittest
from advent10pt1 import start as start_pt1, get_input, find_start, follow_pipes, take_step, advance_pos


class TestDay10(unittest.TestCase):
    test_data_1 = "day10input_test1.txt"
    test_data_2 = "day10input_test2.txt"

    def test_advance_pos(self):
        def test_N(self):
            out_direction = "n"
            position = [1, 1]
            answer = [0, 1]

            return self.assertEqual(advance_pos(out_direction, position), answer)
        
        def test_S(self):
            out_direction = "s"
            position = [1, 1]
            answer = [2, 1]

            return self.assertEqual(advance_pos(out_direction, position), answer)
        
        def test_E(self):
            out_direction = "e"
            position = [1, 1]
            answer = [1, 2]

            return self.assertEqual(advance_pos(out_direction, position), answer)
        
        def test_W(self):
            out_direction = "w"
            position = [1, 1]
            answer = [1, 0]

            return self.assertEqual(advance_pos(out_direction, position), answer)
        
        test_N(self)
        test_S(self)
        test_E(self)
        test_W(self)

    def test_find_start(self):
        def test_1(self):
            file = [
                [".", ".", ".", ".", "."],
                [".", "S", "-", "7", "."],
                [".", "|", ".", "|", "."],
                [".", "L", "-", "J", "."],
                [".", ".", ".", ".", "."]
                ]
            answer = [1, 1]

            return self.assertEqual(find_start(file), answer)

        def test_2(self):
            file = [
                [".", ".", "F", "7", "."],
                [".", "F", "J", "|", "."],
                ["S", "J", ".", "L", "7"],
                ["|", "F", "-", "-", "J"],
                ["L", "J", ".", ".", "."]
            ]
            answer = [2, 0]

            return self.assertEqual(find_start(file), answer)
        
        test_1(self)
        test_2(self)

    def test_follow_pipes(self):
        def test_1(self):
            file = [
                [".", ".", ".", ".", "."],
                [".", "S", "-", "7", "."],
                [".", "|", ".", "|", "."],
                [".", "L", "-", "J", "."],
                [".", ".", ".", ".", "."]
                ]
            start_point = [1, 1]
            answer = 4

            return self.assertEqual(follow_pipes(file, start_point), answer)
        
        test_1(self)

    def test_get_input(self):
        file = self.test_data_1
        answer = [
            [".", ".", ".", ".", "."],
            [".", "S", "-", "7", "."],
            [".", "|", ".", "|", "."],
            [".", "L", "-", "J", "."],
            [".", ".", ".", ".", "."]
            ]
        
        self.assertEqual(get_input(file), answer)

    def test_take_step(self):
        def test_N(self):
            file = [
            [".", ".", ".", ".", "."],
            [".", "S", "-", "7", "."],
            [".", "|", ".", "|", "."],
            [".", "L", "-", "J", "."],
            [".", ".", ".", ".", "."]
            ]
            in_direction = "n"
            position = [1, 3]
            answer = "s"

            return self.assertEqual(take_step(file, in_direction, position), answer)
        
        def test_S(self):
            file = [
            [".", ".", ".", ".", "."],
            [".", "S", "-", "7", "."],
            [".", "|", ".", "|", "."],
            [".", "L", "-", "J", "."],
            [".", ".", ".", ".", "."]
            ]
            in_direction = "s"
            position = [2, 1]
            answer = "n"

            return self.assertEqual(take_step(file, in_direction, position), answer)
        
        def test_W(self):
            file = [
            [".", ".", ".", ".", "."],
            [".", "S", "-", "7", "."],
            [".", "|", ".", "|", "."],
            [".", "L", "-", "J", "."],
            [".", ".", ".", ".", "."]
            ]
            in_direction = "w"
            position = [1, 3]
            answer = "s"

            return self.assertEqual(take_step(file, in_direction, position), answer)
        
        def test_E(self):
            file = [
            [".", ".", ".", ".", "."],
            [".", "S", "-", "7", "."],
            [".", "|", ".", "|", "."],
            [".", "L", "-", "J", "."],
            [".", ".", ".", ".", "."]
            ]
            in_direction = "e"
            position = [3, 1]
            answer = "n"

            return self.assertEqual(take_step(file, in_direction, position), answer)
        
        test_N(self)
        test_S(self)
        test_W(self)
        test_E(self)

    def test_start_pt1(self):
        def test_1(self):
            file = self.test_data_1
            answer = 4
            
            return self.assertEqual(start_pt1(file), answer)
        
        def test_2(self):
            file = self.test_data_2
            answer = 8

            return self.assertEqual(start_pt1(file), answer)
        
        test_1(self)
        test_2(self)


#########
# Start #
#########
if __name__ == "__main__":
    unittest.main()