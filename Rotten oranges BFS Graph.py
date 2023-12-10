#link: https://leetcode.com/problems/rotting-oranges/description/

from collections import deque
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:

        def bfs(r,c,traverseSet):
            orangeQueue = deque()
            orangeQueue.append((r,c))
            while(orangeQueue):
                i,j = orangeQueue.popleft()
                traverseSet.add((i,j))
                for h,v in directions:
                    if (i+h) in range(rows) and (j+v) in range(cols) and grid[i+h][j+v]==1:
                        if(adjMatrix[i+h][j+v]>=0):
                            adjMatrix[i+h][j+v] = min(adjMatrix[i+h][j+v], adjMatrix[i][j]+1)
                        else:
                            adjMatrix[i+h][j+v] = adjMatrix[i][j] + 1
                        if((i+h,j+v) not in traverseSet):  # this is to break a cycle and also identify when a legit optimization can be done
                            orangeQueue.append((i+h,j+v))

        rows = len(grid)
        cols = len(grid[0])
        adjMatrix = [[-2 for r in range(cols)] for c in range(rows)]
        directions = [(-1,0),(0,-1),(1,0),(0,1)]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==2:
                    adjMatrix[i][j]=0
                    bfs(i,j, set()) # pass in a set as a parameter so that we know when to break a cycle
        minVal = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1 and adjMatrix[i][j]==-2:
                    return -1
                else:
                    minVal = max(adjMatrix[i][j],minVal)
        return minVal