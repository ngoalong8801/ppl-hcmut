a = [("$123",2), ("ab",4)]
b = [5, 6]

c = list(map(lambda a, b : (a[0], a[1], b), a, b))
d = list(map(lambda c: c + ("Static",) if c[0][0] == "$" else c + ("Kind",), c))
a = '$dasd'
kind = lambda x : '0' if x[0] == '$' else '1'
fun = lambda x, y : x + y
lis = [1,2,3,4]
b = 5
c = 0

class Test:
    def __init__(self, element1, element2 = None):
        self.element1 = element1
        self.element2 = element2

    # def __init__(self, element1):
    #     self.element1 = element1

    def __str__(self):
        return "Test(" + str(self.element1) +  (("," + str(self.element2) if self.element2 else "")) + ")"
## Test(2,Test(3))

func = lambda x : Test(x.pop())
print(func(lis))


