import math

def pal(string):
    temp=""
    string=string.lower()
    for i in range(len(string)):
        if string[i].isalpha():
            temp+=string[i]
    print(temp)
    if len(string)<=1:
        return True
    else:
        if temp[0]==temp[-1]:
            return pal(temp[1:-1])
        else:
            return False


print(pal("Reviled did I live, said I, as evil I did deliver"))
