# 1. Two Sum

# Easy

# Array
# Hash Table

# solution:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return[i,j]


# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

# Better solution:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for index, value in enumerate(nums):
            sub = target - value
            if sub in d:
                return[d[sub], index]
            else:
                d[value] = index



