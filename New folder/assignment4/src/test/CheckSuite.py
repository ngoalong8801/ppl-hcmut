import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *

class CheckSuite(unittest.TestCase):

    def test_0(self):
        input = Program([ConstDecl(Id("A"),IntLit(10))],[])
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_1(self): # NOT COMPLETE
        input = """
        function _main()
        {
            $a = $b;
        }
        """
        expect = str(UndeclaredIdentifier("$b"))
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_2(self):
        input = """
        function _main()
        {
            _foo();
        }
        """
        expect = str(UndeclaredIdentifier("_foo"))
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_3(self):
        input = """
        define(A,10);
        define(A,10);
        function _main()
        {
            return 0;
        }
        """
        expect = str(Redeclared("Const",Id("A")))
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_4(self):
        input = """
        function _foo($x) {$x = 1; return $x;}
        function _main()
        {
            _foo(1.1);
        }
        """
        expect = str(TypeMismatchInStmt(Call(Id("_foo"),[FloatLit(1.1)])))
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_5(self):
        input = """
        function _foo($x)
        {
            return $x +1;
        }
        function _main()
        {
            $a = _foo(1.1) +. "1";
        }
        """
        expect = str(TypeMismatchInExpr(BinExp("+.",Call(Id("_foo"),[FloatLit(1.1)]),StringLit(1))))
        self.assertTrue(TestChecker.test(input,expect,405))

    def test_6(self):
        input = """
        define(A, 10);
        $x = A;
        function _main()
        {
            $a = $x +. "1";
        }
        """
        expect = str(TypeMismatchInExpr(BinExp("+.",Id("$x"),StringLit(1))))
        self.assertTrue(TestChecker.test(input,expect,406))

    def test_7(self):
        input = """
        define(A, 10);
        $x = A;
        function _main()
        {
            $x = "string";
        }
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_8(self):
        input = """
        function _main()
        {
            _echo("Hello World!");
        }
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_9(self):
        input = """
        function _main()
        {
            $arr = array(array(array(1)), array(array(1,2)));
            $a = $arr[0][0][0] + 1;
        }
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,409))

    def test_10(self):
        input = """
        function _main()
        {
            while(1 + 1)
            {
                _echo("loop");
            }
        }
        """
        expect = str(TypeMismatchInStmt(While(BinExp("+",IntLit(1),IntLit(1)),[Call(Id("_echo"),[StringLit("loop")])])))
        self.assertTrue(TestChecker.test(input,expect,410))

    def test_11(self):
        input = """
        function _main()
        {
            $a = array(1, 2, 3);
            foreach ($a as $key => $value) {
                _echo((("Element " +. int2str($key)) +. ": ") +. int2str($value));
            }
        }
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,411))

    def test_12(self):
        input = """
        function _main()
        {
            break;
        }
        """
        expect = str(TypeMismatchInStmt(Break()))
        self.assertTrue(TestChecker.test(input,expect,412))

    def test_13(self):
        input = """
        function _main()
        {
            continue;
        }
        """
        expect = str(TypeMismatchInStmt(Continue()))
        self.assertTrue(TestChecker.test(input,expect,413))

    def test_14(self):
        input = """
        function _main()
        {
            while(true)
            {
                $a = 0;
                if ($a > 10) {break;}
                else {$a = $a + 1;}
            }
        }
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,414))

    def test_15(self):
        input = """
        function _main()
        {
            while(true)
            {
                $a = 0;
                if ($a > 10) {return;}
                else {$a = $a + 1;}
            }
        }
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,415))

    def test_16(self):
        input = """
        define(A, array(1,2,3));
        function _main()
        {
            $x = A["1"];
        }
        """
        expect = str(TypeMismatchInExpr(ArrayAccess(Id("A"),[StringLit("1")])))
        self.assertTrue(TestChecker.test(input,expect,416))

    def test_17(self):
        input = """
        function _foo(){
            if ($a) {return 1;}
            else {return 0;}
        }
        function _main()
        {
            _foo();
        }
        """
        expect = str(UndeclaredIdentifier("$a"))
        self.assertTrue(TestChecker.test(input,expect,417))

    def test_18(self):
        input = """
        $a = 1;
        function _main()
        {
            $x = !$a;
        }
        """
        expect = str(TypeMismatchInExpr(UnExp("!",Id("$a"))))
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_19(self):
        input = """
        $a = 1;
        function _main()
        {
            $arr = array(1,2,3);
            $x = $arr[$arr[1]];
        }
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,419))

    def test_20(self):
        input = """
        function _foo($x, $y)
        {
            $a = $x;
            return $a;
        }
        function _main()
        {
            $a = 1;
        }
        """
        expect = str(TypeCannotBeInferred(Assign(Id("$a"),Id("$x"))))
        self.assertTrue(TestChecker.test(input,expect,420))

    def test_21(self):
        input = """
        define(A, 1);
        function _main()
        {
            $x = false;
            if (A)
            {
                $x = false;
            }
        }
        """
        expect = str(TypeMismatchInStmt(If([(Id("A"),[Assign(Id("$x"),BoolLit(False))])],[])))
        self.assertTrue(TestChecker.test(input,expect,421))

    def test_22(self):
        input = """
        function _main()
        {
            $x = 1 +. 1;
        }
        """
        expect = str(TypeMismatchInExpr(BinExp("+.",IntLit(1),IntLit(1))))
        self.assertTrue(TestChecker.test(input,expect,422))

    def test_23(self):
        input = """
        function _main()
        {
            $x = int2str(1.1);
        }
        """
        expect = str(TypeMismatchInStmt(Call(Id("int2str"),[FloatLit(1.1)])))
        self.assertTrue(TestChecker.test(input,expect,423))

    def test_24(self):
        input = """
        function _main()
        {
            $x = str2int(1);
        }
        """
        expect = str(TypeMismatchInStmt(Call(Id("str2int"),[IntLit(1)])))
        self.assertTrue(TestChecker.test(input,expect,424))

    def test_25(self):
        input = """
        function _main()
        {
            $x = float2str(1);
        }
        """
        expect = str(TypeMismatchInStmt(Call(Id("float2str"),[IntLit(1)])))
        self.assertTrue(TestChecker.test(input,expect,425))

    def test_26(self):
        input = """
        function _main()
        {
            $x = str2float(1.1);
        }
        """
        expect = str(TypeMismatchInStmt(Call(Id("str2float"),[FloatLit(1.1)])))
        self.assertTrue(TestChecker.test(input,expect,426))

    def test_27(self):
        input = """
        function _main()
        {
            $x = bool2str(1);
        }
        """
        expect = str(TypeMismatchInStmt(Call(Id("bool2str"),[IntLit(1)])))
        self.assertTrue(TestChecker.test(input,expect,427))

    def test_28(self):
        input = """
        function _main()
        {
            $x = str2bool("false");
            $y = $x || true;
        }
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,428))

    def test_29(self):
        input = """
        define(A, 1);
        define(A, true);
        function _main()
        {
            $x = A;
        }
        """
        expect = str(Redeclared("Const",Id("A")))
        self.assertTrue(TestChecker.test(input,expect,429))

    def test_30(self):
        input = """
        $arr = array(1,2,3);
        function _main()
        {
            $arr[1] = 1;
        }
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,430))

    def test_31(self):
        input = """
        function _foo(){}
        function _main()
        {
            $a = _foo();
        }
        """
        expect = str(TypeMismatchInStmt(Assign(Id("$a"),Call(Id("_foo"),[]))))
        self.assertTrue(TestChecker.test(input,expect,431))

    def test_32(self):
        input = """
        function _foo(){}
        function _main()
        {
            $a = 1;
            $a = 1.1;
        }
        """
        expect = str(TypeMismatchInStmt(Assign(Id("$a"),FloatLit(1.1))))
        self.assertTrue(TestChecker.test(input,expect,432))

    def test_33(self):
        input = """
        function _foo(){}
        function _main()
        {
            $a = 1;
            $a = true;
        }
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,433))

    def test_34(self):
        input = """
        function _foo($x, $x){}
        function _main()
        {
            $a = 1;
        }
        """
        expect = str(Redeclared("Var","$x"))
        self.assertTrue(TestChecker.test(input,expect,434))

    def test_35(self):
        input = """
        function _foo($x, $y){}
        function _foo($x, $y){}
        function _main()
        {
            $a = 1;
        }
        """
        expect = str(Redeclared("Func","_foo"))
        self.assertTrue(TestChecker.test(input,expect,435))

    def test_36(self):
        input = """
        function _foo($x, $y)
        {
            $x = 1; $y = 1;
            return $x + $y;
        }
        function _main()
        {
            _foo(1);
        }
        """
        expect = str(TypeMismatchInStmt(Call(Id("_foo"),[IntLit(1)])))
        self.assertTrue(TestChecker.test(input,expect,436))

    def test_37(self):
        input = """
        function _foo($x, $y)
        {
            $x = 1; $y = 1;
            return $x + $y;
        }
        function _main()
        {
            _foo(1, 1.1);
        }
        """
        expect = str(TypeMismatchInStmt(Call(Id("_foo"),[IntLit(1),FloatLit(1.1)])))
        self.assertTrue(TestChecker.test(input,expect,437))

    def test_38(self):
        input = """
        define(A, 1);
        function _main()
        {
            foreach(A as $key=>$value)
            {
                _echo("loop");
            }
        }
        """
        expect = str(TypeMismatchInStmt(ForEach(Id("A"),Id("$key"),Id("$value"),[Call(Id("_echo"),[StringLit("loop")])])))
        self.assertTrue(TestChecker.test(input,expect,438))

    def test_39(self):
        input = """
        define(A, array(1,2,3));
        function _main()
        {
            foreach(A as $key=>$value)
            {
                _echo("loop");
                break;
            }
        }
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,439))

    def test_40(self):
        input = """
        define(A, array(1,2,3));
        function _main()
        {
            foreach(A as $key=>$value)
            {
                if ($value < 2) {continue;}
                else {break;}
            }
        }
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,440))

    def test_41(self):
        input = """
        define(A, array(1,2,3,4));
        function _main()
        {
            $i = 0;
            while(A[$i] < 3)
            {
                _echo(int2str(A[$i]));
                $i = $i + 1;
            }
        }
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,441))

    def test_42(self):
        input = """
        define(A, array(1,2,3,4));
        function _main()
        {
            $i = 0;
            while(A[$i] + 3)
            {
                _echo(int2str(A[$i]));
                $i = $i + 1;
            }
        }
        """
        expect = str(TypeMismatchInStmt(While(BinExp("+",ArrayAccess(Id("A"),[Id("$i")]),IntLit(3)),[Call(Id("_echo"),[Call(Id("int2str"),[ArrayAccess(Id("A"),[Id("$i")])])]),Assign(Id("$i"),BinExp("+",Id("$i"),IntLit(1)))])))
        self.assertTrue(TestChecker.test(input,expect,442))

    def test_43(self):
        input = """
        function _main()
        {
            $x = $y + 1;
        }
        """
        expect = str(UndeclaredIdentifier("$y"))
        self.assertTrue(TestChecker.test(input,expect,443))

    def test_44(self):
        input = """
        function _main()
        {
            _echo($x);
        }
        """
        expect = str(UndeclaredIdentifier("$x"))
        self.assertTrue(TestChecker.test(input,expect,444))

    def test_45(self):
        input = """
        function _main()
        {
            $arr = array(array(1 => 1.11), array(1,2));
        }
        """
        expect = str(InvalidArrayLiteral(ArrayLit([ArrayLit([AssocExp(IntLit(1),FloatLit(1.11))]),ArrayLit([IntLit(1),IntLit(2)])])))
        self.assertTrue(TestChecker.test(input,expect,445))

    def test_46(self):
        input = """
        function _main()
        {
            $arr = array(1, true, "one", 1.1);
        }
        """
        expect = str(InvalidArrayLiteral(ArrayLit([IntLit(1),BoolLit(True),StringLit("one"),FloatLit(1.1)])))
        self.assertTrue(TestChecker.test(input,expect,446))

    def test_47(self):
        input = """
        function _main()
        {
            $arr = array(1, 2, 3,4);
            $x = $arr[1];
            $arr[2] = 5;
        }
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,447))

    def test_48(self):
        input = """
        function _main()
        {
            $arr = array(1, 2, 3,4);
            $x = $arr[true];
            $arr[2] = 5;
        }
        """
        expect = str(TypeMismatchInExpr(ArrayAccess(Id("$arr"),[BoolLit(True)])))
        self.assertTrue(TestChecker.test(input,expect,448))

    def test_49(self):
        input = """
        function _main()
        {
            $arr = array(array(1.0,2.0), array(3.0, 4.0));
            $x = $arr[0];
            $y = $arr[1][1];
        }
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,449))

    def test_50(self):
        input = """
        function _main()
        {
            $arr = array(array("a", "b"), array("c", "d"));
            $x = $arr[1][1];
            $x = $x +. "123";
        }
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,450))

    def test_51(self):
        input = """
        function _main()
        {
            $arr = array(array("a", "b"), array("c", "d"));
            $x = $arr[1][1];
            $y = $x / 2;
        }
        """
        expect = str(TypeMismatchInExpr(BinExp("/",Id("$x"),IntLit(2))))
        self.assertTrue(TestChecker.test(input,expect,451))

    def test_52(self):
        input = """
        function _main()
        {
            $arr = array("one" => 1.0, "two" => 2.0);
            $x = $arr["one"];
        }
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,452))

    def test_53(self):
        input = """
        function _main()
        {
            $arr = array("one" => 1.0, "two" => 2.0);
            $x = $arr[1];
        }
        """
        expect = str(TypeMismatchInExpr(ArrayAccess(Id("$arr"),[IntLit(1)])))
        self.assertTrue(TestChecker.test(input,expect,453))

    def test_54(self):
        input = """
        function _main()
        {
            $arr = array("one" => 1.0, "two" => 2.0);
            $x = $arr["one"] * 1;
        }
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,454))

    def test_55(self):
        input = """
        function _main()
        {
            $arr = array(array("one" => 1.0, "two" => 2.0), array("three" => 3.0, "four" => 4.0));
            $x = $arr[1];
            $y = $arr[0]["two"];
        }
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,455))

    def test_56(self):
        input = """
        function _main()
        {
            $arr = array(array("one" => 1.0, "two" => 2.0), array("three" => 3.0, "four" => 4.0));
            $x = $arr[1];
            $y = $arr[0][1];
        }
        """
        expect = str(TypeMismatchInExpr(ArrayAccess(Id("$arr"),[IntLit(0),IntLit(1)])))
        self.assertTrue(TestChecker.test(input,expect,456))

    def test_57(self):
        input = """
        function _main()
        {
            $arr = array(array("one" => 1.0, "two" => 2.0), array("three" => 3.0, "four" => 4.0));
            $x = $arr[0]["one"] - 2.0;
        }
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,457))

    def test_58(self):
        input = """
        function _main()
        {
            $x = 1 + true;
        }
        """
        expect = str(TypeMismatchInExpr(BinExp("+",IntLit(1),BoolLit(True))))
        self.assertTrue(TestChecker.test(input,expect,456))

    def test_59(self):
        input = """
        function _main($arg)
        {
            $x = "1" +. $arg;
        }
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,459))

    def test_60(self):
        input = """
        function _main($arg)
        {
            $x = true / false;
        }
        """
        expect = str(TypeMismatchInExpr(BinExp("/",BoolLit(True),BoolLit(False))))
        self.assertTrue(TestChecker.test(input,expect,460))

    def test_61(self):
        input = """
        function _main($arg)
        {
            $x = 1 + 2 * 3 / 7.5;
        }
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,461))

    def test_62(self):
        input = """
        function _main($arg)
        {
            $x = true || 1;
        }
        """
        expect = str(TypeMismatchInExpr(BinExp("||",BoolLit(True),IntLit(1))))
        self.assertTrue(TestChecker.test(input,expect,462))

    def test_63(self):
        input = """
        function _main($arg)
        {
            $x = 2 > 3;
            $y = $x && true;
        }
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,463))

    def test_64(self):
        input = """
        function _main($arg)
        {
            $a = "1" +. "2";
            $x = 1.1 +. 3;
        }
        """
        expect = str(TypeMismatchInExpr(BinExp("+.",FloatLit(1.1),IntLit(3))))
        self.assertTrue(TestChecker.test(input,expect,464))

    def test_65(self):
        input = """
        function _main($arg)
        {
            $a = "1" ==. "2";
            $b = $a || false;
            $x = true ==. false;
        }
        """
        expect = str(TypeMismatchInExpr(BinExp("==.",BoolLit(True),BoolLit(False))))
        self.assertTrue(TestChecker.test(input,expect,465))

    def test_66(self):
        input = """
        function _main($arg)
        {
            $a = true;
            $b = !$a;
            $x = !1;
        }
        """
        expect = str(TypeMismatchInExpr(UnExp("!",IntLit(1))))
        self.assertTrue(TestChecker.test(input,expect,466))

    def test_67(self):
        input = """
        function _main($arg)
        {
            $a = 1.234;
            $b = -$a * 3.1 / 7;
            $x = -true;
        }
        """
        expect = str(TypeMismatchInExpr(UnExp("-",BoolLit(True))))
        self.assertTrue(TestChecker.test(input,expect,467))

    def test_68(self):
        input = """
        function _foo($x)
        {
            if ($x == 1){return 1;}
            return _foo($x -1);
        }
        function _main()
        {
            _foo(5.0);
        }
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,468))

    def test_69(self):
        input = """
        function _foo($x)
        {
            if ($x == 1){return 1;}
            return _foo($x -1);
        }
        function _main()
        {
            _foo(5.0, 6.0);
        }
        """
        expect = str(TypeMismatchInStmt(Call(Id("_foo"),[FloatLit(5.0),FloatLit(6.0)])))
        self.assertTrue(TestChecker.test(input,expect,469))

    def test_70(self):
        input = """
        function _foo($x)
        {
            if ($x == 1){return 1;}
            return _foo($x -1);
        }
        function _main()
        {
            _foo();
        }
        """
        expect = str(TypeMismatchInStmt(Call(Id("_foo"),[])))
        self.assertTrue(TestChecker.test(input,expect,470))

    def test_71(self):
        input = """
        $a = 7;
        function _main()
        {
            if($a > 5) { _echo(int2str($a)); }
            elseif ($a == 5) { _echo(bool2str($a == 5));}
            else { _echo(int2str($a) +. "abc");}
        }
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,471))

    def test_72(self):
        input = """
        $a = 7;
        function _main()
        {
            if($a > 5) { _echo(int2str($a)); }
            elseif ($a == 5) { _echo(bool2str($a == 5));}
            else { _echo(int2str($a) +. "abc");}
        }
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,472))

    def test_73(self):
        input = """
        $a = 7;
        function _main()
        {
            $x = 1;
            if ($x +1)
            {$x = 2;}
        }
        """
        expect = str(TypeMismatchInStmt(If([(BinExp("+",Id("$x"),IntLit(1)),[Assign(Id("$x"),IntLit(2))])],[])))
        self.assertTrue(TestChecker.test(input,expect,473))

    def test_74(self):
        input = """
        $a = 7;
        function _foo()
        {
            return true;
        }
        """
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,474))

    def test_75(self):
        input = """
        function _main()
        {
            $x = 5.5;
            $x = true;
            $x = "str";
        }
        """
        expect = str(TypeMismatchInStmt(Assign(Id("$x"),StringLit("str"))))
        self.assertTrue(TestChecker.test(input,expect,475))

    def test_76(self):
        input = """
        function _main()
        {
            $arr = array(1,2,3);
            $x = $arr[1][2];
        }
        """
        expect = str(TypeMismatchInExpr(ArrayAccess(Id("$arr"),[IntLit(1),IntLit(2)])))
        self.assertTrue(TestChecker.test(input,expect,476))

    def test_77(self):
        input = """
        function _main()
        {
            $arr = array(array(1, 2), array("one", "two"));
        }
        """
        expect = str(InvalidArrayLiteral(ArrayLit([ArrayLit([IntLit(1),IntLit(2)]),ArrayLit([StringLit("one"),StringLit("two")])])))
        self.assertTrue(TestChecker.test(input,expect,477))

    def test_78(self):
        input = """
        function _main()
        {
            foreach ($arr as $k => $v) { if ($v % 2 == 0) {$n = $n + $v;} }
            _echo(int2str($n));
        }
        """
        expect = str(UndeclaredIdentifier("$arr"))
        self.assertTrue(TestChecker.test(input,expect,478))

    def test_79(self):
        input = """
        function _main()
        {
            $a = false; $b =  bool2str($a + 1);
        }
        """
        expect = str(TypeMismatchInExpr(BinExp("+",Id("$a"),IntLit(1))))
        self.assertTrue(TestChecker.test(input,expect,479))

    def test_80(self):
        input = """
        define (A,array(1,2,3,4)); $s = "str"; $i = 0;
        function _main()
        {
            while($i < 4)
            {$s = $s +. int2str(A[$i]); $i = $i+1;}
        }
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,480))

    def test_81(self):
        input = """
        function _main()
        {
            $x = 0;
            while($x < 10){ if ($x %2 == 0) {continue;} else {$x = $x + 1;} }
        }
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,481))

    def test_82(self):
        input = """
        $a = 1; $b = 2;
        function _main()
        {
            _swap($a, $b);
        }
        """
        expect = str(UndeclaredIdentifier("_swap"))
        self.assertTrue(TestChecker.test(input,expect,482))

    def test_83(self):
        input = """
        function _main()
        {
            $x = "hcmut" == "HCMUT";
        }
        """
        expect = str(TypeMismatchInExpr(BinExp("==",StringLit("hcmut"),StringLit("HCMUT"))))
        self.assertTrue(TestChecker.test(input,expect,483))

    def test_84(self):
        input = """
        function _main()
        {
            $a = --191 *36/-95 +. "1";
        }
        """
        expect = str(TypeMismatchInExpr(BinExp("+.",BinExp("/",BinExp("*",UnExp("-",UnExp("-",IntLit(191))),IntLit(36)),UnExp("-",IntLit(95))),StringLit(1))))
        self.assertTrue(TestChecker.test(input,expect,484))

    def test_85(self):
        input = """
        function _foo($a)
        {
            $a = 1;
            return $a;
        }
        function _main()
        {
            $x = _foo(_foo(1));
        }
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,485))

    def test_86(self):
        input = """
        function _main()
        {
            $a = true;
            $x = $a + 1;
        }
        """
        expect = str(TypeMismatchInExpr(BinExp("+",Id("$a"),IntLit(1))))
        self.assertTrue(TestChecker.test(input,expect,486))

    def test_87(self):
        input = """
        function _main()
        {
            $arr = array(1,2,3);
            $x = $arr + 1;
        }
        """
        expect = str(TypeMismatchInExpr(BinExp("+",Id("$arr"),IntLit(1))))
        self.assertTrue(TestChecker.test(input,expect,487))

    def test_88(self):
        input = """
        function _main()
        {
            $arr1 = array(array(array(1.1)), array(array(1.1, 2.3)));
            $arr2 = array(array(array(1.1)), array(array(1 => 1.1)));
        }
        """
        expect = str(InvalidArrayLiteral(ArrayLit([ArrayLit([ArrayLit([FloatLit(1.1)])]),ArrayLit([ArrayLit([AssocExp(IntLit(1),FloatLit(1.1))])])])))
        self.assertTrue(TestChecker.test(input,expect,488))

    def test_89(self):
        input = """
        define(A, A);
        function _main()
        {
            $x = 1;
        }
        """
        expect = str(UndeclaredIdentifier("A"))
        self.assertTrue(TestChecker.test(input,expect,490))

    def test_90(self): # NOT COMPLETE
        input = """
        define(A, 1.2345);
        function _f($a){return $a+1;}
        function _g($a){return _f($a) * _f($a+5);}
        function _main()
        {
            $x = _g(1.1) * 2;
        }
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,490))

    def test_91(self):
        input = """
        function _main()
        {
            $a = 1.11 + 4.5 * 3.1;
            _echo(int2str($a));
        }
        """
        expect = str(TypeMismatchInStmt(Call(Id("int2str"),[Id("$a")])))
        self.assertTrue(TestChecker.test(input,expect,491))

    def test_92(self):
        input = """
        function _main()
        {
            $s = ("hcmut" +. "HCMUT") && true;
        }
        """
        expect = str(TypeMismatchInExpr(BinExp("&&",BinExp("+.",StringLit("hcmut"),StringLit("HCMUT")),BoolLit(True))))
        self.assertTrue(TestChecker.test(input,expect,492))

    def test_93(self):
        input = """
        function _f($a)
        {
           if($a) { return 1;}
           return 0;
        }
        function _main()
        {
            _f(true);
        }
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,493))

    def test_94(self):
        input = """
        function _main()
        {
            $x = 1 + 1 < true;
        }
        """
        expect = str(TypeMismatchInExpr(BinExp("<",BinExp("+",IntLit(1),IntLit(1)),BoolLit(True))))
        self.assertTrue(TestChecker.test(input,expect,494))

    def test_95(self):
        input = """
        function _main()
        {
            $x = 1.1;
            $x = 1;
            $x = true;
        }
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,495))

    def test_96(self):
        input = """
        function _main()
        {
            $arr = array(1,2,3);
            $x = $arr[1] + $arr[2];
        }
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,496))

    def test_97(self):
        input = """
        define(A, "1234");
        function _main()
        {
            $a = 10000 % A;
        }
        """
        expect = str(TypeMismatchInExpr(BinExp("%",IntLit(10000),Id("A"))))
        self.assertTrue(TestChecker.test(input,expect,497))

    def test_98(self):
        input = """
        define(A, -1.1 / 2.2 + 3.3 * 4.4);
        function _main()
        {
            bool2str(A);
        }
        """
        expect = str(TypeMismatchInStmt(Call(Id("bool2str"),[Id("A")])))
        self.assertTrue(TestChecker.test(input,expect,498))

    def test_99(self):
        input = """
        function _main()
        {
            return $a;
        }
        """
        expect = str(UndeclaredIdentifier("$a"))
        self.assertTrue(TestChecker.test(input,expect,499))