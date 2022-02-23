from dataclasses import Field
from AST import *
from D96Parser import D96Parser
from D96Visitor import D96Visitor
from StaticError import Variable


class ASTGeneration(D96Visitor):
    def visitProgram(self, ctx: D96Parser.ProgramContext):
        return Program([self.visit(x) for x in ctx.class_decl()])
    
    def visitClass_decl(self, ctx: D96Parser.Class_declContext):
        mem_decl_list = []
        if ctx.COL(): 
            if ctx.mem_decl():
               return ClassDecl(Id(ctx.IDEN(0).getText()), [self.visit(x) for x in ctx.mem_decl()]), Id(ctx.IDEN(1).getText())
            return ClassDecl(Id(ctx.IDEN(0).getText()), [], Id(ctx.IDEN(1).getText()))
        if ctx.mem_decl():
            [ mem_decl_list.extend(self.visit(x)) for x in ctx.mem_decl()]
            return ClassDecl(Id(ctx.IDEN(0).getText()), mem_decl_list)
        return ClassDecl(Id(ctx.IDEN(0).getText()), [])

    def visitMem_decl(self, ctx: D96Parser.Mem_declContext):
        if ctx.attr_decl():
            return self.visit(ctx.attr_decl())
        if ctx.method_decl():
            return self.visit(ctx.method_decl())

    def visitAttr_decl(self, ctx: D96Parser.Attr_declContext):
        if ctx.immutable_attr():
            return self.visit(ctx.immutable_attr())
        return self.visit(ctx.mutable_attr())
    
    def visitImmutable_attr(self, ctx: D96Parser.Immutable_attrContext):
        IdListType = self.visit(ctx.id_list_type())
        IdListTypeKind = list(map(lambda x: x + (Static(), ) if x[0].name[0] == "$" else x + (Instance(),), IdListType))
        if ctx.expr_list():
            exprList = self.visit(ctx.expr_list())
            compList = list(map(lambda x, y : x + (y , ), IdListTypeKind, exprList))
            return [AttributeDecl(kind, ConstDecl(id, dataType, expr)) for (id, dataType, kind, expr) in compList]
        return [AttributeDecl(kind, ConstDecl(id, dataType)) for (id, dataType, kind) in IdListTypeKind]

    def visitMutable_attr(self, ctx: D96Parser.Mutable_attrContext):
        IdListType = self.visit(ctx.id_list_type())
        IdListTypeKind = list(map(lambda x: x + (Static(), )
                              if x[0].name[0] == "$" else x + (Instance(),), IdListType))
        if ctx.expr_list():
            exprList = self.visit(ctx.expr_list())
            compList = list(map(lambda x, y: x + (y, ),
                            IdListTypeKind, exprList))
            return [AttributeDecl(kind, VarDecl(id, dataType, expr)) for (id, dataType, kind, expr) in compList]
        return [AttributeDecl(kind, VarDecl(id, dataType)) for (id, dataType, kind) in IdListTypeKind]
    

        
    def visitId_list_type(self, ctx: D96Parser.Id_list_typeContext):
        dataType = self.visit(ctx.data_type())
        idList = self.visit(ctx.id_list())
        return [(id, dataType) for id in idList]
    
    def visitId_list(self, ctx: D96Parser.Id_listContext):
        return [self.visit(iden_dol) for iden_dol in ctx.iden_dol()]
    
    def visitIden_dol(self, ctx: D96Parser.Iden_dolContext):
            return Id(ctx.IDEN().getText())

    def visitExpr_list(self, ctx: D96Parser.Expr_listContext):
        return [self.visit(x) for x in ctx.expr()]

    def visitData_type(self, ctx: D96Parser.Data_typeContext):
        if ctx.INT():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.STRING():
            return StringType()
        elif ctx.BOOLEAN():
            return BoolType()
        else:
            return self.visit(ctx.getChild(0))
    
    def visitMethod_decl(self, ctx: D96Parser.Method_declContext):
        if ctx.constr_decl():
            return [self.visit(ctx.getChild(0))]
        elif ctx.destr_decl():
            return [self.visit(ctx.getChild(0))]
        else:
            iden_dol = self.visit(ctx.getChild(0))
            kind = lambda x: Static() if x.name[0] == '$' else Instance()
            if ctx.getChildCount() == 4:
                return [MethodDecl(kind(iden_dol), iden_dol, [], self.visit(ctx.getChild(3)))] 
            else:
                return [MethodDecl(kind(iden_dol), iden_dol, self.visit(ctx.getChild(2)), self.visit(ctx.getChild(4)))]
    
    def visitBlock_stmt(self, ctx: D96Parser.Block_stmtContext):
        if ctx.getChildCount() == 3:
            return Block([self.visit(x) for x in ctx.block_item()])
        else:
            return None;
    
    def visitBlock_item(self, ctx: D96Parser.Block_itemContext):
        return self.visit(ctx.getChild(0))
    
    """                  Assign Statement                      """
    def visitAssign_stmt(self, ctx: D96Parser.Assign_stmtContext):
        return self.visit(ctx.getChild(0))
    
    def visitAssign_lhs(self, ctx: D96Parser.Assign_lhsContext):
        return Assign(self.visit(ctx.lhs()), self.visit(ctx.expr()))

    def visitLhs(self, ctx: D96Parser.LhsContext):
        if ctx.IDEN():
            return Id(ctx.IDEN().getText())
        else:
            return self.visit(ctx.getChild(0))
    
    def visitArray_operator(self, ctx: D96Parser.Array_operatorContext):
        return ArrayCell(self.visit(ctx.getChild(0)), self.visit(ctx.getChild(1)))
    
    def visitField_access(self, ctx: D96Parser.Field_accessContext):
        return FieldAccess(self.visit(ctx.getChild(0), Id(ctx.getChild(2).getText())))

    """                  If Statement                      """
    def visitIf_stmt(self, ctx: D96Parser.If_stmtContext):
        expr_thenStmt = self.visit(ctx.getChild(0))
        if ctx.getChildCount() == 3:
            return
        elif(ctx.getChildCount() == 2 ):
            if ctx.elif_elements():
                return If(expr_thenStmt[0], expr_thenStmt[1] , self.visit(ctx.getChild(1)))
        else:
            return If(expr_thenStmt[0], expr_thenStmt[1])

    def visitIf_element(self, ctx: D96Parser.If_stmtContext):
        return (self.visit(ctx.expr()), self.visit(ctx.block_stmt()))

    def visitElif_elements(self, ctx: D96Parser.Elif_elementsContext):
        expr_thenStmt = self.visit(ctx.getChild(0))
        if ctx.getChildCount() == 2:
            return If(expr_thenStmt[0], expr_thenStmt[1], self.visit(ctx.getChild(1)))
        return If(expr_thenStmt[0], expr_thenStmt[1])
        
    def visitElif_element(self, ctx: D96Parser.Elif_elementContext):
        return (self.visit(ctx.expr()), self.visit(ctx.block_stmt()))

    def visitElse_element(self, ctx: D96Parser.Else_elementContext):
        return self.visit(ctx.block_stmt())

    """                  Break Statement                      """
    def visitBreak_stmt(self, ctx: D96Parser.Break_stmtContext):
        return Break()
    """                  Continue Statement                      """
    def visitContinue_stmt(self, ctx: D96Parser.Continue_stmtContext):
        return Continue()
    
    def visitForin_stmt(self, ctx: D96Parser.Forin_stmtContext):
        if ctx.BY():
            return For(Id(ctx.IDEN().getText()), IntLiteral(ctx.INTEGER_LITERAL(0)), IntLiteral(ctx.INTEGER_LITERAL(1)), self.visit(ctx.block_stmt()), IntLiteral(ctx.INTEGER_LITERAL(2)))
        else:
            return For(Id(ctx.IDEN().getText()), IntLiteral(ctx.INTEGER_LITERAL(0)), IntLiteral(ctx.INTEGER_LITERAL(1)), self.visit(ctx.block_stmt()))

    def visitReturn_stmt(self, ctx: D96Parser.Return_stmtContext):
        if ctx.expr():
            return Return(self.visit(ctx.expr()))
        return Return()

    def visitMethod_invocation_stmt(self, ctx: D96Parser.Method_invocation_stmtContext):
        return self.visit(ctx.getChild(0))
    
    def visitMethod_invocation(self, ctx: D96Parser.Method_invocationContext):
        if ctx.expr_list():
            return CallExpr(self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)), self.visit(ctx.getChild(4)))
        return CallExpr(self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)), [])
    "                                                         "
    def visitExpr(self, ctx: D96Parser.ExprContext):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
        else: 
            return self.visit(ctx.getChild(0))
        
    def visitExpr1(self, ctx: D96Parser.Expr1Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
        else: 
            return self.visit(ctx.getChild(0))
    
    def visitExpr2(self, ctx: D96Parser.Expr2Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
        else:
            return self.visit(ctx.getChild(0))
    
    def visitExpr3(self, ctx: D96Parser.Expr3Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
        else:
            return self.visit(ctx.getChild(0))
    
    def visitExpr4(self, ctx: D96Parser.Expr4Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
        else:
            return self.visit(ctx.getChild(0))

    def visitExpr5(self, ctx: D96Parser.Expr5Context):
        if ctx.getChildCount() == 2:
            return UnaryOp(ctx.getChild(0).getText(), self.visit(ctx.getChild(1)))
        else:
            return self.visit(ctx.getChild(0))

    def visitExpr6(self, ctx: D96Parser.Expr6Context):
        if ctx.getChildCount() == 2:
            return UnaryOp(ctx.getChild(0).getText(), self.visit(ctx.getChild(1)))
        else:
            return self.visit(ctx.getChild(0))
    
    def visitExpr7(self, ctx: D96Parser.Expr7Context):
        if ctx.getChildCount() == 2:
            return ArrayCell(self.visit(ctx.getChild(0)), self.visit(ctx.getChild(1)))
        else:
            return self.visit(ctx.getChild(0))
    
    def visitIndex_operators(self, ctx: D96Parser.Index_operatorsContext):
        if ctx.getChildCount() == 4:
            return [self.visit(ctx.getChild(1))] + self.visit(ctx.getChild(3))
        else: 
            return [self.visit(ctx.getChild(1))]

    def visitExpr8(self, ctx: D96Parser.Expr8Context):
        if ctx.getChildCount() == 3:
            return FieldAccess(self.visit(ctx.getChild(0)), Id(ctx.IDEN().getText()))
        elif ctx.getChildCount() == 4:
            return CallExpr(self.visit(ctx.getChild(0)), Id(ctx.IDEN().getText()), [])
        elif ctx.getChildCount() == 5:
            return CallExpr(self.visit(ctx.getChild(0)), Id(ctx.IDEN().getText()), self.visit(ctx.expr_list()))
        else:
            return self.visit(ctx.getChild(0))
        
    def visitExpr9(self, ctx: D96Parser.Expr9Context):
        if ctx.getChildCount() == 3:
            return FieldAccess(self.visit(ctx.getChild(0)), Id(ctx.IDEN().getText()))
        elif ctx.getChildCount() == 4:
            return CallExpr(self.visit(ctx.getChild(0)), Id(ctx.IDEN().getText()), [])
        elif ctx.getChildCount() == 5:
            return CallExpr(self.visit(ctx.getChild(0)), Id(ctx.IDEN().getText()), self.visit(ctx.expr_list()))
        else:
            return self.visit(ctx.getChild(0))
        
    def visitExpr10(self, ctx: D96Parser.Expr10Context):
        if ctx.getChildCount() == 4:
            return NewExpr(Id(ctx.IDEN().getText()), [])
        elif ctx.getChildCount() == 5:
            return NewExpr(Id(ctx.IDEN().getText()), self.visit(ctx.expr_list()))
        else:
            return self.visit(ctx.getChild(0))
    
    def visitExpr11(self, ctx: D96Parser.Expr11Context):
        if ctx.getChildCount() == 3:
            return self.visit(ctx.getChild(1))
        else:
            return self.visit(ctx.getChild(0))
    
    def visitOperands(self, ctx: D96Parser.OperandsContext):
        if ctx.IDEN():
            return ctx.IDEN().getText()
        elif ctx.literal():
            return self.visit(ctx.getChild(0))
        elif ctx.SELF():
            return SelfLiteral()
        else:
            return NullLiteral()
    
    def visitLiteral(self, ctx: D96Parser.LiteralContext):
        if ctx.INTEGER_LITERAL():
            return IntLiteral(int(ctx.INTEGER_LITERAL().getText()))
        elif ctx.FLOAT_LITERAL():
            return FloatLiteral(float(ctx.FLOAT_LITERAL().getText()))
        elif ctx.BOOLEAN_LITERAL():
            return BooleanLiteral(bool(ctx.BOOLEAN_LITERAL().getText()))
        elif ctx.STRING_LITERAL():
            return StringLiteral(ctx.STRING_LITERAL().getText())
        return self.visit(ctx.getChild(0))
    
    def visitArray(self, ctx: D96Parser.ArrayContext):
        return self.visit(ctx.getChild(0))
    
    def visitMuldi_arr(self, ctx: D96Parser.Muldi_arrContext):
        return ArrayLiteral(self.visit(ctx.array_list()))
    
    def visitArray_list(self, ctx: D96Parser.Array_listContext):
        if ctx.getChildCount() == 3:
            return [self.visit(ctx.getChild(0))] + self.visit(ctx.getChild(2))
        return [self.visit(ctx.getChild(0))]
    
    def visitIndx_arr(self, ctx: D96Parser.Indx_arrContext):
        return ArrayLiteral(self.visit(ctx.expr_list()))

    def visitArray_type(self, ctx: D96Parser.Array_typeContext):
        return ArrayType(IntLiteral(int(ctx.INTEGER_LITERAL().getText())), self.visit(ctx.getChild(2)))
        
    

    
    

    # def visitProgram(self, ctx: D96Parser.ProgramContext):
    #     return Program([FuncDecl(Id("main"),
    #                              [],
    #                              self.visit(ctx.mptype()),
    #                              Block([], [self.visit(ctx.body())] if ctx.body() else []))])

    # def visitMptype(self, ctx: D96Parser.MptypeContext):
    #     if ctx.INTTYPE():
    #         return IntType()
    #     else:
    #         return VoidType()

    # def visitBody(self, ctx: D96Parser.BodyContext):
    #     return self.visit(ctx.funcall())

    # def visitFuncall(self, ctx: D96Parser.FuncallContext):
    #     return CallExpr(Id(ctx.ID().getText()), [self.visit(ctx.exp())] if ctx.exp() else [])

    # def visitExp(self, ctx: D96Parser.ExpContext):
    #     if (ctx.funcall()):
    #         return self.visit(ctx.funcall())
    #     else:
    #         return IntLiteral(int(ctx.INTLIT().getText()))
