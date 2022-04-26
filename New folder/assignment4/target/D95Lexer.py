# Generated from main/d95/parser/D95.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2A")
        buf.write("\u0211\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\7\b\u00c8\n\b\f\b\16")
        buf.write("\b\u00cb\13\b\3\t\3\t\7\t\u00cf\n\t\f\t\16\t\u00d2\13")
        buf.write("\t\3\n\3\n\7\n\u00d6\n\n\f\n\16\n\u00d9\13\n\3\13\3\13")
        buf.write("\6\13\u00dd\n\13\r\13\16\13\u00de\3\f\3\f\7\f\u00e3\n")
        buf.write("\f\f\f\16\f\u00e6\13\f\3\f\5\f\u00e9\n\f\3\r\3\r\3\r\6")
        buf.write("\r\u00ee\n\r\r\r\16\r\u00ef\3\16\3\16\3\16\6\16\u00f5")
        buf.write("\n\16\r\16\16\16\u00f6\3\17\5\17\u00fa\n\17\3\17\6\17")
        buf.write("\u00fd\n\17\r\17\16\17\u00fe\3\20\3\20\3\20\3\20\3\20")
        buf.write("\5\20\u0106\n\20\3\21\3\21\3\21\3\21\3\21\5\21\u010d\n")
        buf.write("\21\3\21\3\21\5\21\u0111\n\21\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\5\22\u011a\n\22\3\23\3\23\3\23\5\23\u011f\n")
        buf.write("\23\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3")
        buf.write(" \3 \3 \3!\3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3#\3#\3#\3$\3")
        buf.write("$\3$\3$\3$\5$\u0183\n$\3%\3%\7%\u0187\n%\f%\16%\u018a")
        buf.write("\13%\3%\3%\7%\u018e\n%\f%\16%\u0191\13%\6%\u0193\n%\r")
        buf.write("%\16%\u0194\3%\3%\3&\3&\3&\3&\3&\3&\3&\7&\u01a0\n&\f&")
        buf.write("\16&\u01a3\13&\3&\3&\3\'\3\'\3\'\3(\3(\3)\3)\3)\3*\3*")
        buf.write("\3+\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61")
        buf.write("\3\62\3\62\3\62\3\63\3\63\3\63\3\64\3\64\3\64\3\65\3\65")
        buf.write("\3\66\3\66\3\66\3\66\3\67\3\67\3\67\38\38\38\39\39\3:")
        buf.write("\3:\3;\3;\3<\3<\3=\3=\3>\3>\3?\3?\3@\3@\3A\3A\3B\3B\3")
        buf.write("C\3C\3C\3C\7C\u01ed\nC\fC\16C\u01f0\13C\3C\3C\3C\3C\3")
        buf.write("C\3D\6D\u01f8\nD\rD\16D\u01f9\3D\3D\3E\3E\3F\3F\3F\3F")
        buf.write("\7F\u0204\nF\fF\16F\u0207\13F\3G\3G\3G\3G\7G\u020d\nG")
        buf.write("\fG\16G\u0210\13G\3\u01ee\2H\3\3\5\4\7\5\t\6\13\7\r\b")
        buf.write("\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\2\37\2!\2#\2")
        buf.write("%\20\'\21)\22+\23-\24/\25\61\26\63\27\65\30\67\319\32")
        buf.write(";\33=\34?\35A\36C\2E\2G\2I\37K M!O\"Q#S$U%W&Y\'[(])_*")
        buf.write("a+c,e-g.i/k\60m\61o\62q\63s\64u\65w\66y\67{8}9\177:\u0081")
        buf.write(";\u0083<\u0085=\u0087>\u0089?\u008b@\u008dA\3\2\23\6\2")
        buf.write("\62;C\\aac|\3\2C\\\4\2\629aa\3\2\63;\4\2\62;aa\4\2ZZz")
        buf.write("z\6\2\62;CHaach\4\2DDdd\4\2\62\63aa\4\2--//\3\2\62;\t")
        buf.write("\2))^^ddhhppttvv\3\2$$\5\2\13\f\17\17\"\"\t\2$$^^ddhh")
        buf.write("ppttvv\6\2\n\f\16\17$$^^\3\2\61\61\2\u022a\2\3\3\2\2\2")
        buf.write("\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r")
        buf.write("\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3")
        buf.write("\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2%\3\2\2")
        buf.write("\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2")
        buf.write("\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2")
        buf.write("\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2")
        buf.write("\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3")
        buf.write("\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[")
        buf.write("\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2")
        buf.write("e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2")
        buf.write("\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2")
        buf.write("\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081")
        buf.write("\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2")
        buf.write("\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\3\u008f")
        buf.write("\3\2\2\2\5\u0097\3\2\2\2\7\u009f\3\2\2\2\t\u00a9\3\2\2")
        buf.write("\2\13\u00b3\3\2\2\2\r\u00bc\3\2\2\2\17\u00c5\3\2\2\2\21")
        buf.write("\u00cc\3\2\2\2\23\u00d3\3\2\2\2\25\u00da\3\2\2\2\27\u00e8")
        buf.write("\3\2\2\2\31\u00ea\3\2\2\2\33\u00f1\3\2\2\2\35\u00f9\3")
        buf.write("\2\2\2\37\u0100\3\2\2\2!\u0107\3\2\2\2#\u0112\3\2\2\2")
        buf.write("%\u011e\3\2\2\2\'\u0120\3\2\2\2)\u0126\3\2\2\2+\u012f")
        buf.write("\3\2\2\2-\u0132\3\2\2\2/\u0139\3\2\2\2\61\u013e\3\2\2")
        buf.write("\2\63\u0144\3\2\2\2\65\u014c\3\2\2\2\67\u014f\3\2\2\2")
        buf.write("9\u0158\3\2\2\2;\u015d\3\2\2\2=\u0163\3\2\2\2?\u0169\3")
        buf.write("\2\2\2A\u0170\3\2\2\2C\u0177\3\2\2\2E\u017a\3\2\2\2G\u0182")
        buf.write("\3\2\2\2I\u0184\3\2\2\2K\u0198\3\2\2\2M\u01a6\3\2\2\2")
        buf.write("O\u01a9\3\2\2\2Q\u01ab\3\2\2\2S\u01ae\3\2\2\2U\u01b0\3")
        buf.write("\2\2\2W\u01b3\3\2\2\2Y\u01b5\3\2\2\2[\u01b7\3\2\2\2]\u01b9")
        buf.write("\3\2\2\2_\u01bb\3\2\2\2a\u01bd\3\2\2\2c\u01bf\3\2\2\2")
        buf.write("e\u01c2\3\2\2\2g\u01c5\3\2\2\2i\u01c8\3\2\2\2k\u01ca\3")
        buf.write("\2\2\2m\u01ce\3\2\2\2o\u01d1\3\2\2\2q\u01d4\3\2\2\2s\u01d6")
        buf.write("\3\2\2\2u\u01d8\3\2\2\2w\u01da\3\2\2\2y\u01dc\3\2\2\2")
        buf.write("{\u01de\3\2\2\2}\u01e0\3\2\2\2\177\u01e2\3\2\2\2\u0081")
        buf.write("\u01e4\3\2\2\2\u0083\u01e6\3\2\2\2\u0085\u01e8\3\2\2\2")
        buf.write("\u0087\u01f7\3\2\2\2\u0089\u01fd\3\2\2\2\u008b\u01ff\3")
        buf.write("\2\2\2\u008d\u0208\3\2\2\2\u008f\u0090\7u\2\2\u0090\u0091")
        buf.write("\7v\2\2\u0091\u0092\7t\2\2\u0092\u0093\7\64\2\2\u0093")
        buf.write("\u0094\7k\2\2\u0094\u0095\7p\2\2\u0095\u0096\7v\2\2\u0096")
        buf.write("\4\3\2\2\2\u0097\u0098\7k\2\2\u0098\u0099\7p\2\2\u0099")
        buf.write("\u009a\7v\2\2\u009a\u009b\7\64\2\2\u009b\u009c\7u\2\2")
        buf.write("\u009c\u009d\7v\2\2\u009d\u009e\7t\2\2\u009e\6\3\2\2\2")
        buf.write("\u009f\u00a0\7u\2\2\u00a0\u00a1\7v\2\2\u00a1\u00a2\7t")
        buf.write("\2\2\u00a2\u00a3\7\64\2\2\u00a3\u00a4\7h\2\2\u00a4\u00a5")
        buf.write("\7n\2\2\u00a5\u00a6\7q\2\2\u00a6\u00a7\7c\2\2\u00a7\u00a8")
        buf.write("\7v\2\2\u00a8\b\3\2\2\2\u00a9\u00aa\7h\2\2\u00aa\u00ab")
        buf.write("\7n\2\2\u00ab\u00ac\7q\2\2\u00ac\u00ad\7c\2\2\u00ad\u00ae")
        buf.write("\7v\2\2\u00ae\u00af\7\64\2\2\u00af\u00b0\7u\2\2\u00b0")
        buf.write("\u00b1\7v\2\2\u00b1\u00b2\7t\2\2\u00b2\n\3\2\2\2\u00b3")
        buf.write("\u00b4\7u\2\2\u00b4\u00b5\7v\2\2\u00b5\u00b6\7t\2\2\u00b6")
        buf.write("\u00b7\7\64\2\2\u00b7\u00b8\7d\2\2\u00b8\u00b9\7q\2\2")
        buf.write("\u00b9\u00ba\7q\2\2\u00ba\u00bb\7n\2\2\u00bb\f\3\2\2\2")
        buf.write("\u00bc\u00bd\7d\2\2\u00bd\u00be\7q\2\2\u00be\u00bf\7q")
        buf.write("\2\2\u00bf\u00c0\7n\2\2\u00c0\u00c1\7\64\2\2\u00c1\u00c2")
        buf.write("\7u\2\2\u00c2\u00c3\7v\2\2\u00c3\u00c4\7t\2\2\u00c4\16")
        buf.write("\3\2\2\2\u00c5\u00c9\7&\2\2\u00c6\u00c8\t\2\2\2\u00c7")
        buf.write("\u00c6\3\2\2\2\u00c8\u00cb\3\2\2\2\u00c9\u00c7\3\2\2\2")
        buf.write("\u00c9\u00ca\3\2\2\2\u00ca\20\3\2\2\2\u00cb\u00c9\3\2")
        buf.write("\2\2\u00cc\u00d0\t\3\2\2\u00cd\u00cf\t\2\2\2\u00ce\u00cd")
        buf.write("\3\2\2\2\u00cf\u00d2\3\2\2\2\u00d0\u00ce\3\2\2\2\u00d0")
        buf.write("\u00d1\3\2\2\2\u00d1\22\3\2\2\2\u00d2\u00d0\3\2\2\2\u00d3")
        buf.write("\u00d7\7a\2\2\u00d4\u00d6\t\2\2\2\u00d5\u00d4\3\2\2\2")
        buf.write("\u00d6\u00d9\3\2\2\2\u00d7\u00d5\3\2\2\2\u00d7\u00d8\3")
        buf.write("\2\2\2\u00d8\24\3\2\2\2\u00d9\u00d7\3\2\2\2\u00da\u00dc")
        buf.write("\7\62\2\2\u00db\u00dd\t\4\2\2\u00dc\u00db\3\2\2\2\u00dd")
        buf.write("\u00de\3\2\2\2\u00de\u00dc\3\2\2\2\u00de\u00df\3\2\2\2")
        buf.write("\u00df\26\3\2\2\2\u00e0\u00e4\t\5\2\2\u00e1\u00e3\t\6")
        buf.write("\2\2\u00e2\u00e1\3\2\2\2\u00e3\u00e6\3\2\2\2\u00e4\u00e2")
        buf.write("\3\2\2\2\u00e4\u00e5\3\2\2\2\u00e5\u00e9\3\2\2\2\u00e6")
        buf.write("\u00e4\3\2\2\2\u00e7\u00e9\7\62\2\2\u00e8\u00e0\3\2\2")
        buf.write("\2\u00e8\u00e7\3\2\2\2\u00e9\30\3\2\2\2\u00ea\u00eb\7")
        buf.write("\62\2\2\u00eb\u00ed\t\7\2\2\u00ec\u00ee\t\b\2\2\u00ed")
        buf.write("\u00ec\3\2\2\2\u00ee\u00ef\3\2\2\2\u00ef\u00ed\3\2\2\2")
        buf.write("\u00ef\u00f0\3\2\2\2\u00f0\32\3\2\2\2\u00f1\u00f2\7\62")
        buf.write("\2\2\u00f2\u00f4\t\t\2\2\u00f3\u00f5\t\n\2\2\u00f4\u00f3")
        buf.write("\3\2\2\2\u00f5\u00f6\3\2\2\2\u00f6\u00f4\3\2\2\2\u00f6")
        buf.write("\u00f7\3\2\2\2\u00f7\34\3\2\2\2\u00f8\u00fa\t\13\2\2\u00f9")
        buf.write("\u00f8\3\2\2\2\u00f9\u00fa\3\2\2\2\u00fa\u00fc\3\2\2\2")
        buf.write("\u00fb\u00fd\t\f\2\2\u00fc\u00fb\3\2\2\2\u00fd\u00fe\3")
        buf.write("\2\2\2\u00fe\u00fc\3\2\2\2\u00fe\u00ff\3\2\2\2\u00ff\36")
        buf.write("\3\2\2\2\u0100\u0105\5\27\f\2\u0101\u0102\7g\2\2\u0102")
        buf.write("\u0106\5\35\17\2\u0103\u0104\7G\2\2\u0104\u0106\5\35\17")
        buf.write("\2\u0105\u0101\3\2\2\2\u0105\u0103\3\2\2\2\u0105\u0106")
        buf.write("\3\2\2\2\u0106 \3\2\2\2\u0107\u010c\5\27\f\2\u0108\u0109")
        buf.write("\7g\2\2\u0109\u010d\5\35\17\2\u010a\u010b\7G\2\2\u010b")
        buf.write("\u010d\5\35\17\2\u010c\u0108\3\2\2\2\u010c\u010a\3\2\2")
        buf.write("\2\u010c\u010d\3\2\2\2\u010d\u010e\3\2\2\2\u010e\u0110")
        buf.write("\7\60\2\2\u010f\u0111\5\27\f\2\u0110\u010f\3\2\2\2\u0110")
        buf.write("\u0111\3\2\2\2\u0111\"\3\2\2\2\u0112\u0113\5\27\f\2\u0113")
        buf.write("\u0114\7\60\2\2\u0114\u0119\5\27\f\2\u0115\u0116\7g\2")
        buf.write("\2\u0116\u011a\5\35\17\2\u0117\u0118\7G\2\2\u0118\u011a")
        buf.write("\5\35\17\2\u0119\u0115\3\2\2\2\u0119\u0117\3\2\2\2\u0119")
        buf.write("\u011a\3\2\2\2\u011a$\3\2\2\2\u011b\u011f\5\37\20\2\u011c")
        buf.write("\u011f\5!\21\2\u011d\u011f\5#\22\2\u011e\u011b\3\2\2\2")
        buf.write("\u011e\u011c\3\2\2\2\u011e\u011d\3\2\2\2\u011f&\3\2\2")
        buf.write("\2\u0120\u0121\7d\2\2\u0121\u0122\7t\2\2\u0122\u0123\7")
        buf.write("g\2\2\u0123\u0124\7c\2\2\u0124\u0125\7m\2\2\u0125(\3\2")
        buf.write("\2\2\u0126\u0127\7e\2\2\u0127\u0128\7q\2\2\u0128\u0129")
        buf.write("\7p\2\2\u0129\u012a\7v\2\2\u012a\u012b\7k\2\2\u012b\u012c")
        buf.write("\7p\2\2\u012c\u012d\7w\2\2\u012d\u012e\7g\2\2\u012e*\3")
        buf.write("\2\2\2\u012f\u0130\7k\2\2\u0130\u0131\7h\2\2\u0131,\3")
        buf.write("\2\2\2\u0132\u0133\7g\2\2\u0133\u0134\7n\2\2\u0134\u0135")
        buf.write("\7u\2\2\u0135\u0136\7g\2\2\u0136\u0137\7k\2\2\u0137\u0138")
        buf.write("\7h\2\2\u0138.\3\2\2\2\u0139\u013a\7g\2\2\u013a\u013b")
        buf.write("\7n\2\2\u013b\u013c\7u\2\2\u013c\u013d\7g\2\2\u013d\60")
        buf.write("\3\2\2\2\u013e\u013f\7y\2\2\u013f\u0140\7j\2\2\u0140\u0141")
        buf.write("\7k\2\2\u0141\u0142\7n\2\2\u0142\u0143\7g\2\2\u0143\62")
        buf.write("\3\2\2\2\u0144\u0145\7h\2\2\u0145\u0146\7q\2\2\u0146\u0147")
        buf.write("\7t\2\2\u0147\u0148\7g\2\2\u0148\u0149\7c\2\2\u0149\u014a")
        buf.write("\7e\2\2\u014a\u014b\7j\2\2\u014b\64\3\2\2\2\u014c\u014d")
        buf.write("\7c\2\2\u014d\u014e\7u\2\2\u014e\66\3\2\2\2\u014f\u0150")
        buf.write("\7h\2\2\u0150\u0151\7w\2\2\u0151\u0152\7p\2\2\u0152\u0153")
        buf.write("\7e\2\2\u0153\u0154\7v\2\2\u0154\u0155\7k\2\2\u0155\u0156")
        buf.write("\7q\2\2\u0156\u0157\7p\2\2\u01578\3\2\2\2\u0158\u0159")
        buf.write("\7v\2\2\u0159\u015a\7t\2\2\u015a\u015b\7w\2\2\u015b\u015c")
        buf.write("\7g\2\2\u015c:\3\2\2\2\u015d\u015e\7h\2\2\u015e\u015f")
        buf.write("\7c\2\2\u015f\u0160\7n\2\2\u0160\u0161\7u\2\2\u0161\u0162")
        buf.write("\7g\2\2\u0162<\3\2\2\2\u0163\u0164\7c\2\2\u0164\u0165")
        buf.write("\7t\2\2\u0165\u0166\7t\2\2\u0166\u0167\7c\2\2\u0167\u0168")
        buf.write("\7{\2\2\u0168>\3\2\2\2\u0169\u016a\7f\2\2\u016a\u016b")
        buf.write("\7g\2\2\u016b\u016c\7h\2\2\u016c\u016d\7k\2\2\u016d\u016e")
        buf.write("\7p\2\2\u016e\u016f\7g\2\2\u016f@\3\2\2\2\u0170\u0171")
        buf.write("\7t\2\2\u0171\u0172\7g\2\2\u0172\u0173\7v\2\2\u0173\u0174")
        buf.write("\7w\2\2\u0174\u0175\7t\2\2\u0175\u0176\7p\2\2\u0176B\3")
        buf.write("\2\2\2\u0177\u0178\7^\2\2\u0178\u0179\n\r\2\2\u0179D\3")
        buf.write("\2\2\2\u017a\u017b\7^\2\2\u017b\u017c\t\r\2\2\u017cF\3")
        buf.write("\2\2\2\u017d\u0183\n\16\2\2\u017e\u017f\7$\2\2\u017f\u0183")
        buf.write("\7$\2\2\u0180\u0181\7)\2\2\u0181\u0183\7$\2\2\u0182\u017d")
        buf.write("\3\2\2\2\u0182\u017e\3\2\2\2\u0182\u0180\3\2\2\2\u0183")
        buf.write("H\3\2\2\2\u0184\u0192\7$\2\2\u0185\u0187\5G$\2\u0186\u0185")
        buf.write("\3\2\2\2\u0187\u018a\3\2\2\2\u0188\u0186\3\2\2\2\u0188")
        buf.write("\u0189\3\2\2\2\u0189\u018b\3\2\2\2\u018a\u0188\3\2\2\2")
        buf.write("\u018b\u018f\5C\"\2\u018c\u018e\5G$\2\u018d\u018c\3\2")
        buf.write("\2\2\u018e\u0191\3\2\2\2\u018f\u018d\3\2\2\2\u018f\u0190")
        buf.write("\3\2\2\2\u0190\u0193\3\2\2\2\u0191\u018f\3\2\2\2\u0192")
        buf.write("\u0188\3\2\2\2\u0193\u0194\3\2\2\2\u0194\u0192\3\2\2\2")
        buf.write("\u0194\u0195\3\2\2\2\u0195\u0196\3\2\2\2\u0196\u0197\7")
        buf.write("$\2\2\u0197J\3\2\2\2\u0198\u01a1\7$\2\2\u0199\u01a0\5")
        buf.write("E#\2\u019a\u01a0\n\16\2\2\u019b\u019c\7$\2\2\u019c\u01a0")
        buf.write("\7$\2\2\u019d\u019e\7)\2\2\u019e\u01a0\7$\2\2\u019f\u0199")
        buf.write("\3\2\2\2\u019f\u019a\3\2\2\2\u019f\u019b\3\2\2\2\u019f")
        buf.write("\u019d\3\2\2\2\u01a0\u01a3\3\2\2\2\u01a1\u019f\3\2\2\2")
        buf.write("\u01a1\u01a2\3\2\2\2\u01a2\u01a4\3\2\2\2\u01a3\u01a1\3")
        buf.write("\2\2\2\u01a4\u01a5\7$\2\2\u01a5L\3\2\2\2\u01a6\u01a7\7")
        buf.write("#\2\2\u01a7\u01a8\7?\2\2\u01a8N\3\2\2\2\u01a9\u01aa\7")
        buf.write("@\2\2\u01aaP\3\2\2\2\u01ab\u01ac\7@\2\2\u01ac\u01ad\7")
        buf.write("?\2\2\u01adR\3\2\2\2\u01ae\u01af\7>\2\2\u01afT\3\2\2\2")
        buf.write("\u01b0\u01b1\7>\2\2\u01b1\u01b2\7?\2\2\u01b2V\3\2\2\2")
        buf.write("\u01b3\u01b4\7-\2\2\u01b4X\3\2\2\2\u01b5\u01b6\7/\2\2")
        buf.write("\u01b6Z\3\2\2\2\u01b7\u01b8\7,\2\2\u01b8\\\3\2\2\2\u01b9")
        buf.write("\u01ba\7\61\2\2\u01ba^\3\2\2\2\u01bb\u01bc\7\'\2\2\u01bc")
        buf.write("`\3\2\2\2\u01bd\u01be\7#\2\2\u01beb\3\2\2\2\u01bf\u01c0")
        buf.write("\7(\2\2\u01c0\u01c1\7(\2\2\u01c1d\3\2\2\2\u01c2\u01c3")
        buf.write("\7~\2\2\u01c3\u01c4\7~\2\2\u01c4f\3\2\2\2\u01c5\u01c6")
        buf.write("\7?\2\2\u01c6\u01c7\7?\2\2\u01c7h\3\2\2\2\u01c8\u01c9")
        buf.write("\7?\2\2\u01c9j\3\2\2\2\u01ca\u01cb\7?\2\2\u01cb\u01cc")
        buf.write("\7?\2\2\u01cc\u01cd\7\60\2\2\u01cdl\3\2\2\2\u01ce\u01cf")
        buf.write("\7-\2\2\u01cf\u01d0\7\60\2\2\u01d0n\3\2\2\2\u01d1\u01d2")
        buf.write("\7?\2\2\u01d2\u01d3\7@\2\2\u01d3p\3\2\2\2\u01d4\u01d5")
        buf.write("\7\60\2\2\u01d5r\3\2\2\2\u01d6\u01d7\7.\2\2\u01d7t\3\2")
        buf.write("\2\2\u01d8\u01d9\7=\2\2\u01d9v\3\2\2\2\u01da\u01db\7<")
        buf.write("\2\2\u01dbx\3\2\2\2\u01dc\u01dd\7*\2\2\u01ddz\3\2\2\2")
        buf.write("\u01de\u01df\7+\2\2\u01df|\3\2\2\2\u01e0\u01e1\7]\2\2")
        buf.write("\u01e1~\3\2\2\2\u01e2\u01e3\7_\2\2\u01e3\u0080\3\2\2\2")
        buf.write("\u01e4\u01e5\7}\2\2\u01e5\u0082\3\2\2\2\u01e6\u01e7\7")
        buf.write("\177\2\2\u01e7\u0084\3\2\2\2\u01e8\u01e9\7\61\2\2\u01e9")
        buf.write("\u01ea\7,\2\2\u01ea\u01ee\3\2\2\2\u01eb\u01ed\13\2\2\2")
        buf.write("\u01ec\u01eb\3\2\2\2\u01ed\u01f0\3\2\2\2\u01ee\u01ef\3")
        buf.write("\2\2\2\u01ee\u01ec\3\2\2\2\u01ef\u01f1\3\2\2\2\u01f0\u01ee")
        buf.write("\3\2\2\2\u01f1\u01f2\7,\2\2\u01f2\u01f3\7\61\2\2\u01f3")
        buf.write("\u01f4\3\2\2\2\u01f4\u01f5\bC\2\2\u01f5\u0086\3\2\2\2")
        buf.write("\u01f6\u01f8\t\17\2\2\u01f7\u01f6\3\2\2\2\u01f8\u01f9")
        buf.write("\3\2\2\2\u01f9\u01f7\3\2\2\2\u01f9\u01fa\3\2\2\2\u01fa")
        buf.write("\u01fb\3\2\2\2\u01fb\u01fc\bD\2\2\u01fc\u0088\3\2\2\2")
        buf.write("\u01fd\u01fe\13\2\2\2\u01fe\u008a\3\2\2\2\u01ff\u0205")
        buf.write("\7$\2\2\u0200\u0201\7^\2\2\u0201\u0204\t\20\2\2\u0202")
        buf.write("\u0204\n\21\2\2\u0203\u0200\3\2\2\2\u0203\u0202\3\2\2")
        buf.write("\2\u0204\u0207\3\2\2\2\u0205\u0203\3\2\2\2\u0205\u0206")
        buf.write("\3\2\2\2\u0206\u008c\3\2\2\2\u0207\u0205\3\2\2\2\u0208")
        buf.write("\u0209\7\61\2\2\u0209\u020a\7,\2\2\u020a\u020e\3\2\2\2")
        buf.write("\u020b\u020d\n\22\2\2\u020c\u020b\3\2\2\2\u020d\u0210")
        buf.write("\3\2\2\2\u020e\u020c\3\2\2\2\u020e\u020f\3\2\2\2\u020f")
        buf.write("\u008e\3\2\2\2\u0210\u020e\3\2\2\2 \2\u00c7\u00c9\u00ce")
        buf.write("\u00d0\u00d5\u00d7\u00de\u00e4\u00e8\u00ef\u00f6\u00f9")
        buf.write("\u00fe\u0105\u010c\u0110\u0119\u011e\u0182\u0188\u018f")
        buf.write("\u0194\u019f\u01a1\u01ee\u01f9\u0203\u0205\u020e\3\b\2")
        buf.write("\2")
        return buf.getvalue()


class D95Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    STR2INT = 1
    INT2STR = 2
    STR2FLOAT = 3
    FLOAT2STR = 4
    STR2BOOL = 5
    BOOL2STR = 6
    ID_VARPAR = 7
    ID_CONST = 8
    ID_FUNC = 9
    OCT = 10
    DEC = 11
    HEX = 12
    BIN = 13
    FLOAT = 14
    BREAK = 15
    CONTINUE = 16
    IF = 17
    ELSEIF = 18
    ElSE = 19
    WHILE = 20
    FOREACH = 21
    AS = 22
    FUNCTION = 23
    TRUE = 24
    FALSE = 25
    ARRAY_TYPE = 26
    DEFINE = 27
    RETURN = 28
    ILLEGAL_ESCAPE = 29
    STRING = 30
    NOT_EQUAL = 31
    GREATER = 32
    GREATER_EQUAL = 33
    LESS = 34
    LESS_EQUAL = 35
    ADD = 36
    SUB = 37
    MUL = 38
    DIV = 39
    MOD = 40
    NOT = 41
    AND = 42
    OR = 43
    EQUAL = 44
    ASSIGN = 45
    STR_CMP = 46
    STR_CAT = 47
    ASSOCATE = 48
    DOT = 49
    COMMA = 50
    SEMI = 51
    COLON = 52
    LP = 53
    RP = 54
    LSB = 55
    RSB = 56
    LB = 57
    RB = 58
    COMMENT = 59
    WS = 60
    ERROR_CHAR = 61
    UNCLOSE_STRING = 62
    UNTERMINATED_COMMENT = 63

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'str2int'", "'int2str'", "'str2float'", "'float2str'", "'str2bool'", 
            "'bool2str'", "'break'", "'continue'", "'if'", "'elseif'", "'else'", 
            "'while'", "'foreach'", "'as'", "'function'", "'true'", "'false'", 
            "'array'", "'define'", "'return'", "'!='", "'>'", "'>='", "'<'", 
            "'<='", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", 
            "'=='", "'='", "'==.'", "'+.'", "'=>'", "'.'", "','", "';'", 
            "':'", "'('", "')'", "'['", "']'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "STR2INT", "INT2STR", "STR2FLOAT", "FLOAT2STR", "STR2BOOL", 
            "BOOL2STR", "ID_VARPAR", "ID_CONST", "ID_FUNC", "OCT", "DEC", 
            "HEX", "BIN", "FLOAT", "BREAK", "CONTINUE", "IF", "ELSEIF", 
            "ElSE", "WHILE", "FOREACH", "AS", "FUNCTION", "TRUE", "FALSE", 
            "ARRAY_TYPE", "DEFINE", "RETURN", "ILLEGAL_ESCAPE", "STRING", 
            "NOT_EQUAL", "GREATER", "GREATER_EQUAL", "LESS", "LESS_EQUAL", 
            "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", "AND", "OR", "EQUAL", 
            "ASSIGN", "STR_CMP", "STR_CAT", "ASSOCATE", "DOT", "COMMA", 
            "SEMI", "COLON", "LP", "RP", "LSB", "RSB", "LB", "RB", "COMMENT", 
            "WS", "ERROR_CHAR", "UNCLOSE_STRING", "UNTERMINATED_COMMENT" ]

    ruleNames = [ "STR2INT", "INT2STR", "STR2FLOAT", "FLOAT2STR", "STR2BOOL", 
                  "BOOL2STR", "ID_VARPAR", "ID_CONST", "ID_FUNC", "OCT", 
                  "DEC", "HEX", "BIN", "Num", "FLOAT1", "FLOAT2", "FLOAT3", 
                  "FLOAT", "BREAK", "CONTINUE", "IF", "ELSEIF", "ElSE", 
                  "WHILE", "FOREACH", "AS", "FUNCTION", "TRUE", "FALSE", 
                  "ARRAY_TYPE", "DEFINE", "RETURN", "I_ESCAPE", "ESCAPE", 
                  "TMP", "ILLEGAL_ESCAPE", "STRING", "NOT_EQUAL", "GREATER", 
                  "GREATER_EQUAL", "LESS", "LESS_EQUAL", "ADD", "SUB", "MUL", 
                  "DIV", "MOD", "NOT", "AND", "OR", "EQUAL", "ASSIGN", "STR_CMP", 
                  "STR_CAT", "ASSOCATE", "DOT", "COMMA", "SEMI", "COLON", 
                  "LP", "RP", "LSB", "RSB", "LB", "RB", "COMMENT", "WS", 
                  "ERROR_CHAR", "UNCLOSE_STRING", "UNTERMINATED_COMMENT" ]

    grammarFileName = "D95.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        result = super().emit()
        if tk == self.UNCLOSE_STRING:
            result.text = result.text[1:]
            raise UncloseString(result.text)

        elif tk == self.ILLEGAL_ESCAPE:
            result.text = result.text[1:]
            legal = ['b','f','r','n','t','\'','\\']
            idx = 0;
            check = False
            backslash = False
            for i in result.text:
                if backslash == True:
                    backslash = False
                    idx+=1
                    continue
                if i == '\\':
                    if result.text[idx+1] == '\\' and result.text[idx-1] != '\\':
                        idx+=1
                        backslash = True
                        continue
                    check = False
                    for j in legal:
                        if result.text[idx+1] == j:
                            check = True
                            break
                    if check == False: break
                idx+=1
            result.text = result.text[0:idx+2]
            raise IllegalEscape(result.text)

        elif tk == self.ERROR_CHAR:
            raise ErrorToken(result.text)

        elif tk == self.UNTERMINATED_COMMENT:
            raise UnterminatedComment()

        elif tk == tk == self.FLOAT:
            result.text = result.text.replace("_","")
            value = result.text
            result.text = str(float(value))
            return result
        elif tk == self.HEX:
            result.text = result.text.replace("_","")
            value = result.text
            result.text = str(int(value, 16))
            return result
        elif tk == self.OCT:
            result.text = result.text.replace("_","")
            value = result.text
            result.text = str(int(value, 8))
            return result
        elif tk == self.BIN:
            result.text = result.text.replace("_","")
            value = result.text
            result.text = str(int(value, 2))
            return result
        elif tk == self.DEC:
            result.text = result.text.replace("_","")
            return result
        elif tk == self.STRING:
            result.text = result.text[1:-1]
            return result
        else:
            return result;


