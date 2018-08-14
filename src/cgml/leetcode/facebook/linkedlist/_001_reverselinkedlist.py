# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        prev, curr = None, head
        while curr is not None: prev, curr.next, curr = curr, prev, curr.next
        return prev