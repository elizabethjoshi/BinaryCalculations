def add(x, y):   # function to carry out binary addition and returns the result as a string
    maxlen = max(len(x), len(y))

    # Normalize lengths
    x = x.zfill(maxlen)
    y = y.zfill(maxlen)
    result = ''
    carry = 0
    for i in range(maxlen - 1, -1, -1): #reverse order range, decreasing by 1 in every iteration
        r = carry
        r += 1 if x[i] == '1' else 0
        r += 1 if y[i] == '1' else 0
        result = ('1' if r % 2 == 1 else '0') + result
        carry = 0 if r < 2 else 1
    if carry != 0: result = '1' + result
    result.zfill(maxlen)
    return result[-16:]