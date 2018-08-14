# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        curl1, curl2, carry, sumhead = l1, l2, 0, ListNode(0)
        currsum = sumhead
        while curl1 is not None or curl2 is not None or carry > 0:
            result = 0
            if curl1 is not None: result, curl1 = result + curl1.val, curl1.next
            if curl2 is not None: result, curl2 = result + curl2.val, curl2.next
            result, carry = (result + carry) % 10, int((result + carry) / 10)
            currsum.next = ListNode(result)
            currsum = currsum.next
        return sumhead.next