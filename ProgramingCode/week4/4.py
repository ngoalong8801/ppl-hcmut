def dist(lst, n):
    if not lst: return []
    else:
        value = lst.pop()
        return dist(lst, n) + [(value, n)]


print(dist([1,2,3], 4))