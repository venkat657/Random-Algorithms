class Solution:
    def partition(self, s: str) -> list[list[str]]:
        def isPalindrome(word):
            start=0
            end=len(word)-1
            while(start<end):
                if(word[start]!=word[end]):
                    return False
                start+=1
                end-=1
            return True

        
        def FindPartitions(currentWord, pos, currentCombination):
            if(pos>=len(s) and "".join(currentCombination)==s):
                output.append(currentCombination[:])
                return
            for i in range(pos,len(s)):
                if(isPalindrome(currentWord+s[i])):
                    currentCombination.append(currentWord+s[i])
                    FindPartitions("",i+1, currentCombination)
                    currentCombination.pop()
                currentWord+=s[i]
        output=[]
        FindPartitions("", 0, [])
        return output
    
sol = Solution()
print(sol.partition("aab"));