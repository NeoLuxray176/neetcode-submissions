class Node:
    def __init__(self, key : int, val : int, next : Optional[Node], prev : Optional[Node]):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity

        self.left = Node(key=0, val=0, next=None, prev=None)
        self.right = Node(key=0, val=0, next=None, prev=None)
        self.left.next = self.right
        self.right.prev = self.left
    
    def delete(self, node : Node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def append(self, node : Node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev


    def get(self, key: int) -> int:
        if key in self.cache:
            # Update least recently used
            node = self.cache[key]
            self.delete(node=node)
            self.append(node=node)
            return node.val

        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.delete(node=node)

        node = Node(key=key, val=value, next = None, prev = None)
        self.cache[key] = node
        self.append(node=node)

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.delete(node=lru)
            del self.cache[lru.key]
        
