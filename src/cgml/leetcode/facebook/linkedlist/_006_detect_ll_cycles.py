# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        if head is None: return False
        curr, currRunner = head, head.next
        while curr is not currRunner and currRunner is not None:
            if currRunner.next is None: return False
            curr, currRunner = curr.next, currRunner.next.next
        return currRunner is not None