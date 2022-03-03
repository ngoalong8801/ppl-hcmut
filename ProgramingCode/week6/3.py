from functools import reduce


class ASTGeneration(MPVisitor):

    def visitProgram(self, ctx: MPParser.ProgramContext):

        return Program(reduce(lambda x, y: x + self.visit(y), ctx.vardecl(), []))

    def visitVardecl(self, ctx: MPParser.VardeclContext):
        listID = self.visit(ctx.ids())
        return [VarDecl(x, self.visit(ctx.mptype())) for x in listID]

    def visitMptype(self, ctx: MPParser.MptypeContext):
        if ctx.INTTYPE():
            return IntType()
        return FloatType()

    def visitIds(self, ctx: MPParser.IdsContext):

        return [Id(x.getText()) for x in ctx.ID()]
