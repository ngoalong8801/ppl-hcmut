class TerminalCount(MPVisitor):

    def visitProgram(self, ctx: MPParser.ProgramContext):

        return self.visit(ctx.vardecls()) + 1

    def visitVardecls(self, ctx: MPParser.VardeclsContext):

        return max(self.visit(ctx.vardecl()), self.visit(ctx.vardecltail())) + 1

    def visitVardecltail(self, ctx: MPParser.VardecltailContext):
        if ctx.vardecl():
            return max(self.visit(ctx.vardecl()), self.visit(ctx.vardecltail())) + 1
        return 1

    def visitVardecl(self, ctx: MPParser.VardeclContext):
        return max(self.visit(ctx.mptype()), self.visit(ctx.ids())) + 1

    def visitMptype(self, ctx: MPParser.MptypeContext):

        return 1

    def visitIds(self, ctx: MPParser.IdsContext):
        if ctx.ids():
            return self.visit(ctx.ids()) + 1
        return 1
