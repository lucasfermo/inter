from current import Stack

rStack=Stack()

def toStr(n,base):
    convertString="0123456789ABCDEF"
    while n>0:
        if n<base:
            rStack.push(convertString[n])
        else:
            rStack.push(convertString[n%base])
        n=n//base
    temp=""
    for i in range(rStack.size()):
        temp+=rStack.pop()

    return temp

print(toStr(8,4))
