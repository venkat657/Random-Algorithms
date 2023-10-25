#problem link: https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        def FindPermutations(array, remArray):
            if(len(remArray)==1):
                output.append(array+[remArray[0]])
                return
            for i in range(0,len(remArray)):
                FindPermutations(array+[remArray[i]], remArray[:i]+remArray[i+1:])
            return
        output=[]
        FindPermutations(list(),nums)
        return output
    

sol = Solution()
print(sol.permute([1,2,3]))