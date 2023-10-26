#link : https://leetcode.com/problems/subsets-ii/description/
class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        output = []
        nums.sort()
        def backtrack(i,subset):
            if (i==len(nums)):
                output.append(subset[:])
                return
            subset.append(nums[i])
            backtrack(i+1,subset)
            subset.pop()

            while(i<len(nums)-1 and nums[i]==nums[i+1]):
                i+=1
            backtrack(i+1, subset)
        backtrack(0,[])
        return output

        '''
        def dfs(start, subset):
            if(start>=len(nums)):
                output.add(tuple(subset))
                return
            dfs(start+1,subset+[nums[start]])
            dfs(start+1,subset)
        nums.sort()  
        output=set()
        dfs(0,[])
        return [list(x) for x in output]
        '''


sol = Solution()
print(sol.subsetsWithDup([1,2,2]))