'''
Convert Binary Search Tree to Sorted Doubly Linked List
'''


class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root: return None
        head, tail = self.helper(root)
        head.left = tail
        tail.right = head
        return head

    def helper(self, root):
        if not root: return None, None
        left_head, left_tail = self.helper(root.left)
        right_head, right_tail = self.helper(root.right)
        if left_head:
            left_tail.right = root
            root.left = left_tail
        else:
            left_head = root
        if right_head:
            root.right = right_head
            right_head.left = root
        else:
            right_tail = root
        return left_head, right_tail
