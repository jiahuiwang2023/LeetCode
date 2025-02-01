# 1539. Kth Missing Positive Number

# Easy

# Array
# Binary Search

# binary search solution:
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        arr.insert(0, 0)
        left, right = 0, len(arr)-1
        while left<=right:
            mid = left + (right-left)//2
            temp = arr[mid]-mid
            if temp >= k:
                right = mid-1
            else:
                left = mid+1

        return k+right

# easier solution:
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        for i in arr:
            if k < i:
                break
            k += 1
        return k





