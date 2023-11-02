#link: https://leetcode.com/problems/word-search/submissions/

class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        def backtrack(row,col,wordToMatch, currentWord):
            if(currentWord == word):
                return True
            if(row>=m or col>=n or row<0 or col<0 or wordToMatch[0]!=board[row][col]):
                return False
            someVal,board[row][col]=board[row][col],""
            res = (backtrack(row+1,col,wordToMatch[1:], currentWord+wordToMatch[0])
            or backtrack(row-1,col,wordToMatch[1:], currentWord+wordToMatch[0])
            or backtrack(row,col+1,wordToMatch[1:], currentWord+wordToMatch[0])
            or backtrack(row,col-1,wordToMatch[1:], currentWord+wordToMatch[0]))
            board[row][col]=someVal
            return res
        m,n=len(board),len(board[0])
        for i in range(0,m):
            for j in range(0,n):
                if(board[i][j]==word[0] and backtrack(i,j,word,"")):
                    return True
        return False