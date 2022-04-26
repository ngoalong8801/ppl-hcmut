from abc import ABC, abstractmethod, ABCMeta
from dataclasses import dataclass
from typing import List, Tuple
from AST import *
from StaticError import *
from functools import *
import collections

def compareType(a, b):
    if type(a) is not type(b):
        return False
    if type(a) is  type(()):
        if type(a[0]) is type(b[0]) and type(a[1]) is type(b[1]):
            return True
        else:
            return False
    if type(a) is type([]):
        if len(a) == 0 and len(b) == 0:
            return True
        if len(a) == 0 and len(b) != 0 or len(a) != 0 and len(b) == 0:
            return False
        return compareType(a[0], b[0])
    return True


def compareList(a, b):
    if len(a) == 0 and len(b) == 0:
        return True
    if len(a) != len(b):
        return False
    idx = 0;
    for _ in a:
        if compareType(a[idx], b[idx]) == False:
            return False
        idx += 1
    return True

def checkArrayAccess(arrayType, idx):
    if len(idx) == 0 and len(arrayType) != 0:
        return True
    if len(arrayType) == 0:
        if len(idx) > 1:
            return False
    if type(arrayType[0]) is IntType or type(arrayType[0]) is FloatType or type(arrayType[0]) is StringType or type(arrayType[0]) is BoolType:
        if len(idx) > 1:
            return False
        if type(idx[0]) is IntType:
            return True
        else:
            return False
    if type(arrayType[0]) is type(()):
        if len(idx) > 1:
            return False
        key = arrayType[0][0]
        if type(idx[0]) is type(key):
            return True
        else:
            return False
    if type(arrayType[0]) is type([]):
        if type(idx[0]) is IntType:
            return checkArrayAccess(arrayType[0], idx[1:])
        else:
            return False


class Type(ABC): #abstract class
    pass

class IntType(Type):
    pass

class FloatType(Type):
    pass

class BoolType(Type):
    pass

class StringType(Type):
    pass

class VoidType(Type):
    pass

class NoneType(Type):
    pass


class Visitor(ABC):
    def visit(self, ctx, o):
        return ctx.accept(self, o)

class StaticChecker(Visitor):
    def __init__(self, ast):
        self.ast = ast
        self.o = [{}]


    def check(self):
        return self.visit(self.ast, self.o)


    def visitProgram(self, ctx, o):
        o = [{}]

        o[0]["str2int"] = {'param': {"x": StringType()}, "return": IntType()}
        o[0]["int2str"] = {'param': {"x": IntType()}, "return": StringType()}
        o[0]["str2float"] = {'param': {"x": StringType()}, "return": FloatType()}
        o[0]["float2str"] = {'param': {"x": FloatType()}, "return": StringType()}
        o[0]["str2bool"] = {'param': {"x": StringType()}, "return": BoolType()}
        o[0]["bool2str"] = {'param': {"x": BoolType()}, "return": StringType()}
        o[0]["_echo"] = {'param': {"x": StringType()}, "return": VoidType()}
        o[0]["_read"] = {'param': {}, "return": VoidType()}

        for const in ctx.const:
            self.visit(const, o)
        for nonconst in ctx.nonconst:
            self.visit(nonconst, o)
        if "_main" not in o[0]:
            raise NoEntryPoint()


    def visitConstDecl(self, ctx, o):
        value = self.visit(ctx.value, o)
        if ctx.id.name in o[0]:
            raise Redeclared(Const(), ctx.id)
        o[0][ctx.id.name] = value


    def visitAssign(self, ctx, o):
        rhs = self.visit(ctx.rhs, o)
        if type(ctx.lhs) is Id and ctx.lhs.name not in o[0]:
            o[0][ctx.lhs.name] = NoneType()
            lhs = NoneType()
        else:
            try:
                self.visit(ctx.lhs, o)
            except UndeclaredIdentifier:
                o[0][ctx.lhs.name] = NoneType()
                lhs = NoneType()
            else:
                lhs = self.visit(ctx.lhs, o)
        if type(lhs) is VoidType or type(rhs) is VoidType:
            raise TypeMismatchInStmt(ctx)
        if type(lhs) is NoneType:
            if type(rhs) is NoneType:
                raise TypeCannotBeInferred(ctx)
            else:
                for i in o:
                    if ctx.lhs.name in i:
                        i[ctx.lhs.name] = rhs
                        break
        else:
            if type(rhs) is NoneType:
                for i in o:
                    if ctx.rhs.name in i:
                        i[ctx.rhs.name] = lhs
                        break
            else:
                if type(lhs) is not type(rhs):
                    if type(rhs) is BoolType and type(lhs) is IntType:
                        if type(ctx.lhs) is Id:
                            for i in o:
                                if ctx.lhs.name in i:
                                    i[ctx.lhs.name] = rhs
                                    break
                    elif type(rhs) is IntType or type(rhs) is BoolType and type(lhs) is FloatType:
                        if type(ctx.lhs) is Id:
                            for i in o:
                                if ctx.lhs.name in i:
                                    i[ctx.lhs.name] = rhs
                                    break
                    else:
                        raise TypeMismatchInStmt(ctx)


    def visitParamDecl(self, ctx, o):
        if ctx.id.name in o[0]:
            raise Redeclared(Var(), ctx.id.name)
        o[0][ctx.id.name] = NoneType()


    def visitFuncDecl(self, ctx, o):
        for i in o:
            if ctx.name.name in i:
                raise Redeclared(Func(), ctx.name.name)
        o[0][ctx.name.name] = {'param': {}, "return": VoidType()}
        env = [{}] + o
        for param in ctx.param:
            self.visit(param, env)
        for key in env[0]:
            o[0][ctx.name.name]["param"][key] = env[0][key]
        env[0]["function"] = VoidType()
        for stmt in ctx.body:
            self.visit(stmt, env)
        for key in o[0][ctx.name.name]["param"]:
            o[0][ctx.name.name]["param"][key] = env[0][key]
        o[0][ctx.name.name]["return"] = env[0]["function"]


    def visitForEach(self, ctx, o):
        arr = self.visit(ctx.arr, o)
        if type(arr) is not type([]):
            raise TypeMismatchInStmt(ctx)
        env = [{}] + o
        env[0]["foreach"] = VoidType()
        if len(arr) == 0:
            env[0][ctx.key.name] = IntType()
            env[0][ctx.value.name] = NoneType()
        elif type(arr[0]) is type(()):
            env[0][ctx.key.name] = arr[0][0]
            env[0][ctx.value.name] = arr[0][1]
        else:
            env[0][ctx.key.name] = IntType()
            env[0][ctx.value.name] = arr[0]
        for stmt in ctx.body:
            self.visit(stmt, env)


    def visitWhile(self, ctx, o):
        cond = self.visit(ctx.cond, o)
        if type(cond) is NoneType:
            for i in o:
                if ctx.cond.name in i:
                    i[ctx.cond.name] = BoolType()
                    cond = BoolType()
                    break
        if type(cond) is not BoolType:
            raise TypeMismatchInStmt(ctx)
        env = [{}] + o
        env[0]["while"] = VoidType()
        for stmt in ctx.body:
            self.visit(stmt, env)


    def visitBreak(self, ctx, o):
        for i in o:
            if "while" in i or "foreach" in i:
                return
        raise TypeMismatchInStmt(ctx)


    def visitContinue(self, ctx, o):
        for i in o:
            if "while" in i or "foreach" in i:
                return
        raise TypeMismatchInStmt(ctx)


    def visitReturn(self, ctx, o):
        check = False
        for i in o:
            if "function in i":
                check = True
                break
        if check == False:
            raise TypeMismatchInStmt(ctx)
        else:
            if ctx.exp is None:
                o[0]["function"] = VoidType()
            else:
                typ = self.visit(ctx.exp, o)
                o[0]["function"] = typ


    def visitId(self, ctx, o):
        for i in o:
            if ctx.name in i:
                return i[ctx.name]
        raise UndeclaredIdentifier(ctx.name)


    def visitArrayAccess(self, ctx, o):
        arr = self.visit(ctx.id, o)
        if len(arr) == 0:
            return arr
        if type(arr) is not type([]):
            raise TypeMismatchInExpr(ctx)
        index = []
        for idx in ctx.idx:
            index += [self.visit(idx, o)]
        if len(index) == 0:
            raise TypeMismatchInExpr(ctx)
        if (checkArrayAccess(arr, index) == False):
            raise TypeMismatchInExpr(ctx)
        value = arr[0]
        for _ in range(len(index) -1):
            value = value[0]
        if type(value) is type(()):
            value = value[1]
        return value


    def visitBinExp(self, ctx, o):
        left = self.visit(ctx.left, o)
        right = self.visit(ctx.right, o)
        if ctx.op in ["+", "-", "*", "/", "%"]:
            if type(left) is NoneType:
                if type(right) is IntType or type(right) is FloatType:
                    for i in o:
                        if ctx.left.name in i:
                            i[ctx.left.name] = FloatType()
                            break
                    return FloatType()
                else:
                    raise TypeMismatchInExpr(ctx)
            if type(right) is NoneType:
                if type(left) is IntType or type(left) is FloatType:
                    for i in o:
                        if ctx.right.name in i:
                            i[ctx.right.name] = FloatType()
                            break
                    return FloatType()
                else:
                    raise TypeMismatchInExpr(ctx)
            if type(left) is IntType and type(right) is IntType:
                return IntType()
            elif type(left) is FloatType and (type(right) is IntType or type(right) is FloatType) or type(right) is FloatType and (type(left) is IntType or type(left) is FloatType):
                return FloatType()
            else:
                raise TypeMismatchInExpr(ctx)
        elif ctx.op in ["&&", "||"]:
            if type(left) is NoneType:
                if type(right) is BoolType:
                    for i in o:
                        if ctx.left.name in i:
                            i[ctx.left.name] = BoolType()
                            break
                    return BoolType()
                else:
                    raise TypeMismatchInExpr(ctx)
            if type(right) is NoneType:
                if type(left) is BoolType:
                    for i in o:
                        if ctx.right.name in i:
                            i[ctx.right.name] = BoolType()
                            break
                    return BoolType()
                else:
                    raise TypeMismatchInExpr(ctx)
            if type(left) is BoolType and type(right) is BoolType:
                return BoolType()
            else:
                raise TypeMismatchInExpr(ctx)
        elif ctx.op in ["==", "!=", "<", ">", "<=", ">="]:
            if type(left) is NoneType:
                if type(right) is IntType or type(right) is FloatType:
                    for i in o:
                        if ctx.left.name in i:
                            i[ctx.left.name] = FloatType()
                            break
                    return BoolType()
                else:
                    raise TypeMismatchInExpr(ctx)
            if type(right) is NoneType:
                if type(left) is IntType or type(left) is FloatType:
                    for i in o:
                        if ctx.right.name in i:
                            i[ctx.right.name] = FloatType()
                            break
                    return BoolType()
                else:
                    raise TypeMismatchInExpr(ctx)
            if (type(left) is IntType or type(left) is FloatType) and (type(right) is IntType or type(right) is FloatType):
                return BoolType()
            else:
                raise TypeMismatchInExpr(ctx)
        elif ctx.op == "+.":
            if type(left) is NoneType:
                if type(right) is StringType:
                    for i in o:
                        if ctx.left.name in i:
                            i[ctx.left.name] = StringType()
                            break
                    return StringType()
                else:
                    raise TypeMismatchInExpr(ctx)
            if type(right) is NoneType:
                if type(left) is StringType:
                    for i in o:
                        if ctx.right.name in i:
                            i[ctx.right.name] = StringType()
                            break
                    return StringType()
                else:
                    raise TypeMismatchInExpr(ctx)
            if type(left) is StringType and type(right) is StringType:
                return StringType()
            else:
                raise TypeMismatchInExpr(ctx)
        elif ctx.op == "==.":
            if type(left) is NoneType:
                if type(right) is StringType:
                    for i in o:
                        if ctx.left.name in i:
                            i[ctx.left.name] = StringType()
                            break
                    return BoolType()
                else:
                    raise TypeMismatchInExpr(ctx)
            if type(right) is NoneType:
                if type(left) is StringType:
                    for i in o:
                        if ctx.right.name in i:
                            i[ctx.right.name] = StringType()
                            break
                    return BoolType()
                else:
                    raise TypeMismatchInExpr(ctx)
            if type(left) is StringType and type(right) is StringType:
                return BoolType()
            else:
                raise TypeMismatchInExpr(ctx)


    def visitUnExp(self, ctx, o):
        typ = self.visit(ctx.exp, o)
        if ctx.op == "!":
            if type(typ) is NoneType:
                for i in o:
                    if ctx.name in i:
                        i[ctx.name] = BoolType()
                        break
                return BoolType()
            elif type(typ) is BoolType:
                return BoolType()
            else:
                raise TypeMismatchInExpr(ctx)
        elif ctx.op == "-":
            if type(typ) is NoneType:
                for i in o:
                    if ctx.name in i:
                        i[ctx.name] = FloatType()
                        break
                return FloatType()
            elif type(typ) is IntType:
                return IntType()
            elif type(typ) is FloatType:
                return FloatType()
            else:
                raise TypeMismatchInExpr(ctx)


    def visitAssocExp(self, ctx, o):
        key = self.visit(ctx.key, o)
        value = self.visit(ctx.value, o)
        if type(key) is not IntType and type(key) is not StringType:
            raise InvalidArrayLiteral(ctx)
        return (key,value)


    def visitIntLit(self, ctx, o):
        return IntType()


    def visitFloatLit(self, ctx, o):
        return FloatType()


    def visitBoolLit(self, ctx, o):
        return BoolType()


    def visitStringLit(self, ctx, o):
        return StringType()


    def visitArrayLit(self, ctx, o):
        # Indexed Array: [element_type]
        # Associative Array: [(key_type, value_type)]
        # Multi-dimensional array: [[element_type]] or [[(key_type, value_type)]]
        if len(ctx.value) == 0:
            return []
        values = ctx.value # list element
        typ = self.visit(values[0], o) # type of first element
        if type(typ) is NoneType or type(typ) is VoidType:
            raise InvalidArrayLiteral(ctx)
        for value in values:
            elementType = self.visit(value, o)
            check = compareType(typ, elementType)
            if check == False:
                raise InvalidArrayLiteral(ctx)
        return [typ]


    def visitCall(self, ctx, o):
        isDefine = False
        returnType = VoidType()
        for i in o:
            if ctx.id.name in i:
                if type(i[ctx.id.name]) is type({}):
                    isDefine = True
                    returnType = i[ctx.id.name]["return"]
                    break
        if isDefine == False:
            raise UndeclaredIdentifier(ctx.id.name)
        for i in o:
            if ctx.id.name in i and type(i[ctx.id.name]) is type({}):
                callParam = []
                for arg in ctx.param:
                    param = self.visit(arg, o)
                    callParam.append(param)
                idx = 0
                for j in i[ctx.id.name]["param"]:
                    if type(i[ctx.id.name]["param"][j]) is NoneType:
                        i[ctx.id.name]["param"][j] = callParam[idx]
                    idx += 1
                lstParam = list(i[ctx.id.name]["param"].values())
                idx = 0
                for arg in ctx.param:
                    if type(callParam[idx]) is NoneType:
                        if type(lstParam[idx]) is NoneType:
                            raise TypeCannotBeInferred(ctx)
                        o[0][arg.name] = lstParam[idx]
                        callParam[idx] = lstParam[idx]
                    idx += 1
                if compareList(lstParam, callParam) == False:
                    raise TypeMismatchInStmt(ctx)
                return returnType


    def visitIf(self, ctx, o):
        for ifThen in ctx.ifthenStmt:
            condition = self.visit(ifThen[0], o)
            if type(condition) is NoneType:
                for i in o:
                    if ifThen[0].name in i:
                        i[ifThen[0].name] = BoolType()
                        condition = BoolType()
                        break
            if type(condition) is not BoolType:
                raise TypeMismatchInStmt(ctx)
            env = [{}] + o
            stmts = ifThen[1]
            for stmt in stmts:
                self.visit(stmt, env)
        for elseStmt in ctx.elseStmt:
            env = [{}] + o
            self.visit(elseStmt, env)