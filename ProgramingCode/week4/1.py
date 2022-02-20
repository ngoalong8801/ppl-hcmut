def lstSquare(n):
    if(n == 1): return [1]
    return lstSquare(n - 1) + [n*n]

print(lstSquare(4))