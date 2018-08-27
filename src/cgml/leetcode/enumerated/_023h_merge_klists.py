class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from heapq import heappop, heappush


class Solution(object):
    def mergeKLists(self, lists):
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else lists

    def merge2Lists(self, l1, l2):
        head = point = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l1
                l1 = point.next.next
            point = point.next
        if not l1:
            point.next = l2
        else:
            point.next = l1
        return head.next


#O(nlogk)
class SolutionHeap:

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        h = []
        c = 0  # counter to avoid tie
        dummy = cur = ListNode(1)
        for head in lists:
            if head:
                heappush(h, (head.val, c, head))
                c += 1

        while h:
            v, d, node = heappop(h)
            # we are not using d
            cur.next = node
            cur = cur.next
            if node.next:
                c += 1
                heappush(h, (node.next.val, c, node.next))

        return dummy.next

#O(nlongn)
class Solution2:
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

