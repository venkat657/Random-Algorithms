# H202 -> [(H,2),(O,2)] -> H2O2
# AB2 -> [A->1, B->2]
#rule 1 -> Every other Uppercase character is a separate element
#rule 2 -> If no digit or weight is encountered in the parsing, then the count is only 1   
                # set weight in hashmap to max(1, count encountered)

def countOfElementsStack(chemicalFormula : str):
    stack = []
    result = ""
    elementCountDict = dict()
    if chemicalFormula[0] != '(' and chemicalFormula[-1] != ')':
        return "Invalid input format"
    for index,element in enumerate(chemicalFormula):
        if element.isdigit() and index>0 and chemicalFormula[index-1]==")":
            continue
        if element == ')':
            enclosingCount = int(chemicalFormula[index+1]) if index<len(chemicalFormula)-1 and chemicalFormula[index+1].isdigit() else 1
            while stack and stack[-1] != '(':
                currElementCount = 1
                if stack[-1].isdigit():
                    currElementCount = int(stack.pop())
                currElement = ""
                # below loop is to capture trailing lowercase chars
                while stack and stack[-1]!='(' and not stack[-1].isupper():
                    currChar = stack.pop()
                    currElement = currChar + currElement
                currElement = stack.pop() + currElement
                elementCountDict[currElement] = elementCountDict.get(currElement,0) + (currElementCount * enclosingCount)
            stack.pop()
        else:
            stack.append(element)
    for key in sorted(list(elementCountDict.keys())):
        result+=f"{key}{elementCountDict[key]}"
    return result

print(countOfElementsStack("(HO2)5"))
print(countOfElementsStack("(H2O2)5"))
print(countOfElementsStack("(H2O)"))
print(countOfElementsStack("(C2H4(H2O)5)"))
print(countOfElementsStack("(He2O2)"))
print(countOfElementsStack("(He2O2)3"))
