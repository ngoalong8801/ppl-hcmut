from MPVisitor import MPVisitor
from MPParser import MPParser
from AST import *

class ASTGeneration(MPVisitor):
    def toBool(self,x):
        return x == "True"

    def visitProgram(self,ctx:MPParser.ProgramContext):
        return self.visit(ctx.exp())

    def visitExp(self,ctx:MPParser.ExpContext):
        return Binary(self.visit(ctx.ASSIGN()),self.visit(ctx.) )

    def visitTerm(self,ctx:MPParser.TermContext): 
        return None

    def visitFactor(self,ctx:MPParser.FactorContext):
        return None
  
    def visitOperand(self,ctx:MPParser.OperandContext):
        return None

        

