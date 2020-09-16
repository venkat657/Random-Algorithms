class LinkedList:
    def __init__(self):
        self.head=None

class Node:
    def __init__(self,val):
        self.data=val
        self.next=None

def MapListtoLinkedList(linkedlist,arr):
    linkedlist.head=Node(arr[0])
    currentnode=linkedlist.head
    for i in range(1,len(arr)):
        newnode=Node(arr[i])
        currentnode.next=newnode
        currentnode=newnode

def FindGreaterNodes(outputarr,stack,linkedlist):
    elementscount=0
    currentNode=linkedlist.head
    stack.append(currentNode.data)
    indexstack=[]
    indexstack.append(0)
    currentNode=currentNode.next
    while(currentNode is not None):
        if(len(stack)==0):
            stack.append(currentNode.data)
            currentNode=currentNode.next
            elementscount+=1
            indexstack.append(elementscount)
        if(stack[-1]<currentNode.data):
            outputarr[indexstack.pop()]=currentNode.data
            stack.pop()
        else:
            stack.append(currentNode.data)
            elementscount+=1
            indexstack.append(elementscount)
            currentNode=currentNode.next
            
linkedlist=LinkedList()
arr=list([int(x) for x in input().split()])
#arr=[8,0,1,9,2,5,11,3,1,1,4,6,2,3]
MapListtoLinkedList(linkedlist,arr)    #to convert input array to a linked list
stack=[]
outputarr=[0]*len(arr)
FindGreaterNodes(outputarr,stack,linkedlist)
print(outputarr)
