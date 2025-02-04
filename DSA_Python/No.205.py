# 205. Isomorphic Strings

# Easy

# Hash Table
# String

# Hash table solution:
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic1=dict()
        dic2=dict()
        for i in range(len(s)):
            if (s[i] in dic1 and dic1[s[i]]!=t[i]) or (t[i] in dic2 and dic2[t[i]]!=s[i]):
                return False
            dic1[s[i]]=t[i]
            dic2[t[i]]=s[i]
        return True

# Easier solution:
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        for i in range(len(s)):
            if s.index(s[i]) != t.index(t[i]):
                return False
        return True 
# One-line solution:
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(s)) == len(set(t)) == len(set(zip(s,t)))
