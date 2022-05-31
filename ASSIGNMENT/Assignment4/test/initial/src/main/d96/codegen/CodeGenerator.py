'''
 *   @author Nguyen Hua Phung
 *   @version 1.0
 *   23/10/2015
 *   This file provides a simple version of code generator
 *
'''
from ast import stmt
from AST import VoidType
from Utils import *
from StaticCheck import *
from StaticError import *
from Emitter import Emitter
from Frame import Frame
from abc import ABC, abstractmethod
from functools import reduce


class CodeGenerator(Utils):
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [Symbol("getInt", MType(list(), IntType()), CName(self.libName)),
                Symbol("putInt", MType([IntType()],
                       VoidType()), CName(self.libName)),
                Symbol("putIntLn", MType([IntType()],
                       VoidType()), CName(self.libName)),
                Symbol("readInt",    MType(
                    list(), IntType()), CName(self.libName)),
                Symbol("writeInt",   MType(
                    [IntType()], VoidType()), CName(self.libName)),
                Symbol("writeIntLn", MType(
                    [IntType()], VoidType()), CName(self.libName)),
                Symbol("readFloat", MType(list(), FloatType()),
                       CName(self.libName)),
                Symbol("writeFloat",   MType(
                    [FloatType()], VoidType()), CName(self.libName)),
                Symbol("writeFloatLn", MType(
                    [FloatType()], VoidType()), CName(self.libName)),
                Symbol("readBool", MType(list(), BoolType()),
                       CName(self.libName)),
                Symbol("writeBool",   MType(
                    [BoolType()], VoidType()), CName(self.libName)),
                Symbol("writeBoolLn", MType(
                    [BoolType()], VoidType()), CName(self.libName)),
                Symbol("readStr", MType(list(), StringType()),
                       CName(self.libName)),
                Symbol("writeStr",   MType(
                    [StringType()], VoidType()), CName(self.libName)),
                Symbol("writeStrLn", MType(
                    [StringType()], VoidType()), CName(self.libName))

                ]

    def gen(self, ast, dir_):
        # ast: AST
        # dir_: String

        gl = self.init()
        gc = CodeGenVisitor(ast, gl, dir_)
        gc.visit(ast, None)


class GetEnv(BaseVisitor):
    def __init__(self, astTree):
        self.astTree = astTree
        self.env = []

    def visitProgram(self, ast: Program, o):
        [self.visit(i, False) for i in ast.decl]
        # raise Exception(self.env[3].value.value)
        return self.env

    def visitClassDecl(self, ast: ClassDecl, o):
        isParentvisit = o
        if not isParentvisit:
            self.className = ast.classname.name
        [self.visit(ele, self.env) for ele in ast.memlist]

        if ast.parentname:
            parentClass = None
            for x in self.astTree.decl:
                if x.classname.name == ast.parentname.name:
                    parentClass = x
            self.visit(parentClass, True)

    def visitMethodDecl(self, ast: MethodDecl, o):
        returnType = self.visit(ast.body, o)
        self.env.append(Symbol(ast.name.name, MType(
            [x.varType for x in ast.param], returnType), CName(self.className)))

    def visitBlock(self, ast: Block, o):
        for x in ast.inst:
            if type(x) is Return or type(x) is Block:
                returnType = self.visit(x, o)
                if type(returnType) is not VoidType() and returnType is not None:
                    return returnType
        return VoidType()

    def visitReturn(self, ast: Return, o):
        return self.visit(ast.expr, o)

    def visitBinaryOp(self, ast: BinaryOp, o):
        left = self.visit(ast.left, o)
        right = self.visit(ast.right, o)

        if ast.op in ['-', '+', '*', '/', '%']:
            if type(left) is FloatType or type(right) is FloatType:
                returnType = FloatType()
            returnType = IntType()

        if ast.op in ['&&', '||', '==', '!=', '<', '>', '<=', '>=']:
            returnType = BoolType()
        elif ast.op == '+.':
            returnType = StringType()

        return returnType

    def visitVarDecl(self, ast: VarDecl, o):
        return Symbol(ast.decl.variable.name, ast.decl.varType)

    def visitConstDecl(self, ast: ConstDecl, o):
        return Symbol(ast.decl.constant.name, ast.decl.constType)

    def visitAttributeDecl(self, ast: AttributeDecl, o):
        if type(ast.decl) is VarDecl:
            self.env.append(Symbol(ast.decl.variable.name,
                            ast.decl.varType, CName(self.className)))
        elif type(ast.decl) is ConstDecl:
            self.env.append(Symbol(ast.decl.constant.name,
                            ast.decl.constType, CName(self.className)))

    def visitIntLiteral(self, ast, o):
        return IntType()

    def visitFloatLiteral(self, ast, o):
        return FloatType()


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
    def __init__(self, frame, sym, isLeft, isFirst=False):
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


class CName(Val):
    def __init__(self, value):
        # value: String

        self.value = value

    def __str__(self):
        return "Cname(" + self.value + ")"


class CodeGenVisitor(BaseVisitor, Utils):
    def __init__(self, astTree, env, dir_):
        # astTree: AST
        # env: List[Symbol]
        # dir_: File

        self.astTree = astTree
        glenv = GetEnv(astTree)
        self.env = glenv.visit(astTree, None) + env
        self.className = "D96Class"
        self.path = dir_
        self.emit = Emitter(self.path + "/" + self.className + ".j")

    def lookupFunc(self, name, lst, func):
        for x in lst:
            if name == func(x) and self.className == x.value.value:
                return x
        return None

    def visitProgram(self, ast, c):
        # ast: Program
        # c: Any

        # self.emit.printout(self.emit.emitPROLOG(
        #     self.className, "java.lang.Object"))
        # e = SubBody(None, self.env)
        # for x in ast.decl:
        #     e = self.visit(x, e)
        # # generate default constructor
        # self.genMETHOD(FuncDecl(Id("<init>"), list(), None, Block(
        #     list(), list())), c, Frame("<init>", VoidType))
        # self.emit.emitEPILOG()
        [self.visit(x, c) for x in ast.decl]
        return c

    def visitClassDecl(self, ast, c):
        self.className = ast.classname.name
        # self.emit = Emitter(self.path+"/" + self.className + ".j")
        if ast.parentname == None:
            self.emit.printout(self.emit.emitPROLOG(
                self.className, "java.lang.Object"))
        else:
            self.emit.printout(self.emit.emitPROLOG(
                self.className, ast.parentname.name))
        [self.visit(ele, SubBody(None, self.env))
         for ele in ast.memlist if type(ele) == MethodDecl]
        # generate default constructor
        self.genMETHOD(MethodDecl(Instance(), Id("<init>"), [],
                       Block([])), c, Frame("<init>", VoidType()), True)
        self.emit.emitEPILOG()
        return c

    def genMETHOD(self, consdecl, o, frame, isInit=False):
        returnType = VoidType()
        isMain = consdecl.name.name == "main" and len(
            consdecl.param) == 0 and type(returnType) is VoidType

        returnType = VoidType() if isInit else returnType
        methodName = "<init>" if isInit else consdecl.name.name
        intype = [ArrayPointerType(StringType())] if isMain else list(
            map(lambda x: x.varType, consdecl.param))
        mtype = MType(intype, returnType)

        self.emit.printout(self.emit.emitMETHOD(
            methodName, mtype, not isInit, frame))

        frame.enterScope(True)

        glenv = o

        # Generate code for parameter declarations
        if isInit:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(
                self.className), frame.getStartLabel(), frame.getEndLabel(), frame))
        elif isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayPointerType(
                StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))

        body = consdecl.body
        decls = []
        stmt = []
        for x in body.inst:
            if type(x) is VarDecl or type(x) is ConstDecl:
                decls += [x]
            else:
                stmt += [x]

        if len(decls) > 0:
            variable = reduce(lambda env, ele: SubBody(
                frame, [self.visit(ele, env)]+env.sym), decls, SubBody(frame, []))
            glenv = variable.sym+glenv

        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        # Generate code for statements
        if isInit:
            self.emit.printout(self.emit.emitREADVAR(
                "this", ClassType(Id(self.className)), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        for x in decls:
            if type(x) is VarDecl and x.varInit is not None:
                self.visit(Assign(x.variable, x.varInit),
                           SubBody(frame, glenv))
        list(map(lambda x: self.visit(x, SubBody(frame, glenv)), stmt))

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if type(returnType) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()
        # consdecl: FuncDecl
        # o: Any
        # frame: Frame
        # isInit = consdecl.returnType is None
        # isMain = consdecl.name.name == "main" and len(
        #     consdecl.param) == 0 and type(consdecl.returnType) is VoidType
        # returnType = VoidType() if isInit else consdecl.returnType
        # methodName = "<init>" if isInit else consdecl.name.name
        # intype = [ArrayPointerType(StringType())] if isMain else list()
        # mtype = MType(intype, returnType)

        # self.emit.printout(self.emit.emitMETHOD(
        #     methodName, mtype, not isInit, frame))

        # frame.enterScope(True)

        # glenv = o

        # # Generate code for parameter declarations
        # if isInit:
        #     self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(
        #         self.className), frame.getStartLabel(), frame.getEndLabel(), frame))
        # if isMain:
        #     self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayPointerType(
        #         StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))

        # body = consdecl.body
        # self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        # # Generate code for statements
        # if isInit:
        #     self.emit.printout(self.emit.emitREADVAR(
        #         "this", ClassType(self.className), 0, frame))
        #     self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        # list(map(lambda x: self.visit(x, SubBody(frame, glenv)), body.stmt))

        # self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        # if type(returnType) is VoidType:
        #     self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        # self.emit.printout(self.emit.emitENDMETHOD(frame))
        # frame.exitScope()

    def visitMethodDecl(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        func = self.lookupFunc(ast.name.name, nenv, lambda x: x.name)
        frame = Frame(ast.name, func.mtype.rettype)
        self.genMETHOD(ast, o.sym, frame)
        # ast: FuncDecl
        # o: Any

        # subctxt = o
        # frame = Frame(ast.name, VoidType())
        # self.genMETHOD(ast, subctxt.sym, frame)
        # return SubBody(None, [Symbol(ast.name, MType(list(), VoidType()), CName(self.className))] + subctxt.sym)

    def visitCallExpr(self, ast, o):
        # ast: CallExpr
        # o: Any

        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        sym = self.lookup(ast.method.name, nenv, lambda x: x.name)
        cname = sym.value.value

        ctype = sym.mtype

        in_ = ("", list())
        for x in ast.param:
            str1, typ1 = self.visit(x, Access(frame, nenv, False, True))
            in_ = (in_[0] + str1, in_[1].append(typ1))
        self.emit.printout(in_[0])
        self.emit.printout(self.emit.emitINVOKESTATIC(
            cname + "/" + ast.method.name, ctype, frame))

    def visitIntLiteral(self, ast, o):
        # ast: IntLiteral
        # o: Any

        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHICONST(ast.value, frame), IntType()

    def visitVarDecl(self, ast, o):
        pass

    def visitCallStmt(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        symbols = ctxt.sym
        self.handleCall(ast, frame, symbols, isStmt=True)
        pass

    def handleCall(self, ast: CallStmt or CallExpr, frame, symbols, isStmt):
        # ast: callstmt | callexpr
        # visit obj
        isStatic, ot = self.visit(ast.obj, Access(frame, symbols, False, True))
        className = ot
        sym = next(
            filter(lambda x:
                   ast.method.name == x.name and type(
                       x.value) is CName and x.value.value == className, symbols
                   ),
            False)
        cname = sym.value.value
        ctype = sym.mtype
        paramTypes = ctype.partype

        paramsCode = ""
        idx = 0
        for x in ast.param:
            pCode, pType = self.visit(x, Access(frame, symbols, False))
            paramsCode = paramsCode + pCode
            idx = idx + 1

        if isStatic:
            code = paramsCode + \
                self.emit.emitINVOKESTATIC(
                    cname + "/" + sym.name, ctype, frame)
        else:
            code = paramsCode + \
                self.emit.emitINVOKEVIRTUAL(
                    cname + "/" + sym.name, ctype, frame)

        if isStmt:
            self.emit.printout(code)
        else:
            return code, ctype.rettype

    def visitId(self, ast: Id, o: Access):
        ctxt = o
        frame = ctxt.frame
        symbols = ctxt.sym
        isLeft = ctxt.isLeft
        isFirst = ctxt.isFirst
        # isField = ctxt.isField
        # className = ctxt.className

        if isFirst:  # to get classname in fieldaccess
            # tim trong sym neu k thay ast.name thi day la ten class, neu k thi lay ten class cua ast.name
            ret = ast.name  # classtype or classId
            # if ret in symbols => instance field access
            for i in range(0, len(symbols)-1):
                if symbols[i].name == ast.name:
                    ret = symbols[i].mtype.classname.name
                    sym = symbols[i]
                    #raise Exception(self.emit.emitREADVAR(sym.name, sym.mtype, sym.value.value, frame))
                    self.emit.printout(
                        self.emit.emitREADVAR(
                            sym.name, sym.mtype, sym.value.value, frame)
                    )
                    return False, ret

            return True, ret

        sym = None
        # if isField:  # for field, x.value is Cname
        #     for x in symbols:
        #         if type(x.value) is CName and x.value.value == className and x.name == ast.name:
        #             sym = x
        #             break

        #     if isLeft:
        #         if o.isStatic:
        #             retCode = self.emit.emitPUTSTATIC(
        #                 className + "/" + sym.name, sym.mtype, frame)
        #         else:
        #             retCode = self.emit.emitPUTFIELD(
        #                 className + "/" + sym.name, sym.mtype, frame)
        #     else:
        #         if o.isStatic:
        #             retCode = self.emit.emitGETSTATIC(
        #                 className + "/" + sym.name, sym.mtype, frame)
        #         else:
        #             retCode = self.emit.emitGETFIELD(
        #                 className + "/" + sym.name, sym.mtype, frame)

        # else:  # for local var, x.value is Index
        #     for x in symbols:
        #         if x.name == ast.name:
        #             sym = x
        #             break
        #     if isLeft:
        #         retCode = self.emit.emitWRITEVAR(
        #             sym.name, sym.mtype, sym.value.value, frame)
        #     else:
        #         retCode = self.emit.emitREADVAR(
        #             sym.name, sym.mtype, sym.value.value, frame)

        # return retCode, sym.mtype
