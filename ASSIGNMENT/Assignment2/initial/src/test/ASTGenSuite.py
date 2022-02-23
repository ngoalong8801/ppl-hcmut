import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    # def test_class_declare(self):
    #     """Test 1 """
    #     input = """Class Shape{}"""
    #     expect = str(Program([ClassDecl(Id("Shape"), [])]))
    #     self.assertTrue(TestAST.test(input,expect,300))
    
    # def test_class_declare_abstract(self):
    #     """Test 2 """
    #     input = """Class Square : Shape{}"""
    #     expect = str(Program([ClassDecl(Id("Square"), [], Id("Shape"))]))
    #     self.assertTrue(TestAST.test(input, expect, 301))

    # def test_att_decl(self):
    #     """Test 3"""
    #     input = """Class Shape{
    #             Val a: Int;
    #          }"""
    #     expect = str(Program([ClassDecl(Id("Shape"), [AttributeDecl(Instance(),ConstDecl(Id("a"),IntType(),None))])]))
    #     self.assertTrue(TestAST.test(input, expect, 302))
    
    # def test_att_decl_opas(self):
    #     """Test 4"""
    #     input = """Class Shape{
    #             Val a: Int = 4;
    #          }"""
    #     expect = str(Program([ClassDecl(Id("Shape"), [AttributeDecl(
    #         Instance(), ConstDecl(Id("a"), IntType(), IntLiteral(4)))])]))
    #     self.assertTrue(TestAST.test(input, expect, 303))
    
    # def test_mutable_clr(self):
    #     """Test 5"""
    #     input = """Class Square{
    #             Var abc : Float;
    #          }"""
    #     expect = str(Program([ClassDecl(Id("Square"), [AttributeDecl(Instance(), VarDecl(Id("abc"), FloatType()))])]))
    #     self.assertTrue(TestAST.test(input, expect, 304))
    
    # def test_method_decl(self):
    #     """Test 6"""
    #     input = """Class Square{
    #             Var a, b: Float;
    #          }"""
    #     expect = str(Program([ClassDecl(Id("Square"), [AttributeDecl(Instance(), VarDecl(
    #         Id("a"), FloatType())), AttributeDecl(Instance(), VarDecl(Id("b"), FloatType()))])]))
    #     self.assertTrue(TestAST.test(input, expect, 305))

    # def test_assign_stmt(self):
    #     """Test 7"""
    #     input = """Class assign_test{
    #             getTest(){
    #                 res = 7;
    #             }
    #          }"""
    #     expect = str(Program([ClassDecl(Id("assign_test"), [MethodDecl(
    #         Instance(), Id("getTest"), [], Block([Assign(Id("res"), IntLiteral(7))]))])]))
    #     print(expect)
    #     self.assertTrue(TestAST.test(input, expect, 306))
    
    def test_assign_dstmt(self):
        """Test 7"""
        input = """Class assign_test{
                getTest(){
                    If(a){

                    }
                    Elseif(b){

                    }
                    Elseif(c){
                        
                    }
                }
             }"""
        expect = str(Program([ClassDecl(Id("assign_test"), [MethodDecl(
            Instance(), Id("getTest"), [], Block([Assign(Id("res"), IntLiteral(7))]))])]))
        print(expect)
        self.assertTrue(TestAST.test(input, expect, 307))


    # def test_more_complex_program(self):
    #     """More complex program"""
    #     input = """int main () {
    #         putIntLn(4);
    #     }"""
    #     expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([],[CallExpr(Id("putIntLn"),[IntLiteral(4)])]))]))
    #     self.assertTrue(TestAST.test(input,expect,301))
    
    # def test_call_without_parameter(self):
    #     """More complex program"""
    #     input = """int main () {
    #         getIntLn();
    #     }"""
    #     expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([],[CallExpr(Id("getIntLn"),[])]))]))
    #     self.assertTrue(TestAST.test(input,expect,302))
   