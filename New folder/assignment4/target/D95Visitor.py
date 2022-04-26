# Generated from main/d95/parser/D95.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .D95Parser import D95Parser
else:
    from D95Parser import D95Parser

# This class defines a complete generic visitor for a parse tree produced by D95Parser.

class D95Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by D95Parser#program.
    def visitProgram(self, ctx:D95Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#non_constdecl.
    def visitNon_constdecl(self, ctx:D95Parser.Non_constdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#list_stmt.
    def visitList_stmt(self, ctx:D95Parser.List_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#stmt.
    def visitStmt(self, ctx:D95Parser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#funcdecl.
    def visitFuncdecl(self, ctx:D95Parser.FuncdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#decl_param.
    def visitDecl_param(self, ctx:D95Parser.Decl_paramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#constdecl.
    def visitConstdecl(self, ctx:D95Parser.ConstdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#stmt_assign.
    def visitStmt_assign(self, ctx:D95Parser.Stmt_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#lhs.
    def visitLhs(self, ctx:D95Parser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#stmt_if.
    def visitStmt_if(self, ctx:D95Parser.Stmt_ifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#stmt_elseif.
    def visitStmt_elseif(self, ctx:D95Parser.Stmt_elseifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#stmt_else.
    def visitStmt_else(self, ctx:D95Parser.Stmt_elseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#stmt_foreach.
    def visitStmt_foreach(self, ctx:D95Parser.Stmt_foreachContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#key_for.
    def visitKey_for(self, ctx:D95Parser.Key_forContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#value_for.
    def visitValue_for(self, ctx:D95Parser.Value_forContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#stmt_while.
    def visitStmt_while(self, ctx:D95Parser.Stmt_whileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#stmt_break.
    def visitStmt_break(self, ctx:D95Parser.Stmt_breakContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#stmt_continue.
    def visitStmt_continue(self, ctx:D95Parser.Stmt_continueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#stmt_call.
    def visitStmt_call(self, ctx:D95Parser.Stmt_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#stmt_return.
    def visitStmt_return(self, ctx:D95Parser.Stmt_returnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#expr.
    def visitExpr(self, ctx:D95Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#expr_1.
    def visitExpr_1(self, ctx:D95Parser.Expr_1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#expr_2.
    def visitExpr_2(self, ctx:D95Parser.Expr_2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#expr_3.
    def visitExpr_3(self, ctx:D95Parser.Expr_3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#expr_4.
    def visitExpr_4(self, ctx:D95Parser.Expr_4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#expr_5.
    def visitExpr_5(self, ctx:D95Parser.Expr_5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#expr_6.
    def visitExpr_6(self, ctx:D95Parser.Expr_6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#expr_7.
    def visitExpr_7(self, ctx:D95Parser.Expr_7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#expr_8.
    def visitExpr_8(self, ctx:D95Parser.Expr_8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#operand_index.
    def visitOperand_index(self, ctx:D95Parser.Operand_indexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#index_operator.
    def visitIndex_operator(self, ctx:D95Parser.Index_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#operand.
    def visitOperand(self, ctx:D95Parser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#func_call.
    def visitFunc_call(self, ctx:D95Parser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#list_param.
    def visitList_param(self, ctx:D95Parser.List_paramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#param.
    def visitParam(self, ctx:D95Parser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#type_coersion.
    def visitType_coersion(self, ctx:D95Parser.Type_coersionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#op_string.
    def visitOp_string(self, ctx:D95Parser.Op_stringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#op_relation.
    def visitOp_relation(self, ctx:D95Parser.Op_relationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#op_andor.
    def visitOp_andor(self, ctx:D95Parser.Op_andorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#op_adding.
    def visitOp_adding(self, ctx:D95Parser.Op_addingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#op_multiplyng.
    def visitOp_multiplyng(self, ctx:D95Parser.Op_multiplyngContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#listARRAY.
    def visitListARRAY(self, ctx:D95Parser.ListARRAYContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#array.
    def visitArray(self, ctx:D95Parser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#i_array.
    def visitI_array(self, ctx:D95Parser.I_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#a_array.
    def visitA_array(self, ctx:D95Parser.A_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#m_array.
    def visitM_array(self, ctx:D95Parser.M_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#listKV.
    def visitListKV(self, ctx:D95Parser.ListKVContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#keyValue.
    def visitKeyValue(self, ctx:D95Parser.KeyValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#key.
    def visitKey(self, ctx:D95Parser.KeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#listLIT.
    def visitListLIT(self, ctx:D95Parser.ListLITContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#literal.
    def visitLiteral(self, ctx:D95Parser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#integer.
    def visitInteger(self, ctx:D95Parser.IntegerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#boolean.
    def visitBoolean(self, ctx:D95Parser.BooleanContext):
        return self.visitChildren(ctx)



del D95Parser