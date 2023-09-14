class Node:
    def __init__(self, key:int,val:int, Next=None,prev=None):
        self.key = key
        self.val = val
        self.next = Next
        self.prev = prev
class LRUCache:
    def __init__(self, capacity: int):
        self.NodeDict={}
        self.Capacity=capacity
        self.left,self.right=Node(0,0),Node(0,0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        rightNode = node.next
        leftNode = node.prev
        leftNode.next = rightNode
        rightNode.prev = leftNode
        node.next, node.prev = None,None
    def insert(self, node):
        self.right.prev.next = node
        node.next = self.right
        node.prev = self.right.prev
        self.right.prev = node

    def get(self, key: int) -> int:
        if(key not in self.NodeDict):
            return -1
        node = self.NodeDict[key]
        self.remove(node)
        self.insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if(key not in self.NodeDict):
            node = Node(key,value)
            self.insert(node)
            self.NodeDict[key] = node
        else:
            node = self.NodeDict[key]
            node.val = value
            self.remove(node)
            self.insert(node)
        if(len(self.NodeDict)>self.Capacity):
            removeNode = self.left.next
            self.remove(removeNode)
            del self.NodeDict[removeNode.key]



# Your LRUCache object will be instantiated and called as such:
"""
obj = LRUCache(2)
obj.get(2)
obj.put(2,6)
obj.get(1)
obj.put(1,5)
obj.put(1,2)
obj.get(1)
obj.get(2)
"""

obj = LRUCache(2)
obj.put(1,1)
obj.put(2,2)
obj.get(1)
obj.put(3,3)
obj.get(2)
obj.put(4,4)
obj.get(1)
obj.get(3)
obj.get(4)
"""
obj = LRUCache(2)
obj.put(2,1)
obj.put(2,2)
obj.get(2)
obj.put(1,1)
obj.put(4,1)
obj.get(2)
"""