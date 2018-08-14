# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        prev, curr, runner = None, head, head
        while runner is not None:
            runner = runner.next
            if n > 0: n-=1
            else: prev, curr = curr, curr.next
        if prev: prev.next = curr.next
        else: head = curr.next
        return head