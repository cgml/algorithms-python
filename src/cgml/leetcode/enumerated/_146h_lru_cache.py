class Node:
    def __init__(self, key, val):
        self.key, self.val, self.prev, self.next = key, val, None, None

class LRUCache:
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.head, self.tail, self.d, self.capacity = None, None, {}, capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # not found return -1
        if self.d.get(key, None) is None: return -1

        # find node
        node = self.d[key]

        # if not head node - move to head
        if node.key != self.head.key:

            # if last node - update tale
            if self.tail.key == node.key:
                self.tail, self.tail.next = self.tail.prev, None
            else:
                # otherwise pop from middle
                if node.prev: node.prev.next = node.next
                if node.next: node.next.prev = node.prev

            node.prev, node.next, self.head.prev, self.head = None, self.head, node, node

        return node.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        old_val = self.get(key)
        if old_val >= 0:
            self.head.val = value
            return

        node = Node(key, value)
        self.d[key] = node
        if not self.tail or not self.head:
            self.tail = self.head = node
            return

        # add to head
        node.next, self.head.prev, self.head = self.head, node, node

        # remove tail if exceeded capacity
        if len(self.d) > self.capacity:
            if self.d.get(self.tail.key, False):
                del self.d[self.tail.key]
                self.tail.prev.next, self.tail = None, self.tail.prev

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)