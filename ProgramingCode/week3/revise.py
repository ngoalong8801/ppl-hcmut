class Exp: 
    def eval():
        pass

class BinExp: 
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

    def eval(self):
        if(self.operator == '*'):
            return self.left.eval() * self.right.eval()
        elif(self.operator == '/'):
            return self.left.eval() / self.right.eval()
        elif(self.operator == '+'):
            return self.left.eval() + self.right.eval()
        elif(self.operator == '-'):
            return self.left.eval() - self.right.eval()
    
    def printPrefix(self):
        return self.left.printPrefix() + ' ' + self.operator + ' ' + self.right.printPrefix()

class UnExp: 
    def __init__(self, uOper, operand):
        self.uOper = uOper 
        self.operand = operand
    
    def eval(self):
        if(self.uOper == '+'):
            return self.operand.eval()
        elif(self.uOper == '-'):
            return '-' + self.operand.eval()

    def printPrefix(self):
        return self.uOper + '. ' + self.operand.printPrefix()

class IntLit: 
    def __init__(self, value):
        self.value = value

    def eval(self):
        return self.value
    
    def printPrefix(self):
        return str(self.value)

class FloatLit: 
    def __init__(self, value):
        self.value = value
    
    def eval(self):
        return self.value
    
    def printPrefix(self):
        return str(self.value)


x = BinExp(IntLit(4), '+', IntLit(5))
print(x.printPrefix())
