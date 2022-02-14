class Exp:
    def eval():
        pass
    
class BinExp:
    def __init__(self, left, oper, right):
        self.left = left
        self.oper = oper
        self.right = right
        
    def eval(self):
        if(self.oper == '*'):
            return self.left.eval() * self.right.eval()
        if(self.oper == '/'):
            return self.left.eval() / self.right.eval()
        if(self.oper == '+'):
            return self.left.eval() + self.right.eval()
        if(self.oper == '-'):
            return self.left.eval() - self.right.eval()

class UnExp: 
    def __init__(self, oper, arg):
        self.oper = oper
        self.arg = arg
    
    def eval(self):
        if(self.oper == '+'):
            return self.arg.value
        elif(self.oper == '-'):
            return -self.arg.value

class IntLit: 
    def __init__(self, num):
        self.value = num
    
    def eval(self):
        return self.value

class FloatLit: 
    def __init__(self, num):
        self.value = num
    
    def eval(self):
        return self.value

x = BinExp(IntLit(4), '+', IntLit(5)).eval()
print(x)



