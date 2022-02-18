# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .D96Parser import D96Parser
else:
    from D96Parser import D96Parser

# This class defines a complete generic visitor for a parse tree produced by D96Parser.

class D96Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by D96Parser#program.
    def visitProgram(self, ctx:D96Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_decl.
    def visitClass_decl(self, ctx:D96Parser.Class_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#body_class.
    def visitBody_class(self, ctx:D96Parser.Body_classContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#body_class_main.
    def visitBody_class_main(self, ctx:D96Parser.Body_class_mainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#main_func.
    def visitMain_func(self, ctx:D96Parser.Main_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmt.
    def visitStmt(self, ctx:D96Parser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#att_decl.
    def visitAtt_decl(self, ctx:D96Parser.Att_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#para_list_nor.
    def visitPara_list_nor(self, ctx:D96Parser.Para_list_norContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#para_list_eq.
    def visitPara_list_eq(self, ctx:D96Parser.Para_list_eqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#rest_para.
    def visitRest_para(self, ctx:D96Parser.Rest_paraContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#para.
    def visitPara(self, ctx:D96Parser.ParaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#func_decl.
    def visitFunc_decl(self, ctx:D96Parser.Func_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#destr_decl.
    def visitDestr_decl(self, ctx:D96Parser.Destr_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#constr_decl.
    def visitConstr_decl(self, ctx:D96Parser.Constr_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#block_stmt.
    def visitBlock_stmt(self, ctx:D96Parser.Block_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#block_items.
    def visitBlock_items(self, ctx:D96Parser.Block_itemsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#assign_stmt.
    def visitAssign_stmt(self, ctx:D96Parser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#assign_lhs.
    def visitAssign_lhs(self, ctx:D96Parser.Assign_lhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#method_invo_stmt.
    def visitMethod_invo_stmt(self, ctx:D96Parser.Method_invo_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#params_list_can.
    def visitParams_list_can(self, ctx:D96Parser.Params_list_canContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#params_list.
    def visitParams_list(self, ctx:D96Parser.Params_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#ids_list_with_type.
    def visitIds_list_with_type(self, ctx:D96Parser.Ids_list_with_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#ids_list_with_arr.
    def visitIds_list_with_arr(self, ctx:D96Parser.Ids_list_with_arrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#ids_list.
    def visitIds_list(self, ctx:D96Parser.Ids_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#data_types.
    def visitData_types(self, ctx:D96Parser.Data_typesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#element_types.
    def visitElement_types(self, ctx:D96Parser.Element_typesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#if_stmt.
    def visitIf_stmt(self, ctx:D96Parser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#return_stmt.
    def visitReturn_stmt(self, ctx:D96Parser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#break_stmt.
    def visitBreak_stmt(self, ctx:D96Parser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#continue_stmt.
    def visitContinue_stmt(self, ctx:D96Parser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#forin_stmt.
    def visitForin_stmt(self, ctx:D96Parser.Forin_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr_stmt.
    def visitExpr_stmt(self, ctx:D96Parser.Expr_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr.
    def visitExpr(self, ctx:D96Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#atom.
    def visitAtom(self, ctx:D96Parser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#array_declare.
    def visitArray_declare(self, ctx:D96Parser.Array_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#array.
    def visitArray(self, ctx:D96Parser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#muldi_arr.
    def visitMuldi_arr(self, ctx:D96Parser.Muldi_arrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#indx_arr.
    def visitIndx_arr(self, ctx:D96Parser.Indx_arrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#arr_type.
    def visitArr_type(self, ctx:D96Parser.Arr_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#self_type.
    def visitSelf_type(self, ctx:D96Parser.Self_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_type.
    def visitClass_type(self, ctx:D96Parser.Class_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#member_acc.
    def visitMember_acc(self, ctx:D96Parser.Member_accContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#inst_attr_acc.
    def visitInst_attr_acc(self, ctx:D96Parser.Inst_attr_accContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stat_attr_acc.
    def visitStat_attr_acc(self, ctx:D96Parser.Stat_attr_accContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#inst_meth_invo.
    def visitInst_meth_invo(self, ctx:D96Parser.Inst_meth_invoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stat_meth_invo.
    def visitStat_meth_invo(self, ctx:D96Parser.Stat_meth_invoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#list_expr_method.
    def visitList_expr_method(self, ctx:D96Parser.List_expr_methodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#elem_expr_method.
    def visitElem_expr_method(self, ctx:D96Parser.Elem_expr_methodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#list_literal.
    def visitList_literal(self, ctx:D96Parser.List_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#literal.
    def visitLiteral(self, ctx:D96Parser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#number_literal.
    def visitNumber_literal(self, ctx:D96Parser.Number_literalContext):
        return self.visitChildren(ctx)



del D96Parser