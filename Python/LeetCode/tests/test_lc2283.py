import unittest
from solutions.lc2283 import Solution

class TestDigitCount(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        num = "1210"
        # expect True
        self.assertEqual(self.solution.digitCount(num), True)

    def test_example2(self):
        num = "030"
        # expect False
        self.assertEqual(self.solution.digitCount(num), False)

    def test_example3(self):
        num = "1"
        # expect False
        self.assertEqual(self.solution.digitCount(num), False)

    def test_example4(self):
        num = "0000"
        # expect False
        self.assertEqual(self.solution.digitCount(num), False)

if __name__ == '__main__':
    unittest.main()