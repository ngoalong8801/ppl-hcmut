import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    # def test1(self):
    #     """Class declare"""
    #     input = """
    #                  Class Shape{
    #               }
    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 201))

    # def test2(self):
    #     """Miss } in declare class"""
    #     input = """
    #              Class Shape{
    #         """
    #     expect = "Error on line 3 col 12: <EOF>"
    #     self.assertTrue(TestParser.test(input, expect, 202))

    # def test3(self):
    #     """declare class main"""
    #     input = """
    #              Class main{}
    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 203))

    # def test4(self):
    #     """miss {"""
    #     input = """
    #              Class main}
    #         """
    #     expect = "Error on line 2 col 27: }"
    #     self.assertTrue(TestParser.test(input, expect, 204))

    # def test5(self):
    #     """Error class"""
    #     input = """
    #              class Shape {}
    #         """
    #     expect = "Error on line 2 col 17: class"
    #     self.assertTrue(TestParser.test(input, expect, 205))

    # def test6(self):
    #     """single decalare"""
    #     input = """
    #              Class Shape {
    #                  Val height : Int = 0;
    #              }
    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 206))

    # def test7(self):
    #     """multiple-line declare"""
    #     input = """
    #              Class Shape {
    #                  Val height : Int = 0;
    #                  Var weight : Float = 0;
    #              }
    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 207))

    # def test8(self):
    #     """multiple variable declare"""
    #     input = """
    #              Class Shape {
    #                  Val height : Int = 0;
    #                  Var weight : Float = 0;
    #                  Var color, length: Int = 0, 0;
    #              }
    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 208))

    # def test9(self):
    #     """multiple variable declare"""
    #     input = """
    #              Class Shape {
    #                  Val height : Int = 0;
    #                  Var weight : Float = 0;
    #                  Var color, length: Int = 0, 0;
    #              }
    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 209))

    # def test10(self):
    #     """ test """
    #     input = """
    #              Class Shape {
    #                  Val height : int = 0;
    #                  Var weight : Float = 0;
    #                  Var color, length: Int = 0, 0;
    #              }
    #         """
    #     expect = "Error on line 3 col 34: int"
    #     self.assertTrue(TestParser.test(input, expect, 210))

    # def test11(self):
    #     """ test """
    #     input = """
    #              Class Shape {
    #                  Val height : Int = 0;
    #                  Var weight  Float = 0;
    #                  Var color, length: Int = 0, 0;
    #              }
    #         """
    #     expect = "Error on line 4 col 33: Float"
    #     self.assertTrue(TestParser.test(input, expect, 211))

    # def test12(self):
    #     """ test """
    #     input = """
    #              Class Shape {
    #                  Val height : Int = 0;
    #                  Var weight : Float = 0;
    #                  Vr color, length: Int = 0, 0;
    #              }
    #         """
    #     expect = "Error on line 5 col 24: color"
    #     self.assertTrue(TestParser.test(input, expect, 212))

    # def test13(self):
    #     """ test """
    #     input = """
    #              Class Shape {
    #                  Val height : Int = 0;
    #                  Var weight : Float = 0;
    #                  Var color, length: Int = 0, 0;

    #                 getWeight(){

    #                 }
    #              }
                
    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 213))

    # def test14(self):
    #     """ test """
    #     input = """
    #              Class Shape {
    #                  Val height : Int = 0;
    #                  Var weight : Float = 0;
    #                  Var color, length: Int = 0, 0;

    #                 getWeight()[

    #                 ]
    #              }
                
    #         """
    #     expect = "Error on line 7 col 31: ["
    #     self.assertTrue(TestParser.test(input, expect, 214))

    # def test15(self):
    #     """ test """
    #     input = """
    #              Class Shape {
    #                  Val height : Int = 0;
    #                  Var weight : Float = 0;
    #                  Var color, length: Int = 0, 0;

    #                 getWeight(a : Int){

    #                 }
    #              }
                
    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 215))

    # def test16(self):
    #     """ test """
    #     input = """
    #              Class Shape {
    #                  Val height : Int = 0;
    #                  Var weight : Float = 0;
    #                  Var color, length: Int = 0, 0;

    #                 getWeight(int a){

    #                 }
    #              }

    #         """
    #     expect = "Error on line 7 col 34: a"
    #     self.assertTrue(TestParser.test(input, expect, 216))

    # def test17(self):
    #     """ test """
    #     input = """
    #              Class Shape {
    #                  Val height : Int = 0;
    #                  Var weight : Float = 0;
    #                  Var color, length: Int = 0, 0;

    #                 getWeight(a : Int ; b: Float){

    #                 }
    #              }

    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 217))

    # def test18(self):
    #     """ test """
    #     input = """
    #              Class Shape {
    #                  Val height : Int = 0;
    #                  Var weight : Float = 0;
    #                  Var color, length: Int = 0, 0;

    #                 getWeight(a, c, d : Int ; b: Float){

    #                 }
    #              }

    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 218))

    # def test19(self):
    #     """ test """
    #     input = """
    #              Class Shape {
    #                  Val height : Int = 0;
    #                  Var weight : Float = 0;
    #                  Var color, length: Int = 0, 0;

    #                 getWeight(a, c, d : Int , b: Float){

    #                 }
    #              }

    #         """
    #     expect = "Error on line 7 col 44: ,"
    #     self.assertTrue(TestParser.test(input, expect, 219))

    # def test20(self):
    #     """ test """
    #     input = """
    #              Class Shape {
    #                  Val height : Int = 0;
    #                  Var weight : Float = 0;
    #                  Var color, length: Int = 0, 0;

    #                 ##Here is comment-line
    #                 Here is comment-line
    #                 Here is comment-line##
    #                 getWeight(a, c, d : Int ; b: Float){

    #                 }
    #              }

    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 220))

    # def test21(self):
    #     """ test """
    #     input = """
    #              Class Shape {
    #                  Val height : Int = 0;
    #                  Var weight : Float = 0;
    #                  Var color, length: Int = 0, 0;

    #                 ##Here is comment-line
    #                 Here is comment-line
    #                 Here is comment-line##

    #                 getWeight(a, c, d : Int ; b: Float){

    #                 }
    #             Constructor(){

    #             }
    #         }

    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 221))

    # def test22(self):
    #     """ test """
    #     input = """
    #              Class Shape {
    #                  Val height : Int = 0;
    #                  Var weight : Float = 0;
    #                  Var color, length: Int = 0, 0;

    #                 ##Here is comment-line
    #                 Here is comment-line
    #                 Here is comment-line##

    #                 getWeight(a, c, d : Int ; b: Float){

    #                 }
    #             Constructor(a, c, d : Int ; b: Float){

    #             }
    #         }

    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 222))

    # def test23(self):
    #     """ test """
    #     input = """
    #              Class Shape {
    #                  Val height : Int = 0;
    #                  Var weight : Float = 0;
    #                  Var color, length: Int = 0, 0;

    #                 ##Here is comment-line
    #                 Here is comment-line
    #                 Here is comment-line##

    #                 getWeight(a, c, d : Int ; b: Float){

    #                 }
    #             Constructor(a, c, d : Int ; b: Float){

    #             }
    #             Destructor(){

    #             }
    #         }

    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 223))

    # def test24(self):
    #     """ test """
    #     input = """
    #              Class Shape {
    #                  Val height : Int = 0;
    #                  Var weight : Float = 0;
    #                  Var color, length: Int = 0, 0;

    #                 ##Here is comment-line
    #                 Here is comment-line
    #                 Here is comment-line##

    #                 $getWeight(a, c, d : Int ; b: Float){

    #                 }
    #             Constructor(a, c, d : Int ; b: Float){

    #             }
    #             Destructor(){

    #             }
    #         }

    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 224))

    # def test25(self):
    #     """ test """
    #     input = """
    #              Class Shape {
    #                  Val height : Int = 0;
    #                  Var $weight : Float = 0;
    #                  Var color, length: Int = 0, 0;

    #                 ##Here is comment-line
    #                 Here is comment-line
    #                 Here is comment-line##

    #                 $getWeight(a, c, d : Int ; b: Float){

    #                 }
    #             Constructor(a, c, d : Int ; b: Float){

    #             }
    #             Destructor(){

    #             }
    #         }

    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 225))

    # def test26(self):
    #     """ test """
    #     input = """
    #              Class Shape:People {
    #                  Val height : Int = 0;
    #                  Var $weight : Float = 0;
    #                  Var color, length: Int = 0, 0;

    #                 ##Here is comment-line
    #                 Here is comment-line
    #                 Here is comment-line##

    #                 $getWeight(a, c, d : Int ; b: Float){

    #                 }
    #             Constructor(a, c, d : Int ; b: Float){

    #             }
    #             Destructor(){

    #             }
    #         }

    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 226))

    # def test27(self):
    #     """ test """
    #     input = """
    #              Class Shape:People {
    #                  Val height : Int = 0;
    #                  Var $weight : Float = 0;
    #                  Var color, length: Int = 0, 0;

    #                 ##Here is comment-line
    #                 Here is comment-line
    #                 Here is comment-line##

    #                 $getWeight(a, c, d : Int ; b: Float){
    #                     height = 4;
    #                 }
    #         }

    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 227))

    # def test28(self):
    #     """ test """
    #     input = """
    #              Class Shape:People {
    #                  Val height : Int = 0;
    #                  Var $weight : Float = 0;
    #                  Var color, length: Int = 0, 0;

    #                 ##Here is comment-line
    #                 Here is comment-line
    #                 Here is comment-line##

    #                 $getWeight(a, c, d : Int ; b: Float){
    #                     height = 4
    #                 }
    #         }

    #         """
    #     expect = "Error on line 13 col 20: }"
    #     self.assertTrue(TestParser.test(input, expect, 227))

    # def test28(self):
    #     """ test """
    #     input = """
    #              Class Shape:People {

    #                 $getWeight(a, c, d : Int ; b: Float){
    #                     a = 4;
    #                     b = 3.14592;
    #                     c = a* b -d /2;
    #                 }
    #         }

    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 228))

    # def test29(self):
    #     """ test """
    #     input = """
    #              Class Shape:People {

    #                 $getWeight(a, c, d : Int ; b: Float){
    #                     a = 4;
    #                     b = 3.14592;
    #                     c = a* b -d 2;
    #                 }
    #         }

    #         """
    #     expect = "Error on line 7 col 36: 2"
    #     self.assertTrue(TestParser.test(input, expect, 229))

    # def test30(self):
    #     """ test """
    #     input = """
    #              Class Shape:People {

    #                 $getWeight(a, c, d : Int ; b: Float){
    #                     a = 4;
    #                     b = 3.14592;
    #                     c = a* b -d /2;
    #                     Var s : String;
    #                 }
    #         }

    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 230))

    # def test31(self):
    #     """ test """
    #     input = """
    #              Class Shape:People {
    #                 Val height: Int = ((3+4) || (5%6));
    #         }

    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 231))

    # def test32(self):
    #     """ test """
    #     input = """
    #              Class Shape:People {
    #                 Val height: Int ;
    #                 Var str1 : String = "String 1";
    #                 Var str2 : String = "String 2";
    #                 Var result : Boolean;
    #         }

    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 232))

    # def test33(self):
    #     """ test """
    #     input = """
    #              Class Shape:People {
    #                  Val result: Boolean;
    #                  getHeight(){
    #                     If(!result){
    #                 }
    #             }

    #         }

    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 233))

    # def test34(self):
    #     """ test """
    #     input = """
    #              Class Shape:People {
    #                  Val result: Boolean;
    #                  getHeight(){
    #                 If(((a >= b) && (b < c)) || (a  % 2  == 0 || a != 999) ){
    #                     result = True;
    #                 }
    #             }
    #         }

    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 234))

    # def test35(self):
    #     """ test """
    #     input = """
    #              Class Shape:People {
    #                  Val result: Boolean;
    #                  getHeight(){
    #                     If((a >= b) && (b < c)) || (a  % 2  == 0 || a != 999)){
    #                         result = True;
    #                     }
    #                 }
    #         }

    #         """
    #     expect = "Error on line 5 col 48: ||"
    #     self.assertTrue(TestParser.test(input, expect, 235))

    # def test36(self):
    #     """ test """
    #     input = """
    #              Class Shape:People {
    #                  Val result: Boolean;
    #                  getHeight(){
    #                      If(((a >= b) && (b < c)) || (a  % 2  == 0 || a != 999) ){
    #                           result = True;
    #                       }
    #                       Elseif(a % 3 == 0 ){
    #                           result = False;
    #                       }
    #                 }
    #         }

    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 236))

    # def test37(self):
    #     """ test """
    #     input = """
    #              Class Shape:People {
    #                  Val result: Boolean;
    #                  getHeight(){
    #                      If(((a >= b) && (b < c)) || (a  % 2  == 0 || a != 999) ){
    #                          result = True;
    #                      }
    #                      Elseif(a % 3 == 0 ){
    #                           result = False;
    #                       }
    #                        Else{
    #                             If( a > 100){

    #                             }
    #                            Else{

    #                             }
    #                      }
    #                 }
    #         }

    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 237))

    # def test38(self):
    #     """ test for in 38-45"""
    #     input = """
    #              Class Shape{
    #                  getHeight(){
    #                     Foreach( i In 1 .. 100 By 2){

    #                     }
    #                  }
    #         }

    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 238))

    # def test39(self):
    #     """ test for in 38-45"""
    #     input = """
    #              Class Shape{
    #                  getHeight(){
    #                      Foreach( CN In 1 .. 100 By 2){

    #                      }
    #                  }
    #         }

    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 239))

    # def test40(self):
    #     """ test for in 38-45"""
    #     input = """
    #              Class Shape{
    #                  getHeight(){
    #                      Foreach( i In 1 . 100 By 2){

    #                     }
    #                  }
    #         }

    #         """
    #     expect = "Error on line 4 col 41: ."
    #     self.assertTrue(TestParser.test(input, expect, 240))

    # def test41(self):
    #     """ test for in 38-45"""
    #     input = """
    #              Class Shape{
    #                  getHeight(){
    #                   Foreach( i In 1 .. 100 by 2){

    #                      }
    #                  }
    #         }

    #         """
    #     expect = "Error on line 4 col 45: by"
    #     self.assertTrue(TestParser.test(input, expect, 241))

    # def test42(self):
    #     """ test for in 38-45"""
    #     input = """
    #              Class Shape{
    #                  getHeight(){
    #                          Foreach( i In 1 .. 100 By 2){
    #                              Var a : Int;
    #                              a = a + 3;
    #                       }
    #                  }
    #         }

    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 242))

    # def test43(self):
    #     """ test for in 38-45"""
    #     input = """
    #              Class Shape{
    #                  getHeight(){
    #                     Foreach( i In 1 .. 100 By 2){
    #                          Var a : Int;
    #                         a = a +3;
    #                          If( (a == 6 && a % 9)){
    #                             a =  a + 1000;
    #                          }
    #                      }
    #                  }
    #         }

    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 243))

    # def test44(self):
    #     """ test for in 38-45"""
    #     input = """
    #              Class Shape{
    #                  getHeight(){
    #                          Foreach( i In 1 .. 100 By 2){
    #                           Var a : Int;
    #                           a = a +3;
    #                           If( (a == 6 && a % 9)){
    #                              a =  a + 1000;
    #                           }
    #                           Elseif(a == 9){

    #                           }
    #                       }
    #                  }
    #         }

    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 244))

    # def test45(self):
    #     """ test for in 38-45"""
    #     input = """
    #              Class Shape{
    #                  getHeight(){
    #                      Foreach( i In 1 .. 100 By 2){
    #                         Var a : Int;
    #                         a = a +3;
    #                         If( (a == 6 && a % 9)){
    #                            a =  a + 1000;
    #                         }
    #                         Else{

    #                          }
    #                     }
    #                  }
    #         }

    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 245))

    # def test46(self):
    #     """ test for in 38-45"""
    #     input = """
    #              Class Shape{
    #                  getHeight(){
    #                       Foreach( i In 1 .. 100 By 2){
    #                         Foreach(j In 1 .. 100 By 3){

    #                         }
    #                      }
    #                 }
    #         }

    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 246))

    # def test47(self):
    #     """ test for in 38-45"""
    #     input = """
    #              Class Shape{
    #                  getHeight(){
    #                       Foreach( i In 1 .. 100 ){
    #                         Foreach(j In 1 .. 100 ){

    #                         }
    #                       }
    #                 }
    #         }

    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 247))

    # def test48(self):
    #     """ test break statement 46 - 49"""
    #     input = """
    #              Class Shape{
    #                  getHeight(){
    #                        Foreach( i In 1 .. 100 ){
    #                          Break;
    #                      }
    #                 }
    #         }

    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 248))

    # def test49(self):
    #     """ test break statement 46 - 49"""
    #     input = """
    #              Class Shape{
    #                  getHeight(){
    #                      Foreach( i In 1 .. 100 ){
    #                        Break;
    #                        Break;
    #                   }
    #                 }
    #         }

    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 249))

    # def test50(self):
    #     """ test break statement 46 - 49"""
    #     input = """
    #              Class Shape{
    #                  getHeight(){
    #                       Foreach( i In 1 .. 100 ){
    #                         Break;
    #                         Foreach(j In 1 .. 100 ){
    #                              Break;
    #                        }
    #                   }
    #                 }
    #         }

    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 250))

    # def test51(self):
    #     """ test break statement 46 - 49"""
    #     input = """
    #              Class Shape{
    #                  getHeight(){
    #                     Foreach( i In 1 .. 100 ){
    #                          Break
    #                  }
    #                 }
    #         }

    #         """
    #     expect = "Error on line 6 col 21: }"
    #     self.assertTrue(TestParser.test(input, expect, 251))

    # def test52(self):
    #     """ test break Countinue 50 - 52"""
    #     input = """
    #              Class Shape{
    #                  getHeight(){
    #                    Foreach( i In 1 .. 100 ){
    #                      Continue;
    #                  }
    #                 }
    #         }

    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 252))

    # def test53(self):
    #     """ test Countinue statement 50 - 52"""
    #     input = """
    #              Class Shape{
    #                  getHeight(){
    #                       Foreach( i In 1 .. 100 ){
    #                       Continue;
    #                       Continue;
    #                     }
    #                 }
    #         }

    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 253))

    # def test54(self):
    #     """ test Countinue statement 50 - 52"""
    #     input = """
    #              Class Shape{
    #                  getHeight(){
    #                       Foreach( i In 1 .. 100 ){
    #                           Continue;
    #                         Foreach(j In 1 .. 100 ){
    #                              Continue;
    #                        }
    #                  }
    #                 }
    #         }

    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 254))

    # def test55(self):
    #     """ test resultstatement 53 - 57"""
    #     input = """
    #              Class Shape{
    #                   $getHeight(){
    #                       Return ;
    #                   }
    #         }

    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 255))

    # def test56(self):
    #     """ test resultstatement 53 - 57"""
    #     input = """
    #              Class Shape{
    #                   $getHeight(){
    #                       Return ( (100 - 12 / 16 * 10) + (42.234 * 0.124));
    #                   }
    #         }

    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 256))

    # def test57(self):
    #     """ test resultstatement 53 - 57"""
    #     input = """
    #              Class Shape{
    #                   $getHeight(){
    #                       If(a == b){
    #                           Return True;
    #                       }
    #                   }
    #         }

    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 257))

    # def test58(self):
    #     """ test resultstatement 53 - 57"""
    #     input = """
    #              Class Shape{
    #                   $getHeight(){
    #                       If(a == b){
    #                           Return True;
    #                       }
    #                       Else{
    #                           Return False;
    #                       }
    #                   }
    #         }

    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 258))

    # def test59(self):
    #     """ test resultstatement 53 - 57"""
    #     input = """
    #              Class Shape{
    #                   $getHeight(){
    #                       Foreach(i In 1 .. 1000 By 2){
    #                           Return (True || False && True);
    #                       }
    #                   }
    #         }

    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 259))

    # def test60(self):
    #     """ test resultstatement 53 - 57"""
    #     input = """
    #              Class Shape{
    #                   $getHeight(){
    #                           Return height;
    #                   }
    #         }

    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 260))

    # def test61(self):
    #     """ test resultstatement 53 - 57"""
    #     input = """
    #              Class Shape{
    #                   $getHeight(){
    #                           return $height;
    #                   }
    #         }

    #         """
    #     expect = "Error on line 4 col 37: $height"
    #     self.assertTrue(TestParser.test(input, expect, 261))

    # def test62(self):
    #     """ test resultstatement 53 - 57"""
    #     input = """
    #              Class Shape{
    #                   $getHeight(){

    #                   }
    #         }
    #         Class Program{
    #             main(){
    #                 Shape::$getHeight();
    #             }
    #         }

    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 262))

    # def test63(self):
    #     """ test resultstatement 53 - 57"""
    #     input = """
    #              Class Shape{
    #                   $getHeight(){

    #                   }
    #         }
    #         Class Program{
    #             main(){
    #                 Shape:getHeight();
    #             }
    #         }

    #         """
    #     expect = "Error on line 9 col 25: :"
    #     self.assertTrue(TestParser.test(input, expect, 263))

    # def test64(self):
    #     """ test resultstatement 53 - 57"""
    #     input = """
    #              Class Shape{
    #                   $getHeight(){

    #                   }
    #             }

    #         Class Program{
    #             main(){
    #                 Val arr: Array[Int, 3] = Array(1,2,3);
    #             }
    #         }

    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 264))

    # def test65(self):
    #     """ test resultstatement 53 - 57"""
    #     input = """
    #              Class Shape{
    #                   $getHeight(){

    #                   }
    #             }

    #         Class Program{
    #             main(){
    #                 Val arr: Array[Int, 3] = Array(1,2,3);
    #                 Var r, s: Int;
    #                 r = 2.0;
    #                 Var a, b: Array[Int, 5];
    #                 s = r * r * Self.myPI;
    #                 a[0] = s;
    #             }
    #         }

    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 265))

    # def test66(self):
    #     """ test resultstatement 53 - 57"""
    #     input = """
    #              Class Shape{
    #                  Val height: Int;
    #                   $getHeight(){

    #                   }
    #             }
    #         Class Circle:Shape{

    #         }
    #         Class Program{
    #             main(){

    #             }
    #         }

    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 266))

    # def test67(self):
    #     """ test resultstatement 53 - 57"""
    #     input = """
    #              Class Shape{
    #                  Val height: Int;
    #                   $getHeight(){

    #                   }
    #             }
    #         Class Circle:Shape{

    #         }
    #         Class Program{
    #             main(){
    #                 Out.printString("Hello World");
    #             }
    #         }

    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 267))

    # def test68(self):
    #     """ test resultstatement 53 - 57"""
    #     input = """
    #              Class Shape{
    #                  Val height: Int;
    #                   $getHeight(){

    #                   }
    #             }
    #         Class Circle:Shape{

    #         }
    #         Class Program{
    #             main(){
    #                 Out.printString("Hello World \\n \\b \\f");
    #             }
    #         }

    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 268))

    # def test69(self):
    #     """ test resultstatement 53 - 57"""
    #     input = """
    #              Class Shape{
    #                  Val height: Int;
    #                   $getHeight(){

    #                   }
    #             }
    #         Class Circle:Shape{

    #         }
    #         Class Program{
    #             main(){
    #                 Out.printString("Hello World \\n \\b \\f");
    #                 Foreach (i In 1 .. 100 By 2) {
    #                     Out.printInt(i);
    #                 }
    #             }
    #         }

    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 269))

    # def test70(self):
    #     """ test resultstatement 53 - 57"""
    #     input = """
    #              Class Shape{
    #                  Val height: Int;
    #                   $getHeight(){

    #                   }
    #             }
    #         Class Circle:Shape{

    #         }
    #         Class Program{
    #             main(){
    #                 Var arr : Array[Int, 5];
    #                 Out.printString("Hello World \\n \\b \\f");
    #                 Foreach (i In 1 .. 100 By 2) {
    #                     Out.printInt(i);
    #                 }

    #                 Foreach (x In 5 .. 2) {
    #                     Out.printInt(arr[x]);
    #                 }
    #             }
    #         }

    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 270))

    # def test71(self):
    #     """ test resultstatement 53 - 57"""
    #     input = """
    #              Class Shape{
    #                  Val height: Int;
    #                   $getHeight(){

    #                   }
    #             }
    #         Class Circle:Shape{

    #         }
    #         Class Program{
    #             main(){
    #                 Var arr : Array[Int, 5];
    #                 Out.printString("Hello World \\n \\b \\f");
    #                {
    #                    {
    #                        Out.printString("Test Block Statement \\n");
    #                    }
    #                }
    #             }
    #         }

    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 271))

    # def test72(self):
    #     """ test resultstatement 53 - 57"""
    #     input = """
    #              Class Shape{
    #                  Val height: Int;
    #                   $getHeight(){

    #                   }
    #             }
    #         Class Program{
    #             Var a,b,c: Int;
    #             main(){

    #             }
    #         }

    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 272))

    # def test73(self):
    #     """ test resultstatement 53 - 57"""
    #     input = """
    #              Class Shape{
    #                  Val height: Int;
    #                   $getHeight(){

    #                   }
    #             }
    #         Class Program{
    #             Var a,b,c: Int;
    #             getRandom(){

    #             }
    #             main(){

    #             }

    #         }

    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 273))

    # def test74(self):
    #     """ test resultstatement 53 - 57"""
    #     input = """
    #              Class Shape{
    #                  Val height: Int;
    #                   $getHeight(){

    #                   }
    #             }
    #         Class Program{
    #             Var a,b,c: Int = 3,4,5;
    #             getRandom(){

    #             }
    #             main(){

    #             }

    #         }

    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 274))

    # def test75(self):
    #     """ test resultstatement 53 - 57"""
    #     input = """
    #              Class Shape{
    #                  Val height: Int;
    #                   $getHeight(){

    #                   }
    #             }
    #         Class Program{
    #             Var a,b,c: Int = 3,5;
    #             getRandom(){

    #             }
    #             main(){

    #             }

    #         }

    #         """
    #     expect = "Error on line 9 col 36: ;"
    #     self.assertTrue(TestParser.test(input, expect, 275))

    # def test76(self):
    #     """ test resultstatement 53 - 57"""
    #     input = """
    #              Class Shape{
    #                  Val height: Int;
    #                   $getHeight(){

    #                   }
    #             }
    #         Class Program{
    #             Var a,b,c: Int = 3,5,6,7;
    #             getRandom(){

    #             }
    #             main(){

    #             }

    #         }

    #         """
    #     expect = "Error on line 9 col 38: ,"
    #     self.assertTrue(TestParser.test(input, expect, 276))

    # def test77(self):
    #     """ test resultstatement 53 - 57"""
    #     input = """
    #              Class Shape{
    #                  Val height: Int;
    #                   $getHeight(){

    #                   }
    #             }
    #         Class Program{
    #             Var a: Array[Int, 5] = Array(1,2,3,4,5);
    #             getRandom(){

    #             }
    #             main(){

    #             }

    #         }

    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 277))

    # def test78(self):
    #     """ test resultstatement 53 - 57"""
    #     input = """
    #              Class Shape{
    #                  Val height: Int;
    #                   $getHeight(){

    #                   }
    #             }
    #         Class Program{
    #             Var a: Array[Int, 5] = Array(1,2,3,4,5);
    #             getRandom(){

    #             }
    #             main(){

    #             }

    #         }

    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 278))

    # def test79(self):
    #     """ test resultstatement 53 - 57"""
    #     input = """
    #              Class Shape{
    #                  Val height: Int;
    #                   $getHeight(){

    #                   }
    #             }
    #         Class Program{
    #             Var a, b: Array[Int, 5] = Array(1,2,3,4,5), Array(5,6,7,8,9);
    #             getRandom(){

    #             }
    #             main(){

    #             }

    #         }

    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 279))

    # def test80(self):
    #     """ test resultstatement 53 - 57"""
    #     input = """
    #              Class Shape{
    #                  Val height: Int;
    #                   $getHeight(){

    #                   }
    #             }
    #         Class Program{
    #             Var a, b: Array[Int, 5] = Array(1,2,3,4,5), Array(5,6,7,8,9);
    #             main(){

    #             }
    #             getRandom(){
    #                 Foreach(i In 1 .. 100 By 2){
    #                     If(i == 50 % 2) {
    #                         Return i;
    #                     }
    #                 }
    #             }
    #         }

    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 280))

    # def test81(self):
    #     """ test resultstatement 53 - 57"""
    #     input = """
    #              Class TestString{
    #                  Val str1: String;
    #                   Test(){
    #                         str1 = "@@" +. "SUcc$$$";
    #                   }
    #             }

    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 281))

    # def test82(self):
    #     """ test resultstatement 53 - 57"""
    #     input = """
    #              Class TestString{
    #                  Val str1, str2: String;
    #                   Test(){
    #                         str1 = "@@";
    #                         str2 = "!@@";
    #                         If(str1 ==. str2){
    #                             Return "Equivalent";
    #                         }
    #                         Else{
    #                             Return "Not Equivalent";
    #                         }
    #                   }
    #             }

    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 282))

    # def test81(self):
    #     """ test resultstatement 53 - 57"""
    #     input = """
    #              Class TestString{
    #                  Val str1: String;
    #                   Test(){
    #                         str1 = "@@" +. "SUcc$$$";
    #                   }
    #             }

    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 281))

    # def test83(self):
    #     """ test resultstatement 53 - 57"""
    #     input = """
    #              Class TestString{
    #                  Val str1, str2: String;
    #                   Test(){
    #                         str1 = "@@";
    #                         str2 = "!@@";
    #                         If(str1 =.= str2){
    #                             Return "Equivalent";
    #                         }
    #                         Else{
    #                             Return "Not Equivalent";
    #                         }
    #                   }
    #             }

    #         """
    #     expect = "Error on line 7 col 36: ="
    #     self.assertTrue(TestParser.test(input, expect, 283))

    # def test84(self):
    #     """ test resultstatement 53 - 57"""
    #     input = """
    #              Class TestString{
    #                  Val color : Array[String, 5] = Array("Orange", "Black", "White", "Yellow", "Blue");
    #                   Test(){
    #                        Foreach(i In 1 .. 5){
    #                            Out.printString(color[i]);
    #                        }
    #                   }
    #             }

    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 284))

    # def test85(self):
    #     """ test resultstatement 53 - 57"""
    #     input = """
    #              Class TestString{
    #                  Val colorEG : Array[String, 5] = Array("Orange", "Black", "White", "Yellow", "Blue");
    #                  Val colorVN : Array[String, 5] = Array("Cam", "Den", "Trang", "Vang", "Xanh");
    #                   Test(){
    #                        Foreach(i In 1 .. 5){
    #                            colorEG[i] = colorEG[i] +. " :" +. colorVN[i];
    #                        }
    #                   }
    #             }

    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 285))

    # def test86(self):
    #     """ test resultstatement 53 - 57"""
    #     input = """
    #             Class Test{
    #                 Var a,b: Int;
    #                 random(){

    #                 }

    #             }
    #              Class MethodInvo{
    #                  Var a, b : Int;
    #                   Test(){
    #                      Self.a = 8;
    #                      Self.b = 9;
    #                   }
    #             }

    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 286))

    # def test87(self):
    #     """ test resultstatement 53 - 57"""
    #     input = """
    #             Class Test{
    #                 Var a,b: Int;
    #                 random(){

    #                 }

    #             }
    #              Class MethodInvo{
    #                  Var a, b : Int;
    #                   Test(){
    #                      Self.:a = 8;
    #                      Self.b = 9;
    #                   }
    #             }

    #         """
    #     expect = "Error on line 12 col 30: :"
    #     self.assertTrue(TestParser.test(input, expect, 287))

    # def test88(self):
    #     """ test resultstatement 53 - 57"""
    #     input = """
    #             Class Test{
    #                 Var a,b: Int;
    #                 random(){

    #                 }

    #             }
    #              Class MethodInvo{
    #                  Var a, b : Int;
    #                   Test(){
    #                      Self.a = Test.a;
    #                      Self.b = Test.b;
    #                   }
    #             }

    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 288))

    # def test89(self):
    #     """ test resultstatement 53 - 57"""
    #     input = """
    #             Class Test{
    #                 Var a,b: Int;
    #                 random(){

    #                 }

    #             }
    #              Class MethodInvo{
    #                  Var a, b : Int;
    #                  Var c : Float;
    #                   Test(){
    #                      Self.a = Test.a;
    #                      Self.b = Test.b;
    #                     Self.c = Test.random();
    #                   }
    #             }

    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 289))

    # def test90(self):
    #     """ test resultstatement 53 - 57"""
    #     input = """
    #             Class Test{
    #                 $staticFunc(){

    #                 }

    #             }
    #              Class MethodInvo{

    #                   Test(){
    #                     Test::$staticFunc();
    #                   }
    #             }

    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 290))

    # def test91(self):
    #     """ test resultstatement 53 - 57"""
    #     input = """
    #             Class Test{
    #                 Var $a,  b : Int;

    #             }
    #              Class MethodInvo{

    #                   Test(){
    #                     Test::$a;
    #                   }
    #             }

    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 291))

    # def test92(self):
    #     """ test resultstatement 53 - 57"""
    #     input = """
    #             Class Test{
    #                  Var $a,  b : Int;
    #                 $staticFunc(){

    #                 }

    #             }
    #              Class MethodInvo{

    #                   Test(){
    #                       Test::$a;
    #                     Test::$staticFunc();
    #                   }
    #             }

    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 292))

    # def test93(self):
    #     """ test resultstatement 53 - 57"""
    #     input = """
    #             Class Test{
    #                  Var $a,  b : Int;
    #                 $staticFunc(){

    #                 }

    #             }
    #              Class MethodInvo{

    #                   Test(){
    #                     Test::a;
    #                     Test::$staticFunc();
    #                   }
    #             }

    #         """
    #     expect = "Error on line 12 col 30: a"
    #     self.assertTrue(TestParser.test(input, expect, 293))

    # def test94(self):
    #     """ test resultstatement 53 - 57"""
    #     input = """
    #             Class Test{
    #                  Var $a,  b : Int;
    #                 $staticFunc(){

    #                 }

    #             }
    #              Class MethodInvo{

    #                   Test(){
    #                     Test::$a;
    #                     Test::staticFunc(); ##miss $ character followed##
    #                   }
    #             }

    #         """
    #     expect = "Error on line 13 col 30: staticFunc"
    #     self.assertTrue(TestParser.test(input, expect, 294))

    # def test95(self):
    #     """ test resultstatement 53 - 57"""
    #     input = """
    #             Class Test{

    #                 $staticFunc(a, b: Int){

    #                 }

    #             }
    #              Class MethodInvo{
    #                 Var a, b: Int;
    #                   Test(){
    #                     Test::$staticFunc(a,b); ##miss $ character followed##
    #                   }
    #             }

    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 295))

    # def test95(self):
    #     """ test resultstatement 53 - 57"""
    #     input = """
    #             Class Test{

    #                 $staticFunc(a, b: Int ; c : Float){

    #                 }

    #             }
    #              Class MethodInvo{
    #                 Var a, b: Int;
    #                 Var c: Float;
    #                   Test(){
    #                     Test::$staticFunc(a,b, c); ##miss $ character followed##
    #                   }
    #             }

    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 295))

    # def test96(self):
    #     """ test resultstatement 53 - 57"""
    #     input = """
    #             Class Test{

    #                 $staticFunc(a, b: Int , c : Float){

    #                 }

    #             }
    #              Class MethodInvo{
    #                 Var a, b: Int;
    #                 Var c: Float;
    #                   Test(){
    #                     Test::$staticFunc(a,b, c); ##miss $ character followed##
    #                   }
    #             }

    #         """
    #     expect = "Error on line 4 col 42: ,"
    #     self.assertTrue(TestParser.test(input, expect, 296))

    # def test97(self):
    #     """ test resultstatement 53 - 57"""
    #     input = """
    #             Class Test{

    #               Break;

    #             }

    #         """
    #     expect = "Error on line 4 col 18: Break"
    #     self.assertTrue(TestParser.test(input, expect, 297))

    # def test98(self):
    #     """ test resultstatement 53 - 57"""
    #     input = """
    #             Class Program{
    #                 main(){
    #                     {
    #                         {
    #                             {{{{
    #                         Var a : Int = 4;
    #                         }
    #                         }}}}}
    #                 }
    #             }
    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 298))

    # def test99(self):
    #     """ test resultstatement 53 - 57"""
    #     input = """
    #             Class Program{
    #                 main(){
    #                     {
    #                         {
    #                             {{{
    #                         Var a : Int = 4;
    #                         }
    #                         }}}}}
    #                 }
    #             }
    #         """
    #     expect = "Error on line 11 col 16: }"
    #     self.assertTrue(TestParser.test(input, expect, 299))

    # def test100(self):
    #     """ test resultstatement 53 - 57"""
    #     input = """
    #               Class Program{
    #                 main(){
    #                     {
    #                         {

    #                         Var a : Int = 4;
    #                         }
    #                       }
    #                       {
    #                        {

    #                         Var b: Int = 5;
    #                         }
    #                       }
    #                 }
    #             }
    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 300))

    def test1(self):
        """Class declare"""
        input = """
                     Class Shape{
                         Val a : Int ;
                  }
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 999))
