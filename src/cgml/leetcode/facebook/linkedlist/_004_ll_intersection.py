# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        prevA, currA, countA, prevB, currB, countB = None, headA, 0, None, headB, 0
        while currA is not None: prevA, currA, countA = currA, currA.next, countA+1
        while currB is not None: prevB, currB, countB = currB, currB.next, countB+1
        if prevA is not prevB: return None
        currA, currB = headA, headB
        while currA is not currB:
            if countA - countB > 0: countA, currA = countA-1, currA.next
            elif countA - countB < 0: countB, currB = countB-1, currB.next
            else: currA, currB = currA.next, currB.next
        return currA