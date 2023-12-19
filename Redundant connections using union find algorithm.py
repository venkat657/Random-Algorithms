class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        parent = [i for i in range(len(edges)+1)]
        rank = [1] * (len(edges)+1)

        # employ path compression to set parents to a node accordingly while finding it
        def find(n):
            p = parent[n]
            while p!=parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p
        
        # use union to set the parents to a node when unioning it, we can union two nodes, under the node that has the higher rank and also set its parents, 
        # if two nodes already have the same parent, then return False
        def union(a,b):
            rootA, rootB = find(a), find(b)
            if rootA == rootB:
                return False
            else:
                rankA = rank[rootA]
                rankB = rank[rootB]
                if rankA > rankB:
                    rank[rootA]+=1
                    parent[rootB] = rootA
                else:
                    rank[rootB]+=1
                    parent[rootA] = rootB
                return True
        FinalIndex = 0
        for i in range(len(edges)):
            if(not union(edges[i][0],edges[i][1])):
                FinalIndex = i
        return edges[FinalIndex]