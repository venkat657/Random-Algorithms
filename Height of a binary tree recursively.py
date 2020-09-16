class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def CountHeight(root):
    if(root is None):
        return 0
    else:
        return max(CountHeight(root.right),CountHeight(root.left))+1

root=Node(5)
root.left=Node(2)
root.right=Node(7)
print(CountHeight(root))
