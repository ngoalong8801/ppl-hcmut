a = [(1,2), (3,4)]
b = [5, 6]

c = list(map(lambda a, b : (a[0], a[1], b), a, b))
print(c)

