class Solution:
    def isPalindrome1(self,string):
        for i in range(0,int(len(string)/2)+1):
            if(not(string[i]==string[len(string)-1-i])):
                return False
        return True
    def longestPalindrome(self, s: str) -> str:
        currentPal=""
        maxSIndex=0
        maxEIndex=1
        prevIndex=0
        
        for i in range(0,len(s)):
            currentPal+=s[i]
            if(self.isPalindrome1(currentPal[prevIndex:])):
                if(len(currentPal[prevIndex:])>len(s[maxSIndex:maxEIndex])):
                   maxEIndex=i+1
                   maxSIndex=prevIndex
            elif(self.isPalindrome1(currentPal[0:i+1])):
                   maxEIndex=i+1
                   maxSIndex=0
            elif(self.isPalindrome1(currentPal[prevIndex-1:]) and len(currentPal[prevIndex-1:])>len(s[maxSIndex:maxEIndex])):
                maxSIndex=prevIndex-1
                maxEIndex=i+1
                prevIndex-=1
            else:
                prevIndex+=1
        return s[maxSIndex:maxEIndex]
                     
                   
            
        
s=Solution()
print(s.longestPalindrome("cabbsbb"))
    
