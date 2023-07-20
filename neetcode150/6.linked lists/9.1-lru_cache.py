"""4:17pm - 4:31pm"""

class LLNode:
    def __init__(self, key, val, prev=None, next=None) -> None:
        self.key = key
        self.val, self.prev, self.next = val, prev, next

def add_node(to_add: LLNode, dummy: LLNode):
    last_in_list = dummy.prev
    last_in_list.next, to_add.prev = to_add, last_in_list
    to_add.next, dummy.prev = dummy, to_add

def rmv_node(node: LLNode):
    prev, nxt = node.prev, node.next
    prev.next, nxt.prev = nxt, prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.dummy = LLNode(None, None)
        self.dummy.next, self.dummy.prev = self.dummy, self.dummy
        self.map = {}

    def _add_to_cache(self, key, value):
        """Always adds regardless of capacity"""
        self.size += 1
        node = LLNode(key, value)
        add_node(node, self.dummy)
        self.map[key] = node

    def _rmv_from_cache(self, key):
        """Always removes regardless of capacity"""
        self.size -= 1
        node = self.map[key]
        rmv_node(node)
        del self.map[key]

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        else:
            ret_val = self.map[key].val
            self._rmv_from_cache(key)
            self._add_to_cache(key, ret_val)
            return ret_val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self._rmv_from_cache(key)
        if self.size == self.capacity:
            self._rmv_from_cache(self.dummy.next.key)
        self._add_to_cache(key, value)

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)