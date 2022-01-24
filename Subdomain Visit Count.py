from collections import defaultdict
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        hashTable=defaultdict(int)
        outputArray=[]
        for sites in cpdomains:
            site=sites.split()
            dotCount=site[1].count('.')
            for i in range(0,dotCount+1):
                hashTable["".join(site[1].split('.',i)[i])]+=int(site[0])
        for key,value in hashTable.items():
            string=str(value)+" "+key
            outputArray+=[string]
        return outputArray
            
        
        
