class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None

def CountHeight(root):
    height=0
    if(root is not None):
        leftqueue=[root]
        rightqueue=[]
        while(len(leftqueue)!=0 or len(rightqueue)!=0):
            flag=True
            if(len(rightqueue)==0):
                for i in range(0,len(leftqueue)):
                    if(leftqueue[0] is not None):
                        rightqueue+=[leftqueue[0].left]
                        rightqueue+=[leftqueue[0].right]
                        leftqueue.pop(0)
                        if(flag==True):
                            height+=1
                            flag=False
                    else:
                        leftqueue.pop(0)
            else:
                for i in range(0,len(rightqueue)):
                    #print(len(rightqueue),i)
                    if(rightqueue[0] is not None):
                        leftqueue+=[rightqueue[0].left]
                        leftqueue+=[rightqueue[0].right]
                        rightqueue.pop(0)
                        if(flag==True):
                            height+=1
                            flag=False
                    else:
                        rightqueue.pop(0)
            

    return height
        
                        
root=Node(1)
root.left=Node(0)
root.right=Node(2)
root.left.left=Node(-1)
root.right.right=Node(4)
root.right.right.left=Node(3)
root.right.right.right=Node(5)
print(CountHeight(root))
        
