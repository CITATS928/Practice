import unittest
from solutions.lc1812 import Solution

class TestDetermineColor(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        coordinates = "a1"
        # expect False
        self.assertEqual(self.solution.squareIsWhite(coordinates), False)
    
    def test_example2(self):
        coordinates = "h3"
        # expect True
        self.assertEqual(self.solution.squareIsWhite(coordinates), True)

    def test_example3(self):
        coordinates = "c7"
        # expect False
        self.assertEqual(self.solution.squareIsWhite(coordinates), False)

if __name__ == '__main__':
    unittest.main()