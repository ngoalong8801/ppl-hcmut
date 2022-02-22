a = [("$123",2), ("ab",4)]
b = [5, 6]

c = list(map(lambda a, b : (a[0], a[1], b), a, b))
d = list(map(lambda c: c + ("Static",) if c[0][0] == "$" else c + ("Kind",), c))
print (d)

