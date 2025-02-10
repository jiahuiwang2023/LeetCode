# 1991. Find the Middle Index in Array

# Easy

# Array
# Prefix Sum

# Solution:

class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        leftSum = 0
        rightSum = sum(nums)

        for i in range(len(nums)):
            if leftSum + nums[i] == rightSum:
                return i

            leftSum += nums[i]
            rightSum -= nums[i]

        return -1