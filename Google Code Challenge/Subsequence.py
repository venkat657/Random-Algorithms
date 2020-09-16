def FindMinStack(newstack,value):
    while(len(newstack)>0 and newstack[-1]>=value):
        newstack.pop()
    newstack.append(value)
    return newstack
        
def ifPresent(indexvalues,stackvals):
    if(len(indexvalues)==0):
        return len(stackvals)
    else:
        if(indexvalues[0]>stackvals[-1]):
            stackvals.append(indexvalues[0])
            return ifPresent(indexvalues[1:],stackvals)
        else:
            newstack=FindMinStack(stackvals.copy(),indexvalues[0])
            return max(ifPresent(indexvalues[1:],stackvals),ifPresent(indexvalues[1:],newstack))    
               
def solve (N, M, A, B):
    indexDict={}
    for number in range(0,len(A)):
        indexDict[A[number]]=number
    indexArrB=[-1]*len(B)
    for i in range(0,len(B)):
        if(B[i] in indexDict):
            indexArrB[i]=indexDict[B[i]]
    mincnt=len(A)
    indexvalues=[x for x in indexArrB if x>-1]
    stackvals=[]
    stackvals.append(indexvalues[0])
    return N-ifPresent(indexvalues[1:],stackvals)
    

    

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    out_ = solve(N, M, A, B)
    print (out_)
