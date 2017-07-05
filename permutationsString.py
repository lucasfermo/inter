from current import Stack

def perm(string,step=0,wordList=[]):
    if step==len(string):
        print(" ".join(string))
        wordList.append("".join(string))
    #Everything to right has not been swapped yet
    for i in range(step,len(string)):

        #Copy the string
        stringCopy=list(string)

        #Swap current index with step
        stringCopy[step],stringCopy[i]=stringCopy[i],stringCopy[step]

        #Recurse of portion that has not been swapped yet
        perm(stringCopy,step+1,wordList)

    return wordList



print("lucas"[:0])

print(perm("abc"))
