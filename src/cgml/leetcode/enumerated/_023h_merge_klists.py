class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        ls = []
        for l in lists:
            while l: ls, l = ls+[l.val], l.next
        ls.sort()
        head = cur = ListNode(None)
        for n in ls:
            cur.next = ListNode(n)
            cur = cur.next
        return head.next

#TODO priority queue