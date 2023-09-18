class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        numsDict={}
        outputDict={}
        outputList=[]
        '''
        for i in range(0,len(nums)):
            if(nums[i] not in numsDict):
                numsDict[nums[i]]=0
            numsDict[nums[i]]+=1
        for i in range(0,len(nums)):
            a=nums[i]
            for j in range(i+1,len(nums)):
                b=nums[j]
                for k in range(j+1,len(nums)):
                    c=nums[k]
                    d=target-(a+b+c)     
                    sortedVals = [a,b,c,d]
                    sortedVals.sort()
                    numsDict[a]-=1
                    numsDict[b]-=1
                    numsDict[c]-=1              
                    if(numsDict.get(d,0)>0 and tuple(sortedVals) not in outputDict):
                        outputDict[tuple(sortedVals)]=True
                        outputList+=[sortedVals]
                    numsDict[a]+=1
                    numsDict[b]+=1
                    numsDict[c]+=1
        return outputList         
        '''

        nums.sort()
        for i in range(0,len(nums)):
            if(nums[i] not in numsDict):
                numsDict[nums[i]]=0
            numsDict[nums[i]]+=1
        for i in range(0,len(nums)):
            leftPointer=i+1
            rightPointer=len(nums)-1
            print(outputList)
            while(leftPointer<rightPointer):
                a=nums[i]
                b=nums[leftPointer]
                c=nums[rightPointer]
                d=target-(a+b+c)
                numsDict[a]-=1
                numsDict[b]-=1
                numsDict[c]-=1
                sortedVals=[a,b,c,d]
                if(numsDict.get(d,0)>0 and tuple(sortedVals) not in outputDict):
                    outputDict[tuple(sortedVals)]=True
                    outputList+=[sortedVals]
                    leftPointer=rightPointer
                elif(d>nums[rightPointer]):
                    leftPointer+=1
                elif(d<nums[leftPointer]):
                    rightPointer-=1
                numsDict[a]+=1
                numsDict[b]+=1
                numsDict[c]+=1



a = Solution()
a.fourSum([1,0,-1,0,-2,2],0)
