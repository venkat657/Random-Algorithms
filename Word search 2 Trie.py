class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self,word, letterHash):
        crawler = self.root
        for w in word:
            if(crawler.children[ord(w)-ord('a')] is None):
                crawler.children[ord(w)-ord('a')] = TrieNode()
            letterHash[w] = 1 + letterHash.get(w,0)
            crawler = crawler.children[ord(w)-ord('a')]
        crawler.isEndOfWord = True
    def search(self,word):
        crawler = self.root 
        for w in word:
            if(crawler.children[ord(w)-ord('a')] is None):
                return False
            crawler = crawler.children[ord(w)-ord('a')]
        return crawler.isEndOfWord

class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:

        def dfs(r,c,trieNode,currentWord):
            if(board[r][c]=='' or trieNode.children[ord(board[r][c])-ord('a')] is None):
                return False
            trieNode = trieNode.children[ord(board[r][c])-ord('a')]
            if(trieNode.isEndOfWord and currentWord not in outputSet):
                for cr in currentWord:
                    letterHash[cr]-=1
                outputSet.add(currentWord)
            board[r][c],temp='',board[r][c]
            for h,v in directions:
                if(r+h<0 or c+v<0 or r+h>=len(board) or c+v>=len(board[0]) or board[r+h][c+v]==''):
                    continue
                dfs(r+h,c+v,trieNode,currentWord+board[r+h][c+v])
            board[r][c] = temp if letterHash[temp]>0 else ''
            return
                        

        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        letterHash = {}
        trie = Trie()
        outputSet = set()
        for word in words:
            trie.insert(word,letterHash)
        print(letterHash)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if(board[i][j]!='' and trie.root.children[ord(board[i][j])-ord('a')]):
                    dfs(i,j,trie.root,board[i][j])    
        return list(outputSet)

sol = Solution()
sol.findWords(board=[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words=["oath","pea","eat","rain","hklf", "hf"])