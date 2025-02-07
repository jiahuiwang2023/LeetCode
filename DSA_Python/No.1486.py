# 1486. XOR Operation in an Array

# Easy

# Math
# Bit Manipulation

# Solution:
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        
        ans = 0
        nums = [start + n * 2 for n in range(n)]
        
        for n in nums:
            ans = ans ^ n
        return ans 
        
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        ## RC ##
        ## APPROACH : MATH ##
        res = 0
        for i in range(n):
            res ^= start + 2 * i
        return res