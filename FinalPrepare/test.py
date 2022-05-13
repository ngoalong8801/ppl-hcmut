
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
