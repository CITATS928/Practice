import unittest
from solutions.lc3216 import Solution

class TestGetSmallestString(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        s = "45320"
        self.assertEqual(self.solution.getSmallestString(s), "43520")

    def test_example2(self):
        s = "001"
        self.assertEqual(self.solution.getSmallestString(s), "001")

    def test_example3(self):
        s = "6418"
        self.assertEqual(self.solution.getSmallestString(s), "4618")

    def test_example4(self):
        s = "1357"
        self.assertEqual(self.solution.getSmallestString(s), "1357")

if __name__ == '__main__':
    unittest.main()