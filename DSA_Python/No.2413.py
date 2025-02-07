# 2413. Smallest Even Multiple

# Easy

# Math
# Number Theory

# Solution:

class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n % 2 != 0:
            return 2*n
        else:
            return n