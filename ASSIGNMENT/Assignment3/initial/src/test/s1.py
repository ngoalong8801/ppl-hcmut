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
            Var a: Int;
            }
       Class Program2{
            method_re1(){
                Var pro: Program1 = New Program1();
                Var b: Float;
                pro.a = 4 +  b;

            }
            }
            """
        expect = "Type Mismatch In Statement: AssignStmt(FieldAccess(Id(pro),Id(a)),BinaryOp(+,IntLit(4),Id(b)))"
        self.assertTrue(TestChecker.test(input, expect, 436))

    # def test_type_mismatch_in_stmt_assign_2(self):
    #     """Test 1"""
    #     input = """
    #      Class Program1{
    #         Var a: Int;
    #         }
    #    Class Program2{
    #         method_re1(){
    #             Var pro: Program1 = New Program1();
    #             Var b: Float;
    #             pro.a = 4 +  b;

    #         }
    #         }
    #         """
    #     expect = "Type Mismatch In Statement: AssignStmt(FieldAccess(Id(pro),Id(a)),BinaryOp(+,IntLit(4),Id(b)))"
    #     self.assertTrue(TestChecker.test(input, expect, 437))

    # def test_type_mismatch_in_stmt_assign_3(self):
    #     """Test 1"""
    #     input = """
    #      Class Program1{
    #         Var a: Int;
    #         }
    #    Class Program2{
    #         method_re1(){
    #             Var pro: Program1 = New Program1();
    #             Var b: Float;
    #             pro.a = 4 +  b;

    #         }
    #         }
    #         """
    #     expect = "Type Mismatch In Statement: AssignStmt(FieldAccess(Id(pro),Id(a)),BinaryOp(+,IntLit(4),Id(b)))"
    #     self.assertTrue(TestChecker.test(input, expect, 438))

    def test_type_mismatch_in_stmt_call_1(self):
        """Test 40: E must be in class type;"""
        input = """
         Class Program1{
            test_meth(){

            }
            }
       Class Program2{
            method_re1(){
                Var pro: Program1 = New Program1();
                Var b: Float;
                b.test_meth();

            }
            }
            """
        expect = "Type Mismatch In Statement: Call(Id(b),Id(test_meth),[])"
        self.assertTrue(TestChecker.test(input, expect, 439))

    def test_type_mismatch_in_stmt_call_2(self):
        """Test 40: ; the callee must have void as return type;"""
        input = """
         Class Program1{
            test_meth(){
                    Return 4;
            }
            }
       Class Program2{
            method_re1(){
                Var pro: Program1 = New Program1();
                Var b: Float;
                pro.test_meth();

            }
            }
            """
        expect = "Type Mismatch In Statement: Call(Id(pro),Id(test_meth),[])"
        self.assertTrue(TestChecker.test(input, expect, 440))

    def test_type_mismatch_in_stmt_expr_arr_1(self):
        """Test 40: ; the callee must have void as return type;"""
        input = """

       Class TestArray{
            method_re1(){
                Var a: Array[Int, 4];
                Var b: Int;
                b[4] = 2;

            }
            }
            """
        expect = "Type Mismatch In Expression: ArrayCell(Id(b),[IntLit(4)])"
        self.assertTrue(TestChecker.test(input, expect, 441))

    def test_type_mismatch_in_stmt_expr_arr_2(self):
        """Test 40: ; the callee must have void as return type;"""
        input = """

       Class TestArray{
            method_re1(){
                Var a: Array[Int, 4];
                a[3.6] = 2;

            }
            }
            """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),[FloatLit(3.6)])"
        self.assertTrue(TestChecker.test(input, expect, 442))

    def test_type_mismatch_in_expr_binary_1(self):
        """Test 40: ; the callee must have void as return type;"""
        input = """

       Class TestArray{
            method_re1(){
                Var a: Float;
                a = 4 + "string";

            }
            }
            """
        expect = "Type Mismatch In Expression: BinaryOp(+,IntLit(4),StringLit(string))"
        self.assertTrue(TestChecker.test(input, expect, 443))

    def test_type_mismatch_in_expr_binary_2(self):
        """Test 40: ; the callee must have void as return type;"""
        input = """

       Class TestArray{
            method_re1(){
                Var a: Float;
                a = False && True || 4.5;

            }
            }
            """
        expect = "Type Mismatch In Expression: BinaryOp(||,BinaryOp(&&,BooleanLit(False),BooleanLit(True)),FloatLit(4.5))"
        self.assertTrue(TestChecker.test(input, expect, 444))

    def test_type_mismatch_in_expr_binary_3(self):
        """Test 40: ; the callee must have void as return type;"""
        input = """

       Class TestArray{
            method_re1(){
                Var a: Float;
                a = "string " != "string2";

            }
            }
            """
        expect = "Type Mismatch In Expression: BinaryOp(!=,StringLit(string ),StringLit(string2))"
        self.assertTrue(TestChecker.test(input, expect, 445))

    def test_type_mismatch_in_expr_binary_4(self):
        """Test 40: ; the callee must have void as return type;"""
        input = """

       Class TestArray{
            method_re1(){
                Var a: Float;
                If( ("a" +. "b" > "da")){}

            }
            }
            """
        expect = "Type Mismatch In Expression: BinaryOp(>,StringLit(b),StringLit(da))"
        self.assertTrue(TestChecker.test(input, expect, 446))

    def test_type_mismatch_in_expr_unary_1(self):
        """Test 40: ; the callee must have void as return type;"""
        input = """

       Class TestArray{
            method_re1(){
                Var a: Float;
                a = !(1.23);

            }
            }
            """
        expect = "Type Mismatch In Expression: UnaryOp(!,FloatLit(1.23))"
        self.assertTrue(TestChecker.test(input, expect, 446))

    def test_type_mismatch_in_expr_unary_2(self):
        """Test 40: ; the callee must have void as return type;"""
        input = """

       Class TestArray{
            method_re1(){
                Var a: Float;
                Var b: String;
                If(!(b +. "sda")){}

            }
            }
        Class Program{
            main(){

            }
        }
            """
        expect = "Type Mismatch In Expression: UnaryOp(!,BinaryOp(+.,Id(b),StringLit(sda)))"
        self.assertTrue(TestChecker.test(input, expect, 447))

    def test_type_mismatch_in_expr_unary_3(self):
        """Test 40: ; the callee must have void as return type;"""
        input = """

       Class TestArray{
            method_re1(){
                Var a: Float;
                Var b: String;
                If(-(b +. "sda")){}

            }
            }
        Class Program{
            main(){

            }
        }
            """
        expect = "Type Mismatch In Expression: UnaryOp(-,BinaryOp(+.,Id(b),StringLit(sda)))"
        self.assertTrue(TestChecker.test(input, expect, 448))

    def test_type_mismatch_in_expr_unary_4(self):
        """Test 40: ; the callee must have void as return type;"""
        input = """

       Class TestArray{
            method_re1(){
                Var a: Float;
                a = -((True || False) && False);

            }
            }
            """
        expect = "Type Mismatch In Expression: UnaryOp(-,BinaryOp(&&,BinaryOp(||,BooleanLit(True),BooleanLit(False)),BooleanLit(False)))"
        self.assertTrue(TestChecker.test(input, expect, 449))

    def test_type_mismatch_in_call_method_4(self):
        """Test 40: ; the callee must have void as return type;"""
        input = """

       Class Program{
           method(){
               Return 0;
           }
           main(){
               Var a : Int = Self.method(1,2);
           }
       }
            """
        expect = "Type Mismatch In Statement: CallExpr(Self(),Id(method),[IntLit(1),IntLit(2)])"
        self.assertTrue(TestChecker.test(input, expect, 450))

    # key 45 - 50

    def test_type_mismatch_in_expr_fildaccess_2(self):
        """Test 51: ; For an attribute access E.id, E must be in class type."""
        input = """
        Class Test{
            Var attr: Int;
        }
       Class TestAccess{
            method_re1(){
                Var test : Test = New Test();
                Var tet: Int;
                tet.attr = 4 + 6;

            }
            }
            """
        expect = "Type Mismatch In Expression: FieldAccess(Id(tet),Id(attr))"
        self.assertTrue(TestChecker.test(input, expect, 451))

    def test_type_mismatch_in_expr_fildaccess_2(self):
        """Test 51: ; For an attribute access E.id, E must be in class type."""
        input = """
        Class Test{
            Val attr: Float = True;
        }
       Class TestAccess{
           Var abc: Float;
            method_re1(){
                Self.ac = 5+ 5.6 * 7.9;

            }
            }
            """
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(attr),FloatType,BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 452))

    def test_break_not_in_loop_1(self):
        """Test 51: ; For an attribute access E.id, E must be in class type."""
        input = """
       Class Program{
           Var abc: Float;
            main(){
                Break;

            }
            }
            """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 453))

    def test_break_not_in_loop_2(self):
        """Test 51: ; For an attribute access E.id, E must be in class type."""
        input = """
       Class Program{
           Var abc: Float;
            main(){

                Foreach(i In 1 .. 100 ){
                    {
                        {
                            Break;
                        }
                    }
                }
                If(4 > 5){
                   Break;
                }

            }
            }
            """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 454))

    def test_continue_not_in_loop_1(self):
        """Test 51: ; For an attribute access E.id, E must be in class type."""
        input = """
       Class Program{
           Var abc: Float;
            main(){
                Continue;

            }
            }
            """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 453))

    def test_continue_not_in_loop_2(self):
        """Test 51: ; For an attribute access E.id, E must be in class type."""
        input = """
       Class Program{
           Var abc: Float;
            main(){

                Foreach(i In 1 .. 100 ){
                    {
                        {
                            Continue;
                        }
                    }
                }
                If(4 > 5){
                   Continue;
                }

            }
            }
            """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 454))

    def test_illegal_constant_expr_1(self):
        """Test 51: ; For an attribute access E.id, E must be in class type."""
        input = """
       Class Program{
           Val abc: Int;
            main(){
                Continue;

            }
            }
            """
        expect = "Illegal Constant Expression: None"
        self.assertTrue(TestChecker.test(input, expect, 455))

    def test_illegal_constant_expr_2(self):
        """Test 51: ; For an attribute access E.id, E must be in class type."""
        input = """
       Class Program{

            main(){
                Val x: Float;

            }
            }
            """
        expect = "Illegal Constant Expression: None"
        self.assertTrue(TestChecker.test(input, expect, 456))

    def test_illegal_constant_expr_2(self):
        """ its operands must be a literal or an immutable attribute"""
        input = """
       Class Program{

            main(){
                Val x: Float = 4.6;
                Var a: Int;
                Val ax : Float = 1 + a;

            }
            }
            """
        expect = "Illegal Constant Expression: BinaryOp(+,IntLit(1),Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 457))

    def test_illegal_array_literal_1(self):
        """ its operands must be a literal or an immutable attribute"""
        input = """
       Class Program{

            main(){
                Var a: Array[Int, 3];
                a = Array(1, 2, True);

            }
            }
            """
        expect = "Illegal Array Literal: [IntLit(1),IntLit(2),BooleanLit(True)]"
        self.assertTrue(TestChecker.test(input, expect, 458))

    def test_illegal_array_literal_2(self):
        """ its operands must be a literal or an immutable attribute"""
        input = """
       Class Program{

            main(){
                Var a: Array[Int, 3];
                a = Array("123", 2, True);

            }
            }
            """
        expect = "Illegal Array Literal: [StringLit(123),IntLit(2),BooleanLit(True)]"
        self.assertTrue(TestChecker.test(input, expect, 459))

    def test_type_mismathch_stmt__arr1(self):
        """ its operands must be a literal or an immutable attribute"""
        input = """
       Class Program{

            main(){
                Var a: Array[Int, 3];
                a = Array(1,2,3,4);

            }
            }
            """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a),[IntLit(1),IntLit(2),IntLit(3),IntLit(4)])"
        self.assertTrue(TestChecker.test(input, expect, 460))

    def test_type_mismathch_stmt__arr2(self):
        """ its operands must be a literal or an immutable attribute"""
        input = """
       Class Program{

            main(){
                Var a: Array[Int, 3];
                a = Array(1,2);

            }
            }
            """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a),[IntLit(1),IntLit(2)])"
        self.assertTrue(TestChecker.test(input, expect, 461))

    def test_type_mismathch_stmt__arr2(self):
        """ its operands must be a literal or an immutable attribute"""
        input = """
       Class Program{

            main(){
                Var a: Array[Int, 3];
                a = Array(1.5,2.8, 3.9);

            }
            }
            """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a),[FloatLit(1.5),FloatLit(2.8),FloatLit(3.9)])"
        self.assertTrue(TestChecker.test(input, expect, 462))

    def test_type_mismathch_stmt__arr3(self):
        """ its operands must be a literal or an immutable attribute"""
        input = """
       Class Program{

            main(){
                Var a: Array[String, 2];
                a = Array(True, False);

            }
            }
            """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a),[BooleanLit(True),BooleanLit(False)])"
        self.assertTrue(TestChecker.test(input, expect, 463))

    def test_illegal_member_access_1(self):
        """ its operands must be a literal or an immutable attribute"""
        input = """
       Class A{
        test(a,b : Float){Return 0;}
        Var a: Int = Self.test(1, 2); ## *2 ##
        }
        Class Program{
            main(){
                Var a : Int= A.a;
            }
            }
            """
        expect = "Illegal Member Access: FieldAccess(Id(A),Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 464))

    def test_new_expr_1(self):
        """ its operands must be a literal or an immutable attribute"""
        input = """
       Class A{
        test(a,b : Float){Return 0;}
        Var a: Int = Self.test(1, 2); ## *2 ##
        }
        Class Program{
            main(){
                Var a :A= New A(1,2);
            }
            }
            """
        expect = "Type Mismatch In Statement: NewExpr(Id(A),[IntLit(1),IntLit(2)])"
        self.assertTrue(TestChecker.test(input, expect, 464))

    def test_new_expr_2(self):
        """ its operands must be a literal or an immutable attribute"""
        input = """
       Class A{
        test(a,b : Float){Return 0;}
        Var a: Int = Self.test(1, 2); ## *2 ##
        Constructor(){ }
        }
        Class Program{
            main(){
                Var a :A= New A(1,2);
            }
            }
            """
        expect = "Type Mismatch In Statement: NewExpr(Id(A),[IntLit(1),IntLit(2)])"
        self.assertTrue(TestChecker.test(input, expect, 465))

    def test_new_expr_3(self):
        """ its operands must be a literal or an immutable attribute"""
        input = """
       Class A{
        test(a,b : Float){Return 0;}
        Var a: Int = Self.test(1, 2); ## *2 ##
        Constructor(a, b: Int){ }
        }
        Class Program{
            main(){
                Var a :A= New A(1,2.5);
            }
            }
            """
        expect = "Type Mismatch In Statement: NewExpr(Id(A),[IntLit(1),FloatLit(2.5)])"
        self.assertTrue(TestChecker.test(input, expect, 466))

    def test_new_expr_4(self):
        """ its operands must be a literal or an immutable attribute"""
        input = """
       Class A{
        test(a,b : Float){Return 0;}
        Var a: Int = Self.test(1, 2); ## *2 ##
        Constructor(a, b: Int){ }
        }
        Class Program{
            main(){
                Var a :A= New A(1,2, 3);
            }
            }
            """
        expect = "Type Mismatch In Statement: NewExpr(Id(A),[IntLit(1),IntLit(2),IntLit(3)])"
        self.assertTrue(TestChecker.test(input, expect, 467))

    def test_no_entry_point_1(self):
        """ its operands must be a literal or an immutable attribute"""
        input = """
       Class A{
        test(a,b : Float){Return 0;}
        Var a: Int = Self.test(1, 2); ## *2 ##
        Constructor(a, b: Int){ }
        }
            """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 468))

    def test_no_entry_point_2(self):
        """ its operands must be a literal or an immutable attribute"""
        input = """
       Class A{
        test(a,b : Float){Return 0;}
        Var a: Int = Self.test(1, 2); ## *2 ##
        Constructor(a, b: Int){ }
        }
        Class Program{
            main1(){

            }
        }
            """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 469))

    def test_no_entry_point_3(self):
        """ its operands must be a literal or an immutable attribute"""
        input = """
       Class A{
        test(a,b : Float){Return 0;}
        Var a: Int = Self.test(1, 2); ## *2 ##
        Constructor(a, b: Int){ }
        }
        Class Program{
            main(a, b: Int){

            }
        }
            """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 470))

    def test_type_mis_match_para_argu_stmt_1(self):
        """ its operands must be a literal or an immutable attribute"""
        input = """
       Class A{
        test(a,b : Float){}
        Var a: Int = Self.test(1, 2); ## *2 ##
        }
        Class Program{
            main(){
                Var a : A = New A();
                a.test();
            }
        }
            """
        expect = "Type Mismatch In Statement: CallExpr(Self(),Id(test),[IntLit(1),IntLit(2)])"
        self.assertTrue(TestChecker.test(input, expect, 471))

    def test_type_mis_match_para_argu_stmt_2(self):
        """ its operands must be a literal or an immutable attribute"""
        input = """
       Class A{
        test(){}

        }
        Class Program{
            main(){
                Var a : A = New A();
                a.test(1,2);
            }
        }
            """
        expect = "Type Mismatch In Statement: Call(Id(a),Id(test),[IntLit(1),IntLit(2)])"
        self.assertTrue(TestChecker.test(input, expect, 472))

    def test_type_mis_match_para_argu_stmt_3(self):
        """ its operands must be a literal or an immutable attribute"""
        input = """
       Class A{
        test(a, b: Int; c: Boolean){}

        }
        Class Program{
            main(){
                Var a : A = New A();
                a.test(1,2,True);
                a.test(1,2, 3);
            }
        }
            """
        expect = "Type Mismatch In Statement: Call(Id(a),Id(test),[IntLit(1),IntLit(2),IntLit(3)])"
        self.assertTrue(TestChecker.test(input, expect, 473))

    def test_undecl_var_block_stmt_1(self):
        input = """
        Class Program {
            main() {
                {
                    Var inLopp : Int = 78;
                }
                inLopp = 40;
            }
        }
        """
        expect = "Undeclared Identifier: inLoop"
        self.assertTrue(TestChecker.test(input, expect, 474))

    def test_undecl_var_block_stmt_2(self):
        input = """
        Class Program {
            main() {
                {
                    {
                        Var inLopp : Int = 78;
                    }
                    inLopp = 40;
                }
                
            }
        }
        """
        expect = "Undeclared Identifier: inLoop"
        self.assertTrue(TestChecker.test(input, expect, 475))

    def test_array_cell_1(self):
        input = """
        Class Program {
            main() {
                Var arr: Array[Int, 5] = Array(1, 3, 5, 7, 9);
                arr[3] = 145.65;
            }
        }
        """
        expect = "Type Mismatch In Statement: AssignStmt(ArrayCell(Id(arr),[IntLit(1)]),FloatLit(12.5))"
        self.assertTrue(TestChecker.test(input, expect, 476))

    # def test_illegal_constant_expr(self):
    #     input = """
    #     Class Program {
    #         main() {
    #             Var a : Int;
    #             Val b : Int = a;
    #         }
    #     }
    #     """
    #     expect = "Illegal Constant Expression: Id(a)"
    #     self.assertTrue(TestChecker.test(input, expect, 413))

    # def test_illegal_constant_expr2(self):
    #     input = """
    #     Class Program {
    #         main() {
    #             Var a : Int;
    #             Val b : Int = - a;
    #         }
    #     }
    #     """
    #     expect = "Illegal Constant Expression: Id(a)"
    #     self.assertTrue(TestChecker.test(input,expect,414))

    # def test_type_mismatch_of_unary(self):
    #     input = """
    #     Class Program {
    #         main() {
    #             Var a : Int;
    #             a = - "2";
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: UnaryOp(-,StringLit(2))"
    #     self.assertTrue(TestChecker.test(input,expect,415))

    # def test_type_mismatch_of_unary_bool(self):
    #     input = """
    #     Class Program {
    #         main() {
    #             Var a : Boolean;
    #             a = ! (12);
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: UnaryOp(!,IntLit(12))"
    #     self.assertTrue(TestChecker.test(input,expect,416))

    # def test_binary_op(self):
    #     input = """
    #     Class Program {
    #         main() {
    #             Var a : Int;
    #             a = a + "haha";
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: BinaryOp(+,Id(a),StringLit(haha))"
    #     self.assertTrue(TestChecker.test(input,expect,417))

    # def test_binary_op_devide(self):
    #     input = """
    #     Class Program {
    #         main() {
    #             Var result : Int;
    #             result = 4 / 2;
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: AssignStmt(Id(result),BinaryOp(/,IntLit(4),IntLit(2)))"
    #     self.assertTrue(TestChecker.test(input,expect,418))

    # def test_binary_op_percent(self):
    #     input = """
    #     Class Program {
    #         main() {
    #             Var result : Int;
    #             result = 4 % 2.0;
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: BinaryOp(%,IntLit(4),FloatLit(2.0))"
    #     self.assertTrue(TestChecker.test(input,expect,419))

    # def test_binary_op_compare(self):
    #     input = """
    #     Class Program {
    #         main() {
    #             Var result : Int;
    #             result = 4 >= 2;
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: AssignStmt(Id(result),BinaryOp(>=,IntLit(4),IntLit(2)))"
    #     self.assertTrue(TestChecker.test(input,expect,420))

    # def test_binary_op_compare_diff_type(self):
    #     input = """
    #     Class Program {
    #         main() {
    #             Var result : Boolean;
    #             result = (12 > "good");
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: BinaryOp(>,IntLit(12),StringLit(good))"
    #     self.assertTrue(TestChecker.test(input,expect,421))

    # def test_binary_op_and(self): #?
    #     input = """
    #     Class Program {
    #         main() {
    #             Var result : Boolean;
    #             result = True && 2;
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: BinaryOp(&&,BooleanLit(True),IntLit(2))"
    #     self.assertTrue(TestChecker.test(input,expect,422))

    # def test_binary_op_string_compare(self):
    #     input = """
    #     Class Program {
    #         main() {
    #             Var result : Boolean;
    #             result = "haha" ==. 2;
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: BinaryOp(==.,StringLit(haha),IntLit(2))"
    #     self.assertTrue(TestChecker.test(input,expect,423))

    # def test_binary_op_string_concat(self):
    #     input = """
    #     Class Program {
    #         main() {
    #             Var result : Int;
    #             result = "haha" +. "hehe";
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: AssignStmt(Id(result),BinaryOp(+.,StringLit(haha),StringLit(hehe)))"
    #     self.assertTrue(TestChecker.test(input,expect,424))

    # def test_if_stmt(self): #?
    #     input = """
    #     Class Program {
    #         main() {
    #             Var a : Int = 1;
    #             Var b : Int = 2;

    #             If (1) {
    #                 a = a + 1;
    #             }
    #             Else {
    #                 a = a - 1;
    #             }
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: If(IntLit(1),Block([AssignStmt(Id(a),BinaryOp(+,Id(a),IntLit(1)))]),Block([AssignStmt(Id(a),BinaryOp(-,Id(a),IntLit(1)))]))"
    #     self.assertTrue(TestChecker.test(input,expect,425))

    # def test_if_stmt2(self): #?
    #     input = """
    #     Class Program {
    #         main() {
    #             Var a : Int = 1;
    #             Var b : Int = 2;

    #             If (a > b) {
    #                 Var c : Int = 1;
    #                 a = a + c;
    #             }
    #             Else {
    #                 a = a - 1;
    #                 a = a + c;
    #             }
    #         }
    #     }
    #     """
    #     expect = "Undeclared Identifier: c"
    #     self.assertTrue(TestChecker.test(input,expect,426))

    # def test_for_stmt(self):
    #     input = """
    #     Class Program {
    #         main() {
    #             Var b : Int = 0;
    #             Foreach (a In 1 .. 100 By 2) {
    #                     a = a + 3;
    #             }
    #         }
    #     }
    #     """
    #     expect = "Undeclared Identifier: a"
    #     self.assertTrue(TestChecker.test(input,expect,427))

    # def test_for_stmt2(self):
    #     input = """
    #     Class Program {
    #         main() {
    #             Var a, b : Int = 0, 0;
    #             Foreach (a In 1.5 .. 100 By 2) {
    #                     b = b + 3;
    #             }
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: For(Id(a),FloatLit(1.5),IntLit(100),IntLit(2),Block([AssignStmt(Id(b),BinaryOp(+,Id(b),IntLit(3)))])])"
    #     self.assertTrue(TestChecker.test(input,expect,428))

    # def test_for_stmt3(self):
    #     input = """
    #     Class Program {
    #         main() {
    #             Var a, b : Int = 0, 0;
    #             Foreach (a In 1 .. 100 By 2.5) {
    #                     b = b + 3;
    #             }
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: For(Id(a),IntLit(1),IntLit(100),FloatLit(2.5),Block([AssignStmt(Id(b),BinaryOp(+,Id(b),IntLit(3)))])])"
    #     self.assertTrue(TestChecker.test(input,expect,429))

    # def test_break_not_in_loop(self):
    #     input = """
    #     Class Program {
    #         main() {
    #             Var a, b : Int = 0, 0;
    #             Break;
    #             Foreach (a In 1 .. 100 By 2) {
    #                     b = b + 3;
    #             }
    #         }
    #     }
    #     """
    #     expect = "Break Not In Loop"
    #     self.assertTrue(TestChecker.test(input,expect,430))

    # def test_continue_not_in_loop(self):
    #     input = """
    #     Class Program {
    #         main() {
    #             Var a, b : Int = 0, 0;
    #             Foreach (a In 1 .. 100 By 2) {
    #                     b = b + 3;
    #                     Break;
    #             }
    #             Continue;
    #         }
    #     }
    #     """
    #     expect = "Continue Not In Loop"
    #     self.assertTrue(TestChecker.test(input,expect,431))

    # def test_array_cell(self):
    #     input = """
    #     Class Program {
    #         main() {
    #             Var arr: Array[Int, 5] = Array(1, 3, 5, 7, 9);
    #             arr[1] = 12.5;
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: AssignStmt(ArrayCell(Id(arr),[IntLit(1)]),FloatLit(12.5))"
    #     self.assertTrue(TestChecker.test(input,expect,432))

    # def test_array_cell2(self): # check
    #     input = """
    #     Class Program {
    #         main() {
    #             Var arr: Array[Int, 5] = Array(1, 3, 5, 7, 9);
    #             arr[1] = arr[2] * 2.0;
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: AssignStmt(ArrayCell(Id(arr),[IntLit(1)]),BinaryOp(*,ArrayCell(Id(arr),[IntLit(2)]),FloatLit(2.0)))"
    #     self.assertTrue(TestChecker.test(input,expect,433))

    # def test_array_cell3(self): #?
    #     input = """
    #     Class Program {
    #         main() {
    #             Var arr: Array[Int, 5] = Array(1, 3, 5, 7, 9);
    #             arr[1][2.5] = 12;
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: ArrayCell(Id(arr),[IntLit(1),FloatLit(2.5)])"
    #     self.assertTrue(TestChecker.test(input,expect,434))

    # def test_array_cell4(self):
    #     input = """
    #     Class Program {
    #         main() {
    #             Var a: Int = 1;
    #             a[0] = 12;
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: ArrayCell(Id(a),[IntLit(0)])"
    #     self.assertTrue(TestChecker.test(input,expect,435))

    # def test_new_expr(self):
    #     input = """
    #     Class Program {
    #         main() {
    #             Var a: myClass = New Ast();
    #         }
    #     }
    #     Class myClass {
    #         main() {

    #         }
    #     }
    #     """
    #     expect = "Undeclared Class: Ast"
    #     self.assertTrue(TestChecker.test(input,expect,436))

    # def test_new_expr2(self): # ?
    #     input = """
    #     Class Program {
    #         main() {
    #             Var a: Test;
    #         }
    #     }
    #     Class myClass {
    #         main() {

    #         }
    #     }
    #     """
    #     expect = "Undeclared Class: Test"
    #     self.assertTrue(TestChecker.test(input,expect,437))

    # def test_constructor(self):
    #     input = """
    #     Class Program {
    #         main() {
    #             Var a: myClass = New myClass(1, 2);
    #         }
    #     }
    #     Class myClass {
    #         main() {

    #         }
    #     }
    #     """
    #     expect = "Undeclared Method: Constructor"
    #     self.assertTrue(TestChecker.test(input,expect,438))

    # def test_constructor2(self):
    #     input = """
    #     Class Program {
    #         main() {
    #             Var a: myClass = New myClass(1, 2);
    #         }
    #     }
    #     Class myClass {
    #         Constructor(a, b, c: Int) {

    #         }
    #         main() {

    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: NewExpr(Id(myClass),[IntLit(1),IntLit(2)])"
    #     self.assertTrue(TestChecker.test(input,expect,439))

    # def test_constructor3(self):
    #     input = """
    #     Class Program {
    #         main() {
    #             Var a: myClass = New myClass(1, 2.5);
    #         }
    #     }
    #     Class myClass {
    #         Constructor(a, b: Int) {

    #         }
    #         main() {

    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: NewExpr(Id(myClass),[IntLit(1),FloatLit(2.5)])"
    #     self.assertTrue(TestChecker.test(input,expect,440))

    # def test_fieldAccess_self(self):
    #     input = """
    #     Class Program {
    #         Var a: Int = 1;
    #         main() {
    #             Var b: Int;
    #             b = Self.c;
    #         }
    #     }
    #     """
    #     expect = "Undeclared Attribute: c"
    #     self.assertTrue(TestChecker.test(input,expect,441))

    # def test_fieldAccess(self):
    #     input = """
    #     Class Program {
    #         Var a: Int = 1;
    #         main() {
    #             Var obj: myClass = New myClass();
    #             Var b: Int;
    #             b = obj.d;
    #         }
    #     }
    #     Class myClass {
    #         Var c: Int = 1;
    #     }
    #     """
    #     expect = "Undeclared Attribute: d"
    #     self.assertTrue(TestChecker.test(input,expect,442))

    # def test_fieldAccess2(self):
    #     input = """
    #     Class Program {
    #         Var a: Int = 1;
    #         main() {
    #             Var obj: myClass = New myClass();
    #             Var b: Int;
    #             b = abc.c;
    #         }
    #     }
    #     Class myClass {
    #         Var c: Int = 1;
    #     }
    #     """
    #     expect = "Undeclared Class: abc"
    #     self.assertTrue(TestChecker.test(input,expect,443))

    # def test_return_stmt(self):
    #     input = """
    #     Class Program {
    #         main() {
    #             Var a: Int = 1;
    #             Return b;
    #         }
    #     }
    #     """
    #     expect = "Undeclared Identifier: b"
    #     self.assertTrue(TestChecker.test(input,expect,444))

    # def test_return_stmt2(self): # use Self
    #     input = """
    #     Class Program {
    #         Var a: Int = 1;
    #         main() {
    #             Var b: Int = 1;
    #             Return a;
    #         }
    #     }
    #     """
    #     expect = "Undeclared Identifier: a"
    #     self.assertTrue(TestChecker.test(input,expect,445))

    # def test_return_stmt2(self):
    #     input = """
    #     Class Program {
    #         Val $numOfShape: Int = 0;
    #         main() {

    #         }
    #         $getNumOfShape() {
    #             Return mud::$numOfShape;
    #         }
    #     }
    #     """
    #     expect = "Undeclared Class: mud"
    #     self.assertTrue(TestChecker.test(input,expect,446))

    # def test_return_stmt3(self): # chua fixxx
    #     input = """
    #     Class Program {
    #         Val $numOfShape: Int = 0;
    #         main() {

    #         }
    #         $getNumOfShape() {
    #             Return $numOfShape;
    #         }
    #     }
    #     """
    #     expect = "Undeclared Identifier: $numOfShape"
    #     self.assertTrue(TestChecker.test(input,expect,447))

    # def test_callExpr(self):
    #     input = """
    #     Class Program {
    #         main() {
    #             Return Program::$getName();
    #         }
    #         $getNumOfShape() {
    #             Return 2;
    #         }
    #     }
    #     """
    #     expect = "Undeclared Method: $getName"
    #     self.assertTrue(TestChecker.test(input,expect,448))

    # def test_callExpr2(self):
    #     input = """
    #     Class Program {
    #         main() {
    #             Return Program::$getSum();
    #         }
    #         $getSum(a, b: Int) {
    #             Return a + b;
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: CallExpr(Id(Program),Id($getSum),[])"
    #     self.assertTrue(TestChecker.test(input,expect,449))

    # def test_callExpr3(self):
    #     input = """
    #     Class Program {
    #         main() {
    #             Return Program::$getSum(1, 2.5);
    #         }
    #         $getSum(a, b: Int) {
    #             Return a + b;
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: CallExpr(Id(Program),Id($getSum),[IntLit(1),FloatLit(2.5)])"
    #     self.assertTrue(TestChecker.test(input,expect,450))

    # def test_callExpr4(self):
    #     input = """
    #     Class Program {
    #         main() {
    #             Return myClass::$getAdd(1, 2);
    #         }
    #     }
    #     Class myClass {
    #         main() {

    #         }
    #         $getSum(a, b: Int) {
    #             Return a + b;
    #         }
    #     }
    #     """
    #     expect = "Undeclared Method: $getAdd"
    #     self.assertTrue(TestChecker.test(input,expect,451))

    # def test_var_type_decl(self): # chua check
    #     input = """
    #     Class Program {
    #         Var a: Int = 13.5;
    #         main() {

    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Constant Declaration: VarDecl(Id(a),IntType,FloatLit(13.5))"
    #     self.assertTrue(TestChecker.test(input,expect,452))

    # def test_var_type_decl2(self):
    #     input = """
    #     Class Program {
    #         main() {
    #             Var a: String = 54;
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Constant Declaration: VarDecl(Id(a),StringType,IntLit(54))"
    #     self.assertTrue(TestChecker.test(input,expect,453))

    # def test_callStmt(self):
    #     input = """
    #     Class myClass {
    #         main() {

    #         }
    #         $printName() {

    #         }
    #     }
    #     Class Program {
    #         main() {
    #             Var obj: myClass = New myClass();
    #             myObj::$printName();
    #         }
    #     }
    #     """
    #     expect = "Undeclared Class: myObj"
    #     self.assertTrue(TestChecker.test(input,expect,454))

    # def test_callStmt2(self):
    #     input = """
    #     Class myClass {
    #         main() {

    #         }
    #         $printName() {

    #         }
    #     }
    #     Class Program {
    #         main() {
    #             Var obj: myClass = New myClass();
    #             obj::$printSum();
    #         }
    #     }
    #     """
    #     expect = "Undeclared Method: $printSum"
    #     self.assertTrue(TestChecker.test(input,expect,455))

    # def test_no_entry_point2(self):
    #     input = """
    #     Class myClass {
    #         main() {

    #         }
    #     }
    #     Class Program {

    #     }
    #     """
    #     expect = "No Entry Point"
    #     self.assertTrue(TestChecker.test(input,expect,456))

    # def test_no_entry_point3(self): # not real main
    #     input = """
    #     Class Program {
    #         main(a, b: Int) {

    #         }
    #     }
    #     """
    #     expect = "No Entry Point"
    #     self.assertTrue(TestChecker.test(input,expect,457))

    # def test_class_inherit_class(self):
    #     input = """
    #     Class myClass: myClass {
    #         main() {

    #         }
    #     }
    #     """
    #     expect = "Undeclared Class: myClass"
    #     self.assertTrue(TestChecker.test(input,expect,458))

    # def test_member_access(self):
    #     input = """
    #     Class E {
    #         Var a : Int;
    #         main() {

    #         }
    #     }
    #     Class Program {
    #         main() {
    #                 Var b : Int = E.a;
    #         }
    #     }
    #     """
    #     expect = "Illegal Member Access: FieldAccess(Id(E),Id(a))"
    #     self.assertTrue(TestChecker.test(input,expect,459))

    # def test_array_decl(self):
    #     input = """
    #     Class Program {
    #         Var a: Array[Int, 1] = Array(1, 2, 3, 4);
    #         main() {

    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Constant Declaration: VarDecl(Id(a),ArrayType(1,IntType),[IntLit(1),IntLit(2),IntLit(3),IntLit(4)])"
    #     self.assertTrue(TestChecker.test(input,expect,460))

    # def test_array_decl2(self):
    #     input = """
    #     Class Program {
    #         Var a: Array[Int, 1] = Array(True);
    #         main() {

    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Constant Declaration: VarDecl(Id(a),ArrayType(1,IntType),[BooleanLit(True)])"
    #     self.assertTrue(TestChecker.test(input,expect,461))

    # def test_for_stmt4(self):
    #     input = """
    #     Class A {
    #         main() {

    #         }
    #         foo() {
    #             Val x : Int = 10;
    #             Foreach(x In 1 .. 100 By 1)
    #             {

    #             }
    #         }
    #     }
    #     """
    #     expect = "Cannot Assign To Constant: AssignStmt(Id(x),IntLit(1))"
    #     self.assertTrue(TestChecker.test(input,expect,462))
