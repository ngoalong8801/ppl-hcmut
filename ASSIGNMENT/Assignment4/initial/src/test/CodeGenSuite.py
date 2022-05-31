import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    # def test_int(self):
    #     """
    #     }"""
    #     input = """Class Program{
    #         main(){
    #             io.putInt(4);
    #             }
    #             }"""
    #     expect = "4"
    #     self.assertTrue(TestCodeGen.test(input, expect, 500))

    # def test_float(self):
    #     """
    #     }"""
    #     input = """Class Program{
    #         main(){
    #             io.putFloat(2.567);
    #             }
    #             }"""
    #     expect = "2.567"
    #     self.assertTrue(TestCodeGen.test(input, expect, 501))

    # def test_boolean(self):
    #     """
    #     }"""
    #     input = """Class Program{
    #         main(){
    #             io.putBool(True);
    #             }
    #             }"""
    #     expect = "true"
    #     self.assertTrue(TestCodeGen.test(input, expect, 502))

    # def test_string(self):
    #     """
    #     }"""
    #     input = """Class Program{
    #         main(){
    #             io.putString("Hello World");
    #             }
    #             }"""
    #     expect = "Hello World"
    #     self.assertTrue(TestCodeGen.test(input, expect, 503))

    # def test_boolean_False(self):
    #     """
    #     }"""
    #     input = """Class Program{
    #         main(){
    #             io.putBool(False);
    #             }
    #             }"""
    #     expect = "false"
    #     self.assertTrue(TestCodeGen.test(input, expect, 504))

    # def test_complex_put(self):
    #     input = """Class Program{
    #         main(){
    #             io.putBool(False);
    #             io.putInt(2);
    #             io.putFloat(2.36);
    #             }
    #             }"""
    #     expect = "false22.36"
    #     self.assertTrue(TestCodeGen.test(input, expect, 505))

    # def test_binary_1(self):
    #     """
    #     }"""
    #     input = """Class Program{
    #         main(){
    #             io.putInt(4 + 5);
    #             }
    #             }"""
    #     expect = "9"
    #     self.assertTrue(TestCodeGen.test(input, expect, 506))

    # def test_binary_2(self):
    #     """
    #     }"""
    #     input = """Class Program{
    #         main(){
    #             io.putBool(True || False);
    #             }
    #             }"""
    #     expect = "true"
    #     self.assertTrue(TestCodeGen.test(input, expect, 507))

    # def test_binary_3(self):
    #     """
    #     }"""
    #     input = """Class Program{
    #         main(){
    #             io.putFloat(1 * 2 + 3 - 4.567);
    #             }
    #             }"""
    #     expect = "0.4330001"
    #     self.assertTrue(TestCodeGen.test(input, expect, 508))

    # def test_binary_4(self):
    #     """
    #     }"""
    #     input = """Class Program{
    #         main(){

    #             }
    #             }"""
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input, expect, 509))

    # def test_binary_5(self):
    #     """
    #     }"""
    #     input = """Class Program{
    #         main(){

    #             }
    #             }"""
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input, expect, 510))

    # def test_stmt_vardecl_1(self):
    #     """
    #     }"""
    #     input = """Class Program{
    #         main(){
    #             Var a: Int = 4;
    #             io.putInt(a);
    #             }
    #             }"""
    #     expect = "4"
    #     self.assertTrue(TestCodeGen.test(input, expect, 511))

    # def test_stmt_vardecl_2(self):
    #     """
    #     }"""
    #     input = """Class Program{
    #         main(){
    #             Var a: Boolean = True;
    #             io.putBool(a);
    #             }
    #             }"""
    #     expect = "true"
    #     self.assertTrue(TestCodeGen.test(input, expect, 512))

    # def test_stmt_vardecl_3(self):
    #     """
    #     }"""
    #     input = """Class Program{
    #         main(){
    #             Var str: String = "I hope that one day  there wont have any assignment anymore !!";
    #             io.putString(str);
    #             }
    #             }"""
    #     expect = "I hope that one day  there wont have any assignment anymore !!"
    #     self.assertTrue(TestCodeGen.test(input, expect, 513))

    # def test_stmt_vardecl_complex_1(self):
    #     """
    #     }"""
    #     input = """Class Program{
    #         main(){
    #             Var a: Boolean = True;
    #             Var str: String = "I hope that one day  there wont have any assignment anymore !!";
    #             io.putString(str);
    #             io.putBool(a);
    #             }
    #             }"""
    #     expect = "I hope that one day  there wont have any assignment anymore !!true"
    #     self.assertTrue(TestCodeGen.test(input, expect, 514))

    # def test_stmt_constdecl_1(self):
    #     """
    #     }"""
    #     input = """Class Program{
    #         main(){
    #             Val a: Int = 4;
    #             io.putInt(a);
    #             }
    #             }"""
    #     expect = "4"
    #     self.assertTrue(TestCodeGen.test(input, expect, 515))

    # def test_stmt_constdecl_2(self):
    #     """
    #     }"""
    #     input = """Class Program{
    #         main(){
    #             Val a: Boolean = True;
    #             io.putBool(a);
    #             }
    #             }"""
    #     expect = "true"
    #     self.assertTrue(TestCodeGen.test(input, expect, 516))

    # def test_stmt_constdecl_3(self):
    #     """
    #     }"""
    #     input = """Class Program{
    #         main(){
    #             Val str: String = "I hope that one day  there wont have any assignment anymore !!";
    #             io.putString(str);
    #             }
    #             }"""
    #     expect = "I hope that one day  there wont have any assignment anymore !!"
    #     self.assertTrue(TestCodeGen.test(input, expect, 517))

    # def test_stmt_constdecl_complex_1(self):
    #     """
    #     }"""
    #     input = """Class Program{
    #         main(){
    #             Val a: Boolean = True;
    #             Val str: String = "I hope that one day  there wont have any assignment anymore !!";
    #             io.putString(str);
    #             io.putBool(a);
    #             }
    #             }"""
    #     expect = "I hope that one day  there wont have any assignment anymore !!true"
    #     self.assertTrue(TestCodeGen.test(input, expect, 518))

    # def test_stmt_constdecl_vardecl_mix(self):
    #     """
    #     }"""
    #     input = """Class Program{
    #         main(){
    #             Var num1: Float = 2022.2021;
    #             Val str: String = "I hope that one day  there wont have any assignment anymore !!";
    #             io.putFloat(num1);
    #             io.putString(str);

    #             }
    #             }"""
    #     expect = "2022.2021I hope that one day  there wont have any assignment anymore !!"
    #     self.assertTrue(TestCodeGen.test(input, expect, 519))

    # def test_unary_1(self):
    #     """
    #     }"""
    #     input = """Class Program{
    #         main(){
    #             io.putFloat(-4.567);
    #             }
    #             }"""
    #     expect = "-4.567"
    #     self.assertTrue(TestCodeGen.test(input, expect, 520))

    # def test_unary_2(self):
    #     """
    #     }"""
    #     input = """Class Program{
    #         main(){
    #             io.putBool(!(6 > 7));
    #             }
    #             }"""
    #     expect = "true"
    #     self.assertTrue(TestCodeGen.test(input, expect, 520))

    # def test_unary_3(self):
    #     """
    #     }"""
    #     input = """Class Program{
    #         main(){
    #             io.putFloat(-(4.56 * 78 + 90) * 5);
    #             }
    #             }"""
    #     expect = "-2228.4"
    #     self.assertTrue(TestCodeGen.test(input, expect, 521))

    # def test_unary_3(self):
    #     """
    #     }"""
    #     input = """Class Program{
    #         main(){
    #             io.putFloat(-(4.56 * 78 + 90) * 5);
    #             }
    #             }"""
    #     expect = "-2228.4"
    #     self.assertTrue(TestCodeGen.test(input, expect, 521))

    # def test_binary_comparestring(self):
    #     """
    #     }"""
    #     input = """Class Program{
    #         main(){
    #             Var check: Boolean =("hihi" ==. "hihi");
    #             io.putBool(check);
    #             }
    #             }"""
    #     expect = "true"
    #     self.assertTrue(TestCodeGen.test(input, expect, 521))

    # def test_binary_comparestring_1(self):
    #     """
    #     }"""
    #     input = """Class Program{
    #         main(){
    #             Var check: Boolean =("hihii" ==. "hihi");
    #             io.putBool(check);
    #             }
    #             }"""
    #     expect = "false"
    #     self.assertTrue(TestCodeGen.test(input, expect, 522))

    # def test_binary_concatstring(self):
    #     """
    #     }"""
    #     input = """Class Program{
    #         main(){
    #             Var check: String =("Hello" +. " World");
    #             io.putString(check);
    #             }
    #             }"""
    #     expect = "Hello World"
    #     self.assertTrue(TestCodeGen.test(input, expect, 523))

    # def test_binary_concatstring_1(self):
    #     """
    #     }"""
    #     input = """Class Program{
    #         main(){
    #             Var check: Boolean =(("Hello" +. " World ")==. "Hello World ");
    #             io.putBool(check);
    #             }
    #             }"""
    #     expect = "true"
    #     self.assertTrue(TestCodeGen.test(input, expect, 524))

    # def test_stmt_assign_1(self):
    #     """
    #     }"""
    #     input = """Class Program{
    #         main(){
    #             Var num: Int;
    #             num = 2;
    #             io.putInt(num);
    #             }
    #             }"""
    #     expect = "2"
    #     self.assertTrue(TestCodeGen.test(input, expect, 525))

    # def test_stmt_assign_2(self):
    #     """
    #     }"""
    #     input = """Class Program{
    #         main(){
    #             Var num: Boolean;
    #             num = True;
    #             io.putBool(num);
    #             }
    #             }"""
    #     expect = "true"
    #     self.assertTrue(TestCodeGen.test(input, expect, 526))

    # def test_stmt_assign_3(self):
    #     """
    #     }"""
    #     input = """Class Program{
    #         main(){
    #             Var str: String;
    #             str = "Hello";
    #             io.putString(str);
    #             }
    #             }"""
    #     expect = "Hello"
    #     self.assertTrue(TestCodeGen.test(input, expect, 527))

    # def test_stmt_assign_4(self):
    #     """
    #     }"""
    #     input = """Class Program{
    #         main(){
    #             Var check: Boolean;
    #             check = (6> 7) && (8>9);
    #             io.putBool(check);
    #             }
    #             }"""
    #     expect = "false"
    #     self.assertTrue(TestCodeGen.test(input, expect, 528))

    # def test_stmt_assign_5(self):
    #     """
    #     }"""
    #     input = """Class Program{
    #         main(){
    #             Var check: Int = 0;
    #             check = check + 1;
    #             io.putInt(check);
    #             }
    #             }"""
    #     expect = "1"
    #     self.assertTrue(TestCodeGen.test(input, expect, 529))

    # def test_stmt_assign_6(self):
    #     """
    #     }"""
    #     input = """Class Program{
    #         main(){
    #             Var check: Float = 0;
    #             check = check + 1;
    #             check = check * 2 + 2.56;
    #             io.putFloat(check);
    #             }
    #             }"""
    #     expect = "4.56"
    #     self.assertTrue(TestCodeGen.test(input, expect, 530))

    # def test_field_class_1(self):
    #     """
    #     }"""
    #     input = """Class Program{
    #         Var a: Int = 5;
    #         main(){
    #             io.putInt(Self.a);
    #             }
    #             }"""
    #     expect = "5"
    #     self.assertTrue(TestCodeGen.test(input, expect, 531))

    # def test_field_class_2(self):
    #     """
    #     }"""
    #     input = """Class Program{
    #         Var c: Int = 5;
    #         Var b: Float = 5.67;
    #         main(){
    #             io.putInt(Self.c);
    #             io.putFloat(Self.b);
    #             }
    #             }"""
    #     expect = "55.67"
    #     self.assertTrue(TestCodeGen.test(input, expect, 532))

    # def test_field_class_3(self):
    #     """
    #     }"""
    #     input = """Class Program{
    #         Var a: Int = 5;
    #         Var b: Float = 5.67;
    #         Val c: String = "abc";
    #         main(){
    #             io.putInt(Self.a);
    #             io.putFloat(Self.b);
    #             io.putString(Self.c);
    #             }
    #             }"""
    #     expect = "55.67abc"
    #     self.assertTrue(TestCodeGen.test(input, expect, 533))

    # def test_field_class_4(self):
    #     """
    #     }"""
    #     input = """Class Program{
    #         Var a: Int = 5;
    #         Var b: Float = 5.67;

    #         main(){
    #             io.putInt(Self.a);
    #             io.putFloat(Self.b / Self.a);

    #             }
    #             }"""
    #     expect = "51.1340001"
    #     self.assertTrue(TestCodeGen.test(input, expect, 534))

    # def test_field_class_5(self):
    #     """
    #     }"""
    #     input = """Class Program{
    #         Var a: Int = 5;
    #         Var b: Float = 5.67;

    #         main(){
    #             io.putInt(Self.a + 2 *6);
    #             io.putFloat(Self.b / Self.a);

    #             }
    #             }"""
    #     expect = "171.1340001"
    #     self.assertTrue(TestCodeGen.test(input, expect, 535))

    # def test_stmt_if_1(self):
    #     """
    #     }"""
    #     input = """Class Program{

    #         main(){
    #            If(True){
    #                io.putString("Yes");
    #            }
    #             }
    #             }"""
    #     expect = "Yes"
    #     self.assertTrue(TestCodeGen.test(input, expect, 535))

    # def test_stmt_if_2(self):
    #     """
    #     }"""
    #     input = """Class Program{

    #         main(){
    #            If(False){
    #                io.putString("Yes");
    #            }
    #            Else{
    #                io.putString("No");
    #            }
    #             }
    #             }"""
    #     expect = "No"
    #     self.assertTrue(TestCodeGen.test(input, expect, 536))

    # def test_stmt_if_3(self):
    #     """
    #     }"""
    #     input = """Class Program{

    #         main(){
    #            If(False){
    #                io.putString("Yes");
    #            }
    #            Elseif(True){
    #                  io.putString("In Scope Else if");
    #            }
    #            Else{
    #                io.putString("No");
    #            }
    #             }
    #             }"""
    #     expect = "In Scope Else if"
    #     self.assertTrue(TestCodeGen.test(input, expect, 537))

    # def test_stmt_if_4(self):
    #     """
    #     }"""
    #     input = """Class Program{

    #         main(){
    #             Var check: Boolean = True;
    #            If(!check){
    #                io.putString("Yes");
    #            }
    #            Elseif(check){
    #                  io.putString("In Scope Else if");
    #            }
    #            Else{
    #                io.putString("No");
    #            }

    #            io.putString("EndIF");
    #             }
    #             }"""
    #     expect = "In Scope Else ifEndIF"
    #     self.assertTrue(TestCodeGen.test(input, expect, 538))

    # def test_stmt_if_5(self):
    #     """
    #     }"""
    #     input = """Class Program{

    #         main(){
    #             Var a: Int = 4;
    #             Var b: Int = 5;
    #            If(a < 0){
    #                io.putString("Yes");
    #            }
    #            Elseif(b > 6){
    #                  io.putString("In Scope Else if");
    #            }
    #            Else{
    #                io.putString("No");
    #            }

    #            io.putString("EndIF");
    #             }
    #             }"""
    #     expect = "NoEndIF"
    #     self.assertTrue(TestCodeGen.test(input, expect, 539))

    # def test_stmt_if_6(self):
    #     """
    #     }"""
    #     input = """Class Program{

    #         main(){
    #             Var a: Int = 4;
    #             Var b: Int = 5;
    #            If(a < 0){
    #                io.putString("Yes");
    #            }
    #            Elseif((4 < b) && (b >0)){
    #                  io.putString("In Scope Else if");
    #            }
    #            Else{
    #                io.putString("No");
    #            }

    #            io.putString("EndIF");
    #             }
    #             }"""
    #     expect = "In Scope Else ifEndIF"
    #     self.assertTrue(TestCodeGen.test(input, expect, 540))

    # def test_stmt_for_1(self):
    #     """
    #     }"""
    #     input = """Class Program{

    #         main(){
    #         Var i : Int = 0;
    #          Foreach(i In 0 .. 3){
    #              io.putInt(i);
    #          }
    #             }
    #             }"""
    #     expect = "0123"
    #     self.assertTrue(TestCodeGen.test(input, expect, 541))

    # def test_stmt_for_2(self):
    #     """
    #     }"""
    #     input = """Class Program{

    #         main(){
    #         Var i : Int = 2;
    #          Foreach(i In 0 .. 3){
    #              io.putInt(i);
    #          }
    #             }
    #             }"""
    #     expect = "23"
    #     self.assertTrue(TestCodeGen.test(input, expect, 542))

    # def test_stmt_for_3(self):
    #     """
    #     }"""
    #     input = """Class Program{

    #         main(){
    #         Var i : Int = 4;
    #          Foreach(i In 0 .. 3){
    #              io.putInt(i);
    #          }
    #             }
    #             }"""
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input, expect, 543))

    # def test_stmt_for_4(self):
    #     """
    #     }"""
    #     input = """Class Program{

    #         main(){
    #         Var i : Int = 0;
    #          Foreach(i In 0 .. 4 By 2){
    #              io.putInt(i);
    #          }
    #             }
    #             }"""
    #     expect = "024"
    #     self.assertTrue(TestCodeGen.test(input, expect, 544))

    # def test_stmt_for_5(self):
    #     """
    #     }"""
    #     input = """Class Program{

    #         main(){
    #         Var i : Int = 0;
    #          Foreach(i In 0 .. 4 By 3){
    #              io.putInt(i);
    #          }
    #             }
    #             }"""
    #     expect = "03"
    #     self.assertTrue(TestCodeGen.test(input, expect, 545))

    def test_stmt_for_6(self):
        """
        }"""
        input = """Class Program{
        
            main(){
            Var i : Int = 0;
             Var j: Int = 1;
             Foreach(i In 0 .. 2){
                
                 Foreach(j In 1 .. 2){
                     io.putInt(i);
                     io.putInt(j);
                 }
             }
                }
                }"""
        expect = "0102"
        self.assertTrue(TestCodeGen.test(input, expect, 545))

    def test_stmt_for_7(self):
        """
        }"""
        input = """Class Program{
        
            main(){
            Var i : Int = 0;
             Var j: Int = 1;
             Foreach(i In 0 .. 2){
                
                 Foreach(j In 1 .. 2){
                     io.putString("Hello World");
                 }
             }
                }
                }"""
        expect = "Hello WorldHello World"
        self.assertTrue(TestCodeGen.test(input, expect, 546))

    def test_stmt_Break(self):
        """
        }"""
        input = """Class Program{
        
            main(){
              Var i: Int = 0;

              Foreach(i In 0 .. 3){
                  io.putInt(i);
                  Break;
              }
                }
                }"""
        expect = "0"
        self.assertTrue(TestCodeGen.test(input, expect, 547))

    def test_stmt_Break_2(self):
        """
        }"""
        input = """Class Program{
        
            main(){
              Var i: Int = 0;

              Foreach(i In 0 .. 3){
                  io.putInt(i);
                  If( i == 2){
                      Break;
                  }
              }
                }
                }"""
        expect = "012"
        self.assertTrue(TestCodeGen.test(input, expect, 548))

    def test_stmt_Break_3(self):
        """
        }"""
        input = """Class Program{
        
            main(){
              Var i: Int = 0;

              Foreach(i In 0 .. 3){
                  io.putInt(i);
                  If( i == 2){
                      io.putString("The break point here");
                      Break;
                  }
              }
                }
                }"""
        expect = "012The break point here"
        self.assertTrue(TestCodeGen.test(input, expect, 549))

    def test_stmt_ctn_1(self):
        """
        }"""
        input = """Class Program{
        
            main(){
              Var i: Int = 0;

              Foreach(i In 0 .. 3){
                  io.putInt(i);
                  Break;
                  io.putString("cant reach");
              }
                }
                }"""
        expect = "0"
        self.assertTrue(TestCodeGen.test(input, expect, 550))

    def test_stmt_ctn_2(self):
        """
        }"""
        input = """Class Program{
        
            main(){
              Var i: Int = 0;

              Foreach(i In 0 .. 3){
                  
                  If( i == 2){
                      Continue;
                  }
                  io.putInt(i);
              }
                }
                }"""
        expect = "013"
        self.assertTrue(TestCodeGen.test(input, expect, 551))

    def test_stmt_ctn_3(self):
        """
        }"""
        input = """Class Program{
        
            main(){
              Var i: Int = 0;

              Foreach(i In 0 .. 3){
                  io.putInt(i);
                  If( i == 2){
                      Continue;
                  }
                  io.putString("Skip when encounter continue stmt");
              }
                }
                }"""
        expect = "0Skip when encounter continue stmt1Skip when encounter continue stmt23Skip when encounter continue stmt"
        self.assertTrue(TestCodeGen.test(input, expect, 552))

    # def test_int_ast(self):
    # 	input = Program([
    # 		FuncDecl(Id("main"),[],VoidType(),Block([],[
    # 			CallExpr(Id("putInt"),[IntLiteral(5)])]))])
    # 	expect = "5"
    # 	self.assertTrue(TestCodeGen.test(input,expect,501))
