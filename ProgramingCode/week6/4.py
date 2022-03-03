class ASTGeneration(MPVisitor):

    def visitProgram(self, ctx: MPParser.ProgramContext):

        return self.visit(ctx.mptype())

    def visitMptype(self, ctx: MPParser.MptypeContext):
        if ctx.primtype():
            return self.visit(ctx.primtype())
        return self.visit(ctx.arraytype())

    def visitArraytype(self, ctx: MPParser.ArraytypeContext):

        return ArrayType(self.visit(ctx.dimens()), self.visit(ctx.primtype()))

    def visitPrimtype(self, ctx: MPParser.PrimtypeContext):
        if ctx.INTTYPE():
            return IntType()
        return FloatType()

    def visitDimens(self, ctx: MPParser.DimensContext):
        if len(ctx.dimen()) == 1:
            return self.visit(ctx.dimen(0))
        return reduce(lambda x, y: UnionType(x, self.visit(y)), ctx.dimen()[1:], self.visit(ctx.dimen(0)))

    def visitDimen(self, ctx: MPParser.DimenContext):

        return RangeType(self.visit(ctx.num(0)), self.visit(ctx.num(1)))

    def visitNum(self, ctx: MPParser.DimenContext):
        if ctx.getChildCount() == 2:
            return int("-" + ctx.INTLIT().getText())
        return int(ctx.INTLIT().getText())
