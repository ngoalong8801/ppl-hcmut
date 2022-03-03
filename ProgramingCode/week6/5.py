class ASTGeneration(MPVisitor):

    def visitProgram(self, ctx: MPParser.ProgramContext):
        return self.visit(ctx.mptype())

    def visitMptype(self, ctx: MPParser.MptypeContext):
        if ctx.primtype():
            return self.visit(ctx.primtype())
        return self.visit(ctx.arraytype())

    def visitArraytype(self, ctx: MPParser.ArraytypeContext):
        if ctx.primtype():
            return ArrayType(self.visit(ctx.dimen()), self.visit(ctx.primtype()))
        type = (self.visit(ctx.arraytype())).eleType
        dimens = [(self.visit(ctx.arraytype())).indexType] + \
            [self.visit(ctx.dimen())]
        temp = reduce(lambda x, y: UnionType(x, y), dimens)
        return ArrayType(temp, type)

    def visitPrimtype(self, ctx: MPParser.PrimtypeContext):
        if ctx.INTTYPE():
            return IntType()
        return FloatType()

    def visitDimen(self, ctx: MPParser.DimenContext):
        return RangeType(self.visit(ctx.num(0)), self.visit(ctx.num(1)))

    def visitNum(self, ctx: MPParser.DimenContext):
        if ctx.getChildCount() == 1:
            return int(ctx.INTLIT().getText())
        return -int(ctx.INTLIT().getText())
