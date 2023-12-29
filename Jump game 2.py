#link: https://leetcode.com/problems/jump-game-ii/description/

class Solution:
    def jump(self, nums: list[int]) -> int:

        '''
        #dp approach , time complexity of O(n^2)
        def minjump(pos,currHops):
            if(pos>=len(nums)-1):
                dp[-1] = 0
                return currHops
            if(dp[pos]!=-1):
                return dp[pos]+currHops
            minVal = len(nums) - 1
            if(nums[pos]==0):
                return len(nums)-1
            for i in range(nums[pos],0,-1):
                    minVal = min(minVal,minjump(pos+i,1))
            dp[pos] = minVal
            return minVal + currHops
        dp = [-1] * len(nums)
        return minjump(0,0)
        '''

        #greedy approach , time complexity of O(n)
        l = r = 0
        farthest = 0
        jumps = 0
        while(r<len(nums)-1):
            for i in range(l,r+1):
                farthest = max(farthest, nums[i]+i)
            l = r+1
            r = farthest
            jumps+=1
        return jumps
        