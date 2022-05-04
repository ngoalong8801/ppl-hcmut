
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

        return "MType([" + ','.join(str(i) for i in self.partype) + "]" + ', ' + str(self.rettype) + ")"


class Symbol:
    def __init__(self, name, mtype, value=None):
        self.name = name
        self.mtype = mtype
        self.value = value

    def __str__(self):
        return "Symbol(" + str(self.name) + "," + str(self.mtype)+"," + str(self.value) + ' )'


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
                return Symbol(decl.decl.constant.name, decl.decl.constType, Constant())
            else:
                return Symbol(decl.decl.variable.name, decl.decl.varType, Variable())
        elif type(decl) is ConstDecl:
            return Symbol(decl.constant.name, decl.constType, Constant())
        elif type(decl) is VarDecl:
            if type(decl.varType) is Class:
                return Symbol(decl.variable.name, decl.varType, decl.varType.classname.name)
            return Symbol(decl.variable.name, decl.varType, Variable())

        elif isinstance(decl, MethodDecl):
            return Symbol(decl.name.name, MType([x.varType for x in decl.param], returnType))

    def checkClassDefined(self, list_class, name):
        res = self.lookup(name, list_class, lambda x: x.name)
        if res is not None:
            return True
        return False

    def checkAttClass(self, list_class, name, attName, kind, returnType=None):
        res = self.lookup(name, list_class, lambda x: x.name)
        if res is not None:
            for x in res.mtype:
                if x.name == attName:
                    return x
        return None

    def visitProgram(self, ast, global_envi):
        global_envi = global_envi[:]
        for x in ast.decl:
            global_envi += [self.visit(x, global_envi)]

        return []

    def visitClassDecl(self, ast, global_envi):
        res = self.lookup(ast.classname.name, global_envi, lambda x: x.name)

        if res is not None:
            raise Redeclared(Class(), ast.classname.name)

        local_evi = []
        # self.toListSym(ast.memlist, local_evi)

        for x in ast.memlist:
            local_evi += [self.visit(x, (global_envi, local_evi))]

        return Symbol(ast.classname.name, local_evi, Class())

    def visitAttributeDecl(self, ast, c):
        local_envi = c[1]
        sym = self.convertToSymbol(ast)
        res = self.lookup(sym.name, local_envi, lambda x: x.name)

        if res is None:
            self.visit(ast.decl, (c[0], c[1], [], []))
            return sym
        else:
            raise Redeclared(Attribute(), sym.name)

        # return self.visit(ast.decl, local_envi)

        # is_redeclare = self.lookup(ast.constant, local_envi, lambda x: x.name)
        # if is_redeclare:
        #     raise Redeclared(Constant(), ast.constant.name)

        # return Symbol(ast.constant, MType(None, ast.constType))

    def visitMethodDecl(self, ast, c):
        global_class = c[0]
        global_envi = c[1]
        is_in_loop = False

        res = self.lookup(ast.name.name, global_envi,
                          lambda x: x.name if type(x.mtype) is MType else None)

        # check param of method
        list_param = []
        for x in ast.param:
            list_param.extend(self.visit(x, (list_param, 'para')))

        # check body of method
        returnType = self.visit(
            ast.body, (global_class, global_envi, [], list_param, is_in_loop))

        if res is not None:
            raise Redeclared(Method(), ast.name.name)
        sym = self.convertToSymbol(ast, returnType)
        # print(returnType)
        # print(sym)
        return sym

    def visitVarDecl(self, ast, c):
        kind = global_class = global_envi = local_envi = None
        if c[1] == 'para':
            kind = c[1]
            block_scope = c[0]
        else:
            kind = None
            global_class = c[0]
            global_envi = c[1]
            local_envi = c[2]
            block_scope = c[3]

        sym = self.convertToSymbol(ast)

        # check declared variable
        res = self.lookup(sym.name,  block_scope,
                          lambda x: x.name if type(x.mtype) is not MType else None)

        if type(ast.varType) is ClassType:
            nameClass = self.visit(ast.varType, local_envi)
            checked = self.checkClassDefined(
                global_class, nameClass)
            if not checked:
                raise Undeclared(Class(), nameClass)

        if res is not None:
            if kind == 'para':
                raise Redeclared(Parameter(), sym.name)
            else:
                raise Redeclared(Variable(), sym.name)
        return [sym]

    def visitConstDecl(self, ast, c):
        global_class = c[0]
        global_envi = c[1]
        local_envi = c[2]
        block_scope = c[3]
        sym = self.convertToSymbol(ast)

        # check declared variable
        res = self.lookup(sym.name, block_scope,
                          lambda x: x.name if type(x.mtype) is not MType else None)

        if type(ast.constType) is ClassType:
            nameClass = self.visit(ast.constType, local_envi)
            checked = self.checkClassDefined(
                global_class, nameClass)
            if not checked:
                raise Undeclared(Class(), nameClass)

        if res is not None:
            raise Redeclared(Constant(), sym.name)

        # Check TypeMismatchInConstant
        if ast.value:
            typExpr = self.visit(ast.value, c)
            if type(typExpr) is not type(ast.constType):
                raise TypeMismatchInConstant(ast)
        else:
            raise IllegalConstantExpression(None)

        return [sym]

    def visitBlock(self, ast, c):
        global_class = c[0]
        global_envi = c[1]
        local_envi = c[2]
        block_scope = c[3]
        is_in_loop = c[4]
        returnType = None

        # check redecl
        for x in ast.inst:
            decl = self.visit(
                x, (global_class, global_envi, local_envi, block_scope, is_in_loop))
            if type(decl) is list:
                if type(decl[0]) is Symbol:
                    block_scope.extend(decl)
            elif type(x) is Return:

                # check break, continue

                if((returnType is not decl) and ((type(returnType) is FloatType)
                                                 or (type(decl) is FloatType))):
                    decl = FloatType()
                elif returnType is not decl and returnType is not None:
                    raise TypeMismatchInStatement(x)
                returnType = decl

        # return voidtype if not return any
        if returnType is None:
            returnType = VoidType()
        local_envi.extend(block_scope)
        return returnType

    def visitAssign(self, ast, c):

        lhs = self.visit(ast.lhs, c)
        typeExp = self.visit(ast.exp, c)

        # check assign constant for Iden
        if type(ast.lhs) is Id:
            list_decl = c[1] + c[2] + c[3]
            res = self.lookup(ast.lhs.name, list_decl, lambda x: x.name if type(
                x.mtype) is not MType else None)
            if res is not None:
                if type(res.value) is Constant:
                    raise CannotAssignToConstant(ast)
        elif type(ast.lhs) is FieldAccess:
            if type(lhs.value) is Constant:
                raise CannotAssignToConstant(ast)

        # check miss match

        return

    def visitFieldAccess(self, ast, c):
        global_class = c[0]
        global_envi = c[1]
        local_envi = c[2]
        block_scope = c[3]
        checked = None
        is_constant = False
        if type(ast.obj) is SelfLiteral:
            checked = self.lookup(ast.fieldname.name, global_envi, lambda x: x.name if type(
                x.mtype) is not MType else None)
        else:
            sym = self.lookup(ast.obj.name, local_envi +
                              block_scope, lambda x: x.name)
            if sym is not None:
                checked = self.checkAttClass(
                    global_class, sym.mtype.classname.name, ast.fieldname.name, Attribute())

        # For an attribute access E.id, E must be in class type.
        if not checked:
            raise Undeclared(Attribute(), ast.fieldname.name)

        if isinstance(checked.value, Constant):
            is_constant = True

        return checked

    def visitIf(self, ast, c):
        is_boolean = self.visit(ast.expr, c)
        then_stmt = self.visit(ast.thenStmt, c)

        if ast.elseStmt:
            elseStmt = self.visit(ast.elseStmt, c)

        if type(is_boolean) is not BoolType:
            raise TypeMismatchInStatement(ast)
        return

    def visitFor(self, ast, c):
        typeExpr1 = self.visit(ast.expr1, c)
        typeExpr2 = self.visit(ast.expr2, c)
        is_in_loop = True

        if not(isinstance(typeExpr1, IntType) and isinstance(typeExpr2, IntType)):
            raise TypeMismatchInStatement(ast)

        loop = self.visit(ast.loop, (c[0], c[1], c[2], c[3], is_in_loop))
        return

    def visitBinaryOp(self, ast, c):
        typeLeft = self.visit(ast.left, c)
        typeRight = self.visit(ast.right, c)

        # check Arithmetic operators
        if ast.op in ['-', '+', '*', '/']:
            if isinstance(typeLeft, BoolType) or isinstance(typeRight, BoolType):
                raise TypeMismatchInExpression(ast)
            elif isinstance(typeLeft, FloatType) or isinstance(typeRight, FloatType):
                return FloatType()
            return IntType()
        elif ast.op == '%':
            if not isinstance(typeLeft, IntType) or not isinstance(typeRight, IntType):
                raise TypeMismatchInExpression(ast)
            return IntType()

        # check  Boolean operators
        if ast.op in ['&&', '||']:
            if not(isinstance(typeLeft, BoolType) or isinstance(typeRight, BoolType)):
                raise TypeMismatchInExpression(ast)
            return BoolType()
        elif ast.op == '==.':
            if not(isinstance(typeLeft, StringType) or isinstance(typeRight, StringType)):
                raise TypeMismatchInExpression(ast)
            return BoolType()

        # check Relational operators
        if ast.op == '+.':
            if not(isinstance(typeLeft, StringType) or isinstance(typeRight, StringType)):
                raise TypeMismatchInExpression(ast)
            return StringType()

        # check Relational operators

        if ast.op in ['==', '!=']:
            if(not((isinstance(typeLeft, BoolType) or isinstance(typeLeft, IntType)) and (isinstance(typeRight, BoolType) or isinstance(typeRight, IntType)))):
                raise TypeMismatchInExpression(ast)
            return BoolType()
        elif ast.op in ['<', '>', '<=', '>=']:
            if(not((isinstance(typeLeft, FloatType) or isinstance(typeLeft, IntType)) and (isinstance(typeRight, FloatType) or isinstance(typeRight, IntType)))):
                raise TypeMismatchInExpression(ast)
            return BoolType()

        return None

    def visitUnaryOp(self, ast, c):
        typeBody = self.visit(ast.body, c)
        if ast.op == '-':
            if not(isinstance(typeBody, IntType) or isinstance(typeBody, FloatType)):
                raise TypeMismatchInExpression(ast)
        elif ast.op == '!':
            if not isinstance(typeBody, BoolType):
                raise TypeMismatchInExpression(ast)
        return typeBody

    def visitId(self, ast, c):
        # all decl to check declared or not
        list_decl = c[1] + c[2] + c[3]
        res = self.lookup(ast.name, list_decl, lambda x: x.name if type(
            x.mtype) is not MType else None)

        if res is None:
            raise Undeclared(Identifier(), ast.name)

        # if type(res.value) is Constant:
        #     raise CannotAssignToConstant(as)
        return res.mtype

    def visitArrayCell(self, ast, c):
        typeArr = self.visit(ast.arr, c)
        for x in ast.idx:
            typeIdx = self.visit(x, c)

            if type(typeIdx) is not IntType:
                raise TypeMismatchInExpression(ast)

        if type(typeArr) is not ArrayType:
            raise TypeMismatchInExpression(ast)

        return

    def visitIntLiteral(self, ast, c):
        return IntType()

    def visitFloatLiteral(self, ast, c):
        return FloatType()

    def visitBooleanLiteral(self, ast, c):
        return BoolType()

    def visitStringLiteral(self, ast, c):
        return StringType()

    def visitClassType(self, ast, c):
        return ast.classname.name

    def visitArrayType(self, ast, c):
        return

    def visitCallExpr(self, ast, c):
        global_class = c[0]
        global_envi = c[1]
        local_envi = c[2]
        block_scope = c[3]
        checked = None
        if type(ast.obj) is SelfLiteral:
            checked = self.lookup(ast.method.name, global_envi, lambda x: x.name if type(
                x.mtype) is MType else None)
        else:
            # Check method of class

            sym = self.lookup(ast.obj.name, local_envi +
                              block_scope, lambda x: x.name)
            if not sym:
                raise Undeclared(Class(), ast.obj.name)
            elif (sym and type(sym.mtype) is not ClassType):

                raise TypeMismatchInStatement(ast)
            else:
                checked = self.checkAttClass(
                    global_class, sym.mtype.classname.name, ast.method.name, Method())

        if not checked:
            raise Undeclared(Method(), ast.method.name)
        elif(type(checked.mtype.rettype) is VoidType):
            raise TypeMismatchInStatement(ast)

        return checked.mtype.rettype

    def visitCallStmt(self, ast, c):
        global_class = c[0]
        global_envi = c[1]
        local_envi = c[2]
        block_scope = c[3]
        checked = None
        if type(ast.obj) is SelfLiteral:
            checked = self.lookup(ast.method.name, global_envi, lambda x: x.name if type(
                x.mtype) is MType else None)
        else:
            # Check method of class

            sym = self.lookup(ast.obj.name, local_envi +
                              block_scope, lambda x: x.name)
            if not sym:
                raise Undeclared(Class(), ast.obj.name)
            elif (sym and type(sym.mtype) is not ClassType):

                raise TypeMismatchInStatement(ast)
            else:
                checked = self.checkAttClass(
                    global_class, sym.mtype.classname.name, ast.method.name, Method())

        if not checked:
            raise Undeclared(Method(), ast.method.name)
        elif(type(checked.mtype.rettype) is not VoidType):
            raise TypeMismatchInStatement(ast)

        return

    def visitReturn(self, ast, c):
        returnType = self.visit(ast.expr, c)
        if not returnType:
            return VoidType()
        return returnType

    def visitBreak(self, ast, c):
        is_in_loop = c[3]
        print(is_in_loop)
        if is_in_loop == False:
            raise MustInLoop(ast)

    def visitContinue(self, ast, c):
        is_in_loop = c[3]
        print(is_in_loop)
        if is_in_loop == False:
            raise MustInLoop(ast)

    def visitNewExpr(self, ast, c):
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
