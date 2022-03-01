import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    
    def test_class_declare(self):
        """Test 1 """
        input = """Class Shape{}"""
        expect = str(Program([ClassDecl(Id("Shape"), [])]))
        self.assertTrue(TestAST.test(input,expect,300))
    
    def test_class_declare_abstract(self):
        """Test 2 """
        input = """Class Square : Shape{}"""
        expect = str(Program([ClassDecl(Id("Square"), [], Id("Shape"))]))
        self.assertTrue(TestAST.test(input, expect, 301))

    def test_multiple_class_declare(self):
        """Test 3"""
        input = """Class Shape{
             }
             Class Test{
                 }
                Class Program{}"""
        expect = str(Program([ClassDecl(Id("Shape"), []), ClassDecl(
            Id("Test"), []), ClassDecl(Id("Program"), [])]))
        self.assertTrue(TestAST.test(input, expect, 302))
    
    def test_abstract_and_normal_classdecl(self):
        """Test 4"""
        input = """Class Shape{}
                   Class Abstract: Shape{}
                   Class Orbit{}"""
        expect = str(Program([ClassDecl(Id("Shape"), []), ClassDecl(
            Id("Abstract"), [], Id("Shape")), ClassDecl(Id("Orbit"), [])]))
        self.assertTrue(TestAST.test(input, expect, 303))
    
    def test_immuatable_attribute_decl(self):
        """Test 5"""
        input = """Class testAttribute{
                Val ast : Int;
             }"""
        expect = str(Program([ClassDecl(Id("testAttribute"), [
                     AttributeDecl(Instance(), ConstDecl(Id("ast"), IntType(), None))])]))
        self.assertTrue(TestAST.test(input, expect, 304))
    
    def test_immuatable_attribute_decl_with_value(self):
        """Test 6"""
        input = """Class TestValueAttr{
                Val a : Float = 4.123;
             }"""
        expect = str(Program([ClassDecl(Id("TestValueAttr"), [AttributeDecl(
            Instance(), ConstDecl(Id("a"), FloatType(), FloatLiteral(4.123)))])]))
        self.assertTrue(TestAST.test(input, expect, 305))
    
    def test_mul_immuatable_attribute_decl(self):
        """Test 7"""
        input = """Class TestMulImuAttr{
                Val a, b, c : String;
             }"""
        expect = str(Program([ClassDecl(Id("TestMulImuAttr"), [AttributeDecl(Instance(), ConstDecl(Id("a"), StringType(), None)), AttributeDecl(
            Instance(), ConstDecl(Id("b"), StringType(), None)), AttributeDecl(Instance(), ConstDecl(Id("c"), StringType(), None))])]))
        self.assertTrue(TestAST.test(input, expect, 306))
    
    def test_muatable_attribute_decl(self):
        """Test 8"""
        input = """Class testMutableDecl{
                Var ast : Float;
             }"""
        expect = str(Program([ClassDecl(Id("testMutableDecl"), [
                     AttributeDecl(Instance(), VarDecl(Id("ast"), FloatType()))])]))
        self.assertTrue(TestAST.test(input, expect, 307))
    
    def test_mutable_attribute_decl_with_value(self):
        """Test 9"""
        input = """Class TestMutableValue{
                Val a : Boolean = False;
             }"""
        expect = str(Program([ClassDecl(Id("TestMutableValue"), [AttributeDecl(
            Instance(), ConstDecl(Id("a"), BoolType(), BooleanLiteral(False)))])]))
        self.assertTrue(TestAST.test(input, expect, 308))
    
    def test_mul_mutable_attribute_decl(self):
        """Test 10"""
        input = """Class TestMulImuAttr{
                Var abc, tes, $Immua : Int;
             }"""
        expect = str(Program([ClassDecl(Id("TestMulImuAttr"), [AttributeDecl(Instance(), VarDecl(Id("abc"), IntType())), AttributeDecl(
            Instance(), VarDecl(Id("tes"), IntType())), AttributeDecl(Static(), VarDecl(Id("$Immua"), IntType()))])]))
        self.assertTrue(TestAST.test(input, expect, 309))
    
    def test_mul_mutable_attribute_decl_value(self):
        """Test 11"""
        input = """Class TestMulImuAttr{
                Var abc, tes, $Immua : Int = 1, 3, 2022;
             }"""
        expect = str(Program([ClassDecl(Id("TestMulImuAttr"), [AttributeDecl(Instance(), VarDecl(Id("abc"), IntType(), IntLiteral(1))), AttributeDecl(
            Instance(), VarDecl(Id("tes"), IntType(), IntLiteral(3))), AttributeDecl(Static(), VarDecl(Id("$Immua"), IntType(), IntLiteral(2022)))])]))
        self.assertTrue(TestAST.test(input, expect, 310))

    
    def test_mul_immutable_attribute_decl_value(self):
        """Test 12"""
        input = """Class TestMulImuAttr{
                Val immuVa, $kalixianua, $Ukraina : Float = 1.134, 313.999, 2022.3254325;
             }"""
        expect = str(Program([ClassDecl(Id("TestMulImuAttr"), [AttributeDecl(Instance(), ConstDecl(Id("immuVa"), FloatType(), FloatLiteral(1.134))), AttributeDecl(
            Static(), ConstDecl(Id("$kalixianua"), FloatType(), FloatLiteral(313.999))), AttributeDecl(Static(), ConstDecl(Id("$Ukraina"), FloatType(), FloatLiteral(2022.3254325)))])]))
        self.assertTrue(TestAST.test(input, expect, 311))

    def test_mix_mutable_dadsand_immu_decl(self):
        """Test 13"""
        input = """Class TestMulImuAttr{
                Var abc, tes, $Immua : Int;
                Val immuVa, $kalixianua, $Ukraina : Float;
              }"""
        expect = str(Program([ClassDecl(Id("TestMulImuAttr"), [AttributeDecl(Instance(), VarDecl(Id("abc"), IntType())), AttributeDecl(Instance(), VarDecl(Id("tes"), IntType())), AttributeDecl(Static(), VarDecl(Id("$Immua"), IntType())), AttributeDecl(
            Instance(), ConstDecl(Id("immuVa"), FloatType(), None)), AttributeDecl(Static(), ConstDecl(Id("$kalixianua"), FloatType(), None)), AttributeDecl(Static(), ConstDecl(Id("$Ukraina"), FloatType(), None))])]))
        self.assertTrue(TestAST.test(input, expect, 312))
    
    def test_method_decl(self):
        """Test 14"""
        input = """Class TestMethoddecl{
                    methodTest(){

                    }
              }"""
        expect = str(Program([ClassDecl(Id("TestMethoddecl"), [MethodDecl( Instance(), Id("methodTest"), [], Block([]))])]))
        self.assertTrue(TestAST.test(input, expect, 313))
    
    def test_method_static_decl(self):
        """Test 15"""
        input = """Class TestMethoddecl{
                    $staticMethodTest(){

                    }
              }"""
        expect = str(Program([ClassDecl(Id("TestMethoddecl"), [
                     MethodDecl(Static(), Id("$staticMethodTest"), [], Block([]))])]))
        self.assertTrue(TestAST.test(input, expect, 314))
    
    def test_multi_method_decl(self):
        """Test 16"""
        input = """Class TestMethoddecl{
                    $staticMethodTest(){

                    }
                    methodNormal(){

                    }
              }"""
        expect = str(Program([ClassDecl(Id("TestMethoddecl"), [MethodDecl(Static(), Id("$staticMethodTest"),  [
        ], Block([])), MethodDecl(Instance(), Id("methodNormal"), [], Block([]))])]))
        self.assertTrue(TestAST.test(input, expect, 315))
    
    def test_method_with_param(self):
        """Test 17"""
        input = """Class TestMethoddecl{
                   
                    parammethod(a : Int){

                    }
              }"""
        expect = str(Program([ClassDecl(Id("TestMethoddecl"), [MethodDecl(Instance(),
            Id("parammethod"),  [VarDecl(Id("a"), IntType())], Block([]))])]))
        self.assertTrue(TestAST.test(input, expect, 316))

    def test_method_with_mul_param(self):
        """Test 18"""
        input = """Class TestMethoddecl{
                   
                    $parammethod(a, b, c : Int){

                    }
              }"""
        expect = "Program([ClassDecl(Id(TestMethoddecl),[MethodDecl(Id($parammethod),Static,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType)],Block([]))])])"
        self.assertTrue(TestAST.test(input, expect, 317))
    
    def test_method_with_mul_param_list(self):
        """Test 19"""
        input = """Class TestMethoddecl{
                   
                    $parammethod(a, b, c : Int ; mulPa, Tripba: Float){

                    }
              }"""
        expect = "Program([ClassDecl(Id(TestMethoddecl),[MethodDecl(Id($parammethod),Static,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType),param(Id(mulPa),FloatType),param(Id(Tripba),FloatType)],Block([]))])])"
        self.assertTrue(TestAST.test(input, expect, 318))
    
    def test_Construc_method(self):
        """Test 20"""
        input = """Class TestMethoddecl{
                   
                    Constructor(){

                    }
              }"""
        expect = "Program([ClassDecl(Id(TestMethoddecl),[MethodDecl(Id(Constructor),Instance,[],Block([]))])])"
        self.assertTrue(TestAST.test(input, expect, 319))
    
    def test_Construc_method_withparam(self):
        """Test 21"""
        input = """Class TestMethoddecl{
                   
                    Constructor(par: Int; floatLi, floatLi2: Float){

                    }
              }"""
        expect = "Program([ClassDecl(Id(TestMethoddecl),[MethodDecl(Id(Constructor),Instance,[param(Id(par),IntType),param(Id(floatLi),FloatType),param(Id(floatLi2),FloatType)],Block([]))])])"
        self.assertTrue(TestAST.test(input, expect, 320))
    
    def test_Destruct_method(self):
        """Test 22"""
        input = """Class TestMethoddecl{
                   
                    Destructor(){

                    }
              }"""
        expect = "Program([ClassDecl(Id(TestMethoddecl),[MethodDecl(Id(Destructor),Instance,[],Block([]))])])"
        self.assertTrue(TestAST.test(input, expect, 321))
    
    def test_Program_main(self):
        """Test 23"""
        input = """
        Class TestMain{
            main(){

            }
        }
        Class Program{
                   main(){

                   }
                    
              }"""
        expect = "Program([ClassDecl(Id(TestMain),[MethodDecl(Id(main),Instance,[],Block([]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([]))])])"
        self.assertTrue(TestAST.test(input, expect, 322))
    
    def test_Program_main_with_param(self):
        """Test 24"""
        input = """
        Class Program{
                   
                   main(Instan: Int; astPro: Boolean){

                   }
                    
              }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Instance,[param(Id(Instan),IntType),param(Id(astPro),BoolType)],Block([]))])])"
        self.assertTrue(TestAST.test(input, expect, 323))
    
    def test_Program_main_with_other_func(self):
        """Test 25"""
        input = """
        Class Program{
             test(paramm: Int){
                        
                    }
                   main(){

                   }
                    
              }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(test),Instance,[param(Id(paramm),IntType)],Block([])),MethodDecl(Id(main),Static,[],Block([]))])])"
        self.assertTrue(TestAST.test(input, expect, 324))
    
    def test_mix_mutable_and_immu_decl_with_value(self):
        """Test 26"""
        input = """Class TestMulImuAttr{
                Var abc, tes, $Immua : Int = 34, 56, 90;
                Val immuVa, $kalixianua, $Ukraina : Float = 1.23, 14.53, 0.01;
              }"""
        expect = "Program([ClassDecl(Id(TestMulImuAttr),[AttributeDecl(Instance,VarDecl(Id(abc),IntType,IntLit(34))),AttributeDecl(Instance,VarDecl(Id(tes),IntType,IntLit(56))),AttributeDecl(Static,VarDecl(Id($Immua),IntType,IntLit(90))),AttributeDecl(Instance,ConstDecl(Id(immuVa),FloatType,FloatLit(1.23))),AttributeDecl(Static,ConstDecl(Id($kalixianua),FloatType,FloatLit(14.53))),AttributeDecl(Static,ConstDecl(Id($Ukraina),FloatType,FloatLit(0.01)))])])"
        self.assertTrue(TestAST.test(input, expect, 325))
    
    def test_block_stmt(self):
        """Test 27"""
        input = """Class TestBlock{
                testBlock(){
                    {
                        
                    }
                }
              }"""
        expect = "Program([ClassDecl(Id(TestBlock),[MethodDecl(Id(testBlock),Instance,[],Block([Block([])]))])])"
        self.assertTrue(TestAST.test(input, expect, 326))
    
    def test_assign_stmt(self):
        """Test 28"""
        input = """Class TestBlock{
                testAssign_stmt(){
                        lhs = expr + expr2 - expr3 * expr4;
                }
              }"""
        expect = "Program([ClassDecl(Id(TestBlock),[MethodDecl(Id(testAssign_stmt),Instance,[],Block([AssignStmt(Id(lhs),BinaryOp(-,BinaryOp(+,Id(expr),Id(expr2)),BinaryOp(*,Id(expr3),Id(expr4))))]))])])"
        self.assertTrue(TestAST.test(input, expect, 327))
    
    def test_mul_assign_stmt(self):
        """Test 29"""
        input = """Class TestBlock{
                testAssign_stmt(){
                    {
                        lhs = expr + expr2 - expr3 * expr4;
                        string = "abc" +. "das";
                    }
                }
              }"""
        expect = "Program([ClassDecl(Id(TestBlock),[MethodDecl(Id(testAssign_stmt),Instance,[],Block([Block([AssignStmt(Id(lhs),BinaryOp(-,BinaryOp(+,Id(expr),Id(expr2)),BinaryOp(*,Id(expr3),Id(expr4)))),AssignStmt(Id(string),BinaryOp(+.,StringLit(abc),StringLit(das)))])]))])])"
        self.assertTrue(TestAST.test(input, expect, 328))
    
    def test_Self_assign_stmt(self):
        """Test 30"""
        input = """Class TestBlock{
                testAssign_stmt(){
                        Self.height = (4 + 67) % 2 * 56 / 10;
                        Self.width = (1254 %2 + 5 *4);
                }
              }"""
        expect = "Program([ClassDecl(Id(TestBlock),[MethodDecl(Id(testAssign_stmt),Instance,[],Block([AssignStmt(FieldAccess(Id(Self),Id(height)),BinaryOp(/,BinaryOp(*,BinaryOp(%,BinaryOp(+,IntLit(4),IntLit(67)),IntLit(2)),IntLit(56)),IntLit(10))),AssignStmt(FieldAccess(Id(Self),Id(width)),BinaryOp(+,BinaryOp(%,IntLit(1254),IntLit(2)),BinaryOp(*,IntLit(5),IntLit(4))))]))])])"
        self.assertTrue(TestAST.test(input, expect, 329))
    
    def test_if_stmt(self):
        """Test 31"""
        input = """Class TestIf_Stmt{
                If_stmt(){
                    {
                        If(ma == 0){
                            ma = 9999;
                        }
                    }
                }
              }"""
        expect = "Program([ClassDecl(Id(TestIf_Stmt),[MethodDecl(Id(If_stmt),Instance,[],Block([Block([If(BinaryOp(==,Id(ma),IntLit(0)),Block([AssignStmt(Id(ma),IntLit(9999))]))])]))])])"
        self.assertTrue(TestAST.test(input, expect, 330))
    
    def test_mul_if_stmt(self):
        """Test 32"""
        input = """Class TestIf_Stmt{
                If_stmt(){
                    
                        If(ma == 0){
                            ma = 9999;
                        }
                        
                         If(helloword ==. ("Hello" +. "World")){
                            result = True;
                        }
                    
                }
              }"""
        expect = "Program([ClassDecl(Id(TestIf_Stmt),[MethodDecl(Id(If_stmt),Instance,[],Block([If(BinaryOp(==,Id(ma),IntLit(0)),Block([AssignStmt(Id(ma),IntLit(9999))])),If(BinaryOp(==.,Id(helloword),BinaryOp(+.,StringLit(Hello),StringLit(World))),Block([AssignStmt(Id(result),BooleanLit(True))]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 331))

    def test_if_elseif_stmt(self):
        """Test 33"""
        input = """Class TestIf_Stmt{
                If_stmt(){
                    
                        If(ma == 0){
                            ma = 9999;
                        }
                        Elseif(ma == 456){
                            ma = 67.43524;
                        }
                    
                }
              }"""
        expect = "Program([ClassDecl(Id(TestIf_Stmt),[MethodDecl(Id(If_stmt),Instance,[],Block([If(BinaryOp(==,Id(ma),IntLit(0)),Block([AssignStmt(Id(ma),IntLit(9999))]),If(BinaryOp(==,Id(ma),IntLit(456)),Block([AssignStmt(Id(ma),FloatLit(67.43524))])))]))])])"
        self.assertTrue(TestAST.test(input, expect, 332))
    
    def test_if_mul_elseif_stmt(self):
        """Test 33"""
        input = """Class TestIf_Stmt{
                If_stmt(){
                    
                        If(ma == 0){
                            ma = 9999;
                        }
                        Elseif(ma == 456){
                            ma = 67.43524;
                        }
                        Elseif(ma == (1.234 + 234 * 54 % 2)/ 53){
                            ma = -1 *9999;
                        }
                    
                }
              }"""
        expect = "Program([ClassDecl(Id(TestIf_Stmt),[MethodDecl(Id(If_stmt),Instance,[],Block([If(BinaryOp(==,Id(ma),IntLit(0)),Block([AssignStmt(Id(ma),IntLit(9999))]),If(BinaryOp(==,Id(ma),IntLit(456)),Block([AssignStmt(Id(ma),FloatLit(67.43524))]),If(BinaryOp(==,Id(ma),BinaryOp(/,BinaryOp(+,FloatLit(1.234),BinaryOp(%,BinaryOp(*,IntLit(234),IntLit(54)),IntLit(2))),IntLit(53))),Block([AssignStmt(Id(ma),BinaryOp(*,UnaryOp(-,IntLit(1)),IntLit(9999)))]))))]))])])"
        self.assertTrue(TestAST.test(input, expect, 332))
    
    def test_if_mul_elseif_stmt_Else(self):
        """Test 34"""
        input = """Class TestIf_Stmt{
                If_stmt(){
                    
                        If(ma == 0){
                            ma = 9999;
                        }
                        Elseif(ma == 456){
                            ma = 67.43524;
                        }
                        Elseif(ma == (1.234 + 234 * 54 % 2)/ 53){
                            ma = -1 *9999;
                        }
                        Else{
                            ma = 87;
                        }
                    
                }
              }"""
        expect = "Program([ClassDecl(Id(TestIf_Stmt),[MethodDecl(Id(If_stmt),Instance,[],Block([If(BinaryOp(==,Id(ma),IntLit(0)),Block([AssignStmt(Id(ma),IntLit(9999))]),If(BinaryOp(==,Id(ma),IntLit(456)),Block([AssignStmt(Id(ma),FloatLit(67.43524))]),If(BinaryOp(==,Id(ma),BinaryOp(/,BinaryOp(+,FloatLit(1.234),BinaryOp(%,BinaryOp(*,IntLit(234),IntLit(54)),IntLit(2))),IntLit(53))),Block([AssignStmt(Id(ma),BinaryOp(*,UnaryOp(-,IntLit(1)),IntLit(9999)))]),Block([AssignStmt(Id(ma),IntLit(87))]))))]))])])"
        self.assertTrue(TestAST.test(input, expect, 333))

    def test_if_Else(self):
        """Test 35"""
        input = """Class TestIf_Stmt{
                If_stmt(){
                    
                        If(ma == 0){
                            ma = 9999;
                        }
                        Else{
                            ma = 87;
                        }
                    
                }
              }"""
        expect = "Program([ClassDecl(Id(TestIf_Stmt),[MethodDecl(Id(If_stmt),Instance,[],Block([If(BinaryOp(==,Id(ma),IntLit(0)),Block([AssignStmt(Id(ma),IntLit(9999))]),Block([AssignStmt(Id(ma),IntLit(87))]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 334))

    def test_if_Else(self):
        """Test 36"""
        input = """Class TestIf_Stmt{
                If_stmt(){
                    
                        If(ma == 0){
                            ma = 9999;
                        }
                        Else{
                        }

                        If(Ukrai ==. ("Ukraina will be peaceful")){
                            result = "I don't know";
                        }
                        Else{
                        }
                    
                }
              }"""
        expect = "Program([ClassDecl(Id(TestIf_Stmt),[MethodDecl(Id(If_stmt),Instance,[],Block([If(BinaryOp(==,Id(ma),IntLit(0)),Block([AssignStmt(Id(ma),IntLit(9999))]),Block([])),If(BinaryOp(==.,Id(Ukrai),StringLit(Ukraina will be peaceful)),Block([AssignStmt(Id(result),StringLit(I don't know))]),Block([]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 335))

    def test_if_Else_with_assign(self):
        """Test 37"""
        input = """Class TestIf_Stmt{
                TestIf_assign_stmt(){
                        Ukrai = "";
                        If(Ukrai ==. ("Ukraina will be peaceful")){
                            result = "I don't know";
                        }
                        Else{
                        }
                    
                }
              }"""
        expect = "Program([ClassDecl(Id(TestIf_Stmt),[MethodDecl(Id(TestIf_assign_stmt),Instance,[],Block([AssignStmt(Id(Ukrai),StringLit()),If(BinaryOp(==.,Id(Ukrai),StringLit(Ukraina will be peaceful)),Block([AssignStmt(Id(result),StringLit(I don't know))]),Block([]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 336))
    
    def test_if_Else_with_assign(self):
        """Test 38"""
        input = """Class TestIf_Stmt{
                TestIf_assign_stmt(){
                        Ukrai = "";
                        If(Ukrai ==. ("Ukraina will be peaceful")){
                            result = "I don't know";
                        }
                        Else{
                        }
                    
                }
              }"""
        expect = "Program([ClassDecl(Id(TestIf_Stmt),[MethodDecl(Id(TestIf_assign_stmt),Instance,[],Block([AssignStmt(Id(Ukrai),StringLit()),If(BinaryOp(==.,Id(Ukrai),StringLit(Ukraina will be peaceful)),Block([AssignStmt(Id(result),StringLit(I don't know))]),Block([]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 338))






















# import unittest
# from TestUtils import TestAST
# from AST import *


# class ASTGenSuite(unittest.TestCase):
#     def test_simple_program(self):
#         input = """Class Program {}"""
#         expect = "Program([ClassDecl(Id(Program),[])])"
#         self.assertTrue(TestAST.test(input, expect, 300))

#     def test_simple_program2(self):
#         input = """
#         Class Program { }
#         Class Test { }
#         """
#         expect = "Program([ClassDecl(Id(Program),[]),ClassDecl(Id(Test),[])])"
#         self.assertTrue(TestAST.test(input, expect, 301))

#     def test_simple_program3(self):
#         input = """
#         Class Test:FatherClass { }
#         """
#         expect = "Program([ClassDecl(Id(Test),Id(FatherClass),[])])"
#         self.assertTrue(TestAST.test(input, expect, 302))

#     def test_simple_funcdecl(self):
#         input = """
#         Class Program {
#             testFunc(My1stCons, My2ndCons: Int; MyFloat: Float) {}
#         }
#         """
#         expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(testFunc),Instance,[param(Id(My1stCons),IntType),param(Id(My2ndCons),IntType),param(Id(MyFloat),FloatType)],Block([]))])])"
#         self.assertTrue(TestAST.test(input, expect, 303))

#     def test_simple_vardecl(self):
#         input = """
#         Class Program {
#             Var a, $b: Int;
#         }
#         """
#         expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),IntType)),AttributeDecl(Static,VarDecl(Id($b),IntType))])])"
#         self.assertTrue(TestAST.test(input, expect, 304))

#     def test_simple_vardecl2(self):
#         input = """
#         Class Program {
#             Var a, b: Int = 12, 13;
#         }
#         """
#         expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),IntType,IntLit(12))),AttributeDecl(Instance,VarDecl(Id(b),IntType,IntLit(13)))])])"
#         self.assertTrue(TestAST.test(input, expect, 305))

#     def test_simple_valdecl(self):
#         input = """
#         Class Program {
#             Val c, $d: Int;
#         }
#         """
#         expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(c),IntType,None)),AttributeDecl(Static,ConstDecl(Id($d),IntType,None))])])"
#         self.assertTrue(TestAST.test(input, expect, 306))

#     def test_simple_valdecl2(self):
#         input = """
#         Class Program {
#             Val c, d, e: Int = 12, 13, 10;
#         }
#         """
#         expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(c),IntType,IntLit(12))),AttributeDecl(Instance,ConstDecl(Id(d),IntType,IntLit(13))),AttributeDecl(Instance,ConstDecl(Id(e),IntType,IntLit(10)))])])"
#         self.assertTrue(TestAST.test(input, expect, 307))

#     def test_simple_valdecl3(self):
#         input = """
#         Class Program {
#             Var a: Int = 3 + 2;
#         }
#         """
#         expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),IntType,BinaryOp(+,IntLit(3),IntLit(2))))])])"
#         self.assertTrue(TestAST.test(input, expect, 308))

#     def test_simple_valdecl4(self):  # nhan chia truoc
#         input = """
#         Class Program {
#             Var a: Int = 5 + 3 * 2;
#         }
#         """
#         expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),IntType,BinaryOp(+,IntLit(5),BinaryOp(*,IntLit(3),IntLit(2)))))])])"
#         self.assertTrue(TestAST.test(input, expect, 309))

#     def test_simple_valdecl5(self):  # dau ngoac truoc
#         input = """
#         Class Program {
#             Var a: Int = (5 + 3) * 2;
#         }
#         """
#         expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),IntType,BinaryOp(*,BinaryOp(+,IntLit(5),IntLit(3)),IntLit(2))))])])"
#         self.assertTrue(TestAST.test(input, expect, 310))

#     def test_exp(self):  # fun
#         input = """
#         Class Program {
#             Var a: Int = Self.b;
#         }
#         """
#         expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),IntType,FieldAccess(Id(Self),Id(b))))])])"
#         self.assertTrue(TestAST.test(input, expect, 311))

#     def test_assign_stmt(self):
#         input = """
#         Class Program {
#             testFun() {
#                 a = b;
#             }
#         }
#         """
#         expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(testFun),Instance,[],Block([AssignStmt(Id(a),Id(b))]))])])"
#         self.assertTrue(TestAST.test(input, expect, 312))

#     def test_for_stmt(self):
#         input = """
#         Class Program {
#             testFun() {
#                 Foreach (a In 1 .. 100 By 2) {
#                         a = a + 3;
#                 }
#             }
#         }
#         """
#         expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(testFun),Instance,[],Block([For(Id(a),IntLit(1),IntLit(100),IntLit(2),Block([AssignStmt(Id(a),BinaryOp(+,Id(a),IntLit(3)))])])]))])])"
#         self.assertTrue(TestAST.test(input, expect, 313))

#     def test_return_stmt(self):
#         input = """
#         Class Program {
#             testFun() {
#                 Return;
#             }
#         }
#         """
#         expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(testFun),Instance,[],Block([Return()]))])])"
#         self.assertTrue(TestAST.test(input, expect, 314))

#     def test_return_stmt2(self):
#         input = """
#         Class Program {
#             testFun() {
#                 Return 5;
#             }
#         }
#         """
#         expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(testFun),Instance,[],Block([Return(IntLit(5))]))])])"
#         self.assertTrue(TestAST.test(input, expect, 315))

#     def test_break_stmt(self):
#         input = """
#         Class Program {
#             testFun() {
#                 Foreach (a In 1 .. 100 By 2) {
#                         a = a + 3;
#                         Break;
#                 }
#             }
#         }
#         """
#         expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(testFun),Instance,[],Block([For(Id(a),IntLit(1),IntLit(100),IntLit(2),Block([AssignStmt(Id(a),BinaryOp(+,Id(a),IntLit(3))),Break])])]))])])"
#         self.assertTrue(TestAST.test(input, expect, 316))

#     def test_continue_stmt(self):
#         input = """
#         Class Program {
#             testFun() {
#                 Foreach (a In 1 .. 100 By 2) {
#                         a = a + 3;
#                         Continue;
#                 }
#             }
#         }
#         """
#         expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(testFun),Instance,[],Block([For(Id(a),IntLit(1),IntLit(100),IntLit(2),Block([AssignStmt(Id(a),BinaryOp(+,Id(a),IntLit(3))),Continue])])]))])])"
#         self.assertTrue(TestAST.test(input, expect, 317))

#     def test_member_access_stmt(self):
#         input = """
#         Class Program {
#             testFun() {
#                 obj.getName(12, 3);
#             }
#         }
#         """
#         expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(testFun),Instance,[],Block([Call(Id(obj),Id(getName),[IntLit(12),IntLit(3)])]))])])"
#         self.assertTrue(TestAST.test(input, expect, 318))

#     def test_field_access(self):
#         input = """
#         Class Program {
#             testFun() {
#                 c = a.b;
#                 c = Self.b;
#                 c = a::$b;
#             }
#         }
#         """
#         expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(testFun),Instance,[],Block([AssignStmt(Id(c),FieldAccess(Id(a),Id(b))),AssignStmt(Id(c),FieldAccess(Id(Self),Id(b))),AssignStmt(Id(c),FieldAccess(Id(a),Id($b)))]))])])"
#         self.assertTrue(TestAST.test(input, expect, 319))

#     def test_call_expr(self):
#         input = """
#         Class Program {
#             testFun() {
#                 c = a::$b();
#                 c = a.b();
#                 a.b(3, 4);
#                 a::$b();
#             }
#         }
#         """
#         expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(testFun),Instance,[],Block([AssignStmt(Id(c),CallExpr(Id(a),Id($b),[])),AssignStmt(Id(c),CallExpr(Id(a),Id(b),[])),Call(Id(a),Id(b),[IntLit(3),IntLit(4)]),Call(Id(a),Id($b),[])]))])])"
#         self.assertTrue(TestAST.test(input, expect, 320))

#     def test_vardecl_stmt(self):
#         input = """
#         Class Program {
#             testFun() {
#                 Var a: Int = 12;
#             }
#         }
#         """
#         expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(testFun),Instance,[],Block([AttributeDecl(Instance,VarDecl(Id(a),IntType,IntLit(12)))]))])])"
#         self.assertTrue(TestAST.test(input, expect, 321))

#     def test_if_stmt(self):
#         input = """
#         Class Program {
#             testFun() {
#                 If (a > b) {
#                     a = a + 1;
#                 }
#                 Else {
#                     a = a - 1;
#                 }
#             }
#         }
#         """
#         expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(testFun),Instance,[],Block([If(BinaryOp(>,Id(a),Id(b)),Block([AssignStmt(Id(a),BinaryOp(+,Id(a),IntLit(1)))]),Block([AssignStmt(Id(a),BinaryOp(-,Id(a),IntLit(1)))]))]))])])"
#         self.assertTrue(TestAST.test(input, expect, 322))

#     def test_if_stmt2(self):
#         input = """
#         Class Program {
#             testFun() {
#                 If (a > b) {
#                     a = a + 1;
#                 }
#                 Elseif (a < b) {
#                     a = a - 1;
#                 }
#                 Else {
#                     a = a * 2;
#                 }
#             }
#         }
#         """
#         expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(testFun),Instance,[],Block([If(BinaryOp(>,Id(a),Id(b)),Block([AssignStmt(Id(a),BinaryOp(+,Id(a),IntLit(1)))]),If(BinaryOp(<,Id(a),Id(b)),Block([AssignStmt(Id(a),BinaryOp(-,Id(a),IntLit(1)))]),Block([AssignStmt(Id(a),BinaryOp(*,Id(a),IntLit(2)))])))]))])])"
#         self.assertTrue(TestAST.test(input, expect, 323))

#     def test_constructor_decl(self):
#         input = """Class Program {
#             Constructor() {}
#         }
#         """
#         expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(Constructor),Instance,[],Block([]))])])"
#         self.assertTrue(TestAST.test(input, expect, 324))

#     def test_destructor_decl(self):
#         input = """Class Program {
#             Destructor() {}
#         }
#         """
#         expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(Destructor),Instance,[],Block([]))])])"
#         self.assertTrue(TestAST.test(input, expect, 325))

#     def test_constructor_with_other_func(self):
#         input = """Class A {
#             Constructor() {}
#             MyTest() {
#                 Foreach (var1 In 50 .. 100 By 5) {
#                     Break;
#                 }
#             }
#         }"""
#         expect = "Program([ClassDecl(Id(A),[MethodDecl(Id(Constructor),Instance,[],Block([])),MethodDecl(Id(MyTest),Instance,[],Block([For(Id(var1),IntLit(50),IntLit(100),IntLit(5),Block([Break])])]))])])"
#         self.assertTrue(TestAST.test(input, expect, 326))

#     def test_destructor_with_other_func(self):
#         input = """Class A {
#             MyTest() {
#                 Var a: Int;
#                 Var b: Float = 0.2;
#             }
#             Destructor() {}
#         }"""
#         expect = "Program([ClassDecl(Id(A),[MethodDecl(Id(MyTest),Instance,[],Block([AttributeDecl(Instance,VarDecl(Id(a),IntType)),AttributeDecl(Instance,VarDecl(Id(b),FloatType,FloatLit(0.2)))])),MethodDecl(Id(Destructor),Instance,[],Block([]))])])"
#         self.assertTrue(TestAST.test(input, expect, 327))

#     def test_var_decl_with_some_type(self):
#         input = """Class A {
#             MyTest() {
#                 Var a: Int = 5;
#                 Var b: Float = 3.5;
#                 Var c: String = "Hello";
#                 Var d: Boolean = True;
#             }
#         }"""
#         expect = "Program([ClassDecl(Id(A),[MethodDecl(Id(MyTest),Instance,[],Block([AttributeDecl(Instance,VarDecl(Id(a),IntType,IntLit(5))),AttributeDecl(Instance,VarDecl(Id(b),FloatType,FloatLit(3.5))),AttributeDecl(Instance,VarDecl(Id(c),StringType,StringLit(Hello))),AttributeDecl(Instance,VarDecl(Id(d),BoolType,BooleanLit(True)))]))])])"
#         self.assertTrue(TestAST.test(input, expect, 328))

#     def test_var_with_arr_type(self):
#         input = """Class A {
#             MyTest() {
#                 Var myArray: Array[Int, 5] = Array(1, 3, 5, 7, 9);
#             }
#         }"""
#         expect = "Program([ClassDecl(Id(A),[MethodDecl(Id(MyTest),Instance,[],Block([AttributeDecl(Instance,VarDecl(Id(myArray),ArrayType(5,IntType),[IntLit(1),IntLit(3),IntLit(5),IntLit(7),IntLit(9)]))]))])])"
#         self.assertTrue(TestAST.test(input, expect, 329))

#     def test_for_stmt_without_by(self):
#         input = """Class Program {
#             main() {
#                 Foreach (var1 In 0 .. 10) {
#                     Val myStr: String = "Hello World";
#                 }
#             }
#         }"""
#         expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([For(Id(var1),IntLit(0),IntLit(10),IntLit(1),Block([AttributeDecl(Instance,ConstDecl(Id(myStr),StringType,StringLit(Hello World)))])])]))])])"
#         self.assertTrue(TestAST.test(input, expect, 330))

#     def test_block_stmt_inside_block(self):
#         input = """Class Program {
#             main() {
#                 {
#                     { Val a, b: Int; }
#                 }
#             }
#         }"""
#         expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Block([Block([AttributeDecl(Instance,ConstDecl(Id(a),IntType,None)),AttributeDecl(Instance,ConstDecl(Id(b),IntType,None))])])]))])])"
#         self.assertTrue(TestAST.test(input, expect, 331))

#     def test_exp_order(self):
#         input = """Class Program {
#             Val a: Int = 3 + 4 * 5;
#             Val b: Int = (1 + 2) * 6;
#         }"""
#         expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,BinaryOp(+,IntLit(3),BinaryOp(*,IntLit(4),IntLit(5))))),AttributeDecl(Instance,ConstDecl(Id(b),IntType,BinaryOp(*,BinaryOp(+,IntLit(1),IntLit(2)),IntLit(6))))])])"
#         self.assertTrue(TestAST.test(input, expect, 332))

#     def test_random_mixing(self):
#         input = """Class Program {
#             main() {
#                 Var r, s: Int;
#                 r = 2;
#                 Var a, b: Array[Int, 5];
#                 s = r * r * Self.myPI;
#                 a[0] = s;
#             }
#         }"""
#         expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AttributeDecl(Instance,VarDecl(Id(r),IntType)),AttributeDecl(Instance,VarDecl(Id(s),IntType)),AssignStmt(Id(r),IntLit(2)),AttributeDecl(Instance,VarDecl(Id(a),ArrayType(5,IntType))),AttributeDecl(Instance,VarDecl(Id(b),ArrayType(5,IntType))),AssignStmt(Id(s),BinaryOp(*,BinaryOp(*,Id(r),Id(r)),FieldAccess(Id(Self),Id(myPI)))),AssignStmt(ArrayCell(Id(a),[IntLit(0)]),Id(s))]))])])"
#         self.assertTrue(TestAST.test(input, expect, 333))

#     def test_main_empty(self):
#         input = """Class Program{
#                 main(){

#                 }
#              }
#              """
#         expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([]))])])"
#         self.assertTrue(TestAST.test(input, expect, 334))

#     def test_main_with_other_main(self):
#         input = """Class Program {
#                     main(){

#                     }
#                 }
#                 Class testClass {
#                     main() { }
#                 }
#             """
#         expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([]))]),ClassDecl(Id(testClass),[MethodDecl(Id(main),Instance,[],Block([]))])])"
#         self.assertTrue(TestAST.test(input, expect, 335))

#     def test_main_with_param(self):
#         input = """Class Program {
#                     main(a: Int) {

#                     }
#                 }
#             """
#         expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Instance,[param(Id(a),IntType)],Block([]))])])"
#         self.assertTrue(TestAST.test(input, expect, 336))

#     def test_if_stmt3(self):
#         input = """Class Shape {
#                     testFunc() {
#                         If (a > b) {
#                             a = b;
#                         }
#                         Elseif (a < b) {
#                             c = d;
#                         }
#                         Elseif (a == b) {
#                             e = f;
#                         }
#                     }
#                 }
#             """
#         expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id(testFunc),Instance,[],Block([If(BinaryOp(>,Id(a),Id(b)),Block([AssignStmt(Id(a),Id(b))]),If(BinaryOp(<,Id(a),Id(b)),Block([AssignStmt(Id(c),Id(d))]),If(BinaryOp(==,Id(a),Id(b)),Block([AssignStmt(Id(e),Id(f))]))))]))])])"
#         self.assertTrue(TestAST.test(input, expect, 337))

#     def test_if_stmt4(self):
#         input = """Class Shape {
#                     testFunc() {
#                         If (a > b) {
#                             a = b;
#                         }
#                         Elseif (a < b) {
#                             c = d;
#                         }
#                         Elseif (a == b) {
#                             e = f;
#                         }
#                         Else {
#                             g = h;
#                         }
#                     }
#                 }
#             """
#         expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id(testFunc),Instance,[],Block([If(BinaryOp(>,Id(a),Id(b)),Block([AssignStmt(Id(a),Id(b))]),If(BinaryOp(<,Id(a),Id(b)),Block([AssignStmt(Id(c),Id(d))]),If(BinaryOp(==,Id(a),Id(b)),Block([AssignStmt(Id(e),Id(f))]),Block([AssignStmt(Id(g),Id(h))]))))]))])])"
#         self.assertTrue(TestAST.test(input, expect, 338))

#     def test_return_stmt3(self):
#         input = """Class Shape {
#                     testFunc() {
#                         Return Circle::$getArea();
#                     }
#                 }
#             """
#         expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id(testFunc),Instance,[],Block([Return(CallExpr(Id(Circle),Id($getArea),[]))]))])])"
#         self.assertTrue(TestAST.test(input, expect, 339))

#     def test_string_exp(self):
#         input = """Class Shape {
#                     testFunc() {
#                         Var a: String;
#                         a = a +. "hello";
#                         Return a;
#                     }
#                 }
#             """
#         expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id(testFunc),Instance,[],Block([AttributeDecl(Instance,VarDecl(Id(a),StringType)),AssignStmt(Id(a),BinaryOp(+.,Id(a),StringLit(hello))),Return(Id(a))]))])])"
#         self.assertTrue(TestAST.test(input, expect, 340))

#     def test_string_exp2(self):
#         input = """Class Shape {
#                     testFunc() {
#                         Var a: String;
#                         Return (a ==. "hello");
#                     }
#                 }
#             """
#         expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id(testFunc),Instance,[],Block([AttributeDecl(Instance,VarDecl(Id(a),StringType)),Return(BinaryOp(==.,Id(a),StringLit(hello)))]))])])"
#         self.assertTrue(TestAST.test(input, expect, 341))

#     def test_logic_exp(self):
#         input = """Class Shape {
#                     testFunc() {
#                         Var a: Boolean;
#                         a = (1 == 2) || (3 == 4);
#                         Return a;
#                     }
#                 }
#             """
#         expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id(testFunc),Instance,[],Block([AttributeDecl(Instance,VarDecl(Id(a),BoolType)),AssignStmt(Id(a),BinaryOp(||,BinaryOp(==,IntLit(1),IntLit(2)),BinaryOp(==,IntLit(3),IntLit(4)))),Return(Id(a))]))])])"
#         self.assertTrue(TestAST.test(input, expect, 342))

#     def test_add_sub_exp(self):
#         input = """Class Shape {
#                     testFunc() {
#                         Var a: Int;
#                         a = 1 + (2 - 3);
#                         a = 5 + 6 - 7;
#                         Return a;
#                     }
#                 }
#             """
#         expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id(testFunc),Instance,[],Block([AttributeDecl(Instance,VarDecl(Id(a),IntType)),AssignStmt(Id(a),BinaryOp(+,IntLit(1),BinaryOp(-,IntLit(2),IntLit(3)))),AssignStmt(Id(a),BinaryOp(-,BinaryOp(+,IntLit(5),IntLit(6)),IntLit(7))),Return(Id(a))]))])])"
#         self.assertTrue(TestAST.test(input, expect, 343))

#     def test_mul_div_exp(self):
#         input = """Class Shape {
#                     testFunc() {
#                         Var a: Int;
#                         a = 1 * (2 / 3);
#                         a = 5 * 6 / 7;
#                         a = 12 % 4;
#                         Return a;
#                     }
#                 }
#             """
#         expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id(testFunc),Instance,[],Block([AttributeDecl(Instance,VarDecl(Id(a),IntType)),AssignStmt(Id(a),BinaryOp(*,IntLit(1),BinaryOp(/,IntLit(2),IntLit(3)))),AssignStmt(Id(a),BinaryOp(/,BinaryOp(*,IntLit(5),IntLit(6)),IntLit(7))),AssignStmt(Id(a),BinaryOp(%,IntLit(12),IntLit(4))),Return(Id(a))]))])])"
#         self.assertTrue(TestAST.test(input, expect, 344))

#     def test_not_exp(self):
#         input = """Class Shape {
#                     testFunc() {
#                         Var a: Boolean;
#                         a = !(1 == 2);
#                         Return a;
#                     }
#                 }
#             """
#         expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id(testFunc),Instance,[],Block([AttributeDecl(Instance,VarDecl(Id(a),BoolType)),AssignStmt(Id(a),UnaryOp(!,BinaryOp(==,IntLit(1),IntLit(2)))),Return(Id(a))]))])])"
#         self.assertTrue(TestAST.test(input, expect, 345))

#     def test_sub_unary_exp(self):
#         input = """Class Shape {
#                     testFunc() {
#                         Var a: Int;
#                         a = -(1 + 2);
#                         Return a;
#                     }
#                 }
#             """
#         expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id(testFunc),Instance,[],Block([AttributeDecl(Instance,VarDecl(Id(a),IntType)),AssignStmt(Id(a),UnaryOp(-,BinaryOp(+,IntLit(1),IntLit(2)))),Return(Id(a))]))])])"
#         self.assertTrue(TestAST.test(input, expect, 346))

#     def test_index_op(self):
#         input = """Class Shape {
#                     testFunc() {
#                         Var arr: Array[Int, 3] = Array(1, 2, 3);
#                         a = a[1];
#                         Return a;
#                     }
#                 }
#             """
#         expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id(testFunc),Instance,[],Block([AttributeDecl(Instance,VarDecl(Id(arr),ArrayType(3,IntType),[IntLit(1),IntLit(2),IntLit(3)])),AssignStmt(Id(a),ArrayCell(Id(a),[IntLit(1)])),Return(Id(a))]))])])"
#         self.assertTrue(TestAST.test(input, expect, 347))

#     # def test_index_op2(self):
#     #     input = """Class Shape {
#     #                 testFunc() {
#     #                     a = arr[1][2][3];
#     #                 }
#     #             }
#     #         """
#     #     expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id(testFunc),Instance,[],Block([AssignStmt(Id(a),ArrayCell(ArrayCell(ArrayCell(Id(arr),[IntLit(1)]),[IntLit(2)]),[IntLit(3)]))]))])])"
#     #     self.assertTrue(TestAST.test(input, expect, 348))

#     # def test_new_exp(self):
#     #     input = """Class Test {
#     #         Var myVar1: Shape = New Shape();
#     #     }
#     #         """
#     #     expect = "Program([ClassDecl(Id(Test),[AttributeDecl(Instance,VarDecl(Id(myVar1),Shape,NewExpr(Id(Shape),[])))])])"
#     #     self.assertTrue(TestAST.test(input, expect, 349))

#     def test_self_exp(self):
#         input = """Class Test {
#             Var myVar1: String = Self.name;
#         }
#             """
#         expect = "Program([ClassDecl(Id(Test),[AttributeDecl(Instance,VarDecl(Id(myVar1),StringType,FieldAccess(Id(Self),Id(name))))])])"
#         self.assertTrue(TestAST.test(input, expect, 350))

#     def test_random_mixing2(self):
#         input = """Class Test {
#             Var myVar1: String = "Hello " + Self.name + "!";
#         }
#             """
#         expect = "Program([ClassDecl(Id(Test),[AttributeDecl(Instance,VarDecl(Id(myVar1),StringType,BinaryOp(+,BinaryOp(+,StringLit(Hello ),FieldAccess(Id(Self),Id(name))),StringLit(!))))])])"
#         self.assertTrue(TestAST.test(input, expect, 351))

#     def test_random_mixing3(self):
#         input = """Class Test {
#             testFunc() { }
#             main() { }
#         }
#         Class Program {
#             testFunc2() { }
#             main() { }
#         }
#             """
#         expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(testFunc),Instance,[],Block([])),MethodDecl(Id(main),Instance,[],Block([]))]),ClassDecl(Id(Program),[MethodDecl(Id(testFunc2),Instance,[],Block([])),MethodDecl(Id(main),Static,[],Block([]))])])"
#         self.assertTrue(TestAST.test(input, expect, 352))

#     def test_random_mixing4(self):
#         input = """Class Test {
#             testFunc() { }
#             main() { }
#         }
#         Class Program {
#             testFunc2() { }
#             main() { }
#         }
#         Class Program2 {
#             testFunc3() { }
#             main() { }
#         }
#             """
#         expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id(testFunc),Instance,[],Block([])),MethodDecl(Id(main),Instance,[],Block([]))]),ClassDecl(Id(Program),[MethodDecl(Id(testFunc2),Instance,[],Block([])),MethodDecl(Id(main),Static,[],Block([]))]),ClassDecl(Id(Program2),[MethodDecl(Id(testFunc3),Instance,[],Block([])),MethodDecl(Id(main),Instance,[],Block([]))])])"
#         self.assertTrue(TestAST.test(input, expect, 353))

#     def test_random_mixing5(self):
#         input = """Class Test {
#             $getNumOfShape(My1stCons, My2ndCons: Int; MyFloat: Float) {
#                 If(3 > 2) {My1stCons = 3 + 6;}
#                 Else {My1stCons = 99;}
#             }
#         }"""
#         expect = "Program([ClassDecl(Id(Test),[MethodDecl(Id($getNumOfShape),Static,[param(Id(My1stCons),IntType),param(Id(My2ndCons),IntType),param(Id(MyFloat),FloatType)],Block([If(BinaryOp(>,IntLit(3),IntLit(2)),Block([AssignStmt(Id(My1stCons),BinaryOp(+,IntLit(3),IntLit(6)))]),Block([AssignStmt(Id(My1stCons),IntLit(99))]))]))])])"
#         self.assertTrue(TestAST.test(input, expect, 354))

#     def test_random_mixing6(self):
#         input = """Class Shape {
#             Val $numOfShape: Int = 0;
#             Val immutableAttribute: Int = 0;
#             Var length, width: Int;
#             $getNumOfShape() {

#             }
#         }
#         """
#         expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($numOfShape),IntType,IntLit(0))),AttributeDecl(Instance,ConstDecl(Id(immutableAttribute),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(length),IntType)),AttributeDecl(Instance,VarDecl(Id(width),IntType)),MethodDecl(Id($getNumOfShape),Static,[],Block([]))])])"
#         self.assertTrue(TestAST.test(input, expect, 355))

#     def test_random_mixing7(self):
#         input = """Class Shape {
#             Var a, b, c: Int = 1, 2, 3;
#             $testFunc() {
#                 Foreach (a In 1 .. 100 By 2) {
#                     a = a + 3;
#                 }
#                 b = a * 2;
#             }
#         }
#         Class Program {
#             main() {
#                 Shape::$testFunc();
#             }
#         }
#         """
#         expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Instance,VarDecl(Id(a),IntType,IntLit(1))),AttributeDecl(Instance,VarDecl(Id(b),IntType,IntLit(2))),AttributeDecl(Instance,VarDecl(Id(c),IntType,IntLit(3))),MethodDecl(Id($testFunc),Static,[],Block([For(Id(a),IntLit(1),IntLit(100),IntLit(2),Block([AssignStmt(Id(a),BinaryOp(+,Id(a),IntLit(3)))])]),AssignStmt(Id(b),BinaryOp(*,Id(a),IntLit(2)))]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(Shape),Id($testFunc),[])]))])])"
#         self.assertTrue(TestAST.test(input, expect, 356))

#     def test_random_mixing8(self):
#         input = """Class Program {
#             Var a, b, c: Int = 1, 2 ,3;
#             main() { }
#             testFunc() {
#                 Foreach (i In 0 .. 12 By 3)
#                 {
#                     x = x * x + (3/2)*x + 9;
#                 }
#             }
#         }
#         """
#         expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),IntType,IntLit(1))),AttributeDecl(Instance,VarDecl(Id(b),IntType,IntLit(2))),AttributeDecl(Instance,VarDecl(Id(c),IntType,IntLit(3))),MethodDecl(Id(main),Static,[],Block([])),MethodDecl(Id(testFunc),Instance,[],Block([For(Id(i),IntLit(0),IntLit(12),IntLit(3),Block([AssignStmt(Id(x),BinaryOp(+,BinaryOp(+,BinaryOp(*,Id(x),Id(x)),BinaryOp(*,BinaryOp(/,IntLit(3),IntLit(2)),Id(x))),IntLit(9)))])])]))])])"
#         self.assertTrue(TestAST.test(input, expect, 357))

#     def test_random_mixing9(self):
#         input = """
#         Class Shape {
#             Var a, b, c: Int = 1, 2 ,3;
#             $testFunc() {
#                 Foreach (i In 0 .. 12 By 3)
#                 {
#                     x = i + 1;
#                     Break;
#                 }
#             }
#         }
#         ## Class Program {
#             main () { }
#         } ##
#         """
#         expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Instance,VarDecl(Id(a),IntType,IntLit(1))),AttributeDecl(Instance,VarDecl(Id(b),IntType,IntLit(2))),AttributeDecl(Instance,VarDecl(Id(c),IntType,IntLit(3))),MethodDecl(Id($testFunc),Static,[],Block([For(Id(i),IntLit(0),IntLit(12),IntLit(3),Block([AssignStmt(Id(x),BinaryOp(+,Id(i),IntLit(1))),Break])])]))])])"
#         self.assertTrue(TestAST.test(input, expect, 358))

#     def test_random_mixing10(self):
#         input = """
#         Class Shape {
#             testFunc() {
#                 str = "$ $ $ @@ ***" +. "(0)_(0)";
#             }
#         }
#         """
#         expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id(testFunc),Instance,[],Block([AssignStmt(Id(str),BinaryOp(+.,StringLit($ $ $ @@ ***),StringLit((0)_(0))))]))])])"
#         self.assertTrue(TestAST.test(input, expect, 359))

#     def test_random_mixing11(self):
#         input = """
#         Class Shape {
#             testFunc() { }
#         }
#         Class Circle: Shape {

#         }
#         Class Rectangle: Shape {
        
#         }
#         Class myChild: Circle {

#         }
#         """
#         expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id(testFunc),Instance,[],Block([]))]),ClassDecl(Id(Circle),Id(Shape),[]),ClassDecl(Id(Rectangle),Id(Shape),[]),ClassDecl(Id(myChild),Id(Circle),[])])"
#         self.assertTrue(TestAST.test(input, expect, 360))

#     def test_empty_if_else(self):
#         input = """
#         Class A {
#             func() {
#                 If (a > b) {

#                 }
#                 Elseif (c <= d)
#                 {

#                 }
#                 Elseif (e >= f)
#                 {

#                 }
#                 Else {

#                 }
#             }
#         }
#         """
#         expect = "Program([ClassDecl(Id(A),[MethodDecl(Id(func),Instance,[],Block([If(BinaryOp(>,Id(a),Id(b)),Block([]),If(BinaryOp(<=,Id(c),Id(d)),Block([]),If(BinaryOp(>=,Id(e),Id(f)),Block([]),Block([]))))]))])])"
#         self.assertTrue(TestAST.test(input, expect, 361))
