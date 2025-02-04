# 13. Roman to Integer

# Easy

# Hash Table
# Math
# String

# Solution:
class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        ans = 0

        for i in range(len(s)):
            if i < len(s) - 1 and dict[s[i]] < dict[s[i+1]]:
                ans -= dict[s[i]]
            else:
                ans += dict[s[i]]
        
        return ans

# Easier solution:
class Solution:
    def romanToInt(self, s: str) -> int:
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        
        number = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        
        for char in s:
            number += translations[char]
        return number