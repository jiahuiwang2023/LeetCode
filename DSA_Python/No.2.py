# 2. Add Two Numbers

# Medium

# Recursion
# Linked List
# Math

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# dummy node solution:
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode() 
        cur = dummy
        carry = 0
        while l1 or l2 or carry:
            sum = carry
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            carry = sum // 10
            cur.next = ListNode(sum % 10)
            cur = cur.next
        return dummy.next

# Recursion solution:
class Solution:
    def addTwoNumbers(self, l1, l2):
        if not l1 and not l2:
            return None
        elif not l1:
            return l2
        elif not l2:
            return l1

        a = l1.val + l2.val
        p = ListNode(a % 10)
        p.next = self.addTwoNumbers(l1.next, l2.next)
        if a >= 10:
            p.next = self.addTwoNumbers(p.next, ListNode(1))
        return p



