import unittest
from solutions.lc88 import Solution

class TestMergeSortedArray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        nums1 = [1, 2, 3, 0, 0, 0]
        m = 3
        nums2 = [2, 5, 6]
        n = 3
        self.solution.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1, 2, 2, 3, 5, 6])

    def test_example2(self):
        nums1 = [0, 0, 0]
        m = 0
        nums2 = [2, 5, 6]
        n = 3
        self.solution.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [2, 5, 6])

    def test_example3(self):
        nums1 = [0]
        m = 0
        nums2 = []
        n = 0
        self.solution.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [0])

    def test_example4(self):
        nums1 = [1, 2, 3]
        m = 3
        nums2 = []
        n = 0
        self.solution.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1, 2, 3])

if __name__ == '__main__':
    unittest.main()