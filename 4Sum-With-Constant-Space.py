class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        outputArray=set()
        for i in range(0,len(nums)-3):
            for j in range(i+1,len(nums)-2):
                start=j+1
                end=len(nums)-1
                while(start<end and end<len(nums)):
                    sumVal = nums[i]+nums[j]+nums[start]+nums[end]
                    if(sumVal==target):
                        outputArray.add((nums[i],nums[j],nums[start],nums[end]))
                        start+=1
                        end-=1
                    elif(sumVal>target):
                        end-=1
                    else:
                        start+=1
        return [ list(x) for x in outputArray ]
                        
sol = Solution()
print(sol.fourSum([1,0,-1,0,-2,2],0))
