import math

def convert(n,base):
    convertString="0123456789ABCDEF"
    if n<base:
        return convertString[n]
    else:
        return convert(n//base,base)+convertString[n%base]

print(convert(13,8))
