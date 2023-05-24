"""11:59am - 12:18pm"""


class LRUCache:
    class Node:
        def __init__(self, val, key, prev=None, next=None) -> None:
            self.val = val
            self.key = key
            self.prev = prev
            self.next = next

    def __init__(self, capacity: int):
        self.dummy = LRUCache.Node(None, None)
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy
        self.capacity = capacity
        self.size = 0
        self.key_to_node = {}

    def _bump(self, key):
        """bump key to front"""
        val = self.key_to_node[key].val
        self._rmv(key)
        self._add(key, val)
        return val

    def _rmv(self, key):
        """remove key"""
        self._rmv_node(self.key_to_node[key])

    def _rmv_least_freq_used(self):
        """rmv least freq used"""
        self._rmv_node(self.dummy.prev)

    def _rmv_node(self, node):
        before, after = node.prev, node.next
        before.next, after.prev = after, before
        del self.key_to_node[node.key]
        self.size -= 1

    def _add(self, key, value):
        node = LRUCache.Node(value, key)
        # add to dict
        self.key_to_node[key] = node

        # update pointers
        node.next, self.dummy.next.prev = self.dummy.next, node
        self.dummy.next, node.prev = node, self.dummy

        # check capacity
        self.size += 1
        if self.size > self.capacity:   
            self._rmv_least_freq_used()

    def get(self, key: int) -> int:
        if key in self.key_to_node:
            return self._bump(key)
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_node:
            self._rmv(key)
        self._add(key, value)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)