import unittest
from solutions.lc1247 import Solution

class TestMinSwap(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        s1 = "xx"
        s2 = "yy"
        # expect 1
        self.assertEqual(self.solution.minimumSwap(s1, s2), 1)

    def test_example2(self):
        s1 = "xy"
        s2 = "yx"
        # expect 2
        self.assertEqual(self.solution.minimumSwap(s1, s2), 2)

    def test_example3(self):
        s1 = "xx"
        s2 = "xx"
        # expect 0
        self.assertEqual(self.solution.minimumSwap(s1, s2), 0)

    def test_example4(self):
        s1 = "xx"
        s2 = "xy"
        # expect -1
        self.assertEqual(self.solution.minimumSwap(s1, s2), -1)

    def test_example5(self):
        s1 = "x"
        s2 = "y"
        # expect -1
        self.assertEqual(self.solution.minimumSwap(s1, s2), -1)


if __name__ == '__main__':
    unittest.main()