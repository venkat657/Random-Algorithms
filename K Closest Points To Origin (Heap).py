import heapq
class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        output=[]
        pointHeap = []
        #distanceDict = {}
        for x1,x2 in points:
            distance =  math.sqrt(((0-x1)**2)+((0-x2)**2))
            '''
            if(distance not in distanceDict):
                distanceDict[distance]=[]
            '''
            pointHeap.append((distance,[x1,x2]))
            #distanceDict[distance]+=[[x1,x2]]
        pops=k
        heapq.heapify(pointHeap)
        while(pops>0 and len(pointHeap)>0):
            pops-=1
            output+=[heapq.heappop(pointHeap)[1]]
            '''
            element = heapq.heappop(pointHeap)
            output+=distanceDict[element]
            pops-=len(distanceDict[element])
            '''
        return output