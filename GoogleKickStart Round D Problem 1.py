def FindDiff(a,t,n):
    d=int(abs((t-a))/(n-1))
    return d
def FindMaxLimit(L1,L2,L3,L4):
    valueCount={}
    d1=FindDiff(L1[0],L1[1],3)
    d2=FindDiff(L2[0],L2[1],3)
    d3=FindDiff(L3[0],L3[1],3)
    d4=FindDiff(L4[0],L4[1],3)
    valueCount[L1[0]+d1]=1
    if(L2[0]+d2 in valueCount):
        valueCount[L2[0]+d2]+=1
    else:
        valueCount[L2[0]+d2]=1
    if(L3[0]+d3 in valueCount):
        valueCount[L3[0]+d3]+=1
    else:
        valueCount[L3[0]+d3]=1
    if(L4[0]+d4 in valueCount):
        valueCount[L4[0]+d4]+=1
    else:
        valueCount[L4[0]+d4]=1
    return max(list(valueCount.values()))
        
    
    
def DefaultAPs(a,b,c):
    if((b-a)==(c-b)):
        return 1
    else:
        return 0
testCases=int(input())
for i in range(1,testCases+1):
    G00,G01,G02=map(int,input().split())
    G10,G12=map(int,input().split())
    G20,G21,G22=map(int,input().split())
    y=FindMaxLimit([G00,G22],[G20,G02],[G01,G21],[G10,G12])+DefaultAPs(G00,G10,G20)+DefaultAPs(G20,G21,G22)+DefaultAPs(G00,G01,G02)+DefaultAPs(G02,G12,G22)
    print(str("Case #"+str(i)+": "),end="")
    print(y)
    #FindMaxLimit([G00,G22],[G20,G02],[G01,G21])
