def permutation(str):
    myList = []
    if len(str) ==1:
       myList.append(str)
       return myList
    for char in str:
        newList = permutation(str.replace(char,'',1))
        
        for item in newList:
            item+=char
            myList.append(item)
    return myList


print permutation('111')
       