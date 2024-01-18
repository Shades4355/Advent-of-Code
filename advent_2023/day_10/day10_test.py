import unittest
from advent10pt1 import start as start_pt1, get_input


class TestDay10(unittest.TestCase):
    test_data_1 = "day10input_test1.txt"
    test_data_2 = "day10input_test2.txt"

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