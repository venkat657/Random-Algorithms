# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        self.output = []
        def dfs(node):
            if(node is None):
                self.output.append("N")
                return
            self.output.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
            return
        dfs(root)
        return ",".join(self.output)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        nodes = data.split(",")
        print(nodes)
        self.i=0
        def dfs():
            if(nodes[self.i]=="N"):
                self.i+=1
                return None
            rootNode = TreeNode(nodes[self.i])
            self.i+=1
            rootNode.left = dfs()
            rootNode.right = dfs()
            return rootNode
        return dfs()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))