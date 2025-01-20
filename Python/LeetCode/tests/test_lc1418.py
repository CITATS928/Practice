import unittest
from solutions.lc1418 import Solution

class TestDisplayTable(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        orders = [
            ["David", "3", "Ceviche"],
            ["Corina", "10", "Beef Burrito"],
            ["David", "3", "Fried Chicken"],
            ["Carla", "5", "Water"],
            ["Carla", "5", "Ceviche"],
            ["Rous", "3", "Ceviche"]
        ]
        excepted = [
            ["Table", "Beef Burrito", "Ceviche", "Fried Chicken", "Water"],
            ["3", "0", "2", "1", "0"],
            ["5", "0", "1", "0", "1"],
            ["10", "1", "0", "0", "0"]
        ]
        self.assertEqual(self.solution.displayTable(orders), excepted)

    def test_example2(self):
        orders = [["David", "3", "Ceviche"]]
        expected = [
            ["Table", "Ceviche"], 
            ["3", "1"]
            ]
        self.assertEqual(self.solution.displayTable(orders), expected)
    
    def test_example3(self):
        orders = [
            ["David", "3", "Ceviche"], 
            ["Corina", "3", "Ceviche"], 
            ["Alice", "5", "Ceviche"]
            ]
        expected = [
            ["Table", "Ceviche"], 
            ["3", "2"], 
            ["5", "1"]
            ]
        self.assertEqual(self.solution.displayTable(orders), expected)

    def test_example4(self):
        orders = []
        expected = [["Table"]]
        self.assertEqual(self.solution.displayTable(orders), expected)



if __name__ == '__main__':
    unittest.main()