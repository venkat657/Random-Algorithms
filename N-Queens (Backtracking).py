class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        def BackTrack(currentHash, currentChessBoard, currentRow):
            if(currentRow>=n):
                output.append(["".join(row) for row in currentChessBoard])
                return
            for i in range(0,n):
                if(currentHash[i]!=1):

                    #Check if immediate previous rows' adjacent columns and left and right diagonals hold a queen
                    if(currentRow>0 and i>0 and currentChessBoard[currentRow-1][i-1]=='Q'):
                        continue
                    if(currentRow>0 and i<n-1 and currentChessBoard[currentRow-1][i+1]=='Q'):
                        continue

                    # all elements in a given diagonal will have the same sum of their row, col values. (Difference incase of left/preceding diagonal)
                    if(currentRow+i in rightDiagonalHash or currentRow-i in leftDiagonalHash):
                        continue

                    #set context for exploring current combination
                    currentChessBoard[currentRow][i]='Q'
                    currentHash[i]=1
                    rightDiagonalHash.add(currentRow+i)
                    leftDiagonalHash.add(currentRow-i)
                    BackTrack(currentHash,currentChessBoard,currentRow+1)

                    #(Backtrack) revert before next iteration and exploration of next combination
                    currentChessBoard[currentRow][i]='.'
                    currentHash[i]=0
                    rightDiagonalHash.remove(currentRow+i)
                    leftDiagonalHash.remove(currentRow-i)
        output=[]
        chessBoard = [['.' for i in range(n)] for j in range(n)]
        queenHash = [0]*n
        leftDiagonalHash = set()
        rightDiagonalHash = set()
        BackTrack(queenHash,chessBoard,0)
        return output


sol = Solution()
print(sol.solveNQueens(5))