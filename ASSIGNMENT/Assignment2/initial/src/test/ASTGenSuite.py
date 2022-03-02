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
        expect = "Program([ClassDecl(Id(TestBlock),[MethodDecl(Id(testAssign_stmt),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(height)),BinaryOp(/,BinaryOp(*,BinaryOp(%,BinaryOp(+,IntLit(4),IntLit(67)),IntLit(2)),IntLit(56)),IntLit(10))),AssignStmt(FieldAccess(Self(),Id(width)),BinaryOp(+,BinaryOp(%,IntLit(1254),IntLit(2)),BinaryOp(*,IntLit(5),IntLit(4))))]))])])"
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

    def test_if_Elseif_with_assign(self):
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
    
    def test_if_Elseif_nested(self):
        """Test 38"""
        input = """Class TestIf_Stmt{
                TestIf_Nested(){
                        If(Today == "0203"){
                            If(Tomorow ==. "None"){
                                
                            }
                            Elseif(Yesterday == 4){
                                
                            }
                            Else{

                            }
                        }
                        Else{
                            ma = 123;
                        }
                    
                }
              }"""
        expect = "Program([ClassDecl(Id(TestIf_Stmt),[MethodDecl(Id(TestIf_Nested),Instance,[],Block([If(BinaryOp(==,Id(Today),StringLit(0203)),Block([If(BinaryOp(==.,Id(Tomorow),StringLit(None)),Block([]),If(BinaryOp(==,Id(Yesterday),IntLit(4)),Block([]),Block([])))]),Block([AssignStmt(Id(ma),IntLit(123))]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 337))
    
    def test_if_Elseif_nested2(self):
        """Test 39"""
        input = """Class TestIf_Stmt{
                TestIf_Nested(){
                        If(Today == "0203"){
                            If(Tomorow ==. "None"){
                                If(a == 2){ }
                            }
                            Elseif(Yesterday == 4){}
                            Else{ }
                        }
                        Elseif(b == 7){
                            If(g == 9.81){}
                        }
                        Else{  ma = 123; }
                    
                }
              }"""
        expect = "Program([ClassDecl(Id(TestIf_Stmt),[MethodDecl(Id(TestIf_Nested),Instance,[],Block([If(BinaryOp(==,Id(Today),StringLit(0203)),Block([If(BinaryOp(==.,Id(Tomorow),StringLit(None)),Block([If(BinaryOp(==,Id(a),IntLit(2)),Block([]))]),If(BinaryOp(==,Id(Yesterday),IntLit(4)),Block([]),Block([])))]),If(BinaryOp(==,Id(b),IntLit(7)),Block([If(BinaryOp(==,Id(g),FloatLit(9.81)),Block([]))]),Block([AssignStmt(Id(ma),IntLit(123))])))]))])])"
        self.assertTrue(TestAST.test(input, expect, 338))
    
    def test_if_Elseif_nested3(self):
        """Test 40"""
        input = """Class TestIf_Stmt{
                TestIf_Nested(){
                        If(Today == "0203"){
                            If(Tomorow ==. "None"){
                                If(a == 2){ }
                            }
                            Elseif(Yesterday == 4){}
                            Else{ }
                        }
                        Elseif(b == 7){
                            If(g == 9.81){}
                            Else{}
                            If(fals ==. "False"){}
                            Elseif(true == "True"){}
                        }
                        Else{  ma = 123; }
                    
                }
              }"""
        expect = "Program([ClassDecl(Id(TestIf_Stmt),[MethodDecl(Id(TestIf_Nested),Instance,[],Block([If(BinaryOp(==,Id(Today),StringLit(0203)),Block([If(BinaryOp(==.,Id(Tomorow),StringLit(None)),Block([If(BinaryOp(==,Id(a),IntLit(2)),Block([]))]),If(BinaryOp(==,Id(Yesterday),IntLit(4)),Block([]),Block([])))]),If(BinaryOp(==,Id(b),IntLit(7)),Block([If(BinaryOp(==,Id(g),FloatLit(9.81)),Block([]),Block([])),If(BinaryOp(==.,Id(fals),StringLit(False)),Block([]),If(BinaryOp(==,Id(true),StringLit(True)),Block([])))]),Block([AssignStmt(Id(ma),IntLit(123))])))]))])])"
        self.assertTrue(TestAST.test(input, expect, 339))

    def test_forin_stmt(self):
        """Test 41"""
        input = """
            Class Program{
                main(){
                    Foreach(i In 1 .. 100 By 3){

                    }
                }
            }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([For(Id(i),IntLit(1),IntLit(100),IntLit(3),Block([])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 340))
    
    def test_forin_stmt_without_literate(self):
     """Test 42"""
     input = """
        Class Program{
                main(){
                    Foreach(i In 1 .. 100 ){

                    }
                }
            }
     """
     expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([For(Id(i),IntLit(1),IntLit(100),IntLit(1),Block([])])]))])])"
     self.assertTrue(TestAST.test(input, expect, 341))
    
    def test_forin_stmt_multiple(self):
     """Test 43"""
     input = """
        Class Program{
                main(){
                    Foreach(i In 1 .. 100 ){

                    }
                    Foreach(xx In 99 .. 999 By 3){

                    }
                }
            }
     """
     expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([For(Id(i),IntLit(1),IntLit(100),IntLit(1),Block([])]),For(Id(xx),IntLit(99),IntLit(999),IntLit(3),Block([])])]))])])"
     self.assertTrue(TestAST.test(input, expect, 342))
    
    def test_Foreach_nested(self):
     """Test 44"""
     input = """
        Class ForNested{
            forPro(){
                Foreach(x In 1 .. 100 By 3){
                    Foreach(sad In 1 .. 10 By 2){

                    }
                }
            }
        }
     """
     expect = "Program([ClassDecl(Id(ForNested),[MethodDecl(Id(forPro),Instance,[],Block([For(Id(x),IntLit(1),IntLit(100),IntLit(3),Block([For(Id(sad),IntLit(1),IntLit(10),IntLit(2),Block([])])])])]))])])"
     self.assertTrue(TestAST.test(input, expect, 343))
    
    def test_For_blockstmt(self):
     """Test 45"""
     input = """
        Class ForBlock{
            forBlock(){
                Foreach(x In 1 .. 100 By 3){
                    Out.println("hello");
                }
            }
        }
     """
     expect = "Program([ClassDecl(Id(ForBlock),[MethodDecl(Id(forBlock),Instance,[],Block([For(Id(x),IntLit(1),IntLit(100),IntLit(3),Block([Call(Id(Out),Id(println),[StringLit(hello)])])])]))])])"
     self.assertTrue(TestAST.test(input, expect, 344))
    
    
    
    def test_For_assign(self):
     """Test 46"""
     input = """
     Class ForAssign{
            forBlock(){
                Foreach(x In 1 .. 100 By 3){
                    gh = 123;
                    bg = 900;
                }
            }
        }
     """
     expect = "Program([ClassDecl(Id(ForAssign),[MethodDecl(Id(forBlock),Instance,[],Block([For(Id(x),IntLit(1),IntLit(100),IntLit(3),Block([AssignStmt(Id(gh),IntLit(123)),AssignStmt(Id(bg),IntLit(900))])])]))])])"
     self.assertTrue(TestAST.test(input, expect, 345))
    
    def test_For_If_stmt(self):
     """Test 47"""
     input = """
        Class ForIf{
            forBlock(){
                Foreach(x In 1 .. 100 By 3){
                    If(a == 4){
                        re = 1;
                    }
                    Else{
                        re = 2;
                    }
                }
            }
        }
     """
     expect = "Program([ClassDecl(Id(ForIf),[MethodDecl(Id(forBlock),Instance,[],Block([For(Id(x),IntLit(1),IntLit(100),IntLit(3),Block([If(BinaryOp(==,Id(a),IntLit(4)),Block([AssignStmt(Id(re),IntLit(1))]),Block([AssignStmt(Id(re),IntLit(2))]))])])]))])])"
     self.assertTrue(TestAST.test(input, expect, 346))
    
    def test_If_stmtFor(self):
     """Test 48"""
     input = """
        Class ForIf{
            forBlock(){
                
                    If(a == 4){
                        sum = 0;
                        Foreach(x In 1 .. 10 ){
                            sum = sum + 8;
                            }
                    }
                    Else{
                        suum = -999;
                    }    }
        }
     """
     expect = "Program([ClassDecl(Id(ForIf),[MethodDecl(Id(forBlock),Instance,[],Block([If(BinaryOp(==,Id(a),IntLit(4)),Block([AssignStmt(Id(sum),IntLit(0)),For(Id(x),IntLit(1),IntLit(10),IntLit(1),Block([AssignStmt(Id(sum),BinaryOp(+,Id(sum),IntLit(8)))])])]),Block([AssignStmt(Id(suum),UnaryOp(-,IntLit(999)))]))]))])])"
     self.assertTrue(TestAST.test(input, expect, 347))
    
    def test_If_stmtFor2(self):
     """Test 49"""
     input = """
     Class ForIf{
            forBlock(){
                
                    If(a == 4){
                        sum = 0;
                        Foreach(x In 1 .. 10 ){
                            Foreach(y In 1 .. 9 By 3){
                                If(sum == 0){
                                    sum = sum + 1;
                                }
                            }
                            sum = sum + 8;
                            }
                    }
                    }
        }"""
     expect = "Program([ClassDecl(Id(ForIf),[MethodDecl(Id(forBlock),Instance,[],Block([If(BinaryOp(==,Id(a),IntLit(4)),Block([AssignStmt(Id(sum),IntLit(0)),For(Id(x),IntLit(1),IntLit(10),IntLit(1),Block([For(Id(y),IntLit(1),IntLit(9),IntLit(3),Block([If(BinaryOp(==,Id(sum),IntLit(0)),Block([AssignStmt(Id(sum),BinaryOp(+,Id(sum),IntLit(1)))]))])]),AssignStmt(Id(sum),BinaryOp(+,Id(sum),IntLit(8)))])])]))]))])])"
     self.assertTrue(TestAST.test(input, expect, 348))

    def test_Array_type(self):
     """Test 50"""
     input = """
        Class TestArray{
            Var a : Array[Int, 6];
        }
     """
     expect = "Program([ClassDecl(Id(TestArray),[AttributeDecl(Instance,VarDecl(Id(a),ArrayType(6,IntType)))])])"
     self.assertTrue(TestAST.test(input, expect, 349))
    
    def test_Array_type1(self):
     """Test 51"""
     input = """
        Class TestArray{
            Var a1 : Array[Array[Int,2], 2];
        }
     """
     expect = "Program([ClassDecl(Id(TestArray),[AttributeDecl(Instance,VarDecl(Id(a1),ArrayType(2,ArrayType(2,IntType))))])])"
     self.assertTrue(TestAST.test(input, expect, 350))
    
    def test_Array_type2(self):
     """Test 52"""
     input = """
        Class TestArray{
            Var arr : Array[Float, 6] = Array(1.2, 2.09, 4, 5, 5, 6);
        }
     """
     expect = "Program([ClassDecl(Id(TestArray),[AttributeDecl(Instance,VarDecl(Id(arr),ArrayType(6,FloatType),[FloatLit(1.2),FloatLit(2.09),IntLit(4),IntLit(5),IntLit(5),IntLit(6)]))])])"
     self.assertTrue(TestAST.test(input, expect, 351))

    def test_Array_type3(self):
     """Test 53"""
     input = """
     Class TestArray{
            Var arr : Array[Array[String,2], 2] = Array(
                    Array("Vocka", "Strongbow"),
                    Array("333", "Heliken")
            );
        }"""
     expect = "Program([ClassDecl(Id(TestArray),[AttributeDecl(Instance,VarDecl(Id(arr),ArrayType(2,ArrayType(2,StringType)),[[StringLit(Vocka),StringLit(Strongbow)],[StringLit(333),StringLit(Heliken)]]))])])"
     self.assertTrue(TestAST.test(input, expect, 352))
    
    def test_ClassType(self):
        """Test 54"""
        input = """
                Class Bus{

             }
            Class TestClassType{
                test(){
                    Var typ : Bus;
                }
            }
        """
        expect = "Program([ClassDecl(Id(Bus),[]),ClassDecl(Id(TestClassType),[MethodDecl(Id(test),Instance,[],Block([AttributeDecl(Instance,VarDecl(Id(typ),Bus))]))])])"
        self.assertTrue(TestAST.test(input, expect, 353))
    
    def test_test_ClassType_New(self):
        """Test 55"""
        input = """
           Class Bus{

             }
            Class TestClassType{
                test(){
                    Var typ : Bus = New Bus();
                }
            }"""
        expect = "Program([ClassDecl(Id(Bus),[]),ClassDecl(Id(TestClassType),[MethodDecl(Id(test),Instance,[],Block([AttributeDecl(Instance,VarDecl(Id(typ),Bus,NewExpr(Id(Bus),[])))]))])])"
        self.assertTrue(TestAST.test(input, expect, 354))
    
    def test_test_ClassType_New_param(self):
        """Test 56"""
        input = """
        Class Bus{
            Var speed: Float;

             }
            Class TestClassType{
                test(){
                    Var typ : Bus;
                    typ = New Bus(78.1);
                }
            }"""
        expect = "Program([ClassDecl(Id(Bus),[AttributeDecl(Instance,VarDecl(Id(speed),FloatType))]),ClassDecl(Id(TestClassType),[MethodDecl(Id(test),Instance,[],Block([AttributeDecl(Instance,VarDecl(Id(typ),Bus)),AssignStmt(Id(typ),NewExpr(Id(Bus),[FloatLit(78.1)]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 355))
    
    def test_ClassType_New_param1(self):
        """Test 57"""
        input = """Class Bus{
            Var speed: Float;
            Var color: String;

             }
            Class TestClassType{
                test(){
                    Var typ : Bus;
                    typ = New Bus(78.1, "Blue");
                }
                }
            """
        expect = "Program([ClassDecl(Id(Bus),[AttributeDecl(Instance,VarDecl(Id(speed),FloatType)),AttributeDecl(Instance,VarDecl(Id(color),StringType))]),ClassDecl(Id(TestClassType),[MethodDecl(Id(test),Instance,[],Block([AttributeDecl(Instance,VarDecl(Id(typ),Bus)),AssignStmt(Id(typ),NewExpr(Id(Bus),[FloatLit(78.1),StringLit(Blue)]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 356))
    
    def test_index_operator(self):
        """Test 58"""
        input = """
            Class Operator{
                Var arr: Array[Int, 5];
                test(){
                    a[0] = 12;
                }
            }
        """
        expect = "Program([ClassDecl(Id(Operator),[AttributeDecl(Instance,VarDecl(Id(arr),ArrayType(5,IntType))),MethodDecl(Id(test),Instance,[],Block([AssignStmt(ArrayCell(Id(a),[IntLit(0)]),IntLit(12))]))])])"
        self.assertTrue(TestAST.test(input, expect, 357))

    def test_index_operator1(self):
        """Test 59"""
        input = """
         Class Operator{
                Var arr: Array[Int, 5];
                test(){
                    Foreach(i In 1 .. 5){
                        arr[i] = i;
                    }
                }
            }
        """
        expect = "Program([ClassDecl(Id(Operator),[AttributeDecl(Instance,VarDecl(Id(arr),ArrayType(5,IntType))),MethodDecl(Id(test),Instance,[],Block([For(Id(i),IntLit(1),IntLit(5),IntLit(1),Block([AssignStmt(ArrayCell(Id(arr),[Id(i)]),Id(i))])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 358))

    def test_index_operator2(self):
        """Test 60"""
        input = """
        Class Operator{
                Var arr: Array[Array[Int, 2], 5];
                test(){
                    Out.print(arr[0][1]);
                }
            }
        """
        expect = "Program([ClassDecl(Id(Operator),[AttributeDecl(Instance,VarDecl(Id(arr),ArrayType(5,ArrayType(2,IntType)))),MethodDecl(Id(test),Instance,[],Block([Call(Id(Out),Id(print),[ArrayCell(Id(arr),[IntLit(0),IntLit(1)])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 359))
    
    def test_Member_access_instance(self):
        """Test 61"""
        input = """
            Class Geo{
                Var xAxis: Boolean;
               
            }
            Class Program{
                main(){
                    a.xAxis = True;
                }
            }
        """
        expect = "Program([ClassDecl(Id(Geo),[AttributeDecl(Instance,VarDecl(Id(xAxis),BoolType))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(FieldAccess(Id(a),Id(xAxis)),BooleanLit(True))]))])])"
        self.assertTrue(TestAST.test(input, expect, 360))
    
    def test_Member_access_static(self):
        """Test 62"""
        input = """
        Class Geo{
                Var xAxis: Boolean;
                Val $yAxis: Boolean;
               
            }
            Class Program{
                main(){
                    a::$yAxis = True;
       
                }
            }"""
        expect = "Program([ClassDecl(Id(Geo),[AttributeDecl(Instance,VarDecl(Id(xAxis),BoolType)),AttributeDecl(Static,ConstDecl(Id($yAxis),BoolType,None))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(FieldAccess(Id(a),Id($yAxis)),BooleanLit(True))]))])])"
        self.assertTrue(TestAST.test(input, expect, 361))

    def test_Member_access_attribute(self):
        """Test 63"""
        input = """Class Geo{
                Var xAxis: Boolean;
                Val $yAxis: Boolean;
               
            }
            Class Program{
                main(){
                    a::$yAxis = True;
                    a.xAxis = True;
                }
            }"""
        expect = "Program([ClassDecl(Id(Geo),[AttributeDecl(Instance,VarDecl(Id(xAxis),BoolType)),AttributeDecl(Static,ConstDecl(Id($yAxis),BoolType,None))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(FieldAccess(Id(a),Id($yAxis)),BooleanLit(True)),AssignStmt(FieldAccess(Id(a),Id(xAxis)),BooleanLit(True))]))])])"
        self.assertTrue(TestAST.test(input, expect, 362))

    def test_ins_method_invocation(self):
        """Test 64"""
        input = """Class Geo{
                location(){
                    
                }
            }
            Class Program{
                main(){
                    a = geo.location();
                }
            }"""
        expect = "Program([ClassDecl(Id(Geo),[MethodDecl(Id(location),Instance,[],Block([]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(a),CallExpr(Id(geo),Id(location),[]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 363))

    def test_ins_method_invocation_with_param(self):
        """Test 65"""
        input = """Class Geo{
                location(x : Boolean; y: Boolean){
                    
                }
            }
            Class Program{
                main(){
                    a = geo.location(True, False);
                }
            }"""
        expect = "Program([ClassDecl(Id(Geo),[MethodDecl(Id(location),Instance,[param(Id(x),BoolType),param(Id(y),BoolType)],Block([]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(a),CallExpr(Id(geo),Id(location),[BooleanLit(True),BooleanLit(False)]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 364))

    def test_sta_method_invocation(self):
        """Test 66"""
        input = """Class Geo{
                $location(){
                    
                }
            }
            Class Program{
                main(){
                    a = geo::$location();
                }
            }"""
        expect = "Program([ClassDecl(Id(Geo),[MethodDecl(Id($location),Static,[],Block([]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(a),CallExpr(Id(geo),Id($location),[]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 365))
    
    def test_sta_method_invocation_with_param(self):
        """Test 67"""
        input = """Class Geo{
                  $location(x : Boolean; y: Boolean){
                    
                }
            }
            Class Program{
                main(){
                    a = geo::$location(False, True);
                }
            }"""
        expect = "Program([ClassDecl(Id(Geo),[MethodDecl(Id($location),Static,[param(Id(x),BoolType),param(Id(y),BoolType)],Block([]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(a),CallExpr(Id(geo),Id($location),[BooleanLit(False),BooleanLit(True)]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 366))
    
    def test_mix_member_access(self):
        """Test 68"""
        input = """Class Geo{
            Var xAxis, $yAxis: Boolean;
                location(x : Boolean; y: Boolean){
                    
                }
                $sky(){
                }
            }
            Class Program{
                main(){
                    a.xAxis = True;
                    a::$yAxis = False;
                    b = geo.location(True, False);
                    c = geo::$sky();
                }
            }"""
        expect = "Program([ClassDecl(Id(Geo),[AttributeDecl(Instance,VarDecl(Id(xAxis),BoolType)),AttributeDecl(Static,VarDecl(Id($yAxis),BoolType)),MethodDecl(Id(location),Instance,[param(Id(x),BoolType),param(Id(y),BoolType)],Block([])),MethodDecl(Id($sky),Static,[],Block([]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(FieldAccess(Id(a),Id(xAxis)),BooleanLit(True)),AssignStmt(FieldAccess(Id(a),Id($yAxis)),BooleanLit(False)),AssignStmt(Id(b),CallExpr(Id(geo),Id(location),[BooleanLit(True),BooleanLit(False)])),AssignStmt(Id(c),CallExpr(Id(geo),Id($sky),[]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 367))
    
    def test_Self(self):
        """Test 69"""
        input = """
        Class Area{
            Var len, width : Float;
            calcuArea(){
                Out.print(Self.len * Self.width);
            }
        }
        
        """
        expect = "Program([ClassDecl(Id(Area),[AttributeDecl(Instance,VarDecl(Id(len),FloatType)),AttributeDecl(Instance,VarDecl(Id(width),FloatType)),MethodDecl(Id(calcuArea),Instance,[],Block([Call(Id(Out),Id(print),[BinaryOp(*,FieldAccess(Self(),Id(len)),FieldAccess(Self(),Id(width)))])]))])])"
        self.assertTrue(TestAST.test(input, expect, 368))
    
    def test_Self_Constructor(self):
        """Test 70"""
        input = """ Class Area{
            Var len, width : Float;
            Constructor(len, width : Float){
                Self.width = width;
                Self.len = len;
            }
        }"""
        expect = "Program([ClassDecl(Id(Area),[AttributeDecl(Instance,VarDecl(Id(len),FloatType)),AttributeDecl(Instance,VarDecl(Id(width),FloatType)),MethodDecl(Id(Constructor),Instance,[param(Id(len),FloatType),param(Id(width),FloatType)],Block([AssignStmt(FieldAccess(Self(),Id(width)),Id(width)),AssignStmt(FieldAccess(Self(),Id(len)),Id(len))]))])])"
        self.assertTrue(TestAST.test(input, expect, 369))
    
    def test_Self_Constructor1(self):
        """Test 71"""
        input = """Class Area{
            Var len, $width : Float;
            Constructor(len, width : Float){
                Self.width = width;
                Self::$len = len;
            }
        }"""
        expect = "Program([ClassDecl(Id(Area),[AttributeDecl(Instance,VarDecl(Id(len),FloatType)),AttributeDecl(Static,VarDecl(Id($width),FloatType)),MethodDecl(Id(Constructor),Instance,[param(Id(len),FloatType),param(Id(width),FloatType)],Block([AssignStmt(FieldAccess(Self(),Id(width)),Id(width)),AssignStmt(FieldAccess(Self(),Id($len)),Id(len))]))])])"
        self.assertTrue(TestAST.test(input, expect, 370))
    
    def test_Self_Destruc(self):
        """Test 72"""
        input = """Class Area{
            Var len, width : Float;
            Destructor(){
                Self.width = 0;
                Self.len = 0;
            }
        }"""
        expect = "Program([ClassDecl(Id(Area),[AttributeDecl(Instance,VarDecl(Id(len),FloatType)),AttributeDecl(Instance,VarDecl(Id(width),FloatType)),MethodDecl(Id(Destructor),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(width)),IntLit(0)),AssignStmt(FieldAccess(Self(),Id(len)),IntLit(0))]))])])"
        self.assertTrue(TestAST.test(input, expect, 371))
    
    def test_Self_Destruc1(self):
        """Test 73"""
        input = """Class Area{
            Var len, $width : Float;
            Destructor(){
                Self.width = 0;
                Self::$len = 0;
            }
        }"""
        expect = "Program([ClassDecl(Id(Area),[AttributeDecl(Instance,VarDecl(Id(len),FloatType)),AttributeDecl(Static,VarDecl(Id($width),FloatType)),MethodDecl(Id(Destructor),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(width)),IntLit(0)),AssignStmt(FieldAccess(Self(),Id($len)),IntLit(0))]))])])"
        self.assertTrue(TestAST.test(input, expect, 372))
    
    def test_Break_stmt(self):
        """Test 74"""
        input = """
        Class Brk{
            test(){
                Foreach(x In 1 .. 10){
                    Break;
                }
            }
        } """
        expect = "Program([ClassDecl(Id(Brk),[MethodDecl(Id(test),Instance,[],Block([For(Id(x),IntLit(1),IntLit(10),IntLit(1),Block([Break])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 373))
    
    def test_Break_stmt1(self):
        """Test 75"""
        input = """Class Brk{
            test(){
                Foreach(x In 1 .. 10){
                    If(x == 5){
                        Break;
                    }Else{
                        re = re + 1;
                    }
                }
            }
        } """
        expect = "Program([ClassDecl(Id(Brk),[MethodDecl(Id(test),Instance,[],Block([For(Id(x),IntLit(1),IntLit(10),IntLit(1),Block([If(BinaryOp(==,Id(x),IntLit(5)),Block([Break]),Block([AssignStmt(Id(re),BinaryOp(+,Id(re),IntLit(1)))]))])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 374))
    
    def test_Continue_stmt(self):
        """Test 76"""
        input = """ Class Coun{
            test(){
                Foreach(x In 1 .. 10){
                    Continue;
                }
            }
        }"""
        expect = "Program([ClassDecl(Id(Coun),[MethodDecl(Id(test),Instance,[],Block([For(Id(x),IntLit(1),IntLit(10),IntLit(1),Block([Continue])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 375))
    
    def test_Continue_stmt1(self):
        """Test 77"""
        input = """Class Brk{
            test(){
                Foreach(x In 1 .. 10){
                    If(x == 5){
                        Continue;
                    }Elseif(x == 9){
                        re = 1;
                    }
                }
            }
        }"""
        expect = "Program([ClassDecl(Id(Brk),[MethodDecl(Id(test),Instance,[],Block([For(Id(x),IntLit(1),IntLit(10),IntLit(1),Block([If(BinaryOp(==,Id(x),IntLit(5)),Block([Continue]),If(BinaryOp(==,Id(x),IntLit(9)),Block([AssignStmt(Id(re),IntLit(1))])))])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 376))
    
    def test_mix_Conti_Break(self):
        """Test 78"""
        input = """Class Mix{
            test(){
                Foreach(x In 1 .. 10){
                    If(x == 5){
                        Continue;
                    }Elseif(x == 9){
                        Break;
                    }
                }
            }
        }"""
        expect = "Program([ClassDecl(Id(Mix),[MethodDecl(Id(test),Instance,[],Block([For(Id(x),IntLit(1),IntLit(10),IntLit(1),Block([If(BinaryOp(==,Id(x),IntLit(5)),Block([Continue]),If(BinaryOp(==,Id(x),IntLit(9)),Block([Break])))])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 377))
    
    def test_Return_stmt(self):
        """Test 79"""
        input = """
        Class Res{
            test(a, b : Int){
                Return a + b;
            }
        } """
        expect = "Program([ClassDecl(Id(Res),[MethodDecl(Id(test),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([Return(BinaryOp(+,Id(a),Id(b)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 378))
    
    def test_Return_stmt1(self):
        """Test 80"""
        input = """Class Res{
            cal(a,b : Int){
                Return a + b;
            }
            test(a, b : Int){
                Return Self.cal(a, b);
            }
        } """
        expect = "Program([ClassDecl(Id(Res),[MethodDecl(Id(cal),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([Return(BinaryOp(+,Id(a),Id(b)))])),MethodDecl(Id(test),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([Return(CallExpr(Self(),Id(cal),[Id(a),Id(b)]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 379))
    
    def test_Return_stmt2(self):
        """Test 81"""
        input = """
        Class Car{}
        Class Res{
            test(){
                Return New Car();
            }
        }"""
        expect = "Program([ClassDecl(Id(Car),[]),ClassDecl(Id(Res),[MethodDecl(Id(test),Instance,[],Block([Return(NewExpr(Id(Car),[]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 380))
    
    def test_Return_stmt3(self):
        """Test 40"""
        input = """ Class Car{}
        Class Res{
            test(){
                Return ;
            }
        }"""
        expect = "Program([ClassDecl(Id(Car),[]),ClassDecl(Id(Res),[MethodDecl(Id(test),Instance,[],Block([Return()]))])])"
        self.assertTrue(TestAST.test(input, expect, 381))
    
    def test__method_invo_stmt(self):
        """Test 83"""
        input = """Class Color{getColor(){
            Out.print("Black");
        }}
            Class Program{
                main(){
                    Color.getColor();
                }
                }
                """
        expect = "Program([ClassDecl(Id(Color),[MethodDecl(Id(getColor),Instance,[],Block([Call(Id(Out),Id(print),[StringLit(Black)])]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(Color),Id(getColor),[])]))])])"
        self.assertTrue(TestAST.test(input, expect, 382))
    
    def test__method_invo_stmt_sta(self):
        """Test 84"""
        input = """Class Color{$getColor(){
            Out.print("Black");
        }}
            Class Program{
                main(){
                    Color::$getColor();
                }
                }"""
        expect = "Program([ClassDecl(Id(Color),[MethodDecl(Id($getColor),Static,[],Block([Call(Id(Out),Id(print),[StringLit(Black)])]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(Color),Id($getColor),[])]))])])"
        self.assertTrue(TestAST.test(input, expect, 383))
    
    def test__method_invo_stmt_sta1(self):
        """Test 85"""
        input = """Class Color{$getColor(a : Int; b : Float){
            Out.print("Black");
        }}
            Class Program{
                main(){
                    Color::$getColor(1, 4.2);
                }
                }"""
        expect = "Program([ClassDecl(Id(Color),[MethodDecl(Id($getColor),Static,[param(Id(a),IntType),param(Id(b),FloatType)],Block([Call(Id(Out),Id(print),[StringLit(Black)])]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(Color),Id($getColor),[IntLit(1),FloatLit(4.2)])]))])])"
        self.assertTrue(TestAST.test(input, expect, 384))

    def test__method_invo_stmt1(self):
        """Test 86"""
        input = """Class Color{getColor(a : Int; b : Float){
            Out.print("Black");
        }}
            Class Program{
                main(){
                    Color.getColor(1.234,3.432);
                }
                }
                """
        expect = "Program([ClassDecl(Id(Color),[MethodDecl(Id(getColor),Instance,[param(Id(a),IntType),param(Id(b),FloatType)],Block([Call(Id(Out),Id(print),[StringLit(Black)])]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(Color),Id(getColor),[FloatLit(1.234),FloatLit(3.432)])]))])])"
        self.assertTrue(TestAST.test(input, expect, 385))
    
    def test_mix_method_invo(self):
        """Test 87"""
        input = """Class Color{getColor(a : Int; b : Float){
            Out.print("Black");
        }
        $getPi(){}}
            Class Program{
                main(){
                    Color.getColor(1.234,3.432);
                    Color::$getPi();
                }
                }"""
        expect = "Program([ClassDecl(Id(Color),[MethodDecl(Id(getColor),Instance,[param(Id(a),IntType),param(Id(b),FloatType)],Block([Call(Id(Out),Id(print),[StringLit(Black)])])),MethodDecl(Id($getPi),Static,[],Block([]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(Color),Id(getColor),[FloatLit(1.234),FloatLit(3.432)]),Call(Id(Color),Id($getPi),[])]))])])"
        self.assertTrue(TestAST.test(input, expect, 386))
    
    def test_complexBlock(self):
        """Test 88"""
        input = """Class Program{
                main(){
                    {
                    Var r, s: Int;
                    r = 2.0;
                    Var a, b: Array[Int, 5];
                    s = r * r * Self.myPI;
                    a[0] = s;
                    }
                }
                }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Block([AttributeDecl(Instance,VarDecl(Id(r),IntType)),AttributeDecl(Instance,VarDecl(Id(s),IntType)),AssignStmt(Id(r),FloatLit(2.0)),AttributeDecl(Instance,VarDecl(Id(a),ArrayType(5,IntType))),AttributeDecl(Instance,VarDecl(Id(b),ArrayType(5,IntType))),AssignStmt(Id(s),BinaryOp(*,BinaryOp(*,Id(r),Id(r)),FieldAccess(Self(),Id(myPI)))),AssignStmt(ArrayCell(Id(a),[IntLit(0)]),Id(s))])]))])])"
        self.assertTrue(TestAST.test(input, expect, 387))
    
    def test_Comment(self):
        """Test 89"""
        input = """Class Program{
            ##Here is comment of language code  D96 of my University##
                main(){
                    {
             
                }
                }}"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Block([])]))])])"
        self.assertTrue(TestAST.test(input, expect, 388))
    
    def test_complex_program(self):
        """Test 90"""
        input = """Class Shape{
                     getHeight(){
                          Foreach( i In 1 .. 100 ){
                          Continue;
                          Continue;
                        }
                    }
            }"""
        expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id(getHeight),Instance,[],Block([For(Id(i),IntLit(1),IntLit(100),IntLit(1),Block([Continue,Continue])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 389))
    
    def test_complex_program1(self):
        """Test 91"""
        input = """Class Shape{
                     Val height: Int;
                      $getHeight(){

                      }
                }
            Class Program{
                Var a: Array[Int, 5] = Array(1,2,3,4,5);
                getRandom(){

                }
                main(){

                }

            }"""
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Instance,ConstDecl(Id(height),IntType,None)),MethodDecl(Id($getHeight),Static,[],Block([]))]),ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),ArrayType(5,IntType),[IntLit(1),IntLit(2),IntLit(3),IntLit(4),IntLit(5)])),MethodDecl(Id(getRandom),Instance,[],Block([])),MethodDecl(Id(main),Static,[],Block([]))])])"
        self.assertTrue(TestAST.test(input, expect, 390))
    
    def test_complex_program2(self):
        """Test 92"""
        input = """ Class Program{
                    main(){
                        {
                            {
                                {{{{
                            Var a : Int = 4;
                            }
                            }}}}}
                    }
                }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Block([Block([Block([Block([Block([Block([AttributeDecl(Instance,VarDecl(Id(a),IntType,IntLit(4)))])])])])])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 391))
    
    def test_complex_program3(self):
        """Test 93"""
        input = """  Class Shape {
                     Val height : Int = 0;
                     Var weight : Float = 0;
                     Var color, length: Int = 0, 0;

                    ##Here is comment-line
                    Here is comment-line
                    Here is comment-line##
                    getWeight(a, c, d : Int ; b: Float){

                    }
                 }
"""
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Instance,ConstDecl(Id(height),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(weight),FloatType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(color),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(length),IntType,IntLit(0))),MethodDecl(Id(getWeight),Instance,[param(Id(a),IntType),param(Id(c),IntType),param(Id(d),IntType),param(Id(b),FloatType)],Block([]))])])"
        self.assertTrue(TestAST.test(input, expect, 392))
    
    def test_mul_abstrc_class(self):
        """Test 94"""
        input = """Class Biology{}
                    Class People : Biology{}
                    Class Animal : Biology{}
                    Class Geo : Biology{}"""
        expect = "Program([ClassDecl(Id(Biology),[]),ClassDecl(Id(People),Id(Biology),[]),ClassDecl(Id(Animal),Id(Biology),[]),ClassDecl(Id(Geo),Id(Biology),[])])"
        self.assertTrue(TestAST.test(input, expect, 393))
    
    def test_comple_program4(self):
        """Test 95"""
        input = """ Class Shape{}
        Class Rectangle: Shape {
                        getArea() {
                        Return Self.length * Self.width;
                        } 
                        }
                        Class Program {
                        main() {
                        Out.printInt(Shape::$numOfShape);
                        } }"""
        expect = "Program([ClassDecl(Id(Shape),[]),ClassDecl(Id(Rectangle),Id(Shape),[MethodDecl(Id(getArea),Instance,[],Block([Return(BinaryOp(*,FieldAccess(Self(),Id(length)),FieldAccess(Self(),Id(width))))]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(Out),Id(printInt),[FieldAccess(Id(Shape),Id($numOfShape))])]))])])"
        self.assertTrue(TestAST.test(input, expect, 394))
    
    def test_comple_program5(self):
        """Test 96"""
        input = """ Class Shape{
                     Val height: Int;
                      $getHeight(){

                      }
                }
            Class Circle:Shape{

            }
            Class Program{
                main(){
                    Out.printString("Hello World \\n \\b \\f");
                }
            }"""
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Instance,ConstDecl(Id(height),IntType,None)),MethodDecl(Id($getHeight),Static,[],Block([]))]),ClassDecl(Id(Circle),Id(Shape),[]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(Out),Id(printString),[StringLit(Hello World \\n \\b \\f)])]))])])"
        self.assertTrue(TestAST.test(input, expect, 395))
    
    def test_complex_program6(self):
        """Test 97"""
        input = """Class Program{
                main(){
                    If(a == 1){
                        If(a ==2 ){
                            If(a == 3){
                                
                            }Elseif(a == 6){}
                        }
                    }
                }
            }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([If(BinaryOp(==,Id(a),IntLit(1)),Block([If(BinaryOp(==,Id(a),IntLit(2)),Block([If(BinaryOp(==,Id(a),IntLit(3)),Block([]),If(BinaryOp(==,Id(a),IntLit(6)),Block([])))]))]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 397))
    
    def test_complex_program7(self):
        """Test 98"""
        input = """Class Program{
                main(){
                    If(a == 1){
                        If(a ==2 ){
                            If(a == 3){
                                
                            }Else{}
                        }
                    }
                }
            }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([If(BinaryOp(==,Id(a),IntLit(1)),Block([If(BinaryOp(==,Id(a),IntLit(2)),Block([If(BinaryOp(==,Id(a),IntLit(3)),Block([]),Block([]))]))]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 397))
    
    def test_complex_program8(self):
        """Test 99"""
        input = """Class Program{
                main(){
                    If(a == 1){
                        If(a ==2 ){
                            If(a == 3){
                                Foreach(i In 1 .. 5 By 1){

                                }
                            }Else{}
                        }
                    }
                }
            }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([If(BinaryOp(==,Id(a),IntLit(1)),Block([If(BinaryOp(==,Id(a),IntLit(2)),Block([If(BinaryOp(==,Id(a),IntLit(3)),Block([For(Id(i),IntLit(1),IntLit(5),IntLit(1),Block([])])]),Block([]))]))]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 398))
    
    def test_if_Elseidfsaedf56f_neste(self):
        """Test 40"""
        input = """Class Program{
                main(){
                    If(a == 1){
                        If(a ==2 ){
                            If(a == 3){
                                Foreach(i In 1 .. 5 By 1){
                                    Shape::$height();
                                    Shape.width();
                                }
                            }Else{}
                        }
                    }
                }
            }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([If(BinaryOp(==,Id(a),IntLit(1)),Block([If(BinaryOp(==,Id(a),IntLit(2)),Block([If(BinaryOp(==,Id(a),IntLit(3)),Block([For(Id(i),IntLit(1),IntLit(5),IntLit(1),Block([Call(Id(Shape),Id($height),[]),Call(Id(Shape),Id(width),[])])])]),Block([]))]))]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 399))
    

   






