def TwoComp(n): # function that returns the 2s complement of the binary input, both input and output are strings
    li = list(n)
    for i in range(len(li)):
        li[i] = "0" if li[i] == "1" else "1"
    return add("".join(li), "1")