class UnionFind:
    def __init__(self, n, edges:list[list[int]] = None):
        self.parent = [i for i in range(n)]
        self.rank = [1] * (n)

    '''
    apply path compression to the parent finding process 
    so that the next time a child doesn't have to struggle walking the same path its parent did 
    p.s: there, I explained it in the most layman way possible.
    '''
    def find(self, node):
        parent = None
        if(self.parent): 
            parent = self.parent[node]
            while parent!=self.parent[parent]:
                self.parent[parent] = self.parent[self.parent[parent]]
                parent = self.parent[parent]
        return parent
    
    def union(self, nodeA, nodeB):
        parentOfA, parentofB = self.find(nodeA), self.find(nodeB)
        rankofA, rankOfB = self.rank[parentOfA], self.rank[parentofB]
        if(parentOfA == parentofB):
            return parentOfA
        if(rankofA > rankOfB):
            self.rank[parentOfA] += 1
            self.parent[parentofB] = parentOfA
            return parentOfA
        else:
            self.rank[parentofB] += 1
            self.parent[parentOfA] = parentofB
            return parentofB

class NodeComponent:
    def __init__(self,n:int = 0, edges:list[list[int]] = None)-> None:
        self.nodesNum = n
        self.edges = edges
        self.parentSet = set()  # alternatively use a count property who value is updated based on return value from union operation
        self.unionFind = UnionFind(self.nodesNum, self.edges) 
    def findConnectedComponents(self)-> int:
        for edge in self.edges:
            self.parentSet.add(self.unionFind.union(edge[0],edge[1]))
        return len(self.parentSet)
    
nodeComponent = NodeComponent(n=5, edges=[[0,1],[1,2],[3,4]])
print(nodeComponent.findConnectedComponents())