def powGen(agr):
    return lambda x: x ** agr
square = powGen(2)
print(square(4))
