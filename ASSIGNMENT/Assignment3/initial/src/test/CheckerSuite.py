import unittest
from TestUtils import TestChecker
from AST import *


class CheckerSuite(unittest.TestCase):
    # def test_undeclared_function(self):
    #     """Simple program: int main() {} """
    #     input = """Class Program{
    #         }
    #         Class Program1{
    #         }
    #         Class Program{
    #         }
    #         """
    #     expect = "Redeclared Class: Program"
    #     self.assertTrue(TestChecker.test(input, expect, 400))

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

    # def test_redeclared_method(self):
    #     """Simple program: int main() {} """
    #     input = """Class Shape{
    #                   Val methodOne: Int;
    #                      methodOne(a: Int){

    #                      }

    #            }
    #            Class Program1{
    #                 Val methodOne: Int;
    #                 method(){

    #                     Var a: Shape1 = New Shape1();

    #                 }
    #             }
    #            """
    #     expect = "Undeclared Class: Shape1"
    #     self.assertTrue(TestChecker.test(input, expect, 403))
    # def test_redeclared_method(self):
    #     """Simple program: int main() {} """
    #     input = """Class Shape{
    #                   Val methodOne: Int;
    #                      methodOne(a: Int){

    #                      }

    #            }
    #            Class Program1{
    #                 Val methodOne: Int;
    #                 method(){

    #                     Var a: Shape = New Shape();
    #                     a.methodOn1e();

    #                 }
    #             }
    #            """
    #     expect = "Undeclared Method: methodOn1e"
    #     self.assertTrue(TestChecker.test(input, expect, 403))

    # def test_redeclared_method(self):
    #     """Simple program: int main() {} """
    #     input = """Class Shape{
    #                   Val methodOne: Int;
    #                      methodOne(a: Int){

    #                      }

    #            }
    #            Class Program1{
    #                 Val methodOne: Int;
    #                 method(){

    #                 }
    #                 method1(){

    #                     Self.metho1d();

    #                 }
    #             }
    #            """
    #     expect = "Undeclared Method: methodOn1e"
    #     self.assertTrue(TestChecker.test(input, expect, 403))

    # def test_redeclared_method(self):
    #     """Simple program: int main() {} """
    #     input = """
    #            Class Program1{
    #                 Val methodOne: Int;

    #                 method1(){
    #                     Val a: Int = 4;
    #                     a = 5;

    #                 }
    #             }
    #            """
    #     expect = "Undeclared Method: methodOn1e"
    #     self.assertTrue(TestChecker.test(input, expect, 403))

    # def test_redeclared_method(self):
    #     """Simple program: int main() {} """
    #     input = """
    #            Class Program1{
    #                 Val methodOne: Int;

    #                 method1(){
    #                     Val a: Int = 4;
    #                     Self.methodOne = 6;

    #                 }
    #             }
    #            """
    #     expect = "Cannot Assign To Constant: AssignStmt(FieldAccess(Self(),Id(methodOne)),IntLit(6))"
    #     self.assertTrue(TestChecker.test(input, expect, 403))

    # def test_redeclared_method(self):
    #     """Simple program: int main() {} """
    #     input = """
    #             Class Program{
    #                 Val ab : Int;
    #                 method(){

    #                 }
    #             }
    #            Class Program1{
    #                 Val methodOne: Int;

    #                 method1(){
    #                     Var a: Program = New Program();
    #                     a.ab = 6;

    #                 }
    #             }
    #            """
    #     expect = "Cannot Assign To Constant: AssignStmt(FieldAccess(Id(a),Id(ab)),IntLit(6))"
    #     self.assertTrue(TestChecker.test(input, expect, 403))

    # def test_redeclared_method(self):
    #     """Simple program: int main() {} """
    #     input = """
    #             Class Program{
    #                 Val ab : Int;
    #                 method(){
    #                     Var a : Int;
    #                     Var b: Int;
    #                     If(a + b){

    #                     }
    #                 }
    #             }

    #            """
    #     expect = "Type Mismatch In Statement: If(BinaryOp(+,Id(a),Id(b)),Block([]))"
    #     self.assertTrue(TestChecker.test(input, expect, 403))

    # def test_redeclared_method(self):
    #     """Simple program: int main() {} """
    #     input = """
    #             Class Program{

    #                 method(){
    #                     Var a : Array[Int, 6];
    #                     a[1.2] = 6;

    #                 }
    #             }

    #            """
    #     expect = "Type Mismatch In Expression: ArrayCell(Id(a),[FloatLit(1.2)])"
    #     self.assertTrue(TestChecker.test(input, expect, 403))

    # def test_redeclared_method(self):
    #     """Simple program: int main() {} """
    #     input = """
    #             Class Program{

    #                 method(){
    #                     Foreach( i In 1.3 .. 100 ){

    #                     }

    #                 }
    #             }

    #            """
    #     expect = "Type Mismatch In Statement: For(Id(i),FloatLit(1.3),IntLit(100),IntLit(1),Block([])])"
    #     self.assertTrue(TestChecker.test(input, expect, 403))

    # def test_redeclared_method(self):
    #     """Simple program: int main() {} """
    #     input = """
    #     Class Pro{
    #         method(a, b: Int){
    #             Return a;
    #             Val c : Boolean;
    #             Return c;
    #         }
    #     }

    #            """
    #     expect = "Type Mismatch In Statement: Return(Id(c))"
    #     self.assertTrue(TestChecker.test(input, expect, 403))

    def test_redeclared_method(self):
        """Simple program: int main() {} """
        input = """
        Class Proa{
            method(){
                Return 5;
            }
        }
        Class Pro{
            method(){
                Var a : Proa = New Proa();
                a.method();
                
            }
        }
             

               """
        expect = "Type Mismatch In Statement: Return(Id(c))"
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
