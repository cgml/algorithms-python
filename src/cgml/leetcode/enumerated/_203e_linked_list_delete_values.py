# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        while head and head.val == val: head = head.next
        p, c = None, head
        while c:
            if c.val == val: p.next, p, c = c.next, p, c.next
            else: p, c = c, c.next
        return head