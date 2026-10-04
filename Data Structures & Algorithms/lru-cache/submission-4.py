class Node:
    def __init__(self, key : int = 0, val : int = 0, next : Optional[Node] = None, prev : Optional[Node] = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.left = Node()
        self.right = Node()
        self.cap = capacity

        self.left.next = self.right
        self.right.prev = self.left
        
        

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.delete(node)
            self.append(node)
            return node.val
        else:
            return -1

    def delete(self, node : Node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def append(self, node : Node):
        prev, next = self.right.prev, self.right
        prev.next = next.prev = node
        node.next, node.prev = next, prev
        
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.delete(node)
        
        node = Node(key=key, val=value)
        self.cache[key] = node
        self.append(node)

        if len(self.cache) > self.cap:
            node = self.left.next
            self.delete(node)
            del self.cache[node.key]
        
