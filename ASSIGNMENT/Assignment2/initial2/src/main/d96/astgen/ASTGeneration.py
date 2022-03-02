from functools import reduce
from D96Visitor import D96Visitor
from D96Parser import D96Parser
from AST import *

class ASTGeneration(D96Visitor):
    className = None
    def visitProgram(self, ctx: D96Parser.ProgramContext):
        return Program([self.visit(x) for x in ctx.class_decl()])
    
    def visitClass_decl(self, ctx: D96Parser.Class_declContext):
        mem_decl_list = []
        global className 
        className = ctx.IDEN(0).getText()
        if ctx.mem_decl():
            [mem_decl_list.extend(self.visit(x)) for x in ctx.mem_decl()]
            if ctx.COL():
                return ClassDecl(Id(ctx.IDEN(0).getText()), mem_decl_list, Id(ctx.IDEN(1).getText()))
            return ClassDecl(Id(ctx.IDEN(0).getText()), mem_decl_list)
        if ctx.COL():
            return ClassDecl(Id(ctx.IDEN(0).getText()), [], Id(ctx.IDEN(1).getText()))
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
            if ctx.IDEN():
                return Id(ctx.IDEN().getText())
            return Id(ctx.DOL_IDEN().getText())

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
        elif ctx.IDEN():
            return ctx.IDEN().getText()
        else:
            return self.visit(ctx.getChild(0))
    
    def visitMethod_decl(self, ctx: D96Parser.Method_declContext):
        global className
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.getChild(0))]
        else:
            iden_dol = self.visit(ctx.iden_dol())
            if(className == 'Program' and iden_dol == Id("main") and not ctx.params_list()):
                 kind = lambda x: Static()
            else:
                 kind = lambda x: Static() if x.name[0] == '$' else Instance()
            if ctx.params_list():
                return [MethodDecl(kind(iden_dol), iden_dol, self.visit(ctx.params_list()), self.visit(ctx.block_stmt()))]
            return [MethodDecl(kind(iden_dol), iden_dol, [], self.visit(ctx.block_stmt()))]
    
    def visitConstr_decl(self, ctx: D96Parser.Constr_declContext):
        if ctx.params_list():
            return MethodDecl(Instance(), Id(ctx.CONSTRUCTOR().getText()),self.visit(ctx.params_list()) , self.visit(ctx.block_stmt()))
        return MethodDecl(Instance(), Id(ctx.CONSTRUCTOR().getText()), [], self.visit(ctx.block_stmt()))

    def visitDestr_decl(self, ctx: D96Parser.Destr_declContext):
        return MethodDecl(Instance(), Id(ctx.DESTRUCTOR().getText()), [], self.visit(ctx.block_stmt()))

    def visitParams_list(self, ctx: D96Parser.Params_listContext):
        return  reduce(lambda x, y: x + self.visit(y), ctx.param_decl(), [])

    def visitParam_decl(self, ctx: D96Parser.Param_declContext):
        return [VarDecl(id, varType) for(id, varType) in self.visit(ctx.id_list_type())]

    def visitBlock_stmt(self, ctx: D96Parser.Block_stmtContext):
        if ctx.block_item():
            listItem = reduce(lambda x, y : x + self.visit(y) if isinstance(self.visit(y), list) 
                                else x + [self.visit(y)], ctx.block_item(), [])
            return Block(listItem)
        return Block([]);
    
    def visitBlock_item(self, ctx: D96Parser.Block_itemContext):
        return self.visit(ctx.getChild(0))
    
    """                  Assign Statement                      """
    def visitAssign_stmt(self, ctx: D96Parser.Assign_stmtContext):
        return self.visit(ctx.assign_lhs())
    
    def visitAssign_lhs(self, ctx: D96Parser.Assign_lhsContext):
        return Assign(self.visit(ctx.lhs()), self.visit(ctx.expr()))

    def visitLhs(self, ctx: D96Parser.LhsContext):
        if ctx.IDEN():
            return Id(ctx.IDEN().getText())
        else:
            return self.visit(ctx.getChild(0))
    
    def visitArray_operator(self, ctx: D96Parser.Array_operatorContext):
        return ArrayCell(self.visit(ctx.expr8()), [self.visit(x) for x in ctx.expr()])
    
    def visitField_access(self, ctx: D96Parser.Field_accessContext):
        return FieldAccess(self.visit(ctx.expr()), Id(ctx.getChild(2).getText()))

    """                  If Statement                      """
    def visitIf_stmt(self, ctx: D96Parser.If_stmtContext):
        if ctx.else_stmt():
            return If(self.visit(ctx.expr()), self.visit(ctx.block_stmt()), self.visit(ctx.else_stmt()))
        else:
            return If(self.visit(ctx.expr()), self.visit(ctx.block_stmt()))

    # def visitIf_element(self, ctx: D96Parser.If_elementContext):
    #     return (self.visit(ctx.expr()), self.visit(ctx.block_stmt()))
    
    def visitElse_stmt(self, ctx: D96Parser.Else_stmtContext):
        if ctx.ELSEIF():
            if ctx.else_stmt():
               return If(self.visit(ctx.expr()), self.visit(ctx.block_stmt()), self.visit(ctx.else_stmt()))
            return If(self.visit(ctx.expr()), self.visit(ctx.block_stmt()))
        return self.visit(ctx.block_stmt())
    
    # def visitElif_element(self, ctx: D96Parser.Elif_elementContext):
    #     return (self.visit(ctx.expr()), self.visit(ctx.block_stmt()))
    
    # def visitElse_element(self, ctx: D96Parser.Else_elementContext):
    #     return self.visit(ctx.block_stmt())
 
    """                  Break Statement                      """
    def visitBreak_stmt(self, ctx: D96Parser.Break_stmtContext):
        return Break()
    """                  Continue Statement                      """
    def visitContinue_stmt(self, ctx: D96Parser.Continue_stmtContext):
        return Continue()
    
    def visitForin_stmt(self, ctx: D96Parser.Forin_stmtContext):
        if ctx.BY():
            return For(Id(ctx.IDEN().getText()), IntLiteral(int(ctx.INTEGER_LITERAL(0).getText())), IntLiteral(int(ctx.INTEGER_LITERAL(1).getText())), self.visit(ctx.block_stmt()), IntLiteral(int(ctx.INTEGER_LITERAL(2).getText())))
        else:
            return For(Id(ctx.IDEN().getText()), IntLiteral(int(ctx.INTEGER_LITERAL(0).getText())), IntLiteral(int(ctx.INTEGER_LITERAL(1).getText())), self.visit(ctx.block_stmt()), IntLiteral(1))

    def visitReturn_stmt(self, ctx: D96Parser.Return_stmtContext):
        if ctx.expr():
            return Return(self.visit(ctx.expr()))
        return Return()

    def visitMethod_invocation_stmt(self, ctx: D96Parser.Method_invocation_stmtContext):
        return self.visit(ctx.method_invocation())
    
    def visitMethod_invocation(self, ctx: D96Parser.Method_invocationContext):
        if ctx.expr_list():
            return CallStmt(self.visit(ctx.expr()), Id(ctx.getChild(2).getText()), self.visit(ctx.expr_list()))
        return CallStmt(self.visit(ctx.expr()), Id(ctx.getChild(2).getText()), [])
    "                                                         "
    def visitExpr(self, ctx: D96Parser.ExprContext):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.expr1(0)), self.visit(ctx.expr1(1)))
        return self.visit(ctx.expr1(0))
        
    def visitExpr1(self, ctx: D96Parser.Expr1Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.expr2(0)), self.visit(ctx.expr2(1)))
        return self.visit(ctx.expr2(0))
    
    def visitExpr2(self, ctx: D96Parser.Expr2Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.expr2()), self.visit(ctx.expr3()))
        else:
            return self.visit(ctx.expr3())
    
    def visitExpr3(self, ctx: D96Parser.Expr3Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.expr3()), self.visit(ctx.expr4()))
        else:
            return self.visit(ctx.expr4())
    
    def visitExpr4(self, ctx: D96Parser.Expr4Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.expr4()), self.visit(ctx.expr5()))
        else:
            return self.visit(ctx.expr5())

    def visitExpr5(self, ctx: D96Parser.Expr5Context):
        if ctx.getChildCount() == 2:
            return UnaryOp(ctx.getChild(0).getText(), self.visit(ctx.expr5()))
        else:
            return self.visit(ctx.expr6())

    def visitExpr6(self, ctx: D96Parser.Expr6Context):
        if ctx.getChildCount() == 2:
            return UnaryOp(ctx.getChild(0).getText(), self.visit(ctx.expr6()))
        else:
            return self.visit(ctx.expr7())
    
    def visitExpr7(self, ctx: D96Parser.Expr7Context):
        if ctx.expr():
            return ArrayCell(self.visit(ctx.expr8()), [self.visit(x) for x in ctx.expr()])
        return self.visit(ctx.expr8())

    def visitExpr8(self, ctx: D96Parser.Expr8Context):
        if ctx.expr_list():
            return CallExpr(self.visit(ctx.expr8()), Id(ctx.IDEN().getText()), self.visit(ctx.expr_list()))
            
        elif ctx.LB() and ctx.RB():
            return CallExpr(self.visit(ctx.expr8()), Id(ctx.IDEN().getText()), [])
        elif ctx.expr8():
           return FieldAccess(self.visit(ctx.expr8()), Id(ctx.IDEN().getText()))
        else:
            return self.visit(ctx.expr9())

    def visitExpr9(self, ctx: D96Parser.Expr9Context):
        if ctx.expr_list():
            return CallExpr(self.visit(ctx.expr9()), Id(ctx.DOL_IDEN().getText()), self.visit(ctx.expr_list()))

        elif ctx.LB() and ctx.RB():
            return CallExpr(self.visit(ctx.expr9()), Id(ctx.DOL_IDEN().getText()), [])
        elif ctx.expr9():
           return FieldAccess(self.visit(ctx.expr9()), Id(ctx.DOL_IDEN().getText()))
        else:
            return self.visit(ctx.expr10())
        
    def visitExpr10(self, ctx: D96Parser.Expr10Context):
        if ctx.expr_list():
            return NewExpr(Id(ctx.IDEN().getText()), self.visit(ctx.expr_list()))
        elif ctx.NEW():
            return NewExpr(Id(ctx.IDEN().getText()), [])
        return self.visit(ctx.expr11())
    
    def visitExpr11(self, ctx: D96Parser.Expr11Context):
        if ctx.getChildCount() == 3:
            return self.visit(ctx.expr())
        else:
            return self.visit(ctx.operands())
    
    def visitOperands(self, ctx: D96Parser.OperandsContext):
        if ctx.IDEN():
            return Id(ctx.IDEN().getText())
        elif ctx.literal():
            return self.visit(ctx.getChild(0))
        elif ctx.SELF():
            return SelfLiteral()
        else:
            return NullLiteral()
    def visitList_literal(self, ctx: D96Parser.List_literalContext):
        return [self.visit(x) for x in ctx.literal()]

    def visitLiteral(self, ctx: D96Parser.LiteralContext):
        if ctx.INTEGER_LITERAL():
            return IntLiteral(int(ctx.INTEGER_LITERAL().getText()))
        elif ctx.FLOAT_LITERAL():
            
            return FloatLiteral(float(ctx.FLOAT_LITERAL().getText()))
        elif ctx.BOOLEAN_LITERAL():
            return BooleanLiteral(ctx.BOOLEAN_LITERAL().getText() == 'True')
        elif ctx.STRING_LITERAL():
            return StringLiteral(ctx.STRING_LITERAL().getText())
        return self.visit(ctx.array())
    
    def visitArray(self, ctx: D96Parser.ArrayContext):
        return self.visit(ctx.getChild(0))
    
    def visitMuldi_arr(self, ctx: D96Parser.Muldi_arrContext):
        return ArrayLiteral(self.visit(ctx.array_list()))
    
    def visitArray_list(self, ctx: D96Parser.Array_listContext):
        return [self.visit(x)for x in ctx.indx_arr()]
    
    def visitIndx_arr(self, ctx: D96Parser.Indx_arrContext):
        return ArrayLiteral(self.visit(ctx.expr_list()))

    def visitArray_type(self, ctx: D96Parser.Array_typeContext):
        return ArrayType(ctx.INTEGER_LITERAL().getText(), self.visit(ctx.data_type()))
        
    

    
    