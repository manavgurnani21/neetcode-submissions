class LRUCache:
    class Node:
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.prev = None
            self.next = None

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.itemCount = 0
        self.head = self.Node(-1, 0)
        self.tail = self.Node(-1, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insertNode(self, node):
        insertPoint = self.tail.prev
        insertPoint.next = node
        node.next = self.tail
        self.tail.prev = node
        node.prev = insertPoint
    
    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None

    def get(self, key: int) -> int:
        # return -1 if no key exists in hashmap
        if key not in self.cache:
            return -1
        # return value if found
        else:
            node = self.cache[key]
            # update tail with most recently used (remove from DLL and add to tail)
            self.removeNode(node)
            self.insertNode(node)
            return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value # updating value of node
            # updating MRU
            self.removeNode(node)
            self.insertNode(node)
            self.cache[key] = node
        else:
            node = self.Node(key, value)
            if self.itemCount < self.capacity:
                self.itemCount += 1
            else:
                # remove head.next
                evict = self.head.next
                self.removeNode(evict)
                self.cache.pop(evict.key)
            self.insertNode(node)
            self.cache[key] = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)