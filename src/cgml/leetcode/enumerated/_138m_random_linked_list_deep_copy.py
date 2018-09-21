'''
Time Complexity : O(N)O(N)
Space Complexity : O(1)O(1)
'''
class RandomListNode:
    def __init__(self, x):
        self.label, self.random, self.next = x, None, None


class SolutionON(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head is None: return None
        dc = dhead = RandomListNode(head.label)
        d, cc = {dc.label: dc}, head.next
        while cc:
            dc.next = RandomListNode(cc.label)
            d[dc.next.label] = dc.next
            dc, cc = dc.next, cc.next

        dc, c = dhead, head
        while c:
            if c.random: dc.random = d[c.random.label]
            dc, c = dc.next, c.next
        return dhead


class SolutionO1(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return head

        # Creating a new weaved list of original and copied nodes.
        ptr = head
        while ptr:

            # Cloned node
            new_node = RandomListNode(ptr.label)

            # Inserting the cloned node just next to the original node.
            # If A->B->C is the original linked list,
            # Linked list after weaving cloned nodes would be A->A'->B->B'->C->C'
            new_node.next = ptr.next
            ptr.next = new_node
            ptr = new_node.next

        ptr = head

        # Now link the random pointers of the new nodes created.
        # Iterate the newly created list and use the original nodes random pointers,
        # to assign references to random pointers for cloned nodes.
        while ptr:
            ptr.next.random = ptr.random.next if ptr.random else None
            ptr = ptr.next.next

        # Unweave the linked list to get back the original linked list and the cloned list.
        # i.e. A->A'->B->B'->C->C' would be broken to A->B->C and A'->B'->C'
        ptr_old_list = head # A->B->C
        ptr_new_list = head.next # A'->B'->C'
        head_old = head.next
        while ptr_old_list:
            ptr_old_list.next = ptr_old_list.next.next
            ptr_new_list.next = ptr_new_list.next.next if ptr_new_list.next else None
            ptr_old_list = ptr_old_list.next
            ptr_new_list = ptr_new_list.next
        return head_old