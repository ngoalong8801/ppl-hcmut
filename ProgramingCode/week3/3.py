
class Exp:
    def accept(self, visitor):
        return visitor.visit(self)
    
class BinExp(Exp):
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
    
    def printPrefix(self):
        return self.oper + ' ' + self.left.printPrefix() + ' ' + self.right.printPrefix()

    def printPostfix(self):
        return self.left.printPostfix() + ' ' + self.right.printPostfix() + ' ' + self.oper


class UnExp(Exp):
    def __init__(self, oper, arg):
        self.oper = oper
        self.arg = arg
    
    def eval(self):
        if(self.oper == '+'):
            return self.arg.value
        elif(self.oper == '-'):
            return -self.arg.value
    
    def printPrefix(self):
        return self.oper + '. ' + self.arg.printPrefix()
    
    def printPostfix(self):
        return self.arg.printPostfix()+ ' ' + self.oper + '.' 


class IntLit(Exp):
    def __init__(self, num):
        self.value = num
    
    def eval(self):
        return self.value

    def printPrefix(self):
        return str(self.value)
    
    def printPostfix(self):
        return str(self.value)


class FloatLit(Exp):
    def __init__(self, num):
        self.value = num
    
    def eval(self):
        return self.value

    def printPrefix(self):
        return str(self.value)
    
    def printPostfix(self):
        return str(self.value)

class Visitor:
    def visit(self, cl):
        pass

class PrintPrefix(Visitor):
    def visit(self, cl):
        return cl.printPrefix()

class Eval(Visitor):
    def visit(self, cl):
        return cl.eval()

class PrintPostfix(Visitor):
    def visit(self, cl):
        return cl.printPostfix()



    




