class ASTGeneration(MPVisitor):

    def visitProgram(self, ctx: MPParser.ProgramContext):
        return 1 + self.visit(ctx.vardecls())

    def visitVardecls(self, ctx: MPParser.VardeclsContext):

        return 1 + self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail())

    def visitVardecltail(self, ctx: MPParser.VardecltailContext):
        if ctx.vardecl():
            return 1 + self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail())
        return 1

    def visitVardecl(self, ctx: MPParser.VardeclContext):
        return 1 + self.visit(ctx.mptype()) + self.visit(ctx.ids())

    def visitMptype(self, ctx: MPParser.MptypeContext):
        return 1

    def visitIds(self, ctx: MPParser.IdsContext):
        if ctx.ids():
            return 1 + self.visit(ctx.ids())
        return 1
