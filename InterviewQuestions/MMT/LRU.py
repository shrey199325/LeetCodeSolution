"""
LRU cache:
cap = 3
R1: 1->2,
R2: 2->3
R1: 1->2
R3: 3->5

R(1), R(3)

get -> O(1)
put -> O(1)
"""


class DllNode:
    def __init__(self, val=-1, key=-1):
        self.val = val
        self.key = key
        self.prev = self.next = None


class LRUCache:
    def __init__(self, cap):
        self.cap = cap
        self.cache = dict()
        self.head = DllNode()
        self.back = DllNode()
        self.head.next = self.back
        self.back.prev = self.head

    def insert(self, key, val):
        tmp = self.head.next
        self.cache[key] = DllNode(val, key)
        self.head.next = self.cache[key]
        self.cache[key].prev = self.head
        self.cache[key].next = tmp
        tmp.prev = self.cache[key]

    def remove(self, key):
        prev = self.cache[key].prev
        next_node = self.cache[key].next
        prev.next = next_node
        next_node.prev = prev
        self.cache[key].prev = self.cache[key].next = None
        self.cache.pop(key)

    def get(self, key):
        if key in self.cache:
            tmp = self.cache[key]
            self.remove(key)
            self.insert(key, tmp.val)
            return tmp.val
        return None

    def put(self, key, val):
        if key in self.cache:
            self.remove(key)
        self.insert(key, val)
        if len(self.cache) > self.cap:
            self.remove(self.back.prev.key)


cache = LRUCache(2)
cache.put(1,2)
print(cache.cache)
cache.put(3,4)
print(cache.cache)
cache.put(10,11)
print(cache.cache)
print(cache.get(3))
print(cache.cache)
cache.put(15,16)
print(cache.cache)
