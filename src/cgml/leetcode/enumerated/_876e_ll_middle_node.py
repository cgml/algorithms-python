# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head):
        c, r = head, head.next
        while r: c, r = (c.next, r.next) if not r.next else (c.next, r.next.next)
        return c