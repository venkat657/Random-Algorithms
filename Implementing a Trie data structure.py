class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.Head = TrieNode()

    def insert(self, word: str) -> None:
        crawler = self.Head
        for w in word:
            if(not crawler.children[ord(w)-ord('a')]):
                crawler.children[ord(w)-ord('a')]=TrieNode()
            crawler = crawler.children[ord(w)-ord('a')]
        crawler.isEndOfWord = True


    def search(self, word: str) -> bool:
        crawler = self.Head
        for w in word:
            if(crawler.children[ord(w)-ord('a')] is None):
                return False
            crawler = crawler.children[ord(w)-ord('a')]
        return crawler.isEndOfWord

    def startsWith(self, prefix: str) -> bool:
        crawler = self.Head
        for p in prefix:
            if(crawler.children[ord(p)-ord('a')] is None):
                return False
            crawler = crawler.children[ord(p)-ord('a')]
        return True


# Your Trie object will be instantiated and called as such:
obj = Trie()
word="apps"
prefix = "app"
obj.insert(word)
param_2 = obj.search(word)
param_3 = obj.startsWith(prefix)