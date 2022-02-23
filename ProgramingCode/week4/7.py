#Scala has function compose to compose two functions but Python does not have this function. Write function compose that can takes at least two functions  as its parameters and returns the composition of these parameter functions. For example compose(f,g,h)(x) is defined as f(g(h(x))).





square = lambda x : x * x
increase = lambda x : x + 1
def compose(func1, func2, *func):
    function = list((func1, func2) + func)
    def inner(x):
        if len(function) > 1:
            return inner(function.pop()(x))
        return function.pop(0)(x)
    return inner
   

f = compose(increase, square)

print(f(3))
