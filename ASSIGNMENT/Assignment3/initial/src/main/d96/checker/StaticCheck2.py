
"""
 * @author nhphung
"""
from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *


class MType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype

    def __str__(self):
        return ""


class Symbol:
    def __init__(self, name, mtype, value=None):
        self.name = name
        self.mtype = mtype
        self.value = value

    def __str__(self):
        return "Symbol(" + str(self.name) + "," + str(self.mtype)


class StaticChecker(BaseVisitor, Utils):

    global_envi = [
        # Symbol("getInt", MType([], IntType())),
        # Symbol("putIntLn", MType([IntType()], VoidType()))
    ]
    # global_envi = []

    def __init__(self, ast):
        self.ast = ast

    def check(self):
        return self.visit(self.ast, StaticChecker.global_envi)

    def printSym(self, lis):
        for x in lis:
            print(x)
        print("end")

    def convertToSymbol(self, decl, returnType=None):
        # Function convert declare to Symbol
        if isinstance(decl, AttributeDecl):
            if type(decl.decl) is ConstDecl:
                return Symbol(decl.decl.constant.name, decl.decl.constType)
            else:
                return Symbol(decl.decl.variable.name, decl.decl.varType)
        elif type(decl) is ConstDecl:
            return Symbol(decl.constant.name, decl.constType)
        elif type(decl) is VarDecl:
            return Symbol(decl.variable.name, decl.varType)
        elif isinstance(decl, MethodDecl):
            return Symbol(decl.name.name, MType([x.varType for x in decl.param], returnType))

    def toListSym(self, listDecl, listSym, c=None):
        for x in listDecl:
            returnType = None
            if isinstance(x, MethodDecl):
                returnType = self.visit(x.body, listSym)
            sym = self.convertToSymbol(x, returnType)
            res = self.lookup(sym.name, listSym, lambda x: x.name)
            if res is None:
                listSym.append(sym)
            elif type(sym.mtype) is MType:
                raise Redeclared(Method(), sym.name)
            else:
                if type(x) is AttributeDecl:
                    raise Redeclared(Attribute(), sym.name)

    def visitProgram(self, ast, global_envi):
        global_envi = global_envi[:]
        for x in ast.decl:
            global_envi += [self.visit(x, global_envi)]

        return []

    def visitClassDecl(self, ast, global_envi):
        if ast.classname.name in global_envi:
            raise Redeclared(Class(), ast.classname.name)

        local_evi = []
        # self.toListSym(ast.memlist, local_evi)

        for x in ast.memlist:
            local_evi += [self.visit(x, local_evi)]
            print(local_evi)

        return ast.classname.name

    def visitAttributeDecl(self, ast, local_envi):
        sym = self.convertToSymbol(ast)
        res = self.lookup(sym.name, local_envi, lambda x: x.name)

        if res is None:
            return sym
        else:
            raise Redeclared(Attribute(), sym.name)

        # return self.visit(ast.decl, local_envi)

    def visitConstDecl(self, ast, local_envi):
        return
        # is_redeclare = self.lookup(ast.constant, local_envi, lambda x: x.name)
        # if is_redeclare:
        #     raise Redeclared(Constant(), ast.constant.name)

        # return Symbol(ast.constant, MType(None, ast.constType))

    def visitMethodDecl(self, ast, global_envi):
        sym = self.convertToSymbol(ast)
        res = self.lookup(sym.name, global_envi,
                          lambda x: x.name if type(x.mtype) is MType else None)

        # check param of method
        list_param = []
        for x in ast.param:
            list_param.extend(self.visit(x, (list_param, 'para')))

        # check body of method
        self.visit(ast.body, (global_envi, list_param))

        if res is not None:
            raise Redeclared(Method(), sym.name)

        return sym

    def visitVarDecl(self, ast, c):
        if c[1] == 'para':
            kind = c[1]
            local_envi = c[0]
        else:
            kind = None
            global_envi = c[0]
            local_envi = c[1]

        sym = self.convertToSymbol(ast)
        # print(local_envi)
        res = self.lookup(sym.name, local_envi, lambda x: x.name)
        if res is not None:
            if kind == 'para':
                raise Redeclared(Parameter(), sym.name)
            else:
                raise Redeclared(Variable(), sym.name)
        return [sym]
        # is_redeclare = self.lookup(ast.variable, local_envi, lambda x: x.name)
        # if is_redeclare:
        #     raise Redeclared(Variable(), ast.variable.name)

        # return Symbol(ast.variable, MType(None, ast.varType))
        # is_redeclare = self.lookup(
        #     ast.name, local_envi, lambda x: x.name)

        # if is_redeclare:
        #     raise Redeclared(Method(), ast.name.name)

        # return Symbol(ast.name, MType([x for x in ast.param], ast.kind))

    def visitBlock(self, ast, c):
        global_envi = c[0]
        local_envi = c[1]
        # check redecl
        for x in ast.inst:
            print(x)
            local_envi.extend(self.visit(x, (global_envi, local_envi)))

    def visitAssign(self, ast, c):

        return self.visit(ast.lhs, c)

    def visitId(self, ast, c):
        # all decl to check declared or not
        list_decl = c[0] + c[1]
        res = self.lookup(ast.name, list_decl, lambda x: x.name if type(
            x.mtype) is not MType else None)

        if res is None:
            raise Undeclared(Identifier(), ast.name)
        return []

    def visitCallExpr(self, ast, c):
        pass

        # def visitFuncDecl(self, ast, c):
        #     return list(map(lambda x: self.visit(x, (c, True)), ast.body.stmt))

        # def visitCallExpr(self, ast, c):
        #     at = [self.visit(x, (c[0], False)) for x in ast.param]

        #     res = self.lookup(ast.method.name, c[0], lambda x: x.name)
        #     if res is None or not type(res.mtype) is MType:
        #         raise Undeclared(Function(), ast.method.name)
        #     elif len(res.mtype.partype) != len(at):
        #         if c[1]:
        #             raise TypeMismatchInStatement(ast)
        #         else:
        #             raise TypeMismatchInExpression(ast)
        #     else:
        #         return res.mtype.rettype

        # def visitIntLiteral(self, ast, c):
        #     return IntType()
