import collections
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if(endWord not in wordList):
            return 0
        wordPattern = collections.defaultdict(list)
        wordList.append(beginWord)
        #idea is to create a pattern which can map all the list of words that match the pattern, this will be useful to perform the iteration.
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                wordPattern[pattern].append(word)
        
        path = 1
        visit = set(beginWord)  # use a visit set to not re-iterate already visited words.
        queue = collections.deque([beginWord]) # use queue for DFS
        while queue: 
            for i in range(len(queue)):
                word = queue.popleft()
                if(endWord == word):
                    return path
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for neighbor in wordPattern[pattern]:
                        if(neighbor not in visit):
                            visit.add(neighbor)
                            queue.append(neighbor)
            path+=1
        return 0