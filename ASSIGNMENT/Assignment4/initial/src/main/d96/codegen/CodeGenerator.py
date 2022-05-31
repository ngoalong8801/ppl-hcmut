'''
 *   @author Nguyen Hua Phung
 *   @version 1.0
 *   23/10/2015
 *   This file provides a simple version of code generator
 *
'''

from functools import reduce
from pydoc import classname
from re import sub
import AST as AS
from AST import *
from Utils import *
from StaticCheck import *
from StaticError import *
from Emitter import Emitter
from Frame import Frame
from abc import ABC, abstractmethod


class ClassData:
    def __init__(self, cname, pname, mem):
        self.cname = cname
        self.pname = pname
        self.mem = mem


class CodeGenerator(Utils):
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [Symbol("getInt", MType(list(), IntType()), CName(self.libName)),
                Symbol("putInt", MType([IntType()],
                       VoidType()), CName(self.libName)),
                Symbol("putIntLn", MType([IntType()],
                       VoidType()), CName(self.libName)),
                Symbol("putFloat", MType(
                    [FloatType()], VoidType()), CName(self.libName)),
                Symbol("putFloatLn", MType(
                    [FloatType()], VoidType()), CName(self.libName)),
                Symbol("putBool", MType([BoolType()],
                       VoidType()), CName(self.libName)),
                Symbol("putBoolLn", MType(
                    [BoolType()], VoidType()), CName(self.libName)),
                Symbol("putString", MType(
                    [StringType()], VoidType()), CName(self.libName)),
                Symbol("putStringLn", MType(
                    [StringType()], VoidType()), CName(self.libName)),
                Symbol("putLn", MType([], VoidType()), CName(self.libName))
                ]

    def gen(self, ast, dir_):
        # ast: AST
        # dir_: String
        globEnv = GlobalEnv().visit(ast, None)
        gl = [ClassData("io", "", self.init())]
        gc = CodeGenVisitor(ast, gl + globEnv, dir_)
        gc.visit(ast, None)


class StringType(Type):

    def __str__(self):
        return "StringType"

    def accept(self, v, param):
        return None


class ArrayPointerType(Type):
    def __init__(self, ctype):
        # cname: String
        self.eleType = ctype

    def __str__(self):
        return "ArrayPointerType({0})".format(str(self.eleType))

    def accept(self, v, param):
        return None


class ClassType(Type):
    def __init__(self, cname):
        self.cname = cname

    def __str__(self):
        return "Class({0})".format(str(self.cname))

    def accept(self, v, param):
        return None


class SubBody():
    def __init__(self, frame, sym):
        # frame: Frame
        # sym: List[Symbol]

        self.frame = frame
        self.sym = sym


class Access():
    def __init__(self, frame, sym, isLeft, isFirst):
        # frame: Frame
        # sym: List[Symbol]
        # isLeft: Boolean
        # isFirst: Boolean

        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst


class Val(ABC):
    pass


class Index(Val):
    def __init__(self, value):
        # value: Int

        self.value = value


class Const(Val):
    def __init__(self, value):
        # value: Int

        self.value = value


class CName(Val):
    def __init__(self, value):
        # value: String

        self.value = value


class Scope():
    def __init__(self, gloS=[], classS=[], methodS=[], blockS=[]):
        self.gloS = gloS
        self.classS = classS
        self.methodS = methodS
        self.blockS = blockS


class GlobalEnv(BaseVisitor):
    def lookup(self, name, lst, func):
        for x in lst:
            if name == func(x):
                return x
        return None

    def visitProgram(self, ast, c):
        scope = Scope(list(), list(), list(), list())
        for x in ast.decl:
            scope.gloS += [self.visit(x, scope)]
        return scope.gloS

    def visitClassDecl(self, ast, c):
        self.classname = ast.classname.name
        # memlist = list(map(lambda i: self.visit(i, c), ast.memlist))
        c.classS = []
        for x in ast.memlist:
            c.classS += [self.visit(x, c)]

        if ast.parentname is None:
            parentName = ""
        else:
            parentName = ast.parentname.name
        return ClassData(ast.classname.name, parentName, c.classS)

    def visitAttributeDecl(self, ast, c):
        decl = ast.decl
        if type(decl) is VarDecl:
            return Symbol(decl.variable.name, decl.varType, Index(decl.varInit))
        return Symbol(decl.constant.name, decl.constType, Const(decl.value))

    def visitMethodDecl(self, ast, c):
        c.methodS = []
        c.blockS = []
        for x in ast.param:
            c.methodS += [self.visit(x, c)]
        returnType = self.visit(ast.body, c)
        if returnType is None:
            returnType = VoidType()
        return Symbol(ast.name.name, MType([x.varType for x in ast.param], returnType), CName(self.classname))

    def visitBlock(self, ast, c):
        for x in ast.inst:
            if type(x) is VarDecl or type(x) is ConstDecl:
                c.blockS += [self.visit(x, c)]
            elif type(x) is Block:
                self.visit(x, Scope(c.gloS, c.glassS, c.methodS, c.blockS))
            elif type(x) is Return:
                return self.visit(x, c)
            else:
                self.visit(x, c)

    def visitConstDecl(self, ast, c):
        return Symbol(ast.constant.name, ast.constType, ast.value)

    def visitVarDecl(self, ast, c):
        return Symbol(ast.variable.name, ast.varType, ast.varInit)

    def visitBinaryOp(self, ast, c):
        if ast.op in ['-', '+', '*', '/', '%']:
            left = self.visit(ast.left, c)
            right = self.visit(ast.right, c)
            if type(left) is FloatType or type(right) is FloatType:
                return FloatType()
            return IntType()
        elif ast.op in ['==', '!=', '<', '>', '<=', '>=', '&&', '||', '==.']:
            return BoolType()
        else:
            return StringType()

    def visitId(self, ast, c):
        res = self.lookup(ast.name, c.methodS + c.blockS, lambda x: x.name if type(
            x.mtype) is not MType else None)
        return res.mtype

    def visitReturn(self, ast, c):
        return self.visit(ast.expr, c)

    def visitCallStmt(self, ast, c):
        pass

    def visitAssign(self, ast, c):
        pass

    def visitIf(self, ast, c):
        pass

    def visitFor(self, ast, c):
        pass

    def visitContinue(self, ast, c):
        pass

    def visitBreak(self, ast, c):
        pass

    def visitIntLiteral(self, ast, c):
        return IntType()

    def visitFloatLiteral(self, ast, c):
        return FloatType()

    def visitStringLiteral(self, ast, c):
        return StringType()


class CodeGenVisitor(BaseVisitor, Utils):
    def __init__(self, astTree, env, dir_):
        # astTree: AST
        # env: List[Symbol]
        # dir_: File

        self.astTree = astTree
        self.env = env
        self.className = "D96Class"
        self.path = dir_
        self.emit = Emitter(self.path + "/" + self.className + ".j")

    def visitProgram(self, ast, c):
        # ast: Program
        # c: Any

        [self.visit(i, c)for i in ast.decl]
        return c

    def visitClassDecl(self, ast, c):
        self.className = ast.classname.name
        self.emit = Emitter(self.path+"/" + self.className + ".j")
        if ast.parentname == None:
            self.emit.printout(self.emit.emitPROLOG(
                self.className, "java.lang.Object"))
        else:
            self.emit.printout(self.emit.emitPROLOG(
                self.className, ast.parentname.name))

        # generate for constructor
        self.genMETHOD(MethodDecl(Instance(), Id("<init>"), list(
        ), Block([])), ([], None), Frame("<init>", VoidType()))

        # visit method
        [self.visit(ele, SubBody(None, []))
         for ele in ast.memlist if type(ele) == MethodDecl]

        self.emit.emitEPILOG()
        return c

    def visitAttributeDecl(self, ast: AttributeDecl, o: SubBody):
        pass

    def visitMethodDecl(self, ast: MethodDecl, o: SubBody):
        returnType = VoidType()

        # Determine return type of method
        if ast.name.name != "main":
            for i in self.env:
                if type(i) is ClassData and i.cname == self.className:
                    for x in i.mem:
                        if x.name == ast.name.name and type(x.mtype) is MType:
                            returnType = x.mtype.rettype
        else:
            returnType = VoidType()
        frame = Frame(ast.name.name, returnType)
        self.genMETHOD(ast, (o.sym, returnType), frame)

    def genMETHOD(self, ast: MethodDecl, o, frame: Frame):
        sym = o[0]
        returnType = o[1]

        # check constructor
        isStatic = True if type(ast.kind) is Static else False
        isInit = returnType is None
        isMain = ast.name.name == "main"

        if isInit:
            returnType = VoidType()
        methodName = "<init>" if isInit else ast.name.name

        inType = [ArrayPointerType(StringType())] if isMain else list(
            map(lambda x: x.varType, ast.param))

        mType = MType(inType, returnType)

        self.emit.printout(self.emit.emitMETHOD(
            methodName, mType, isStatic, frame))

        frame.enterScope(True)
        glEnv = sym

        # generate for parameter
        if isInit or not isStatic:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(
                self.className), frame.getStartLabel(), frame.getEndLabel(), frame))
        elif isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayPointerType(
                StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
        else:
            local = reduce(lambda env, ele: SubBody(
                frame, [self.visit(ele, env)]+env.sym), ast.param, SubBody(frame, []))
            glEnv = local.sym+glEnv

        # generate decl
        body = ast.body
        variable = SubBody(frame, [])
        for x in body.inst:
            if type(x) is VarDecl or type(x) is ConstDecl:
                variable.sym += [self.visit(x, variable)]

        glEnv = variable.sym+glEnv

        # Start Label
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        # Generate code for statements
        if isInit:
            self.emit.printout(self.emit.emitREADVAR(
                "this", ClassType(self.className), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))

        # visit inst in block
        for x in ast.body.inst:
            if type(x) is VarDecl and x.varInit is not None:
                self.visit(Assign(x.variable, x.varInit),
                           SubBody(frame, glEnv))
            elif type(x) is ConstDecl:
                self.visit(Assign(x.constant, x.value),
                           SubBody(frame, glEnv))
            else:
                self.visit(x, SubBody(frame, glEnv))

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if type(returnType) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()

    def visitBlock(self, ast: Block, o: SubBody):
        env = o.sym
        frame = o.frame

        frame.enterScope(False)
        nEnv = SubBody(frame, [])
        for x in ast.inst:
            if type(x) is VarDecl or type(x) is ConstDecl:
                nEnv.sym += [self.visit(x, nEnv)]
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        # visit stmt in block
        for x in ast.inst:
            if type(x) is not VarDecl or type(x) is not ConstDecl:
                self.visit(x, SubBody(frame, nEnv.sym + env))

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        frame.exitScope()

    def visitVarDecl(self, ast: VarDecl, o: SubBody):
        frame = o.frame
        env = o.sym
        index = frame.getNewIndex()
        self.emit.printout(self.emit.emitVAR(
            index, ast.variable.name, ast.varType, frame.getStartLabel(), frame.getEndLabel(), frame))
        return Symbol(ast.variable.name, ast.varType, Index(index))

    def visitConstDecl(self, ast: ConstDecl, o: SubBody):
        frame = o.frame
        env = o.sym
        index = frame.getNewIndex()
        self.emit.printout(self.emit.emitVAR(
            index, ast.constant.name, ast.constType, frame.getStartLabel(), frame.getEndLabel(), frame))
        return Symbol(ast.constant.name, ast.constType, Index(index))

    def visitAssign(self, ast: Assign, o: SubBody):
        ctxt = o
        frame = ctxt.frame
        nEnv = ctxt.sym
        rc, rt = self.visit(ast.exp, Access(frame, nEnv, False, True))
        lc, lt = self.visit(ast.lhs, Access(frame, nEnv, True, True))
        if (type(rt) is IntType and type(lt) == FloatType):
            self.emit.printout(rc + self.emit.emitI2F(frame))
        else:
            self.emit.printout(rc)
        self.emit.printout(lc)

    def visitCallStmt(self, ast: CallStmt, o: SubBody):
        ctxt = o
        frame = ctxt.frame
        nEnv = ctxt.sym
        if type(ast.obj) is SelfLiteral:
            sym = self.handleAccess(ast, o, self.className)
        else:
            objc, objt = self.visit(ast.obj, o)
            sym = self.handleAccess(ast, o, objc)
        cname = sym.value.value
        ctype = sym.mtype
        paramList = ("", list())

        # generate code for param of call statement
        for x in ast.param:
            code1, typ1 = self.visit(x, Access(frame, nEnv, False, True))
            paramList = (paramList[0] + code1, paramList[1].append(typ1))
        self.emit.printout(paramList[0])

        self.emit.printout(self.emit.emitINVOKESTATIC(
            cname + "/" + ast.method.name, ctype, frame))

    def handleAccess(self, ast, o, name):
        if type(ast) is FieldAccess:
            nameField = ast.fieldname.name
        else:
            nameField = ast.method.name
        crrClass = self.lookup(name, self.env, lambda x: x.cname)
        method = self.lookup(
            nameField, crrClass.mem, lambda x: x.name)
        if method is not None:
            return method
        if crrClass.pname != "":
            return self.handleAccess(ast, o, crrClass.pname)

    def visitIf(self, ast: If, o: SubBody):
        ctxt = o
        frame = ctxt.frame
        nEnv = ctxt.sym
        expc, expt = self.visit(
            ast.expr, Access(frame, nEnv, False, True))
        self.emit.printout(expc)
        label1 = frame.getNewLabel()
        label2 = frame.getNewLabel()
        self.emit.printout(self.emit.emitIFFALSE(label1, frame))
        self.visit(ast.thenStmt, ctxt)
        self.emit.printout(self.emit.emitGOTO(label2, frame))
        self.emit.printout(self.emit.emitLABEL(label1, frame))
        if ast.elseStmt is not None:
            self.visit(ast.elseStmt, SubBody(frame, nEnv))
        self.emit.printout(self.emit.emitLABEL(label2, frame))

    def visitFor(self, ast: For, o: SubBody):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        e1c, e1t = self.visit(ast.expr1, Access(frame, nenv, False, True))
        e2c, e2t = self.visit(ast.expr2, Access(frame, nenv, False, True))
        lhscW, lhstW = self.visit(ast.id, Access(
            frame, nenv, True, True))
        lhscR, lhstR = self.visit(ast.id, Access(
            frame, nenv, False, False))

        labelStart = frame.getNewLabel()
        labelEnd = frame.getNewLabel()
        frame.enterLoop()
        # Start Loop
        self.emit.printout(self.emit.emitLABEL(labelStart, frame))

        # conditon 1
        self.emit.printout(lhscR)
        self.emit.printout(e1c)
        self.emit.printout(self.emit.emitIFICMPLT(labelEnd, frame))
        # condition 2

        self.emit.printout(lhscR)
        self.emit.printout(e2c)
        self.emit.printout(self.emit.emitIFICMPGT(labelEnd, frame))

        self.visit(ast.loop, o)
        self.emit.printout(self.emit.emitLABEL(
            frame.getContinueLabel(), frame))

        # update iterate value
        self.emit.printout(lhscR)
        if ast.expr3 is not None:
            self.emit.printout(self.emit.emitPUSHCONST(self.emit.emitExpr(
                Index(ast.expr3), IntType()), IntType(), frame))
        else:
            self.emit.printout(self.emit.emitPUSHICONST(1, frame))
        self.emit.printout(self.emit.emitADDOP('+', IntType(), frame))
        self.emit.printout(lhscW)

        self.emit.printout(self.emit.emitGOTO(labelStart, frame))  # loop
        self.emit.printout(self.emit.emitLABEL(labelEnd, frame))
        self.emit.printout(self.emit.emitLABEL(frame.getBreakLabel(), frame))
        frame.exitLoop()

    def visitContinue(self, ast: Continue, o: SubBody):
        ctxt = o
        frame = ctxt.frame
        self.emit.printout(self.emit.emitGOTO(frame.getContinueLabel(), frame))

    def visitBreak(self, ast: Break, o: SubBody):
        ctxt = o
        frame = ctxt.frame
        self.emit.printout(self.emit.emitGOTO(frame.getBreakLabel(), frame))

    def visitUnaryOp(self, ast: UnaryOp, o: SubBody):
        bdc, bdt = self.visit(ast.body, o)
        frame = o.frame
        if str(ast.op) == '-':
            return bdc + self.emit.emitNEGOP(bdt, frame), bdt
        if str(ast.op) == '!':
            return bdc + self.emit.emitNOT(bdt, frame), bdt

    def visitBinaryOp(self, ast: BinaryOp, o: SubBody or Access):
        frame = o.frame
        exp1, exp1T = self.visit(ast.left, o)
        exp2, exp2T = self.visit(ast.right, o)
        typeOp = exp2T

        if (type(exp1T) is FloatType or type(exp2T) is FloatType or ast.op == "/"):

            typeOp = FloatType()
            if type(exp1T) is IntType:
                exp1 = exp1 + self.emit.emitI2F(frame)
            if type(exp2T) is IntType:
                exp2 = exp2 + self.emit.emitI2F(frame)

        if ast.op in ['+', '-']:
            return exp1 + exp2 + self.emit.emitADDOP(ast.op, typeOp, frame), typeOp
        elif ast.op in ['*', '/']:
            return exp1 + exp2 + self.emit.emitMULOP(ast.op, typeOp, frame), typeOp
        elif ast.op == '%':
            return exp1 + exp2 + self.emit.emitMOD(ast.op, typeOp, frame), typeOp

        if ast.op == '&&':
            return exp1 + exp2 + self.emit.emitANDOP(frame), typeOp
        if ast.op == '||':
            return exp1 + exp2 + self.emit.emitOROP(frame),  typeOp
        if ast.op in [">", ">=", "<", "<=", "!=", "==", '==.']:
            return exp1 + exp2 + self.emit.emitREOP(ast.op,  typeOp, frame), typeOp
        if ast.op == '+.':
            return self.emit.emitConcat("\""+exp1[6:len(exp1)-2] +
                                        exp2[6:len(exp2)-2]+"\"", frame), StringType()

    def visitId(self, ast: Id, o: Access):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        sym = self.lookup(ast.name, nenv, lambda x: x.name)
        if sym is None:
            crrClass = self.lookup(
                self.className, self.env, lambda x: x.cname)
            sym = self.lookup(ast.name, crrClass.mem, lambda x: x.name)

        if sym is None:
            if crrClass.pname != "":
                pntClass = self.lookup(
                    crrClass.pname, self.env, lambda x: x.cname)
                sym = self.lookup(
                    ast.method, pntClass.mem, lambda x: x.name)

        if sym is not None:

            if type(sym.value) is Index:
                if ctxt.isLeft == True:
                    if ctxt.isFirst == True:
                        return (self.emit.emitWRITEVAR(ast.name, sym.mtype, sym.value.value, frame), sym.mtype)
                    else:
                        if type(sym.mtype) is ClassType:
                            return (sym.mtype.classname.name, sym.mtype)
                        return (ast.name, sym.mtype)
                else:
                    if ctxt.isFirst == True:
                        if type(sym.value) is Index:
                            return (self.emit.emitREADVAR(ast.name, sym.mtype, sym.value.value, frame), sym.mtype)
                        else:
                            return (self.emit.emitREADCONST(sym.value.value, sym.mtype, frame), sym.mtype)
                    else:
                        return (self.emit.emitREADVAR(ast.name, sym.mtype, sym.value.value, frame), sym.mtype)
            else:
                return (ast.name, sym.mtype)
        sym = self.lookup(ast.name, self.env, lambda x: x.cname)
        if sym is not None:
            return (ast.name, ClassType(ast.name))

    def visitFieldAccess(self, ast: FieldAccess, o: SubBody or Access):
        ctxt = o
        frame = ctxt.frame
        if type(ast.obj) is SelfLiteral:
            sym = self.handleAccess(ast, o, self.className)
        else:
            objc, objt = self.visit(
                ast.obj, Access(frame, ctxt.sym, True, False))
            sym = self.handleAccess(ast, o, objc)
        if sym is not None:
            if(ctxt.isLeft == True):
                return (self.emit.emitPUTSTATIC(objc+"."+sym.name, sym.mtype, frame), sym.mtype)
            if sym.value is not None:
                return (self.emit.emitPUSHCONST(self.emit.emitExpr(sym.value, sym.mtype), sym.mtype, frame), sym.mtype)
            return (self.emit.emitGETSTATIC(objc+"."+sym.name, sym.mtype, frame), sym.mtype)

    def visitReturn(self, ast: Return, o: SubBody):
        pass

    def visitIntLiteral(self, ast, o):
        return self.emit.emitPUSHICONST(ast.value, o.frame), IntType()

    def visitFloatLiteral(self, ast, o):
        return self.emit.emitPUSHFCONST(str(ast.value), o.frame), FloatType()

    def visitStringLiteral(self, ast, o):
        return self.emit.emitPUSHCONST(ast.value, StringType(), o.frame), StringType()

    def visitBooleanLiteral(self, ast, o):
        return self.emit.emitPUSHICONST(str(ast.value), o.frame), BoolType()

    def visitArrayCell(self, ast: ArrayCell, o: SubBody):
        pass

    def visitNewExp(self, ast: NewExpr, o: SubBody):
        pass
