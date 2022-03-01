# import unittest
# from TestUtils import TestAST
# from AST import *

# class ASTGenSuite(unittest.TestCase):
#     # def test_class_declare(self):
#     #     """Test 1 """
#     #     input = """Class Shape{}"""
#     #     expect = str(Program([ClassDecl(Id("Shape"), [])]))
#     #     self.assertTrue(TestAST.test(input,expect,300))
    
#     # def test_class_declare_abstract(self):
#     #     """Test 2 """
#     #     input = """Class Square : Shape{}"""
#     #     expect = str(Program([ClassDecl(Id("Square"), [], Id("Shape"))]))
#     #     self.assertTrue(TestAST.test(input, expect, 301))

#     # def test_multiple_class_declare(self):
#     #     """Test 3"""
#     #     input = """Class Shape{
#     #          }
#     #          Class Test{
#     #              }
#     #             Class Program{}"""
#     #     expect = str(Program([ClassDecl(Id("Shape"), []), ClassDecl(
#     #         Id("Test"), []), ClassDecl(Id("Program"), [])]))
#     #     self.assertTrue(TestAST.test(input, expect, 302))
    
#     # def test_abstract_and_normal_classdecl(self):
#     #     """Test 4"""
#     #     input = """Class Shape{}
#     #                Class Abstract: Shape{}
#     #                Class Orbit{}"""
#     #     expect = str(Program([ClassDecl(Id("Shape"), []), ClassDecl(
#     #         Id("Abstract"), [], Id("Shape")), ClassDecl(Id("Orbit"), [])]))
#     #     self.assertTrue(TestAST.test(input, expect, 303))
    
#     # def test_immuatable_attribute_decl(self):
#     #     """Test 5"""
#     #     input = """Class testAttribute{
#     #             Val ast : Int;
#     #          }"""
#     #     expect = str(Program([ClassDecl(Id("testAttribute"), [
#     #                  AttributeDecl(Instance(), ConstDecl(Id("ast"), IntType(), None))])]))
#     #     self.assertTrue(TestAST.test(input, expect, 304))
    
#     # def test_immuatable_attribute_decl_with_value(self):
#     #     """Test 6"""
#     #     input = """Class TestValueAttr{
#     #             Val a : Float = 4.123;
#     #          }"""
#     #     expect = str(Program([ClassDecl(Id("Square"), [AttributeDecl(Instance(), VarDecl(
#     #         Id("a"), FloatType())), AttributeDecl(Instance(), VarDecl(Id("b"), FloatType()))])]))
#     #     self.assertTrue(TestAST.test(input, expect, 305))

#     def test_assign_stmt(self):
#         """Test 7"""
#         input = """Class assign_test{
#                 getTest(){
#                     res = 7 + 6;
#                 }
#              }"""
#         expect = str(Program([ClassDecl(Id("assign_test"), [MethodDecl(
#             Instance(), Id("getTest"), [], Block([Assign(Id("res"), IntLiteral(7))]))])]))
#         print(expect)
#         self.assertTrue(TestAST.test(input, expect, 306))
    
#     def test_assign_stmt(self):
#         """Test 7"""
#         input = """Class Program{
#                 main(){

#                 }
#              }
#              Class Shape{
#                  main(){

#                  }
#                  pro(){

#                  }
#              }"""
#         expect = str(Program([ClassDecl(Id("Program"), [MethodDecl(Static(), Id("main"), [], Block([]))]), ClassDecl(
#             Id("Shape"), [MethodDecl(Instance(), Id("main"), [], Block([])), MethodDecl(Instance(), Id("pro"), [], Block([]))])]))
#         print(expect)
#         self.assertTrue(TestAST.test(input, expect, 307))
    
#     # def test_assign_dstmt(self):
#     #     """Test 7"""
#     #     input = """Class assign_test{
#     #             getTest(){
#     #                 If(a){

#     #                 }
                   
#     #                 Else{
#     #                     a = 4;
#     #                 }
#     #             }
#     #          }"""
#     #     expect = str(Program([ClassDecl(Id("assign_test"), [MethodDecl(
#     #         Instance(), Id("getTest"), [], Block([Assign(Id("res"), IntLiteral(7))]))])]))
#     #     print(expect)
#     #     self.assertTrue(TestAST.test(input, expect, 307))


#     # def test_more_complex_program(self):
#     #     """More complex program"""
#     #     input = """int main () {
#     #         putIntLn(4);
#     #     }"""
#     #     expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([],[CallExpr(Id("putIntLn"),[IntLiteral(4)])]))]))
#     #     self.assertTrue(TestAST.test(input,expect,301))
    
#     # def test_call_without_parameter(self):
#     #     """More complex program"""
#     #     input = """int main () {
#     #         getIntLn();
#     #     }"""
#     #     expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([],[CallExpr(Id("getIntLn"),[])]))]))
#     #     self.assertTrue(TestAST.test(input,expect,302))

#     def test_if_stmt3(self):
#         input = """Class Shape {
#                     testFunc() {
#                         If (a > b) {
#                             a = b;
#                         }
                        
#                     }
#                 }
#             """
#         expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id(testFunc),Instance,[],Block([If(BinaryOp(>,Id(a),Id(b)),Block([AssignStmt(Id(a),Id(b))]),If(BinaryOp(<,Id(a),Id(b)),Block([AssignStmt(Id(c),Id(d))]),If(BinaryOp(==,Id(a),Id(b)),Block([AssignStmt(Id(e),Id(f))]))))]))])])"
#         self.assertTrue(TestAST.test(input, expect, 337))
import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    # def test_simple_program(self):
    #     input = """Class Program {}"""
    #     expect = "Program([ClassDecl(Id(Program),[])])"
    #     self.assertTrue(TestAST.test(input, expect, 300))

    # def test_simple_program2(self):
    #     input = """
    #     Class Program { }
    #     Class Test { }
    #     """
    #     expect = "Program([ClassDecl(Id(Program),[]),ClassDecl(Id(Test),[])])"
    #     self.assertTrue(TestAST.test(input, expect, 301))

    # def test_simple_program3(self):
    #     input = """
    #     Class Test:FatherClass { }
    #     """
    #     expect = "Program([ClassDecl(Id(Test),Id(FatherClass),[])])"
    #     self.assertTrue(TestAST.test(input, expect, 302))

    # def test_simple_funcdecl(self):
    #     input = """
    #     Class Program {
    #         testFunc(My1stCons, My2ndCons: Int; MyFloat: Float) {}
    #     }
    #     """
    #     expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(testFunc),Instance,[param(Id(My1stCons),IntType),param(Id(My2ndCons),IntType),param(Id(MyFloat),FloatType)],Block([]))])])"
    #     self.assertTrue(TestAST.test(input, expect, 303))

    # def test_simple_vardecl(self):
    #     input = """
    #     Class Program {
    #         Var a, $b: Int;
    #     }
    #     """
    #     expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),IntType)),AttributeDecl(Static,VarDecl(Id($b),IntType))])])"
    #     self.assertTrue(TestAST.test(input, expect, 304))

    # def test_simple_vardecl2(self):
    #     input = """
    #     Class Program {
    #         Var a, b: Int = 12, 13;
    #     }
    #     """
    #     expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),IntType,IntLit(12))),AttributeDecl(Instance,VarDecl(Id(b),IntType,IntLit(13)))])])"
    #     self.assertTrue(TestAST.test(input, expect, 305))

    # def test_simple_valdecl(self):
    #     input = """
    #     Class Program {
    #         Val c, $d: Int;
    #     }
    #     """
    #     expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(c),IntType,None)),AttributeDecl(Static,ConstDecl(Id($d),IntType,None))])])"
    #     self.assertTrue(TestAST.test(input, expect, 306))

    # def test_simple_valdecl2(self):
    #     input = """
    #     Class Program {
    #         Val c, d, e: Int = 12, 13, 10;
    #     }
    #     """
    #     expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(c),IntType,IntLit(12))),AttributeDecl(Instance,ConstDecl(Id(d),IntType,IntLit(13))),AttributeDecl(Instance,ConstDecl(Id(e),IntType,IntLit(10)))])])"
    #     self.assertTrue(TestAST.test(input, expect, 307))

    # def test_simple_valdecl3(self):
    #     input = """
    #     Class Program {
    #         Var a: Int = 3 + 2;
    #     }
    #     """
    #     expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),IntType,BinaryOp(+,IntLit(3),IntLit(2))))])])"
    #     self.assertTrue(TestAST.test(input, expect, 308))

    # def test_simple_valdecl4(self):  # nhan chia truoc
    #     input = """
    #     Class Program {
    #         Var a: Int = 5 + 3 * 2;
    #     }
    #     """
    #     expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),IntType,BinaryOp(+,IntLit(5),BinaryOp(*,IntLit(3),IntLit(2)))))])])"
    #     self.assertTrue(TestAST.test(input, expect, 309))

    # def test_simple_valdecl5(self):  # dau ngoac truoc
    #     input = """
    #     Class Program {
    #         Var a: Int = (5 + 3) * 2;
    #     }
    #     """
    #     expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),IntType,BinaryOp(*,BinaryOp(+,IntLit(5),IntLit(3)),IntLit(2))))])])"
    #     self.assertTrue(TestAST.test(input, expect, 310))

    # def test_exp(self):  # fun
    #     input = """
    #     Class Program {
    #         Var a: Int = Self.b;
    #     }
    #     """
    #     expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),IntType,FieldAccess(Id(Self),Id(b))))])])"
    #     self.assertTrue(TestAST.test(input, expect, 311))

    # def test_assign_stmt(self):
    #     input = """
    #     Class Program {
    #         testFun() {
    #             a = b;
    #         }
    #     }
    #     """
    #     expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(testFun),Instance,[],Block([AssignStmt(Id(a),Id(b))]))])])"
    #     self.assertTrue(TestAST.test(input, expect, 312))

    # def test_for_stmt(self):
    #     input = """
    #     Class Program {
    #         testFun() {
    #             Foreach (a In 1 .. 100 By 2) {
    #                     a = a + 3;
    #             }
    #         }
    #     }
    #     """
    #     expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(testFun),Instance,[],Block([For(Id(a),IntLit(1),IntLit(100),IntLit(2),Block([AssignStmt(Id(a),BinaryOp(+,Id(a),IntLit(3)))])])]))])])"
    #     self.assertTrue(TestAST.test(input, expect, 313))

    # def test_return_stmt(self):
    #     input = """
    #     Class Program {
    #         testFun() {
    #             Return;
    #         }
    #     }
    #     """
    #     expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(testFun),Instance,[],Block([Return()]))])])"
    #     self.assertTrue(TestAST.test(input, expect, 314))

    # def test_return_stmt2(self):
    #     input = """
    #     Class Program {
    #         testFun() {
    #             Return 5;
    #         }
    #     }
    #     """
    #     expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(testFun),Instance,[],Block([Return(IntLit(5))]))])])"
    #     self.assertTrue(TestAST.test(input, expect, 315))

    # def test_break_stmt(self):
    #     input = """
    #     Class Program {
    #         testFun() {
    #             Foreach (a In 1 .. 100 By 2) {
    #                     a = a + 3;
    #                     Break;
    #             }
    #         }
    #     }
    #     """
    #     expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(testFun),Instance,[],Block([For(Id(a),IntLit(1),IntLit(100),IntLit(2),Block([AssignStmt(Id(a),BinaryOp(+,Id(a),IntLit(3))),Break])])]))])])"
    #     self.assertTrue(TestAST.test(input, expect, 316))

    # def test_continue_stmt(self):
    #     input = """
    #     Class Program {
    #         testFun() {
    #             Foreach (a In 1 .. 100 By 2) {
    #                     a = a + 3;
    #                     Continue;
    #             }
    #         }
    #     }
    #     """
    #     expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(testFun),Instance,[],Block([For(Id(a),IntLit(1),IntLit(100),IntLit(2),Block([AssignStmt(Id(a),BinaryOp(+,Id(a),IntLit(3))),Continue])])]))])])"
    #     self.assertTrue(TestAST.test(input, expect, 317))

    # def test_member_access_stmt(self):
    #     input = """
    #     Class Program {
    #         testFun() {
    #             obj.getName(12, 3);
    #         }
    #     }
    #     """
    #     expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(testFun),Instance,[],Block([Call(Id(obj),Id(getName),[IntLit(12),IntLit(3)])]))])])"

    #     self.assertTrue(TestAST.test(input, expect, 318))

    # def test_field_access(self):
    #     input = """
    #     Class Program {
    #         testFun() {
    #             c = a.b;
    #             c = self.b;
    #             c = a::$b;
    #         }
    #     }
    #     """
    #     expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(testFun),Instance,[],Block([AssignStmt(Id(c),FieldAccess(Id(a),Id(b))),AssignStmt(Id(c),FieldAccess(Id(self),Id(b))),AssignStmt(Id(c),FieldAccess(Id(a),Id($b)))]))])])"
    #     self.assertTrue(TestAST.test(input, expect, 319))

    # def test_call_expr(self):
    #     input = """
    #     Class Program {
    #         testFun() {
    #             c = a::$b();
    #             c = a.b();
    #             a.b(3, 4);
    #             a::$b();
    #         }
    #     }
    #     """
    #     expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(testFun),Instance,[],Block([AssignStmt(Id(c),CallExpr(Id(a),Id($b),[])),AssignStmt(Id(c),CallExpr(Id(a),Id(b),[])),Call(Id(a),Id(b),[IntLit(3),IntLit(4)]),Call(Id(a),Id($b),[])]))])])"
    #     self.assertTrue(TestAST.test(input, expect, 320))

    # def test_vardecl_stmt(self):
    #     input = """
    #     Class Program {
    #         testFun() {
    #             Var a: Int = 12;
    #         }
    #     }
    #     """
    #     expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(testFun),Instance,[],Block([AttributeDecl(Instance,VarDecl(Id(a),IntType,IntLit(12)))]))])])"
    #     self.assertTrue(TestAST.test(input, expect, 321))

    # def test_if_stmt(self):
    #     input = """
    #     Class Program {
    #         testFun() {
    #             If (a > b) {
    #                 a = a + 1;
    #             }
    #             Else {
    #                 a = a - 1;
    #             }
    #         }
    #     }
    #     """
    #     expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(testFun),Instance,[],Block([If(BinaryOp(>,Id(a),Id(b)),Block([AssignStmt(Id(a),BinaryOp(+,Id(a),IntLit(1)))]),Block([AssignStmt(Id(a),BinaryOp(+,Id(a),IntLit(1)))]))]))])])"
                
    #     self.assertTrue(TestAST.test(input, expect, 322))

    def test_if_stmt2(self):
        input = """
        Class Program {
            testFun() {
                If (a > b) {
                    a = a + 1;
                }
                Elseif (a < b) {
                    a = a - 1;
                }
                Else {
                    a = a * 2;
                }
            }
        }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(testFun),Instance,[],Block([If(BinaryOp(>,Id(a),Id(b)),Block([AssignStmt(Id(a),BinaryOp(+,Id(a),IntLit(1)))]),If(BinaryOp(<,Id(a),Id(b)),Block([AssignStmt(Id(a),BinaryOp(-,Id(a),IntLit(1)))]),Block([AssignStmt(Id(a),BinaryOp(*,Id(a),IntLit(2)))])))]))])])"
        self.assertTrue(TestAST.test(input, expect, 323))

    def test_constructor_decl(self):
        input = """Class Program {
            Constructor() {}
        }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(Constructor),Instance,[],Block([]))])])"
        self.assertTrue(TestAST.test(input, expect, 324))

    def test_destructor_decl(self):
        input = """Class Program {
            Destructor() {}
        }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(Destructor),Instance,[],Block([]))])])"
        self.assertTrue(TestAST.test(input, expect, 325))

    def test_constructor_with_other_func(self):
        input = """Class A {
            Constructor() {}
            MyTest() {
                Foreach (var1 In 50 .. 100 By 5) {
                    Break;
                }
            }
        }"""
        expect = "Program([ClassDecl(Id(A),[MethodDecl(Id(Constructor),Instance,[],Block([])),MethodDecl(Id(MyTest),Instance,[],Block([For(Id(var1),IntLit(50),IntLit(100),IntLit(5),Block([Break])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 326))

    def test_destructor_with_other_func(self):
        input = """Class A {
            MyTest() {
                Var a: Int;
                Var b: Float = 0.2;
            }
            Destructor() {}
        }"""
        expect = "Program([ClassDecl(Id(A),[MethodDecl(Id(MyTest),Instance,[],Block([AttributeDecl(Instance,VarDecl(Id(a),IntType)),AttributeDecl(Instance,VarDecl(Id(b),FloatType,FloatLit(0.2)))])),MethodDecl(Id(Destructor),Instance,[],Block([]))])])"
        self.assertTrue(TestAST.test(input, expect, 327))

    def test_var_decl_with_some_type(self):
        input = """Class A {
            MyTest() {
                Var a: Int = 5;
                Var b: Float = 3.5;
                Var c: String = "Hello";
                Var d: Boolean = True;
            }
        }"""
        expect = "Program([ClassDecl(Id(A),[MethodDecl(Id(MyTest),Instance,[],Block([AttributeDecl(Instance,VarDecl(Id(a),IntType,IntLit(5))),AttributeDecl(Instance,VarDecl(Id(b),FloatType,FloatLit(3.5))),AttributeDecl(Instance,VarDecl(Id(c),StringType,StringLit(Hello))),AttributeDecl(Instance,VarDecl(Id(d),BoolType,BooleanLit(True)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 328))

    # def test_var_with_arr_type(self):
    #     input = """Class A {
    #         MyTest() {
    #             Var myArray: Array[Int, 5] = Array(1, 3, 5, 7, 9);
    #         }
    #     }"""
    #     expect = "Program([ClassDecl(Id(A),[MethodDecl(Id(MyTest),Instance,[],Block([AttributeDecl(Instance,VarDecl(Id(myArray),ArrayType(5,IntType),[IntLit(1),IntLit(3),IntLit(5),IntLit(7),IntLit(9)]))]))])])"
    #     self.assertTrue(TestAST.test(input, expect, 329))

    def test_for_stmt_without_by(self):
        input = """Class Program {
            main() {
                Foreach (var1 In 0 .. 10) {
                    Val myStr: String = "Hello World";
                }
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([For(Id(var1),IntLit(0),IntLit(10),IntLit(1),Block([AttributeDecl(Instance,ConstDecl(Id(myStr),StringType,StringLit(Hello World)))])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 330))

    def test_block_stmt_inside_block(self):
        input = """Class Program {
            main() {
                {
                    { Val a, b: Int; }
                }
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Block([Block([AttributeDecl(Instance,ConstDecl(Id(a),IntType,None)),AttributeDecl(Instance,ConstDecl(Id(b),IntType,None))])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 331))

    def test_exp_order(self):
        input = """Class Program {
            Val a: Int = 3 + 4 * 5;
            Val b: Int = (1 + 2) * 6;
        }"""
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,BinaryOp(+,IntLit(3),BinaryOp(*,IntLit(4),IntLit(5))))),AttributeDecl(Instance,ConstDecl(Id(b),IntType,BinaryOp(*,BinaryOp(+,IntLit(1),IntLit(2)),IntLit(6))))])])"
        self.assertTrue(TestAST.test(input, expect, 332))

    # def test_random_mixing(self):
    #     input = """Class Program {
    #         main() {
    #             Var r, s: Int;
    #             r = 2;
    #             Var a, b: Array[Int, 5];
    #             s = r * r * Self.myPI;
    #             a[0] = s;
    #         }
    #     }"""
    #     expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AttributeDecl(Instance,VarDecl(Id(r),IntType)),AttributeDecl(Instance,VarDecl(Id(s),IntType)),AssignStmt(Id(r),IntLit(2)),AttributeDecl(Instance,VarDecl(Id(a),ArrayType(5,IntType))),AttributeDecl(Instance,VarDecl(Id(b),ArrayType(5,IntType))),AssignStmt(Id(s),BinaryOp(*,BinaryOp(*,Id(r),Id(r)),FieldAccess(Id(Self),Id(myPI)))),AssignStmt(ArrayCell(Id(a),[IntLit(0)]),Id(s))]))])])"
    #     self.assertTrue(TestAST.test(input, expect, 333))

    def test_main_empty(self):
        input = """Class Program{
                main(){

                }
             }
             """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([]))])])"
        self.assertTrue(TestAST.test(input, expect, 334))

    def test_main_with_other_main(self):
        input = """Class Program {
                    main(){

                    }
                }
                Class testClass {
                    main() { }
                }
            """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([]))]),ClassDecl(Id(testClass),[MethodDecl(Id(main),Instance,[],Block([]))])])"
        self.assertTrue(TestAST.test(input, expect, 335))

    def test_main_with_param(self):
        input = """Class Program {
                    main(a: Int) {

                    }
                }
            """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Instance,[param(Id(a),IntType)],Block([]))])])"
        self.assertTrue(TestAST.test(input, expect, 336))

    def test_if_stmt3(self):
        input = """Class Shape {
                    testFunc() {
                        If (a > b) {
                            a = b;
                        }
                        Elseif (a < b) {
                            c = d;
                        }
                        Elseif (a == b) {
                            e = f;
                        }
                    }
                }
            """
        expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id(testFunc),Instance,[],Block([If(BinaryOp(>,Id(a),Id(b)),Block([AssignStmt(Id(a),Id(b))]),If(BinaryOp(<,Id(a),Id(b)),Block([AssignStmt(Id(c),Id(d))]),If(BinaryOp(==,Id(a),Id(b)),Block([AssignStmt(Id(e),Id(f))]))))]))])])"
        self.assertTrue(TestAST.test(input, expect, 337))

    def test_if_stmt4(self):
        input = """Class Shape {
                    testFunc() {
                        If (a > b) {
                            a = b;
                        }
                        Elseif (a < b) {
                            c = d;
                        }
                        Elseif (a == b) {
                            e = f;
                        }
                        Else {
                            g = h;
                        }
                    }
                }
            """
        expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id(testFunc),Instance,[],Block([If(BinaryOp(>,Id(a),Id(b)),Block([AssignStmt(Id(a),Id(b))]),If(BinaryOp(<,Id(a),Id(b)),Block([AssignStmt(Id(c),Id(d))]),If(BinaryOp(==,Id(a),Id(b)),Block([AssignStmt(Id(e),Id(f))]),Block([AssignStmt(Id(g),Id(h))]))))]))])])"
        self.assertTrue(TestAST.test(input, expect, 338))
