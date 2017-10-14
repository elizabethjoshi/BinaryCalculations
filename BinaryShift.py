def LeftShift(a) : #function to carry out left shift
    a=list(a)
    return "".join(a[-(len(a)-1):])

def RightShift(a) : #function to carry out right shift
    a=list(a)
    for i in range (len(a)-1,0,-1) :
        a[i]=a[i-1]
    return "".join(a)