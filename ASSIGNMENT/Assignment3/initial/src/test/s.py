import unittest
from TestUtils import TestChecker
from AST import *


class CheckerSuite(unittest.TestCase):
    def test_no_entry_point(self):
        input = """Class myClass {
            myFun() { }
        }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 400))

    def test_redecl_class(self):
        input = """
        Class myClass {
            main() { }
        }
        Class myClass {
            main() { }
        }"""
        expect = "Redeclared Class: myClass"
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test_redecl_func(self):
        input = """Class myClass {
            main() { }
            getName() { }
            getName() { }
        }"""
        expect = "Redeclared Method: getName"
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test_redecl_var(self):
        input = """Class myClass {
            Var a, a: Int;
            main() { }
        }"""
        expect = "Redeclared Attribute: a"
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_redeclare_param(self):
        input = """Class myClass {
            main(a, b, a: Int) { }
        }"""
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test_redeclare_var_inside_method(self):
        input = """
        Class myClass {
            main(a, b: Int) {
                Var a : Int;
            }
        }"""
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_assign_stmt(self):
        input = """
        Class Program {
            main(a, b: Int) {
                c = 2;
            }
        }"""
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input, expect, 406))

    def test_redeclare_const_stmt(self):
        input = """
        Class Program {
            main(a, b: Int) {
                Var d, c : Int;
                Val c : Float = 2.0;
            }
        }"""
        expect = "Redeclared Constant: c"
        self.assertTrue(TestChecker.test(input, expect, 407))

    def test_undeclare_class_parent(self):
        input = """
        Class Program: myClass {
            
        }
        """
        expect = "Undeclared Class: myClass"
        self.assertTrue(TestChecker.test(input, expect, 408))

    def test_cannot_assign_to_constant(self):
        input = """
        Class Program {
            main() {
                Val a : Int = 2;
                a = 3;
            }
        }
        """
        expect = "Cannot Assign To Constant: AssignStmt(Id(a),IntLit(3))"
        self.assertTrue(TestChecker.test(input, expect, 409))

    def test_type_mismatch_in_constant(self):
        input = """
        Class Program {
            main() {
                Val a : Int = 2.5;
            }
        }
        """
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(a),IntType,FloatLit(2.5))"
        self.assertTrue(TestChecker.test(input, expect, 410))

    def test_type_mismatch_in_constant2(self):
        input = """
        Class Program {
            main() {
                Val a : Float = "2.5";
            }
        }
        """
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(a),FloatType,StringLit(2.5))"
        self.assertTrue(TestChecker.test(input, expect, 411))

    def test_undecl_var_block_stmt(self):
        input = """
        Class Program {
            main() {
                {
                    Var a : Int;
                }
                a = 12;
            }
        }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test_illegal_constant_expr(self):
        input = """
        Class Program {
            main() {
                Var a : Int;
                Val b : Int = a;
            }
        }
        """
        expect = "Illegal Constant Expression: Id(a)"
        self.assertTrue(TestChecker.test(input, expect, 413))

    def test_illegal_constant_expr2(self):
        input = """
        Class Program {
            main() {
                Var a : Int;
                Val b : Int = - a;
            }
        }
        """
        expect = "Illegal Constant Expression: Id(a)"
        self.assertTrue(TestChecker.test(input, expect, 414))

    def test_type_mismatch_of_unary(self):
        input = """
        Class Program {
            main() {
                Var a : Int;
                a = - "2";
            }
        }
        """
        expect = "Type Mismatch In Expression: UnaryOp(-,StringLit(2))"
        self.assertTrue(TestChecker.test(input, expect, 415))

    def test_type_mismatch_of_unary_bool(self):
        input = """
        Class Program {
            main() {
                Var a : Boolean;
                a = ! (12);
            }
        }
        """
        expect = "Type Mismatch In Expression: UnaryOp(!,IntLit(12))"
        self.assertTrue(TestChecker.test(input, expect, 416))

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
    #     self.assertTrue(TestChecker.test(input, expect, 417))

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
    #     self.assertTrue(TestChecker.test(input, expect, 418))

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
    #     self.assertTrue(TestChecker.test(input, expect, 419))

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
    #     self.assertTrue(TestChecker.test(input, expect, 420))

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
    #     self.assertTrue(TestChecker.test(input, expect, 421))

    # def test_binary_op_and(self):  # ?
    #     input = """
    #     Class Program {
    #         main() {
    #             Var result : Boolean;
    #             result = True && 2;
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: BinaryOp(&&,BooleanLit(True),IntLit(2))"
    #     self.assertTrue(TestChecker.test(input, expect, 422))

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
    #     self.assertTrue(TestChecker.test(input, expect, 423))

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
    #     self.assertTrue(TestChecker.test(input, expect, 424))

    # def test_if_stmt(self):  # ?
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
    #     self.assertTrue(TestChecker.test(input, expect, 425))

    # def test_if_stmt2(self):  # ?
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
    #     self.assertTrue(TestChecker.test(input, expect, 426))

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
    #     self.assertTrue(TestChecker.test(input, expect, 427))

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
    #     self.assertTrue(TestChecker.test(input, expect, 428))

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
    #     self.assertTrue(TestChecker.test(input, expect, 429))

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
    #     self.assertTrue(TestChecker.test(input, expect, 430))

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
    #     self.assertTrue(TestChecker.test(input, expect, 431))

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
    #     self.assertTrue(TestChecker.test(input, expect, 432))

    # def test_array_cell2(self):  # check
    #     input = """
    #     Class Program {
    #         main() {
    #             Var arr: Array[Int, 5] = Array(1, 3, 5, 7, 9);
    #             arr[1] = arr[2] * 2.0;
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: AssignStmt(ArrayCell(Id(arr),[IntLit(1)]),BinaryOp(*,ArrayCell(Id(arr),[IntLit(2)]),FloatLit(2.0)))"
    #     self.assertTrue(TestChecker.test(input, expect, 433))

    # def test_array_cell3(self):  # ?
    #     input = """
    #     Class Program {
    #         main() {
    #             Var arr: Array[Int, 5] = Array(1, 3, 5, 7, 9);
    #             arr[1][2.5] = 12;
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: ArrayCell(Id(arr),[IntLit(1),FloatLit(2.5)])"
    #     self.assertTrue(TestChecker.test(input, expect, 434))

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
    #     self.assertTrue(TestChecker.test(input, expect, 435))

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
    #     self.assertTrue(TestChecker.test(input, expect, 436))

    # def test_new_expr2(self):  # ?
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
    #     self.assertTrue(TestChecker.test(input, expect, 437))

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
    #     self.assertTrue(TestChecker.test(input, expect, 438))

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
    #     self.assertTrue(TestChecker.test(input, expect, 439))

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
    #     self.assertTrue(TestChecker.test(input, expect, 440))

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
    #     self.assertTrue(TestChecker.test(input, expect, 441))

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
    #     self.assertTrue(TestChecker.test(input, expect, 442))

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
    #     self.assertTrue(TestChecker.test(input, expect, 443))

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
    #     self.assertTrue(TestChecker.test(input, expect, 444))

    # def test_return_stmt2(self):  # use Self
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
    #     self.assertTrue(TestChecker.test(input, expect, 445))

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
    #     self.assertTrue(TestChecker.test(input, expect, 446))

    # def test_return_stmt3(self):  # chua fixxx
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
    #     self.assertTrue(TestChecker.test(input, expect, 447))

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
    #     self.assertTrue(TestChecker.test(input, expect, 448))

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
    #     self.assertTrue(TestChecker.test(input, expect, 449))

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
    #     self.assertTrue(TestChecker.test(input, expect, 450))

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
    #     self.assertTrue(TestChecker.test(input, expect, 451))

    # def test_var_type_decl(self):  # chua check
    #     input = """
    #     Class Program {
    #         Var a: Int = 13.5;
    #         main() {

    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Constant Declaration: VarDecl(Id(a),IntType,FloatLit(13.5))"
    #     self.assertTrue(TestChecker.test(input, expect, 452))

    # def test_var_type_decl2(self):
    #     input = """
    #     Class Program {
    #         main() {
    #             Var a: String = 54;
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Constant Declaration: VarDecl(Id(a),StringType,IntLit(54))"
    #     self.assertTrue(TestChecker.test(input, expect, 453))

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
    #     self.assertTrue(TestChecker.test(input, expect, 454))

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
    #     self.assertTrue(TestChecker.test(input, expect, 455))

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
    #     self.assertTrue(TestChecker.test(input, expect, 456))

    # def test_no_entry_point3(self):  # not real main
    #     input = """
    #     Class Program {
    #         main(a, b: Int) {

    #         }
    #     }
    #     """
    #     expect = "No Entry Point"
    #     self.assertTrue(TestChecker.test(input, expect, 457))

    # def test_class_inherit_class(self):
    #     input = """
    #     Class myClass: myClass {
    #         main() {

    #         }
    #     }
    #     """
    #     expect = "Undeclared Class: myClass"
    #     self.assertTrue(TestChecker.test(input, expect, 458))

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
    #     self.assertTrue(TestChecker.test(input, expect, 459))

    # def test_array_decl(self):
    #     input = """
    #     Class Program {
    #         Var a: Array[Int, 1] = Array(1, 2, 3, 4);
    #         main() {

    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Constant Declaration: VarDecl(Id(a),ArrayType(1,IntType),[IntLit(1),IntLit(2),IntLit(3),IntLit(4)])"
    #     self.assertTrue(TestChecker.test(input, expect, 460))

    # def test_array_decl2(self):
    #     input = """
    #     Class Program {
    #         Var a: Array[Int, 1] = Array(True);
    #         main() {

    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Constant Declaration: VarDecl(Id(a),ArrayType(1,IntType),[BooleanLit(True)])"
    #     self.assertTrue(TestChecker.test(input, expect, 461))

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
    #     self.assertTrue(TestChecker.test(input, expect, 462))
