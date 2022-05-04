import unittest
from TestUtils import TestChecker
from AST import *


class CheckerSuite(unittest.TestCase):
    def test_redeclared_variable_1(self):
        """Test 1"""
        input = """Class Program{

                test(){
                    Var a: Int;
                    Var a: Int = 4;
                }
            }
            
            """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 400))

    def test_redeclared_variable_2(self):
        """Test 1"""
        input = """Class Program{

                test(){
                    
                    If(5 > 4){
                        Var a: Int;
                        Var a: Int = 4;
                    }
                }
            }
            
            """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test_redeclared_constant_1(self):
        """Test 1"""
        input = """Class Program{

                test(){
                    Val a: Int = 5;
                    Val a: Int = 4;
                }
            }
            
            """
        expect = "Redeclared Constant: a"
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test_redeclared_constant_2(self):
        """Test 1"""
        input = """Class Program{

                test(){
                    
                    If(5 > 4){
                        Val a: Int = 5;
                        Val a: Int = 4;
                    }
                }
            }
            
            """
        expect = "Redeclared Constant: a"
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_redeclared_attribute_1(self):
        """Test 1"""
        input = """Class Program{
                Var redecl: Int;
                Var redecl: Int;

                test(){
                    
                }
            }
            
            """
        expect = "Redeclared Attribute: redecl"
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test_redeclared_attribute_2(self):
        """Test 1"""
        input = """Class Program{
                Var redecl: Int;
                

                test(){
                    
                }
                Val redecl: Int = 5;
            }
            
            """
        expect = "Redeclared Attribute: redecl"
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_redeclared_class_1(self):
        """Test 1"""
        input = """Class Program1{
            }
            Class Program1{
            }
            
            """
        expect = "Redeclared Class: Program1"
        self.assertTrue(TestChecker.test(input, expect, 406))

    def test_redeclared_class_2(self):
        """Test 1"""
        input = """Class Program1{
            }
            Class Program2{

            }
            Class Program1{
            }
            
            """
        expect = "Redeclared Class: Program1"
        self.assertTrue(TestChecker.test(input, expect, 407))

    def test_redeclared_method_1(self):
        """Test 1"""
        input = """
        Class Program1{
            method_re(){

            }
            method_re(){
                
            }

            }
            
        Class Program{
            }
            
            
            """
        expect = "Redeclared Method: method_re"
        self.assertTrue(TestChecker.test(input, expect, 408))

    def test_redeclared_method_2(self):
        """Test 1"""
        input = """
        Class Program1{
            method_re1(){

            }
            }
            
        Class Program{
            method_re(){
                
            }
            method_re(){
                
            }
            }
            
            
            """
        expect = "Redeclared Method: method_re"
        self.assertTrue(TestChecker.test(input, expect, 409))

    def test_redeclared_method_3(self):
        """Test 1"""
        input = """
        Class Program1{
            method_re1(){

            }
            }
            
        Class Program{
            method_re(){
                
            }
            method_re(a, b: Int){
                
            }
            }
            
            
            """
        expect = "Redeclared Method: method_re"
        self.assertTrue(TestChecker.test(input, expect, 410))

    def test_redeclared_param_1(self):
        """Test 1"""
        input = """
        Class Program1{
            method_re1(a,b: Int; a: Float){

            }
            }
            
       
            
            
            """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 411))

    def test_redeclared_param_2(self):
        """Test 1"""
        input = """
        Class Program1{
            method_re1(para, para: String){

            }
            }

            """
        expect = "Redeclared Parameter: para"
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test_redeclared_param_3(self):
        """Test 1"""
        input = """
        Class Program1{
            method_re1(){

            }
            method_re2(para, para: String){

            }
            }

            """
        expect = "Redeclared Parameter: para"
        self.assertTrue(TestChecker.test(input, expect, 413))

    def test_redeclared_variable_para_1(self):
        """Test 1"""
        input = """
        Class Program1{
            method_re1(re_var, a: Float){
                Var re_var: Float;
                
            }
            }

            """
        expect = "Redeclared Variable: re_var"
        self.assertTrue(TestChecker.test(input, expect, 414))

    def test_redeclared_constant_para_1(self):
        """Test 1"""
        input = """
        Class Program1{
            method_re1(re_const, a: Float){
                Val re_const: Float = 1.4;
              
            }
            }

            """
        expect = "Redeclared Constant: re_const"
        self.assertTrue(TestChecker.test(input, expect, 415))

    def test_undeclared_iden_1(self):
        """Test 1"""
        input = """
        Class Program1{
            method_re1(){
                ano_iden = 1.4;
              
            }
            }

            """
        expect = "Undeclared Identifier: ano_iden"
        self.assertTrue(TestChecker.test(input, expect, 416))

    def test_undeclared_iden_2(self):
        """Test 1"""
        input = """
        Class Program1{
            method_re1(a: Int){
                a = 4;
                ano_iden = 1.4;
              
            }
            }

            """
        expect = "Undeclared Identifier: ano_iden"
        self.assertTrue(TestChecker.test(input, expect, 417))

    def test_undeclared_attr_1(self):
        """Test 1"""
        input = """
        Class Program1{
            method_re1(){
                Self.a = 4;
              
            }
            }

            """
        expect = "Undeclared Attribute: a"
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test_undeclared_attr_2(self):
        """Test 1"""
        input = """
        Class Program1{
            }
        Class Program2{
            method_re1(){
                Var pro: Program1 = New Program1();
                pro.un_dec = 5;
              
            }
            }

            """
        expect = "Undeclared Attribute: un_dec"
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test_undeclared_method_1(self):
        """Test 1"""
        input = """
        Class Program1{
            method(){
               Self.metho(); 
            }
            }
       
            

            """
        expect = "Undeclared Method: metho"
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test_undeclared_method_2(self):
        """Test 1"""
        input = """
        Class Program1{
            method(){
                Var a: Int;
               a = Self.metho(); 
            }
            }
       
            

            """
        expect = "Undeclared Method: metho"
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test_undeclared_method_3(self):
        """Test 1"""
        input = """
        Class Program1{
            method(){
            }
            }
       Class Program2{
            method_re1(){
                Var pro: Program1 = New Program1();
                Var var_1 : Int;
                var_1 = pro.meth();
              
            }
            }
            

            """
        expect = "Undeclared Method: meth"
        self.assertTrue(TestChecker.test(input, expect, 422))

    def test_undeclared_method_4(self):
        """Test 1"""
        input = """
        Class Program1{
            method(){
                Return 1;
            }
            }
       Class Program2{
            method_re1(){
                Var pro: Program1 = New Program1();
                Var var_1 : Int;
                var_1 = pro.method();
                Self.method();
              
            }
            }
            

            """
        expect = "Undeclared Method: method"
        self.assertTrue(TestChecker.test(input, expect, 423))

    def test_undeclared_class_1(self):
        """Test 1"""
        input = """
        Class Program1{
            method(){
                Return 1;
            }
            }
       Class Program2{
            method_re1(){
                Var pro: Program3 = New Program1();
              
              
            }
            }
            

            """
        expect = "Undeclared Class: Program3"
        self.assertTrue(TestChecker.test(input, expect, 424))

    def test_undeclared_class_2(self):
        """Test 1"""
        input = """
        Class Program1{
            method(){
                Return 1;
            }
            }
       Class Program2{
            method_re1(){
                Val pro: Program3 = New Program1();
              
              
            }
            }
            

            """
        expect = "Undeclared Class: Program3"
        self.assertTrue(TestChecker.test(input, expect, 425))

    def test_undeclared_class_3(self):
        """Test 1"""
        input = """
        Class Program1{
            Var a: NoCla;
            method(){
                Return 1;
            }
            }
            """
        expect = "Undeclared Class: NoCla"
        self.assertTrue(TestChecker.test(input, expect, 426))

    def test_cannot_ass_constant_1(self):
        """Test 1"""
        input = """
        Class Program1{
            
            method(){
               Val cons : Float = 4.5;
               cons = 4.6;
            }
        }
            """
        expect = "Cannot Assign To Constant: AssignStmt(Id(cons),FloatLit(4.6))"
        self.assertTrue(TestChecker.test(input, expect, 427))

    def test_cannot_ass_constant_2(self):
        """Test 1"""
        input = """
        Class Program1{
            
            method(){
                Foreach( i In 2 .. 100 ){
                    Val cons : Float = 4.5;
                    cons = 4.6;
                  }
            }
        }
            """
        expect = "Cannot Assign To Constant: AssignStmt(Id(cons),FloatLit(4.6))"
        self.assertTrue(TestChecker.test(input, expect, 428))

    def test_type_mismatch_in_if_1(self):
        """Test 1"""
        input = """
        Class Program1{
            
            method(){
                If(5){

                }
            }
        }
            """
        expect = "Type Mismatch In Statement: If(IntLit(5),Block([]))"
        self.assertTrue(TestChecker.test(input, expect, 429))

    def test_type_mismatch_in_if_2(self):
        """Test 1"""
        input = """
        Class Program1{
            
            method(){
                If(5 > 4){

                }Elseif(78){}
            }
        }
            """
        expect = "Type Mismatch In Statement: If(IntLit(78),Block([]))"
        self.assertTrue(TestChecker.test(input, expect, 430))

    def test_type_mismatch_in_if_3(self):
        """Test 1"""
        input = """
        Class Program1{
            
            method(){
                If(5 > 4){
                    If(3+4){}

                }Elseif(6 < 3){}
                Else{}
            }
        }
            """
        expect = "Type Mismatch In Statement: If(BinaryOp(+,IntLit(3),IntLit(4)),Block([]))"
        self.assertTrue(TestChecker.test(input, expect, 431))

    def test_type_mismatch_in_if_4(self):
        """Test 1"""
        input = """
        Class Program1{
            
            method(){
                If(5 > 4){
                    If(3+4 > 9){}
                    Elseif("add" +. "dads"){}

                }Elseif(6 < 3){}
                Else{}
            }
        }
            """
        expect = "Type Mismatch In Statement: If(BinaryOp(+.,StringLit(add),StringLit(dads)),Block([]))"
        self.assertTrue(TestChecker.test(input, expect, 432))

    def test_type_mismatch_in_for_1(self):
        """Test 1"""
        input = """
        Class Program1{
            
            method(){
               Foreach(i In 4.6 .. 100 By 2){

                }
            }
        }
            """
        expect = "Type Mismatch In Statement: For(Id(i),FloatLit(4.6),IntLit(100),IntLit(2),Block([])])"
        self.assertTrue(TestChecker.test(input, expect, 433))

    def test_type_mismatch_in_for_2(self):
        """Test 1"""
        input = """
        Class Program1{
            
            method(){
               Foreach(i In 4 .. 10.01 By 2){

                }
            }
        }
            """
        expect = "Type Mismatch In Statement: For(Id(i),IntLit(4),FloatLit(10.01),IntLit(2),Block([])])"
        self.assertTrue(TestChecker.test(input, expect, 434))

    def test_type_mismatch_in_for_3(self):
        """Test 1"""
        input = """
        Class Program1{
            
            method(){
               Foreach(i In "4.87" .. 10.01 By 2){

                }
            }
        }
            """
        expect = "Type Mismatch In Statement: For(Id(i),StringLit(4.87),FloatLit(10.01),IntLit(2),Block([])])"
        self.assertTrue(TestChecker.test(input, expect, 435))

    def test_type_mismatch_in_stmt_assign_1(self):
        """Test 1"""
        input = """
         Class Program1{
            Val a: Int = 4;
            }
       Class Program2{
            method_re1(){
                Var pro: Program1 = New Program1();
                pro.a = 4;
              
            }
            }
            """
        expect = "Type Mismatch In Statement: For(Id(i),StringLit(4.87),FloatLit(10.01),IntLit(2),Block([])])"
        self.assertTrue(TestChecker.test(input, expect, 435))

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

    # def test_redeclared_method(self):
    #     """Simple program: int main() {} """
    #     input = """
    #     Class Proa{
    #         method(){
    #             Return 5;
    #         }
    #     }
    #     Class Pro{
    #         method(){
    #             Var a : Proa = New Proa();
    #             a.method();

    #         }
    #     }

    #            """
    #     expect = "Type Mismatch In Statement: Return(Id(c))"
    #     self.assertTrue(TestChecker.test(input, expect, 403))

    # def test_redeclared_method(self):
    #     """Simple program: int main() {} """
    #     input = """
    #     Class Proa{
    #         method(){

    #         }
    #     }
    #     Class Pro{
    #         method(){
    #             Var a : Proa = New Proa();
    #             Var c: Int;
    #             c = a.method();

    #         }
    #     }

    #            """
    #     expect = "Type Mismatch In Statement: CallExpr(Id(a),Id(method),[])"
    #     self.assertTrue(TestChecker.test(input, expect, 403))

    # def test_redeclared_method(self):
    #     """Simple program: int main() {} """
    #     input = """
    #     Class Proa{
    #         method(){

    #         }
    #     }
    #     Class Pro{
    #         method(){
    #             Val a : Float = False;

    #         }
    #     }
    # def test_redeclared_method(self):
    #     """Simple program: int main() {} """
    #     input = """
    #     Class Proa{
    #         method(){

    #         }
    #     }
    #     Class Pro{
    #         method(){
    #             Val a : Float = False;

    #         }
    #     }

    # def test_redeclared_method(self):
    #     """Simple program: int main() {} """
    #     input = """
    #     Class Proa{
    #         method(){

    #         }
    #     }
    #     Class Pro{

    #         method(){
    #             Foreach( i In 1 .. 100 ){
    #                     If(True){

    #                     }
    #             }

    #            Break;

    #         }
    #     }

    #            """
    #     expect = "Break Not In Loop"
    #     self.assertTrue(TestChecker.test(input, expect, 403))

    # def test_redeclared_method(self):
    #     """Simple program: int main() {} """
    #     input = """
    #     Class Proa{
    #         method(){

    #         }
    #     }
    #     Class Pro{

    #         method(){
    #             Val x: Int;
    #             Foreach( i In 1 .. 100 ){
    #                     If(True){

    #                     }
    #             }

    #         }
    #     }

    #            """
    #     expect = "Break Not In Loop"
    #     self.assertTrue(TestChecker.test(input, expect, 403))

    #            """
    #     expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(a),FloatType,BooleanLit(False))"
    #     self.assertTrue(TestChecker.test(input, expect, 403))

    #            """
    #     expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(a),FloatType,BooleanLit(False))"
    #     self.assertTrue(TestChecker.test(input, expect, 403))

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
