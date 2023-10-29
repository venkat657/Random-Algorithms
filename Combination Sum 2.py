#link: https://leetcode.com/problems/combination-sum-ii/description/
class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        def backtrack(combination,rem,start):
            if(rem<0):
                return
            if(rem==0):
                output.append(combination[:])
                return
            else:
                for i in range(start,len(candidates)):
                    if(i>start and candidates[i]==candidates[i-1]):
                        continue
                    if(candidates[i]>target or rem<candidates[i]):
                        break
                    combination.append(candidates[i])
                    backtrack(combination,rem-candidates[i],i+1)
                    combination.pop()
                return
        output=[]
        candidates.sort()
        backtrack(list(),target,0)
        return output
    
sol =Solution()
print(sol.combinationSum2([10,1,2,7,6,1,5],8))