from queue import Queue
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        q=Queue()
        nodes=[]
        if(root):
            q.put(root)
            while(not q.empty()):
                root=q.get()
                if(root):
                    q.put(root.left)
                    q.put(root.right)
                    nodes.append(root.val)
                else:
                    nodes.append(root)
                #print(q)
                #print(nodes)
        return str(nodes)

root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.right.left=TreeNode(4)
root.right.right=TreeNode(5)
codec=Codec()
print(codec.serialize(root))
