import unittest
from TestUtils import TestChecker
from AST import *


class CheckerSuite(unittest.TestCase):
    #     def test_undeclared_function(self):
    #         """Simple program: int main() {} """
    #         input = """Class Program{
    #         }
    #         Class Program1{
    #         }
    #         Class Program{
    #         }
    #         """
    #         expect = "Redeclared Class: Program"
    #         self.assertTrue(TestChecker.test(input, expect, 400))

    # def test_undeclared_function1(self):
    #     """Simple program: int main() {} """
    #     input = """Class Program{
    #         Val a : Int;
    #         Var a: Int;
    #     }
    #    """
    #     expect = "Redeclared Attribute: a"
    #     self.assertTrue(TestChecker.test(input, expect, 401))

    # def test_redeclared_method(self):
    #     """Simple program: int main() {} """
    #     input = """Class Program{
    #         methodOne(){
    #         }
    #         methodOne(){
    #         }
    #     }
    #    """
    #     expect = "Redeclared Method: methodOne"
    #     self.assertTrue(TestChecker.test(input, expect, 402))

    # def test_redeclared_method(self):
    #     """Simple program: int main() {} """
    #     input = """Class Program{
    #         methodOne(){
    #         }
    #     }

    #     Class Program1{
    #         Val a : Int;
    #         Val b: Int;
    #         Var b : Int;
    #     }
    #    """
    #     expect = "Redeclared Attribute: b"
    #     self.assertTrue(TestChecker.test(input, expect, 403))

    # def test_redeclared_method(self):
    #     """Simple program: int main() {} """
    #     input = """Class Program{
    #         Val methodOne: Int;
    #         methodOne(){
    #         }

    #     }
    #    """
    #     expect = "Redeclared Method: methodOne"
    #     self.assertTrue(TestChecker.test(input, expect, 402))

    # def test_redeclared_method(self):
    #     """Simple program: int main() {} """
    #     input = """Class Program{
    #         Val methodOne: Int;
    #         methodOne(a, b, t: Int; c, a, n: Float){

    #         }

    #     }
    #    """
    #     expect = "Redeclared Parameter: a"
    #     self.assertTrue(TestChecker.test(input, expect, 403))

    # def test_redeclared_method(self):
    #     """Simple program: int main() {} """
    #     input = """Class Program{
    #         Val methodOne: Int;
    #         methodOne(a, c, t: Int){
    #             Var a: Int;
    #         }

    #     }
    #    """
    #     expect = "Redeclared Variable: a"
    #     self.assertTrue(TestChecker.test(input, expect, 403))
    # def test_redeclared_method(self):
    #     """Simple program: int main() {} """
    #     input = """Class Program{
    #         Val methodOne: Int;
    #         methodOne(a, c, t: Int){
    #             b = 5;
    #         }

    #     }
    #    """
    #     expect = "Undeclared Identifier: b"
    #     self.assertTrue(TestChecker.test(input, expect, 403))

    def test_redeclared_method(self):
        """Simple program: int main() {} """
        input = """Class Program{
                 Val methodOne: Int;
                  methodOne(a: Int){
                  
                    }

             }
             Class Program1{
                  Val methodOne: Int;

              }
            """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 403))

# def test_undeclared_function(self):
#     """Simple program: int main() {} """
#     input = """int main() {foo();}"""
#     expect = "Undeclared Function: foo"
#     self.assertTrue(TestChecker.test(input, expect, 400))

# def test_diff_numofparam_stmt(self):
#     """More complex program"""
#     input = """int main () {
#         putIntLn();
#     }"""
#     expect = "Type Mismatch In Statement: CallExpr(Id(putIntLn),List())"
#     self.assertTrue(TestChecker.test(input,expect,401))

# def test_diff_numofparam_expr(self):
#     """More complex program"""
#     input = """int main () {
#         putIntLn(getInt(4));
#     }"""
#     expect = "Type Mismatch In Expression: CallExpr(Id(getInt),List(IntLiteral(4)))"
#     self.assertTrue(TestChecker.test(input,expect,402))

# def test_undeclared_function_use_ast(self):
#     """Simple program: int main() {} """
#     input = Program([FuncDecl(Id("main"),[],IntType(),Block([],[
#         CallExpr(Id("foo"),[])]))])
#     expect = "Undeclared Function: foo"
#     self.assertTrue(TestChecker.test(input,expect,403))

# def test_diff_numofparam_expr_use_ast(self):
#     """More complex program"""
#     input = Program([
#             FuncDecl(Id("main"),[],IntType(),Block([],[
#                 CallExpr(Id("putIntLn"),[
#                     CallExpr(Id("getInt"),[IntLiteral(4)])
#                     ])]))])
#     expect = "Type Mismatch In Expression: CallExpr(Id(getInt),List(IntLiteral(4)))"
#     self.assertTrue(TestChecker.test(input,expect,404))

# def test_diff_numofparam_stmt_use_ast(self):
#     """More complex program"""
#     input = Program([
#             FuncDecl(Id("main"),[],IntType(),Block([],[
#                 CallExpr(Id("putIntLn"),[])]))])
#     expect = "Type Mismatch In Statement: CallExpr(Id(putIntLn),List())"
#     self.assertTrue(TestChecker.test(input,expect,405))
