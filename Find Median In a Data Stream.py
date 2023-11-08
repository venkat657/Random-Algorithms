#leetcode link: https://leetcode.com/problems/find-median-from-data-stream/
import heapq
class MedianFinder:

    def __init__(self):
        self.leftHeap = []  #minHeap
        self.rightHeap = [] #maxHeap
        heapq.heapify(self.leftHeap)
        heapq.heapify(self.rightHeap)

    def addNum(self, num: int) -> None:
        if(len(self.leftHeap)==0):
            heapq.heappush(self.leftHeap, -1*num)
        else:
            if(num<-1*self.leftHeap[0]):
                heapq.heappush(self.leftHeap,-1*num)
            else:
                heapq.heappush(self.rightHeap,num)
        while(len(self.leftHeap)-len(self.rightHeap)>=2):
            poppedVal = -1*heapq.heappop(self.leftHeap)
            heapq.heappush(self.rightHeap,poppedVal)
        while(len(self.rightHeap)-len(self.leftHeap)>=2):
            poppedVal = heapq.heappop(self.rightHeap)
            heapq.heappush(self.leftHeap,-1*poppedVal)




    def findMedian(self) -> float:
        leftHeapLen = len(self.leftHeap)
        rightHeapLen = len(self.rightHeap)
        if(leftHeapLen==rightHeapLen):
            return ((-1*self.leftHeap[0])+(self.rightHeap[0]))/2
        else:
            if(leftHeapLen>rightHeapLen):
                return -1*self.leftHeap[0]
            else:
                return self.rightHeap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()