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
        if ctx.func_decl():
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
    
    def visitData_type(self, ctx: D96Parser.Data_typeContext):
        if ctx.INT():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.STRING():
            return StringType()
        elif ctx.BOOLEAN():
            return BoolType()
    
    def visitExpr_list(self, ctx: D96Parser.Expr_listContext):
        return [self.visit(x) for x in ctx.expr()]
    
    def visitExpr(self, ctx: D96Parser.ExprContext):
        if ctx.getChildCount == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
        else: 
            return self.visit(ctx.getChild(0))
        
    def visitExpr1(self, ctx: D96Parser.Expr1Context):
        if ctx.getChildCount == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
        else: 
            return self.visit(ctx.getChild(0))
    
    def visitExpr2(self, ctx: D96Parser.Expr2Context):
        if ctx.getChildCount == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
        else:
            return self.visit(ctx.getChild(0))
    
    def visitExpr3(self, ctx: D96Parser.Expr3Context):
        if ctx.getChildCount == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
        else:
            return self.visit(ctx.getChild(0))
    
    def visitExpr4(self, ctx: D96Parser.Expr4Context):
        if ctx.getChildCount == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
        else:
            return self.visit(ctx.getChild(0))

    def visitExpr5(self, ctx: D96Parser.Expr5Context):
        if ctx.getChildCount == 2:
            return UnaryOp(ctx.getChild(0).getText(), self.visit(ctx.getChild(1)))
        else:
            return self.visit(ctx.getChild(0))

    def visitExpr6(self, ctx: D96Parser.Expr6Context):
        if ctx.getChildCount == 2:
            return UnaryOp(ctx.getChild(0).getText(), self.visit(ctx.getChild(1)))
        else:
            return self.visit(ctx.getChild(0))
    
    def visitExpr7(self, ctx: D96Parser.Expr7Context):
        if ctx.getChildCount == 2:
            return ArrayCell(self.visit(ctx.getChild(0)), self.visit(ctx.getChild(1)))
        else:
            return self.visit(ctx.getChild(0))
    
    def visitIndex_operators(self, ctx: D96Parser.Index_operatorsContext):
        if ctx.getChildCount == 4:
            return [self.visit(ctx.getChild(1))] + self.visit(ctx.getChild(3))
        else: 
            return [self.visit(ctx.getChild(1))]

    def visitExpr8(self, ctx: D96Parser.Expr8Context):
        if ctx.getChildCount == 3:
            return FieldAccess(self.visit(ctx.getChild(0)), Id(ctx.IDEN().getText()))
        elif ctx.getChildCount == 4:
            return CallExpr(self.visit(ctx.getChild(0)), Id(ctx.IDEN().getText()), [])
        elif ctx.getChildCount == 5:
            return CallExpr(self.visit(ctx.getChild(0)), Id(ctx.IDEN().getText()), self.visit(ctx.expr_list()))
        else:
            return self.visit(ctx.getChild(0))
        
    def visitExpr9(self, ctx: D96Parser.Expr9Context):
        if ctx.getChildCount == 3:
            return FieldAccess(self.visit(ctx.getChild(0)), Id(ctx.IDEN().getText()))
        elif ctx.getChildCount == 4:
            return CallExpr(self.visit(ctx.getChild(0)), Id(ctx.IDEN().getText()), [])
        elif ctx.getChildCount == 5:
            return CallExpr(self.visit(ctx.getChild(0)), Id(ctx.IDEN().getText()), self.visit(ctx.expr_list()))
        else:
            return self.visit(ctx.getChild(0))
        
    def visitExpr10(self, ctx: D96Parser.Expr10Context):
        if ctx.getChildCount == 4:
            return NewExpr(Id(ctx.IDEN().getText()), [])
        elif ctx.getChildCount == 5:
            return NewExpr(Id(ctx.IDEN().getText()), self.visit(ctx.expr_list()))
        else:
            return self.visit(ctx.getChild(0))
    
    def visitExpr11(self, ctx: D96Parser.Expr11Context):
        if ctx.getChildCount == 3:
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
