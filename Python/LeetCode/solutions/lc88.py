# 88. Merge Sorted Array
# https://leetcode.com/problems/merge-sorted-array/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[m+i] = nums2[i]
        nums1.sort()

# 优化：
# 创建3个指针，分别指向nums1的最后一个有效元素，nums2的最后一个元素，和nums1的最后一个元素。
# 从后往前遍历，比较nums1和nums2的元素大小，将较大的元素放到nums1的最后一个位置。
# 如果nums1遍历完，nums2还有剩余元素，将剩余元素放到nums1的最前面。

class Solution2:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        p1 = m-1 # nums1的最后一个有效元素
        p2 = n-1 # nums2的最后一个元素
        p = m+n-1 # nums1的最后一个元素

        while p1>=0 and p2>=0: # 如果nums1和nums2都还有元素
            if nums1[p1] > nums2[p2]: # 如果nums1的最后一个元素大于nums2的最后一个元素
                nums1[p] = nums1[p1] # 将nums1的最后一个元素放到nums1的最后一个位置
                p1-=1
            else:  # 如果nums2的最后一个元素大于nums1的最后一个元素
                nums1[p] = nums2[p2] # 将nums2的最后一个元素放到nums1的最后一个位置
                p2-=1
            p-=1
        
        if p2>=0:
            nums1[:p2+1] = nums2[:p2+1]
