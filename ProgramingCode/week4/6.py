#Let lst be a list of integer and n be any value, use list comprehension approach to write function dist(lst,n) that returns the list of pairs of an element of lst and n.
def dist(lst, n):
    return [(x, n) for x in lst]


print(dist([1, 2, 3], 4))
