from D95Visitor import D95Visitor
from D95Parser import D95Parser
from AST import *

class ASTGeneration(D95Visitor):

    # Visit a parse tree produced by D95Parser#program.
    def visitProgram(self, ctx: D95Parser.ProgramContext):
        constdecls = ctx.constdecl()
        non_constdecls = ctx.non_constdecl()
        const = []
        nonconst = []
        for constdecl in constdecls:
            const += [self.visit(constdecl)]
        for non_constdecl in non_constdecls:
            nonconst += [self.visit(non_constdecl)]
        return Program(const, nonconst)


    # Visit a parse tree produced by D95Parser#non_constdecl.
    def visitNon_constdecl(self, ctx:D95Parser.Non_constdeclContext):
        if ctx.stmt_assign():
            return self.visit(ctx.stmt_assign())
        else: return self.visit(ctx.funcdecl())


    # Visit a parse tree produced by D95Parser#list_stmt.
    def visitList_stmt(self, ctx:D95Parser.List_stmtContext):
        if ctx.stmt():
            return [self.visit(ctx.stmt())] + self.visit(ctx.list_stmt())
        else: return []


    # Visit a parse tree produced by D95Parser#stmt.
    def visitStmt(self, ctx:D95Parser.StmtContext):
        if ctx.stmt_if():
            return self.visit(ctx.stmt_if())
        elif ctx.stmt_assign():
            return self.visit(ctx.stmt_assign())
        elif ctx.stmt_foreach():
            return self.visit(ctx.stmt_foreach())
        elif ctx.stmt_while():
            return self.visit(ctx.stmt_while())
        elif ctx.stmt_break():
            return self.visit(ctx.stmt_break())
        elif ctx.stmt_continue():
            return self.visit(ctx.stmt_continue())
        elif ctx.stmt_call():
            return self.visit(ctx.stmt_call())
        else: return self.visit(ctx.stmt_return())


    # Visit a parse tree produced by D95Parser#funcdecl.
    def visitFuncdecl(self, ctx:D95Parser.FuncdeclContext):
        name = Id(ctx.ID_FUNC().getText())
        param = self.visit(ctx.decl_param())
        body = self.visit(ctx.list_stmt())
        return FuncDecl(name, param, body)


    # Visit a parse tree produced by D95Parser#decl_param. return [ParamDecl]
    def visitDecl_param(self, ctx:D95Parser.Decl_paramContext):
        if ctx.decl_param():
            return [ParamDecl(Id(ctx.ID_VARPAR().getText()))] + self.visit(ctx.decl_param())
        elif ctx.ID_VARPAR():
            return [ParamDecl(Id(ctx.ID_VARPAR().getText()))]
        else: return []


    # Visit a parse tree produced by D95Parser#constdecl.
    def visitConstdecl(self, ctx:D95Parser.ConstdeclContext):
        id = Id(ctx.ID_CONST().getText())
        value = self.visit(ctx.expr())
        return ConstDecl(id, value)


    # Visit a parse tree produced by D95Parser#stmt_assign.
    def visitStmt_assign(self, ctx:D95Parser.Stmt_assignContext):
        lhs = self.visit(ctx.lhs())
        rhs = self.visit(ctx.expr())
        return Assign(lhs, rhs)


    # Visit a parse tree produced by D95Parser#lhs.
    def visitLhs(self, ctx:D95Parser.LhsContext):
        if ctx.ID_VARPAR():
            return Id(ctx.ID_VARPAR().getText())
        else: return self.visit(ctx.expr_8())


    # Visit a parse tree produced by D95Parser#stmt_if.
    def visitStmt_if(self, ctx:D95Parser.Stmt_ifContext):
        if_expr = self.visit(ctx.expr())
        if_listStmt = self.visit(ctx.list_stmt())
        ifthenStmt = [(if_expr,if_listStmt)] + self.visit(ctx.stmt_elseif())
        elseStmt = self.visit(ctx.stmt_else())
        return If(ifthenStmt, elseStmt)


    # Visit a parse tree produced by D95Parser#stmt_elseif.
    def visitStmt_elseif(self, ctx:D95Parser.Stmt_elseifContext):
        if ctx.stmt_elseif():
            expr = self.visit(ctx.expr())
            listStmt = self.visit(ctx.list_stmt())
            return [(expr, listStmt)] + self.visit(ctx.stmt_elseif())
        else: return []


    # Visit a parse tree produced by D95Parser#stmt_else.
    def visitStmt_else(self, ctx:D95Parser.Stmt_elseContext):
        if ctx.list_stmt():
            return self.visit(ctx.list_stmt())
        else: return []


    # Visit a parse tree produced by D95Parser#stmt_foreach.-- NOT COMPLETE
    def visitStmt_foreach(self, ctx:D95Parser.Stmt_foreachContext):
        if ctx.ID_VARPAR():
            arr = Id(ctx.ID_VARPAR().getText())
        elif ctx.ID_CONST():
            arr = Id(ctx.ID_CONST().getText())
        else:
            arr = self.visit(ctx.array())
        key = self.visit(ctx.key_for())
        value = self.visit(ctx.value_for())
        body = self.visit(ctx.list_stmt())
        return ForEach(arr, key, value, body)


    # Visit a parse tree produced by D95Parser#key_for.
    def visitKey_for(self, ctx: D95Parser.Key_forContext):
        if ctx.ID_VARPAR():
            return Id(ctx.ID_VARPAR().getText())
        else:
            return Id(ctx.ID_CONST().getText())


    # Visit a parse tree produced by D95Parser#value_for.
    def visitValue_for(self, ctx: D95Parser.Value_forContext):
        if ctx.ID_VARPAR():
            return Id(ctx.ID_VARPAR().getText())
        else:
            return Id(ctx.ID_CONST().getText())


    # Visit a parse tree produced by D95Parser#stmt_while.
    def visitStmt_while(self, ctx: D95Parser.Stmt_whileContext):
        cond = self.visit(ctx.expr())
        body = self.visit(ctx.list_stmt())
        return While(cond, body)


    # Visit a parse tree produced by D95Parser#stmt_break.
    def visitStmt_break(self, ctx:D95Parser.Stmt_breakContext):
        return Break()


    # Visit  a parse tree produced by D95Parser#stmt_continue.
    def visitStmt_continue(self, ctx:D95Parser.Stmt_continueContext):
        return Continue()


    # Visit a parse tree produced by D95Parser#stmt_call.
    def visitStmt_call(self, ctx:D95Parser.Stmt_callContext):
        return self.visit(ctx.func_call())


    # Visit a parse tree produced by D95Parser#stmt_return.
    def visitStmt_return(self, ctx:D95Parser.Stmt_returnContext):
        if ctx.expr():
            return Return(self.visit(ctx.expr()))
        else: return Return(None)


    # Visit a parse tree produced by D95Parser#expr.
    def visitExpr(self, ctx:D95Parser.ExprContext):
        if ctx.expr_1():
            return self.visit(ctx.expr_1())
        else:
            return self.visit(ctx.array())


    # Visit a parse tree produced by D95Parser#expr.
    def visitExpr_1(self, ctx: D95Parser.ExprContext):
        operand = ctx.expr_2()
        if ctx.op_string():
            left = self.visit(operand[0])
            right = self.visit(operand[1])
            op = self.visit(ctx.op_string()).getText()
            return BinExp(op, left, right)
        else:
            return self.visit(operand[0])


    # Visit a parse tree produced by D95Parser#expr_2.
    def visitExpr_2(self, ctx: D95Parser.Expr_2Context):
        operand = ctx.expr_3()
        if ctx.op_relation():
            left = self.visit(operand[0])
            right = self.visit(operand[1])
            op = self.visit(ctx.op_relation()).getText()
            return BinExp(op, left, right)
        else:
            return self.visit(operand[0])


    # Visit a parse tree produced by D95Parser#expr_3.
    def visitExpr_3(self, ctx: D95Parser.Expr_3Context):
        if ctx.op_andor():
            left = self.visit(ctx.expr_3())
            right = self.visit(ctx.expr_4())
            op = self.visit(ctx.op_andor()).getText()
            return BinExp(op, left, right)
        else:
            return self.visit(ctx.expr_4())


    # Visit a parse tree produced by D95Parser#expr_4.
    def visitExpr_4(self, ctx: D95Parser.Expr_4Context):
        if ctx.op_adding():
            left = self.visit(ctx.expr_4())
            right = self.visit(ctx.expr_5())
            op = self.visit(ctx.op_adding()).getText()
            return BinExp(op, left, right)
        else:
            return self.visit(ctx.expr_5())


    # Visit a parse tree produced by D95Parser#expr_5.
    def visitExpr_5(self, ctx: D95Parser.Expr_5Context):
        if ctx.op_multiplyng():
            left = self.visit(ctx.expr_5())
            right = self.visit(ctx.expr_6())
            op = self.visit(ctx.op_multiplyng()).getText()
            return BinExp(op, left, right)
        else:
            return self.visit(ctx.expr_6())


    # Visit a parse tree produced by D95Parser#expr_6.
    def visitExpr_6(self, ctx: D95Parser.Expr_6Context):
        if ctx.expr_6():
            op = ctx.NOT().getText()
            exp = self.visit(ctx.expr_6())
            return UnExp(op, exp)
        else:
            return self.visit(ctx.expr_7())


    # Visit a parse tree produced by D95Parser#expr_7.
    def visitExpr_7(self, ctx: D95Parser.Expr_7Context):
        if ctx.expr_7():
            op = ctx.SUB().getText()
            exp = self.visit(ctx.expr_7())
            return UnExp(op, exp)
        else:
            return self.visit(ctx.expr_8())


    # Visit a parse tree produced by D95Parser#expr_8.
    def visitExpr_8(self, ctx: D95Parser.Expr_8Context):
        if ctx.operand_index():
            id = self.visit(ctx.operand_index())
            idx = self.visit(ctx.index_operator())
            return ArrayAccess(id,idx)
        else:
            return self.visit(ctx.operand())


    # Visit a parse tree produced by D95Parser#operand_index.
    def visitOperand_index(self, ctx:D95Parser.Operand_indexContext):
        if ctx.ID_VARPAR():
            return Id(ctx.ID_VARPAR().getText())
        else:
            return Id(ctx.ID_CONST().getText())


    # Visit a parse tree produced by D95Parser#index_operator.
    def visitIndex_operator(self, ctx:D95Parser.Index_operatorContext):
        if ctx.index_operator():
            return [self.visit(ctx.expr_1())] + self.visit(ctx.index_operator())
        else:
            return [self.visit(ctx.expr_1())]


    # Visit a parse tree produced by D95Parser#operand.
    def visitOperand(self, ctx: D95Parser.OperandContext):
        if ctx.literal():
            return self.visit(ctx.literal())
        elif ctx.ID_VARPAR():
            return Id(ctx.ID_VARPAR().getText())
        elif ctx.ID_CONST():
            return Id(ctx.ID_CONST().getText())
        elif ctx.func_call():
            return self.visit(ctx.func_call())
        else: return self.visit(ctx.expr())


    # Visit a parse tree produced by D95Parser#func_call.
    def visitFunc_call(self, ctx:D95Parser.Func_callContext):
        if ctx.ID_FUNC():
            id = Id(ctx.ID_FUNC().getText())
        else: id = Id(self.visit(ctx.type_coersion()).getText())
        param = self.visit(ctx.list_param())
        return Call(id, param)


    # Visit a parse tree produced by D95Parser#list_param.
    def visitList_param(self, ctx:D95Parser.List_paramContext):
        if ctx.list_param():
            return [self.visit(ctx.param())] + self.visit(ctx.list_param())
        elif ctx.param():
            return [self.visit(ctx.param())]
        else: return []


    # Visit a parse tree produced by D95Parser#param.
    def visitParam(self, ctx:D95Parser.ParamContext):
        if ctx.literal():
            return self.visit(ctx.literal())
        elif ctx.ID_VARPAR():
            return Id(ctx.ID_VARPAR().getText())
        else: return self.visit(ctx.expr())


    # Visit a parse tree produced by D95Parser#type_coersion.
    def visitType_coersion(self, ctx:D95Parser.Type_coersionContext):
        if ctx.STR2INT():
            return ctx.STR2INT()
        elif ctx.INT2STR():
            return ctx.INT2STR()
        elif ctx.STR2BOOL():
            return ctx.STR2BOOL()
        elif ctx.BOOL2STR():
            return ctx.BOOL2STR()
        elif ctx.STR2FLOAT():
            return ctx.STR2FLOAT()
        else: return ctx.FLOAT2STR()


    # Visit a parse tree produced by D95Parser#op_string.
    def visitOp_string(self, ctx:D95Parser.Op_stringContext):
        if ctx.STR_CAT():
            return ctx.STR_CAT()
        else: return ctx.STR_CMP()


    # Visit a parse tree produced by D95Parser#op_relation.
    def visitOp_relation(self, ctx:D95Parser.Op_relationContext):
        if ctx.EQUAL():
            return ctx.EQUAL()
        elif ctx.NOT_EQUAL():
            return ctx.NOT_EQUAL()
        elif ctx.LESS():
            return ctx.LESS()
        elif ctx.LESS_EQUAL():
            return ctx.LESS_EQUAL()
        elif ctx.GREATER():
            return ctx.GREATER()
        else: return ctx.GREATER_EQUAL()


    # Visit a parse tree produced by D95Parser#op_andor.
    def visitOp_andor(self, ctx:D95Parser.Op_andorContext):
        if ctx.AND():
            return ctx.AND()
        else: return ctx.OR()


    # Visit a parse tree produced by D95Parser#op_adding.
    def visitOp_adding(self, ctx:D95Parser.Op_addingContext):
        if ctx.ADD():
            return ctx.ADD()
        else: return  ctx.SUB()


    # Visit a parse tree produced by D95Parser#op_multiplyng.
    def visitOp_multiplyng(self, ctx:D95Parser.Op_multiplyngContext):
        if ctx.MUL():
            return ctx.MUL()
        elif ctx.DIV():
            return ctx.DIV()
        else:
            return ctx.MOD()


    # Visit a parse tree produced by D95Parser#listARRAY.
    def visitListARRAY(self, ctx:D95Parser.ListARRAYContext):
        if ctx.listARRAY():
            return [self.visit(ctx.array())] + self.visit(ctx.listARRAY())
        else: return [self.visit(ctx.array())]


    # Visit a parse tree produced by D95Parser#array.
    def visitArray(self, ctx:D95Parser.ArrayContext):
        if ctx.i_array():
            return self.visit(ctx.i_array())
        elif ctx.a_array():
            return self.visit(ctx.a_array())
        else:
            return self.visit(ctx.m_array())


    # Visit a parse tree produced by D95Parser#i_array.
    def visitI_array(self, ctx:D95Parser.I_arrayContext):
        return ArrayLit(self.visit(ctx.listLIT()))


    # Visit a parse tree produced by D95Parser#a_array.
    def visitA_array(self, ctx:D95Parser.A_arrayContext):
        return ArrayLit(self.visit(ctx.listKV()))


    # Visit a parse tree produced by D95Parser#m_array.
    def visitM_array(self, ctx:D95Parser.M_arrayContext):
        return ArrayLit(self.visit(ctx.listARRAY()))


    # Visit a parse tree produced by D95Parser#listKV.
    def visitListKV(self, ctx:D95Parser.ListKVContext):
        if ctx.listKV():
            return [self.visit(ctx.keyValue())] + self.visit(ctx.listKV())
        else: return [self.visit(ctx.keyValue())]


    # Visit a parse tree produced by D95Parser#keyValue.
    def visitKeyValue(self, ctx:D95Parser.KeyValueContext):
        key = self.visit(ctx.key())
        value = self.visit(ctx.expr())
        return AssocExp(key, value)


    # Visit a parse tree produced by D95Parser#key.
    def visitKey(self, ctx:D95Parser.KeyContext):
        if ctx.integer():
            return self.visit(ctx.integer())
        elif ctx.STRING():
            return StringLit(ctx.STRING().getText())
        else: return Id(ctx.ID_VARPAR().getText())


    # Visit a parse tree produced by D95Parser#listLIT.
    def visitListLIT(self, ctx:D95Parser.ListLITContext):
        if ctx.listLIT():
            return [self.visit(ctx.literal())] + self.visit(ctx.listLIT())
        elif ctx.literal():
            return [self.visit(ctx.literal())]
        else: return []


    # Visit a parse tree produced by D95Parser#literal.
    def visitLiteral(self, ctx:D95Parser.LiteralContext):
        if ctx.FLOAT():
            return FloatLit(float(ctx.FLOAT().getText()))
        elif ctx.boolean():
            return self.visit(ctx.boolean())
        elif ctx.STRING():
            return StringLit(ctx.STRING().getText())
        else: return self.visit(ctx.integer())


    # Visit a parse tree produced by D95Parser#integer.
    def visitInteger(self, ctx:D95Parser.IntegerContext):
        if ctx.DEC():
            return IntLit(int(ctx.DEC().getText()))
        elif ctx.OCT():
            return IntLit(int(ctx.OCT().getText()))
        elif ctx.HEX():
            return IntLit(int(ctx.HEX().getText()))
        else: return IntLit(int(ctx.BIN().getText()))


    # Visit a parse tree produced by D95Parser#boolean.
    def visitBoolean(self, ctx:D95Parser.BooleanContext):
        if ctx.TRUE():
            return BoolLit(True)
        else: return BoolLit(False)




