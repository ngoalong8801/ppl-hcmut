# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2B")
        buf.write("\u0269\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\5\3\5\3\5\7\5")
        buf.write("\u00a4\n\5\f\5\16\5\u00a7\13\5\3\5\3\5\3\5\3\5\3\5\7\5")
        buf.write("\u00ae\n\5\f\5\16\5\u00b1\13\5\3\5\3\5\3\5\3\5\3\5\7\5")
        buf.write("\u00b8\n\5\f\5\16\5\u00bb\13\5\3\5\3\5\5\5\u00bf\n\5\3")
        buf.write("\5\3\5\3\6\3\6\7\6\u00c5\n\6\f\6\16\6\u00c8\13\6\3\6\6")
        buf.write("\6\u00cb\n\6\r\6\16\6\u00cc\3\6\5\6\u00d0\n\6\3\7\3\7")
        buf.write("\3\7\3\7\3\7\7\7\u00d7\n\7\f\7\16\7\u00da\13\7\3\7\5\7")
        buf.write("\u00dd\n\7\3\7\6\7\u00e0\n\7\r\7\16\7\u00e1\7\7\u00e4")
        buf.write("\n\7\f\7\16\7\u00e7\13\7\5\7\u00e9\n\7\3\7\3\7\7\7\u00ed")
        buf.write("\n\7\f\7\16\7\u00f0\13\7\3\7\5\7\u00f3\n\7\3\7\6\7\u00f6")
        buf.write("\n\7\r\7\16\7\u00f7\7\7\u00fa\n\7\f\7\16\7\u00fd\13\7")
        buf.write("\3\7\7\7\u0100\n\7\f\7\16\7\u0103\13\7\3\7\5\7\u0106\n")
        buf.write("\7\3\7\3\7\3\7\6\7\u010b\n\7\r\7\16\7\u010c\3\7\5\7\u0110")
        buf.write("\n\7\3\7\6\7\u0113\n\7\r\7\16\7\u0114\6\7\u0117\n\7\r")
        buf.write("\7\16\7\u0118\3\7\5\7\u011c\n\7\3\7\3\7\6\7\u0120\n\7")
        buf.write("\r\7\16\7\u0121\3\7\5\7\u0125\n\7\3\7\6\7\u0128\n\7\r")
        buf.write("\7\16\7\u0129\6\7\u012c\n\7\r\7\16\7\u012d\3\7\5\7\u0131")
        buf.write("\n\7\5\7\u0133\n\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\5\b\u0140\n\b\3\t\3\t\3\t\3\t\7\t\u0146\n\t\f")
        buf.write("\t\16\t\u0149\13\t\3\t\3\t\3\t\3\n\3\n\5\n\u0150\n\n\3")
        buf.write("\13\3\13\3\13\3\f\3\f\3\f\5\f\u0158\n\f\3\r\3\r\5\r\u015c")
        buf.write("\n\r\3\r\6\r\u015f\n\r\r\r\16\r\u0160\3\16\3\16\3\17\3")
        buf.write("\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24")
        buf.write("\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\30\3\31\3\31")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\5\33\u0188\n\33\3\34\3\34\3\34\3\34\7\34\u018e\n")
        buf.write("\34\f\34\16\34\u0191\13\34\3\34\3\34\3\34\3\34\3\34\3")
        buf.write("\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3 \3!\3")
        buf.write("!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3")
        buf.write("#\3$\3$\3$\3$\3$\3$\3$\3$\3$\3%\3%\3%\3&\3&\3&\3&\3&\3")
        buf.write("&\3&\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3(\3(\3(\3(\3)\3")
        buf.write(")\3)\3)\3)\3)\3)\3*\3*\3*\3*\3*\3+\3+\3+\3+\3,\3,\3,\3")
        buf.write(",\3,\3,\3,\3,\3,\3,\3,\3,\3-\3-\3-\3-\3-\3-\3-\3-\3-\3")
        buf.write("-\3-\3.\3.\3.\3/\3/\3/\3\60\3\60\3\61\3\61\3\61\3\62\3")
        buf.write("\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67")
        buf.write("\38\38\38\39\39\39\3:\3:\3:\3;\3;\3;\3<\3<\3<\3=\3=\3")
        buf.write(">\3>\3>\3?\3?\3@\3@\3A\3A\3A\3A\3B\3B\3B\3C\3C\7C\u0241")
        buf.write("\nC\fC\16C\u0244\13C\3D\3D\7D\u0248\nD\fD\16D\u024b\13")
        buf.write("D\3E\6E\u024e\nE\rE\16E\u024f\3E\3E\3F\3F\7F\u0256\nF")
        buf.write("\fF\16F\u0259\13F\3F\3F\3G\3G\7G\u025f\nG\fG\16G\u0262")
        buf.write("\13G\3G\3G\3G\3H\3H\3H\3\u018f\2I\3\3\5\4\7\5\t\6\13\2")
        buf.write("\r\7\17\b\21\t\23\2\25\2\27\2\31\2\33\2\35\2\37\n!\13")
        buf.write("#\f%\r\'\16)\17+\20-\21/\22\61\23\63\24\65\25\67\269\27")
        buf.write(";\30=\31?\32A\33C\34E\35G\36I\37K M!O\"Q#S$U%W&Y\'[(]")
        buf.write(")_*a+c,e-g.i/k\60m\61o\62q\63s\64u\65w\66y\67{8}9\177")
        buf.write(":\u0081;\u0083<\u0085=\u0087>\u0089?\u008b@\u008dA\u008f")
        buf.write("B\3\2\30\3\2\63;\4\2\62;aa\3\2\62;\3\2\62\62\4\2DDdd\3")
        buf.write("\2\63\63\3\2\62\63\3\2aa\4\2ZZzz\4\2\62;CH\3\2\629\3\2")
        buf.write("))\3\2$$\4\2$$^^\t\2))^^ddhhppttvv\3\2^^\4\2GGgg\5\2-")
        buf.write("-//aa\5\2C\\aac|\6\2\62;C\\aac|\3\2&&\5\2\13\f\17\17\"")
        buf.write("\"\2\u0290\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2")
        buf.write("\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\37\3\2\2")
        buf.write("\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2")
        buf.write("\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63")
        buf.write("\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2")
        buf.write("\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2")
        buf.write("\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3")
        buf.write("\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y")
        buf.write("\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2")
        buf.write("c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2")
        buf.write("\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2")
        buf.write("\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3")
        buf.write("\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2")
        buf.write("\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d")
        buf.write("\3\2\2\2\2\u008f\3\2\2\2\3\u0091\3\2\2\2\5\u0099\3\2\2")
        buf.write("\2\7\u009e\3\2\2\2\t\u00be\3\2\2\2\13\u00cf\3\2\2\2\r")
        buf.write("\u0132\3\2\2\2\17\u013f\3\2\2\2\21\u0141\3\2\2\2\23\u014f")
        buf.write("\3\2\2\2\25\u0151\3\2\2\2\27\u0157\3\2\2\2\31\u0159\3")
        buf.write("\2\2\2\33\u0162\3\2\2\2\35\u0164\3\2\2\2\37\u0166\3\2")
        buf.write("\2\2!\u0168\3\2\2\2#\u016a\3\2\2\2%\u016c\3\2\2\2\'\u016e")
        buf.write("\3\2\2\2)\u0170\3\2\2\2+\u0172\3\2\2\2-\u0174\3\2\2\2")
        buf.write("/\u0176\3\2\2\2\61\u0179\3\2\2\2\63\u017b\3\2\2\2\65\u0187")
        buf.write("\3\2\2\2\67\u0189\3\2\2\29\u0197\3\2\2\2;\u019d\3\2\2")
        buf.write("\2=\u01a1\3\2\2\2?\u01a7\3\2\2\2A\u01af\3\2\2\2C\u01b6")
        buf.write("\3\2\2\2E\u01bb\3\2\2\2G\u01c1\3\2\2\2I\u01ca\3\2\2\2")
        buf.write("K\u01cd\3\2\2\2M\u01d4\3\2\2\2O\u01d9\3\2\2\2Q\u01e1\3")
        buf.write("\2\2\2S\u01e8\3\2\2\2U\u01ed\3\2\2\2W\u01f1\3\2\2\2Y\u01fd")
        buf.write("\3\2\2\2[\u0208\3\2\2\2]\u020b\3\2\2\2_\u020e\3\2\2\2")
        buf.write("a\u0210\3\2\2\2c\u0213\3\2\2\2e\u0215\3\2\2\2g\u0217\3")
        buf.write("\2\2\2i\u0219\3\2\2\2k\u021b\3\2\2\2m\u021d\3\2\2\2o\u021f")
        buf.write("\3\2\2\2q\u0222\3\2\2\2s\u0225\3\2\2\2u\u0228\3\2\2\2")
        buf.write("w\u022b\3\2\2\2y\u022e\3\2\2\2{\u0230\3\2\2\2}\u0233\3")
        buf.write("\2\2\2\177\u0235\3\2\2\2\u0081\u0237\3\2\2\2\u0083\u023b")
        buf.write("\3\2\2\2\u0085\u023e\3\2\2\2\u0087\u0245\3\2\2\2\u0089")
        buf.write("\u024d\3\2\2\2\u008b\u0253\3\2\2\2\u008d\u025c\3\2\2\2")
        buf.write("\u008f\u0266\3\2\2\2\u0091\u0092\7R\2\2\u0092\u0093\7")
        buf.write("t\2\2\u0093\u0094\7q\2\2\u0094\u0095\7i\2\2\u0095\u0096")
        buf.write("\7t\2\2\u0096\u0097\7c\2\2\u0097\u0098\7o\2\2\u0098\4")
        buf.write("\3\2\2\2\u0099\u009a\7o\2\2\u009a\u009b\7c\2\2\u009b\u009c")
        buf.write("\7k\2\2\u009c\u009d\7p\2\2\u009d\6\3\2\2\2\u009e\u009f")
        buf.write("\7&\2\2\u009f\b\3\2\2\2\u00a0\u00a1\5\13\6\2\u00a1\u00a5")
        buf.write("\5_\60\2\u00a2\u00a4\5\35\17\2\u00a3\u00a2\3\2\2\2\u00a4")
        buf.write("\u00a7\3\2\2\2\u00a5\u00a3\3\2\2\2\u00a5\u00a6\3\2\2\2")
        buf.write("\u00a6\u00a8\3\2\2\2\u00a7\u00a5\3\2\2\2\u00a8\u00a9\5")
        buf.write("\31\r\2\u00a9\u00bf\3\2\2\2\u00aa\u00ab\5\13\6\2\u00ab")
        buf.write("\u00af\5_\60\2\u00ac\u00ae\5\35\17\2\u00ad\u00ac\3\2\2")
        buf.write("\2\u00ae\u00b1\3\2\2\2\u00af\u00ad\3\2\2\2\u00af\u00b0")
        buf.write("\3\2\2\2\u00b0\u00bf\3\2\2\2\u00b1\u00af\3\2\2\2\u00b2")
        buf.write("\u00b3\5\13\6\2\u00b3\u00b4\5\31\r\2\u00b4\u00bf\3\2\2")
        buf.write("\2\u00b5\u00b9\5_\60\2\u00b6\u00b8\5\35\17\2\u00b7\u00b6")
        buf.write("\3\2\2\2\u00b8\u00bb\3\2\2\2\u00b9\u00b7\3\2\2\2\u00b9")
        buf.write("\u00ba\3\2\2\2\u00ba\u00bc\3\2\2\2\u00bb\u00b9\3\2\2\2")
        buf.write("\u00bc\u00bd\5\31\r\2\u00bd\u00bf\3\2\2\2\u00be\u00a0")
        buf.write("\3\2\2\2\u00be\u00aa\3\2\2\2\u00be\u00b2\3\2\2\2\u00be")
        buf.write("\u00b5\3\2\2\2\u00bf\u00c0\3\2\2\2\u00c0\u00c1\b\5\2\2")
        buf.write("\u00c1\n\3\2\2\2\u00c2\u00c6\t\2\2\2\u00c3\u00c5\t\3\2")
        buf.write("\2\u00c4\u00c3\3\2\2\2\u00c5\u00c8\3\2\2\2\u00c6\u00c4")
        buf.write("\3\2\2\2\u00c6\u00c7\3\2\2\2\u00c7\u00ca\3\2\2\2\u00c8")
        buf.write("\u00c6\3\2\2\2\u00c9\u00cb\t\4\2\2\u00ca\u00c9\3\2\2\2")
        buf.write("\u00cb\u00cc\3\2\2\2\u00cc\u00ca\3\2\2\2\u00cc\u00cd\3")
        buf.write("\2\2\2\u00cd\u00d0\3\2\2\2\u00ce\u00d0\t\4\2\2\u00cf\u00c2")
        buf.write("\3\2\2\2\u00cf\u00ce\3\2\2\2\u00d0\f\3\2\2\2\u00d1\u00d2")
        buf.write("\t\5\2\2\u00d2\u00e8\t\6\2\2\u00d3\u00e9\t\5\2\2\u00d4")
        buf.write("\u00d8\t\7\2\2\u00d5\u00d7\t\b\2\2\u00d6\u00d5\3\2\2\2")
        buf.write("\u00d7\u00da\3\2\2\2\u00d8\u00d6\3\2\2\2\u00d8\u00d9\3")
        buf.write("\2\2\2\u00d9\u00e5\3\2\2\2\u00da\u00d8\3\2\2\2\u00db\u00dd")
        buf.write("\t\t\2\2\u00dc\u00db\3\2\2\2\u00dc\u00dd\3\2\2\2\u00dd")
        buf.write("\u00df\3\2\2\2\u00de\u00e0\t\b\2\2\u00df\u00de\3\2\2\2")
        buf.write("\u00e0\u00e1\3\2\2\2\u00e1\u00df\3\2\2\2\u00e1\u00e2\3")
        buf.write("\2\2\2\u00e2\u00e4\3\2\2\2\u00e3\u00dc\3\2\2\2\u00e4\u00e7")
        buf.write("\3\2\2\2\u00e5\u00e3\3\2\2\2\u00e5\u00e6\3\2\2\2\u00e6")
        buf.write("\u00e9\3\2\2\2\u00e7\u00e5\3\2\2\2\u00e8\u00d3\3\2\2\2")
        buf.write("\u00e8\u00d4\3\2\2\2\u00e9\u0133\3\2\2\2\u00ea\u00ee\t")
        buf.write("\2\2\2\u00eb\u00ed\t\4\2\2\u00ec\u00eb\3\2\2\2\u00ed\u00f0")
        buf.write("\3\2\2\2\u00ee\u00ec\3\2\2\2\u00ee\u00ef\3\2\2\2\u00ef")
        buf.write("\u00fb\3\2\2\2\u00f0\u00ee\3\2\2\2\u00f1\u00f3\t\t\2\2")
        buf.write("\u00f2\u00f1\3\2\2\2\u00f2\u00f3\3\2\2\2\u00f3\u00f5\3")
        buf.write("\2\2\2\u00f4\u00f6\t\4\2\2\u00f5\u00f4\3\2\2\2\u00f6\u00f7")
        buf.write("\3\2\2\2\u00f7\u00f5\3\2\2\2\u00f7\u00f8\3\2\2\2\u00f8")
        buf.write("\u00fa\3\2\2\2\u00f9\u00f2\3\2\2\2\u00fa\u00fd\3\2\2\2")
        buf.write("\u00fb\u00f9\3\2\2\2\u00fb\u00fc\3\2\2\2\u00fc\u0101\3")
        buf.write("\2\2\2\u00fd\u00fb\3\2\2\2\u00fe\u0100\t\4\2\2\u00ff\u00fe")
        buf.write("\3\2\2\2\u0100\u0103\3\2\2\2\u0101\u00ff\3\2\2\2\u0101")
        buf.write("\u0102\3\2\2\2\u0102\u0106\3\2\2\2\u0103\u0101\3\2\2\2")
        buf.write("\u0104\u0106\t\4\2\2\u0105\u00ea\3\2\2\2\u0105\u0104\3")
        buf.write("\2\2\2\u0106\u0133\3\2\2\2\u0107\u0108\t\5\2\2\u0108\u011b")
        buf.write("\t\n\2\2\u0109\u010b\t\13\2\2\u010a\u0109\3\2\2\2\u010b")
        buf.write("\u010c\3\2\2\2\u010c\u010a\3\2\2\2\u010c\u010d\3\2\2\2")
        buf.write("\u010d\u010f\3\2\2\2\u010e\u0110\t\t\2\2\u010f\u010e\3")
        buf.write("\2\2\2\u010f\u0110\3\2\2\2\u0110\u0112\3\2\2\2\u0111\u0113")
        buf.write("\t\13\2\2\u0112\u0111\3\2\2\2\u0113\u0114\3\2\2\2\u0114")
        buf.write("\u0112\3\2\2\2\u0114\u0115\3\2\2\2\u0115\u0117\3\2\2\2")
        buf.write("\u0116\u010a\3\2\2\2\u0117\u0118\3\2\2\2\u0118\u0116\3")
        buf.write("\2\2\2\u0118\u0119\3\2\2\2\u0119\u011c\3\2\2\2\u011a\u011c")
        buf.write("\t\13\2\2\u011b\u0116\3\2\2\2\u011b\u011a\3\2\2\2\u011c")
        buf.write("\u0133\3\2\2\2\u011d\u0130\t\5\2\2\u011e\u0120\t\f\2\2")
        buf.write("\u011f\u011e\3\2\2\2\u0120\u0121\3\2\2\2\u0121\u011f\3")
        buf.write("\2\2\2\u0121\u0122\3\2\2\2\u0122\u0124\3\2\2\2\u0123\u0125")
        buf.write("\t\t\2\2\u0124\u0123\3\2\2\2\u0124\u0125\3\2\2\2\u0125")
        buf.write("\u0127\3\2\2\2\u0126\u0128\t\f\2\2\u0127\u0126\3\2\2\2")
        buf.write("\u0128\u0129\3\2\2\2\u0129\u0127\3\2\2\2\u0129\u012a\3")
        buf.write("\2\2\2\u012a\u012c\3\2\2\2\u012b\u011f\3\2\2\2\u012c\u012d")
        buf.write("\3\2\2\2\u012d\u012b\3\2\2\2\u012d\u012e\3\2\2\2\u012e")
        buf.write("\u0131\3\2\2\2\u012f\u0131\t\f\2\2\u0130\u012b\3\2\2\2")
        buf.write("\u0130\u012f\3\2\2\2\u0131\u0133\3\2\2\2\u0132\u00d1\3")
        buf.write("\2\2\2\u0132\u0105\3\2\2\2\u0132\u0107\3\2\2\2\u0132\u011d")
        buf.write("\3\2\2\2\u0133\u0134\3\2\2\2\u0134\u0135\b\7\3\2\u0135")
        buf.write("\16\3\2\2\2\u0136\u0137\7V\2\2\u0137\u0138\7t\2\2\u0138")
        buf.write("\u0139\7w\2\2\u0139\u0140\7g\2\2\u013a\u013b\7H\2\2\u013b")
        buf.write("\u013c\7c\2\2\u013c\u013d\7n\2\2\u013d\u013e\7u\2\2\u013e")
        buf.write("\u0140\7g\2\2\u013f\u0136\3\2\2\2\u013f\u013a\3\2\2\2")
        buf.write("\u0140\20\3\2\2\2\u0141\u0147\7$\2\2\u0142\u0146\5\23")
        buf.write("\n\2\u0143\u0144\t\r\2\2\u0144\u0146\t\16\2\2\u0145\u0142")
        buf.write("\3\2\2\2\u0145\u0143\3\2\2\2\u0146\u0149\3\2\2\2\u0147")
        buf.write("\u0145\3\2\2\2\u0147\u0148\3\2\2\2\u0148\u014a\3\2\2\2")
        buf.write("\u0149\u0147\3\2\2\2\u014a\u014b\7$\2\2\u014b\u014c\b")
        buf.write("\t\4\2\u014c\22\3\2\2\2\u014d\u0150\5\25\13\2\u014e\u0150")
        buf.write("\n\17\2\2\u014f\u014d\3\2\2\2\u014f\u014e\3\2\2\2\u0150")
        buf.write("\24\3\2\2\2\u0151\u0152\7^\2\2\u0152\u0153\t\20\2\2\u0153")
        buf.write("\26\3\2\2\2\u0154\u0155\7^\2\2\u0155\u0158\n\20\2\2\u0156")
        buf.write("\u0158\n\21\2\2\u0157\u0154\3\2\2\2\u0157\u0156\3\2\2")
        buf.write("\2\u0158\30\3\2\2\2\u0159\u015b\t\22\2\2\u015a\u015c\5")
        buf.write("\33\16\2\u015b\u015a\3\2\2\2\u015b\u015c\3\2\2\2\u015c")
        buf.write("\u015e\3\2\2\2\u015d\u015f\5\35\17\2\u015e\u015d\3\2\2")
        buf.write("\2\u015f\u0160\3\2\2\2\u0160\u015e\3\2\2\2\u0160\u0161")
        buf.write("\3\2\2\2\u0161\32\3\2\2\2\u0162\u0163\t\23\2\2\u0163\34")
        buf.write("\3\2\2\2\u0164\u0165\t\4\2\2\u0165\36\3\2\2\2\u0166\u0167")
        buf.write("\7*\2\2\u0167 \3\2\2\2\u0168\u0169\7+\2\2\u0169\"\3\2")
        buf.write("\2\2\u016a\u016b\7}\2\2\u016b$\3\2\2\2\u016c\u016d\7\177")
        buf.write("\2\2\u016d&\3\2\2\2\u016e\u016f\7]\2\2\u016f(\3\2\2\2")
        buf.write("\u0170\u0171\7_\2\2\u0171*\3\2\2\2\u0172\u0173\7=\2\2")
        buf.write("\u0173,\3\2\2\2\u0174\u0175\7<\2\2\u0175.\3\2\2\2\u0176")
        buf.write("\u0177\7<\2\2\u0177\u0178\7<\2\2\u0178\60\3\2\2\2\u0179")
        buf.write("\u017a\7.\2\2\u017a\62\3\2\2\2\u017b\u017c\7E\2\2\u017c")
        buf.write("\u017d\7n\2\2\u017d\u017e\7c\2\2\u017e\u017f\7u\2\2\u017f")
        buf.write("\u0180\7u\2\2\u0180\64\3\2\2\2\u0181\u0182\7X\2\2\u0182")
        buf.write("\u0183\7c\2\2\u0183\u0188\7n\2\2\u0184\u0185\7X\2\2\u0185")
        buf.write("\u0186\7c\2\2\u0186\u0188\7t\2\2\u0187\u0181\3\2\2\2\u0187")
        buf.write("\u0184\3\2\2\2\u0188\66\3\2\2\2\u0189\u018a\7%\2\2\u018a")
        buf.write("\u018b\7%\2\2\u018b\u018f\3\2\2\2\u018c\u018e\13\2\2\2")
        buf.write("\u018d\u018c\3\2\2\2\u018e\u0191\3\2\2\2\u018f\u0190\3")
        buf.write("\2\2\2\u018f\u018d\3\2\2\2\u0190\u0192\3\2\2\2\u0191\u018f")
        buf.write("\3\2\2\2\u0192\u0193\7%\2\2\u0193\u0194\7%\2\2\u0194\u0195")
        buf.write("\3\2\2\2\u0195\u0196\b\34\5\2\u01968\3\2\2\2\u0197\u0198")
        buf.write("\7C\2\2\u0198\u0199\7t\2\2\u0199\u019a\7t\2\2\u019a\u019b")
        buf.write("\7c\2\2\u019b\u019c\7{\2\2\u019c:\3\2\2\2\u019d\u019e")
        buf.write("\7K\2\2\u019e\u019f\7p\2\2\u019f\u01a0\7v\2\2\u01a0<\3")
        buf.write("\2\2\2\u01a1\u01a2\7H\2\2\u01a2\u01a3\7n\2\2\u01a3\u01a4")
        buf.write("\7q\2\2\u01a4\u01a5\7c\2\2\u01a5\u01a6\7v\2\2\u01a6>\3")
        buf.write("\2\2\2\u01a7\u01a8\7D\2\2\u01a8\u01a9\7q\2\2\u01a9\u01aa")
        buf.write("\7q\2\2\u01aa\u01ab\7n\2\2\u01ab\u01ac\7g\2\2\u01ac\u01ad")
        buf.write("\7c\2\2\u01ad\u01ae\7p\2\2\u01ae@\3\2\2\2\u01af\u01b0")
        buf.write("\7U\2\2\u01b0\u01b1\7v\2\2\u01b1\u01b2\7t\2\2\u01b2\u01b3")
        buf.write("\7k\2\2\u01b3\u01b4\7p\2\2\u01b4\u01b5\7i\2\2\u01b5B\3")
        buf.write("\2\2\2\u01b6\u01b7\7P\2\2\u01b7\u01b8\7w\2\2\u01b8\u01b9")
        buf.write("\7n\2\2\u01b9\u01ba\7n\2\2\u01baD\3\2\2\2\u01bb\u01bc")
        buf.write("\7D\2\2\u01bc\u01bd\7t\2\2\u01bd\u01be\7g\2\2\u01be\u01bf")
        buf.write("\7c\2\2\u01bf\u01c0\7m\2\2\u01c0F\3\2\2\2\u01c1\u01c2")
        buf.write("\7E\2\2\u01c2\u01c3\7q\2\2\u01c3\u01c4\7p\2\2\u01c4\u01c5")
        buf.write("\7v\2\2\u01c5\u01c6\7k\2\2\u01c6\u01c7\7p\2\2\u01c7\u01c8")
        buf.write("\7w\2\2\u01c8\u01c9\7g\2\2\u01c9H\3\2\2\2\u01ca\u01cb")
        buf.write("\7K\2\2\u01cb\u01cc\7h\2\2\u01ccJ\3\2\2\2\u01cd\u01ce")
        buf.write("\7G\2\2\u01ce\u01cf\7n\2\2\u01cf\u01d0\7u\2\2\u01d0\u01d1")
        buf.write("\7g\2\2\u01d1\u01d2\7k\2\2\u01d2\u01d3\7h\2\2\u01d3L\3")
        buf.write("\2\2\2\u01d4\u01d5\7G\2\2\u01d5\u01d6\7n\2\2\u01d6\u01d7")
        buf.write("\7u\2\2\u01d7\u01d8\7g\2\2\u01d8N\3\2\2\2\u01d9\u01da")
        buf.write("\7H\2\2\u01da\u01db\7q\2\2\u01db\u01dc\7t\2\2\u01dc\u01dd")
        buf.write("\7g\2\2\u01dd\u01de\7c\2\2\u01de\u01df\7e\2\2\u01df\u01e0")
        buf.write("\7j\2\2\u01e0P\3\2\2\2\u01e1\u01e2\7T\2\2\u01e2\u01e3")
        buf.write("\7g\2\2\u01e3\u01e4\7v\2\2\u01e4\u01e5\7w\2\2\u01e5\u01e6")
        buf.write("\7t\2\2\u01e6\u01e7\7p\2\2\u01e7R\3\2\2\2\u01e8\u01e9")
        buf.write("\7u\2\2\u01e9\u01ea\7g\2\2\u01ea\u01eb\7n\2\2\u01eb\u01ec")
        buf.write("\7h\2\2\u01ecT\3\2\2\2\u01ed\u01ee\7P\2\2\u01ee\u01ef")
        buf.write("\7g\2\2\u01ef\u01f0\7y\2\2\u01f0V\3\2\2\2\u01f1\u01f2")
        buf.write("\7E\2\2\u01f2\u01f3\7q\2\2\u01f3\u01f4\7p\2\2\u01f4\u01f5")
        buf.write("\7u\2\2\u01f5\u01f6\7v\2\2\u01f6\u01f7\7t\2\2\u01f7\u01f8")
        buf.write("\7w\2\2\u01f8\u01f9\7e\2\2\u01f9\u01fa\7v\2\2\u01fa\u01fb")
        buf.write("\7q\2\2\u01fb\u01fc\7t\2\2\u01fcX\3\2\2\2\u01fd\u01fe")
        buf.write("\7F\2\2\u01fe\u01ff\7g\2\2\u01ff\u0200\7u\2\2\u0200\u0201")
        buf.write("\7v\2\2\u0201\u0202\7t\2\2\u0202\u0203\7w\2\2\u0203\u0204")
        buf.write("\7e\2\2\u0204\u0205\7v\2\2\u0205\u0206\7q\2\2\u0206\u0207")
        buf.write("\7t\2\2\u0207Z\3\2\2\2\u0208\u0209\7K\2\2\u0209\u020a")
        buf.write("\7p\2\2\u020a\\\3\2\2\2\u020b\u020c\7D\2\2\u020c\u020d")
        buf.write("\7{\2\2\u020d^\3\2\2\2\u020e\u020f\7\60\2\2\u020f`\3\2")
        buf.write("\2\2\u0210\u0211\7\60\2\2\u0211\u0212\7\60\2\2\u0212b")
        buf.write("\3\2\2\2\u0213\u0214\7-\2\2\u0214d\3\2\2\2\u0215\u0216")
        buf.write("\7/\2\2\u0216f\3\2\2\2\u0217\u0218\7,\2\2\u0218h\3\2\2")
        buf.write("\2\u0219\u021a\7\61\2\2\u021aj\3\2\2\2\u021b\u021c\7\'")
        buf.write("\2\2\u021cl\3\2\2\2\u021d\u021e\7#\2\2\u021en\3\2\2\2")
        buf.write("\u021f\u0220\7(\2\2\u0220\u0221\7(\2\2\u0221p\3\2\2\2")
        buf.write("\u0222\u0223\7~\2\2\u0223\u0224\7~\2\2\u0224r\3\2\2\2")
        buf.write("\u0225\u0226\7>\2\2\u0226\u0227\7?\2\2\u0227t\3\2\2\2")
        buf.write("\u0228\u0229\7@\2\2\u0229\u022a\7?\2\2\u022av\3\2\2\2")
        buf.write("\u022b\u022c\7#\2\2\u022c\u022d\7?\2\2\u022dx\3\2\2\2")
        buf.write("\u022e\u022f\7?\2\2\u022fz\3\2\2\2\u0230\u0231\7?\2\2")
        buf.write("\u0231\u0232\7?\2\2\u0232|\3\2\2\2\u0233\u0234\7>\2\2")
        buf.write("\u0234~\3\2\2\2\u0235\u0236\7@\2\2\u0236\u0080\3\2\2\2")
        buf.write("\u0237\u0238\7?\2\2\u0238\u0239\7?\2\2\u0239\u023a\7\60")
        buf.write("\2\2\u023a\u0082\3\2\2\2\u023b\u023c\7-\2\2\u023c\u023d")
        buf.write("\7\60\2\2\u023d\u0084\3\2\2\2\u023e\u0242\t\24\2\2\u023f")
        buf.write("\u0241\t\25\2\2\u0240\u023f\3\2\2\2\u0241\u0244\3\2\2")
        buf.write("\2\u0242\u0240\3\2\2\2\u0242\u0243\3\2\2\2\u0243\u0086")
        buf.write("\3\2\2\2\u0244\u0242\3\2\2\2\u0245\u0249\t\26\2\2\u0246")
        buf.write("\u0248\t\25\2\2\u0247\u0246\3\2\2\2\u0248\u024b\3\2\2")
        buf.write("\2\u0249\u0247\3\2\2\2\u0249\u024a\3\2\2\2\u024a\u0088")
        buf.write("\3\2\2\2\u024b\u0249\3\2\2\2\u024c\u024e\t\27\2\2\u024d")
        buf.write("\u024c\3\2\2\2\u024e\u024f\3\2\2\2\u024f\u024d\3\2\2\2")
        buf.write("\u024f\u0250\3\2\2\2\u0250\u0251\3\2\2\2\u0251\u0252\b")
        buf.write("E\5\2\u0252\u008a\3\2\2\2\u0253\u0257\7$\2\2\u0254\u0256")
        buf.write("\5\23\n\2\u0255\u0254\3\2\2\2\u0256\u0259\3\2\2\2\u0257")
        buf.write("\u0255\3\2\2\2\u0257\u0258\3\2\2\2\u0258\u025a\3\2\2\2")
        buf.write("\u0259\u0257\3\2\2\2\u025a\u025b\bF\6\2\u025b\u008c\3")
        buf.write("\2\2\2\u025c\u0260\7$\2\2\u025d\u025f\5\23\n\2\u025e\u025d")
        buf.write("\3\2\2\2\u025f\u0262\3\2\2\2\u0260\u025e\3\2\2\2\u0260")
        buf.write("\u0261\3\2\2\2\u0261\u0263\3\2\2\2\u0262\u0260\3\2\2\2")
        buf.write("\u0263\u0264\5\27\f\2\u0264\u0265\bG\7\2\u0265\u008e\3")
        buf.write("\2\2\2\u0266\u0267\13\2\2\2\u0267\u0268\bH\b\2\u0268\u0090")
        buf.write("\3\2\2\2.\2\u00a5\u00af\u00b9\u00be\u00c6\u00cc\u00cf")
        buf.write("\u00d8\u00dc\u00e1\u00e5\u00e8\u00ee\u00f2\u00f7\u00fb")
        buf.write("\u0101\u0105\u010c\u010f\u0114\u0118\u011b\u0121\u0124")
        buf.write("\u0129\u012d\u0130\u0132\u013f\u0145\u0147\u014f\u0157")
        buf.write("\u015b\u0160\u0187\u018f\u0242\u0249\u024f\u0257\u0260")
        buf.write("\t\3\5\2\3\7\3\3\t\4\b\2\2\3F\5\3G\6\3H\7")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    FLOAT_LITERAL = 4
    INTEGER_LITERAL = 5
    BOOLEAN_LITERAL = 6
    STRING_LITERAL = 7
    LB = 8
    RB = 9
    LP = 10
    RP = 11
    LSB = 12
    RSB = 13
    SEMI = 14
    COL = 15
    DCOL = 16
    COM = 17
    CLASS = 18
    ATTR = 19
    BLOCK_COMMENT = 20
    ARRAY = 21
    INT = 22
    FLOAT = 23
    BOOLEAN = 24
    STRING = 25
    NULL = 26
    BREAK = 27
    CONTINUE = 28
    IF = 29
    ELSEIF = 30
    ELSE = 31
    FOREACH = 32
    RETURN = 33
    SELF = 34
    NEW = 35
    CONSTRUCTOR = 36
    DESTRUCTOR = 37
    IN = 38
    BY = 39
    DOT = 40
    DDOT = 41
    OP_ADD = 42
    OP_SUB = 43
    OP_MUL = 44
    OP_DIV = 45
    OP_MOD = 46
    OP_NOT = 47
    OP_AND = 48
    OP_OR = 49
    OP_LTE = 50
    OP_GTE = 51
    OP_NEQ = 52
    OP_AS = 53
    OP_EQ = 54
    OP_LT = 55
    OP_GT = 56
    OP_EQ_STR = 57
    OP_ADD_STR = 58
    IDEN = 59
    DOL_IDEN = 60
    WS = 61
    UNCLOSE_STRING = 62
    ILLEGAL_ESCAPE = 63
    ERROR_CHAR = 64

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Program'", "'main'", "'$'", "'('", "')'", "'{'", "'}'", "'['", 
            "']'", "';'", "':'", "'::'", "','", "'Class'", "'Array'", "'Int'", 
            "'Float'", "'Boolean'", "'String'", "'Null'", "'Break'", "'Continue'", 
            "'If'", "'Elseif'", "'Else'", "'Foreach'", "'Return'", "'self'", 
            "'New'", "'Constructor'", "'Destructor'", "'In'", "'By'", "'.'", 
            "'..'", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", 
            "'<='", "'>='", "'!='", "'='", "'=='", "'<'", "'>'", "'==.'", 
            "'+.'" ]

    symbolicNames = [ "<INVALID>",
            "FLOAT_LITERAL", "INTEGER_LITERAL", "BOOLEAN_LITERAL", "STRING_LITERAL", 
            "LB", "RB", "LP", "RP", "LSB", "RSB", "SEMI", "COL", "DCOL", 
            "COM", "CLASS", "ATTR", "BLOCK_COMMENT", "ARRAY", "INT", "FLOAT", 
            "BOOLEAN", "STRING", "NULL", "BREAK", "CONTINUE", "IF", "ELSEIF", 
            "ELSE", "FOREACH", "RETURN", "SELF", "NEW", "CONSTRUCTOR", "DESTRUCTOR", 
            "IN", "BY", "DOT", "DDOT", "OP_ADD", "OP_SUB", "OP_MUL", "OP_DIV", 
            "OP_MOD", "OP_NOT", "OP_AND", "OP_OR", "OP_LTE", "OP_GTE", "OP_NEQ", 
            "OP_AS", "OP_EQ", "OP_LT", "OP_GT", "OP_EQ_STR", "OP_ADD_STR", 
            "IDEN", "DOL_IDEN", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "ERROR_CHAR" ]

    ruleNames = [ "T__0", "T__1", "T__2", "FLOAT_LITERAL", "DEC_FORM", "INTEGER_LITERAL", 
                  "BOOLEAN_LITERAL", "STRING_LITERAL", "STR_CHAR", "ESC_SEQ", 
                  "ESC_ILLEGAL", "EXPONENT", "SIGN", "DIGIT", "LB", "RB", 
                  "LP", "RP", "LSB", "RSB", "SEMI", "COL", "DCOL", "COM", 
                  "CLASS", "ATTR", "BLOCK_COMMENT", "ARRAY", "INT", "FLOAT", 
                  "BOOLEAN", "STRING", "NULL", "BREAK", "CONTINUE", "IF", 
                  "ELSEIF", "ELSE", "FOREACH", "RETURN", "SELF", "NEW", 
                  "CONSTRUCTOR", "DESTRUCTOR", "IN", "BY", "DOT", "DDOT", 
                  "OP_ADD", "OP_SUB", "OP_MUL", "OP_DIV", "OP_MOD", "OP_NOT", 
                  "OP_AND", "OP_OR", "OP_LTE", "OP_GTE", "OP_NEQ", "OP_AS", 
                  "OP_EQ", "OP_LT", "OP_GT", "OP_EQ_STR", "OP_ADD_STR", 
                  "IDEN", "DOL_IDEN", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "ERROR_CHAR" ]

    grammarFileName = "D96.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[3] = self.FLOAT_LITERAL_action 
            actions[5] = self.INTEGER_LITERAL_action 
            actions[7] = self.STRING_LITERAL_action 
            actions[68] = self.UNCLOSE_STRING_action 
            actions[69] = self.ILLEGAL_ESCAPE_action 
            actions[70] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def FLOAT_LITERAL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            				y = str(self.text);
            				self.text = y.replace('_', '');
            			
     

    def INTEGER_LITERAL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

            				y = str(self.text);
            				self.text = y.replace('_', '');
            			
     

    def STRING_LITERAL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            					y = str(self.text)
            					self.text = y[1:len(y)-1]
            				
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            		y = str(self.text)
            		raise UncloseString(y[1:])
            	
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

            		y = str(self.text)
            		raise IllegalEscape(y[1:])
            	
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

            		raise ErrorToken(self.text);
            	
     


