# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        outputString=[]
        queue = deque()
        queue.append(root)
        while(len(queue)>0):
            currLength = len(queue)
            while(currLength>0):
                currNode = queue.popleft()
                if(currNode):
                    queue.append(currNode.left)
                    queue.append(currNode.right)
                val = str(currNode.val) if currNode else "N"
                outputString.append(val)
                currLength-=1
        return ",".join(outputString)    
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        rootNode = None
        nodes = data.split(",")#list(map(int,data.split(",")))
        #print(nodes)
        queue = deque()
        rootNode = TreeNode(nodes[0]) if nodes[0]!="N" else None
        if(rootNode):
            queue.append(rootNode)
        i=0
        while(len(queue)>0):
            currLength = len(queue)
            while(currLength):
                currNode = queue.popleft()
                if(currNode and (2*i)+1<len(nodes)):
                    currNode.left = TreeNode(nodes[(2*i)+1]) if nodes[(2*i)+1]!="N" else None
                    currNode.right = TreeNode(nodes[(2*i)+2]) if nodes[(2*i)+2]!="N" else None
                    queue.append(currNode.left)
                    queue.append(currNode.right)
                    i+=1
                currLength-=1
        return rootNode
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))