from ast import List
from functools import reduce
lis = ["d", ["a", "c"], "c"]

ls = reduce(lambda x, y: x + y if isinstance(x, list) else x + reduce(lambda a, b: a + b, y, ""), lis, "")
# print(isinstance(lis, list))
print(ls)