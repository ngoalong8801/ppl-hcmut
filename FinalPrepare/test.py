
from xmlrpc.client import Boolean, boolean


def visitContinue(self, ast, o):
    ctxt = o
    frame = ctxt
    self.emit.printout(self.emit.emitGOTO(frame.getContinueLabel(), frame))


def visitDoWhile(self, ast, o):
    ctxt = o
    frame = ctxt
    frame.enterLoop()

    cnt_label = frame.getContinueLabel()
    brk_label = frame.getBreakLabel()
    s_label = frame.getNewLabel()
    e_label = frame.getNewLabel()

    self.emit.printout(self.emit.emitLABEL(s_label, frame))
    self.visit(body, o)

    self.emit.printout(self.emit.emitLABEL(cnt_label, frame))
    self.emit.printout(self.visit(expr, Access(frame, o.sym, False)))
    self.emit.printout(self.emit.emitIFTRUE(s_label, frame))
    self.emit.printout(self.emit.emitLABEL(e_label, frame))

    frame.exitLoop()


def visitBinary(self, ast, o):
    ctxt = o
    frame = ctxt
    rs = ""
    returnType = IntType()
    end_label = frame.getNewLabel()
    short_label = frame.getNewLabel()
    lc, lt = self.visit(ast.left, Access(frame, o.sym, False))
    if ast.op == '+' or ast.op == '/':
        rc, rt = self.visit(ast.right, Access(frame, o.sym, False))
        rs += lc
        if type(lt) is FloatType:
            rs += self.emit.emitI2F(frame)
            returnType = FloatType()
        rs += rc
        if type(rt) is FloatType:
            rs += self.emit.emitI2F(frame)
            returnType = FloatType()

        if ast.op == '+':
            rs += self.emit.emitADDOP(ast.op, returnType, frame)
        elif ast.op == '/':
            rs += self.emit.emitMUL(ast.op, returnType, frame)
            returnType = FloatType()
    else:
        rs += lc
        rs += self.emitIFTRUE(short_label, frame)
        rc, rt = self.visit(ast.right, Access(frame, o.sym, False))
        rs += rc
        rs += self.emitIFTRUE(short_label, frame)
        rs += self.emit.emitPUSHICONST(0, frame)
        rs += self.emit.emitGOTO(end_label, frame)

        rs += self.emit.emitLABEL(short_label, frame)
        rs += self.emit.emitPUSHICONST(1, frame)
        rs += self.emit.emitLABEL(end_label, frame)
        returnType = BoolType()

    return rs, returnType


int mul_exception(Node root){
    try{
        return mul(root)
    }
    catch(int x){
        return 0
    }
}

int mul(Node root){
    if (root == null) return 1
    else if (root.val == 0)  throw 0
    return root.val * roo
}


def visitIf(self, ast, o):
    ctxt = o
    frame = ctxt.frame
    loop_label = frame.getNewLabel()
    end_label = frame.getNewLabel()
    frame.enterLoop()

    self.visit(stmt, o)
    self.emit.printout(self.visit(exp, Access(frame, o.sym, False)))
    self.emit.printout(self.emitIFTRUE(end_label, frame))

    self.visit(stmt2, o)
    self.emit.printout(self.emitContinue(frame.getContinueLabel(), frame))
    self.emit.printout(self.emit.emitGOTO(loop_label, frame))

    self.emit.printout(self.emit.emitLABEL(end_label, frame))
    self.emit.printout(self.emit.emitLABEL(frame.getBreakLabel(), frame))


def visitFuncDecl(self, ast, o):
    o = []
    list_param = []
    for i in params:
        list_param += self.visit(i, list_param)

    check_list = []
    for i in ast.body:
        check_list += self.visit(i, (list_param, check_list))


def visitParamDecl(self, ast, o):
    typeFirst = self.visit(ast.first, o)
    if typeFirst:
        return [ast.name.name]
    return []


def visitBoolLit(self, ast, o):
    return ast.value


def visitAssign(self, ast, o):
    name = ast.lhs.name
    if name in o[1] and name in o[0]:
        raise FirstParamReassignment(ast)
    return [name]


def visitDoWhile(self, ast, o):
    ctxt = o
    frame = ctxt.frame
    s_label = frame.getNewLabel()
    e_label = frame.getNewLabel()
    frame.enterLoop()

    self.visit(ast.stmt1, o)
    self.emit.printout(self.visit(ast.expr, Access(frame, o.sym, False)))
