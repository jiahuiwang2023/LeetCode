# 69. Sqrt(x)

# Easy

# Math
# Binary Search

# Solution:

class Solution:
    def mySqrt(self, x: int) -> int:
        left = 1
        right = x
        ans = 0
        while left <= right:
            mid = (left + right)//2
            if mid*mid > x:
                right = mid - 1
            else:
                left = mid + 1
                ans = mid
        return ans
            
