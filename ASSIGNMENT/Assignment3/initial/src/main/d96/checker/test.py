def a():
    return []


l = []
l.extend(a())
l.extend([3])
print(l)
