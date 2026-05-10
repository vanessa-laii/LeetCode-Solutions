class Node:
    def __init__(self, key, value):
        self.prev = None
        self.next = None
        self.key = key
        self.value = value

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        
        self.tail, self.head = Node(0, 0), Node(0,0)
        self.head.next, self.tail.prev = self.tail, self.head
    
    def delete(self, node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev
    
    def insert(self, node):
        prev_tail = self.tail.prev
        node.prev = prev_tail
        prev_tail.next = node

        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
            # move node around
        node = self.cache[key]
        self.delete(node)
        self.insert(node)
            
        
        return node.value
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.delete(self.cache[key])
        newNode = Node(key, value)
        self.cache[key] = newNode
        self.insert(newNode)

        if len(self.cache) > self.cap:
            lru = self.head.next
            self.delete(lru)
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)