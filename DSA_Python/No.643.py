# 643. Maximum Average Subarray I

# Easy

# Array
# Sliding Window

# solution 1:

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currSum = maxSum = sum(nums[:k])

        for i in range(k, len(nums)):
            currSum += nums[i] - nums[i - k]
            maxSum = max(maxSum, currSum)

        return maxSum / k

# solution 2:

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = -inf
        sum = 0
        for i, x in enumerate(nums):
            sum += x
            if i < k - 1:
                continue
            max_sum = max(max_sum, sum)
            sum -= nums[i - k + 1]
        return max_sum/k

        