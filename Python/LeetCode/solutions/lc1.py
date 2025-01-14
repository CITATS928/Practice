# 1. Two Sum
# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
        return []
    
# 使用一个字典来储存已经遍历过的数字，key是数字本身，value是数字的index。
# 遍历nums寻找差值，如果target-nums[i]在字典中，返回两个数字的index。
# 每次遍历的时候，达成以下目的：
# 1. target - 当前数字 = 差值
# 2. 这个差值之前有储存在字典中吗
# 如果见过，直接返回它的index和当前数字的index
# 如果没见过，把当前数字储存在字典中，等待下次遍历

class Solution2:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dic = {}

        for i in range(len(nums)):
            if target-nums[i] in dic:
                return [i, dic[target-nums[i]]] # 返回当前数字的index和之前数字的index
            dic[nums[i]] = i  # 储存当前数字的index
        
        # 如果没有找到
        return []
    