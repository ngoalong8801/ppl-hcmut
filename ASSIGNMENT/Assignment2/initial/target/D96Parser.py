# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3B")
        buf.write("\u022d\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\3\2\3\2\3\2\7\2l\n\2\f\2\16\2o\13\2\3\2\3\2\7\2s\n\2")
        buf.write("\f\2\16\2v\13\2\3\2\3\2\3\2\3\2\7\2|\n\2\f\2\16\2\177")
        buf.write("\13\2\3\2\3\2\7\2\u0083\n\2\f\2\16\2\u0086\13\2\3\2\3")
        buf.write("\2\5\2\u008a\n\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3\u0092\n\3")
        buf.write("\3\4\3\4\3\4\3\4\5\4\u0098\n\4\3\5\3\5\5\5\u009c\n\5\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\5\7\u00a8\n\7\3")
        buf.write("\b\3\b\3\b\5\b\u00ad\n\b\3\b\3\b\3\t\3\t\3\t\3\t\5\t\u00b5")
        buf.write("\n\t\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u00bd\n\n\3\n\3\n\3\n")
        buf.write("\3\n\5\n\u00c3\n\n\3\13\3\13\5\13\u00c7\n\13\3\13\3\13")
        buf.write("\3\13\5\13\u00cc\n\13\3\13\3\13\5\13\u00d0\n\13\5\13\u00d2")
        buf.write("\n\13\3\f\3\f\3\r\3\r\3\r\5\r\u00d9\n\r\3\r\3\r\3\r\7")
        buf.write("\r\u00de\n\r\f\r\16\r\u00e1\13\r\3\r\3\r\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\17\3\17\3\17\5\17\u00ed\n\17\3\17\3\17\3")
        buf.write("\17\3\20\3\20\3\20\7\20\u00f5\n\20\f\20\16\20\u00f8\13")
        buf.write("\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\5\21\u0106\n\21\3\22\3\22\3\22\3\23\3\23\3")
        buf.write("\23\3\23\3\24\3\24\3\24\3\24\3\24\5\24\u0114\n\24\3\24")
        buf.write("\3\24\3\25\3\25\3\25\7\25\u011b\n\25\f\25\16\25\u011e")
        buf.write("\13\25\3\26\3\26\3\26\3\26\3\26\7\26\u0125\n\26\f\26\16")
        buf.write("\26\u0128\13\26\5\26\u012a\n\26\3\26\3\26\3\26\3\26\3")
        buf.write("\26\7\26\u0131\n\26\f\26\16\26\u0134\13\26\3\26\5\26\u0137")
        buf.write("\n\26\5\26\u0139\n\26\3\27\3\27\3\27\3\27\3\30\3\30\3")
        buf.write("\30\3\30\3\31\3\31\3\31\7\31\u0146\n\31\f\31\16\31\u0149")
        buf.write("\13\31\3\32\3\32\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3")
        buf.write("\34\3\34\3\34\3\34\3\34\3\34\7\34\u015a\n\34\f\34\16\34")
        buf.write("\u015d\13\34\3\34\3\34\5\34\u0161\n\34\3\35\3\35\5\35")
        buf.write("\u0165\n\35\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3")
        buf.write(" \3 \3 \3 \3 \3 \3 \3 \3 \5 \u0178\n \3 \3 \3 \3!\3!\3")
        buf.write("!\3\"\3\"\3\"\3\"\3\"\3\"\5\"\u0186\n\"\3\"\3\"\3\"\3")
        buf.write("\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"")
        buf.write("\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\7\"\u01a3\n\"")
        buf.write("\f\"\16\"\u01a6\13\"\3#\5#\u01a9\n#\3#\3#\3#\3#\3#\3#")
        buf.write("\3#\3#\3#\3#\3#\3#\3#\5#\u01b8\n#\3$\3$\3$\5$\u01bd\n")
        buf.write("$\3%\3%\5%\u01c1\n%\3&\3&\3&\3&\3&\7&\u01c8\n&\f&\16&")
        buf.write("\u01cb\13&\3&\5&\u01ce\n&\3&\3&\3\'\3\'\3\'\3\'\3\'\3")
        buf.write("(\3(\3(\3(\3(\3(\3(\3)\3)\3)\3)\3*\3*\3*\3*\5*\u01e6\n")
        buf.write("*\3*\3*\3+\3+\3+\3+\5+\u01ee\n+\3,\3,\3,\3,\3-\3-\3-\3")
        buf.write("-\3.\3.\3.\3.\3.\5.\u01fd\n.\3.\3.\3/\3/\3/\3/\3/\5/\u0206")
        buf.write("\n/\3/\3/\3\60\3\60\3\60\7\60\u020d\n\60\f\60\16\60\u0210")
        buf.write("\13\60\3\60\3\60\3\61\3\61\3\61\3\61\3\61\3\61\5\61\u021a")
        buf.write("\n\61\3\62\3\62\3\62\7\62\u021f\n\62\f\62\16\62\u0222")
        buf.write("\13\62\3\62\3\62\3\63\3\63\3\63\5\63\u0229\n\63\3\64\3")
        buf.write("\64\3\64\2\3B\65\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36")
        buf.write(" \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdf\2\f\4\2")
        buf.write("\4\4==\3\2=>\3\2\30\33\4\2--\61\61\3\2.\60\3\2,-\3\2\62")
        buf.write("\63\4\2\64\668:\3\2;<\3\2\6\b\2\u024e\2t\3\2\2\2\4\u008d")
        buf.write("\3\2\2\2\6\u0097\3\2\2\2\b\u009b\3\2\2\2\n\u009d\3\2\2")
        buf.write("\2\f\u00a7\3\2\2\2\16\u00a9\3\2\2\2\20\u00b0\3\2\2\2\22")
        buf.write("\u00c2\3\2\2\2\24\u00d1\3\2\2\2\26\u00d3\3\2\2\2\30\u00d5")
        buf.write("\3\2\2\2\32\u00e4\3\2\2\2\34\u00e9\3\2\2\2\36\u00f1\3")
        buf.write("\2\2\2 \u0105\3\2\2\2\"\u0107\3\2\2\2$\u010a\3\2\2\2&")
        buf.write("\u010e\3\2\2\2(\u0117\3\2\2\2*\u0138\3\2\2\2,\u013a\3")
        buf.write("\2\2\2.\u013e\3\2\2\2\60\u0142\3\2\2\2\62\u014a\3\2\2")
        buf.write("\2\64\u014c\3\2\2\2\66\u014e\3\2\2\28\u0162\3\2\2\2:\u0168")
        buf.write("\3\2\2\2<\u016b\3\2\2\2>\u016e\3\2\2\2@\u017c\3\2\2\2")
        buf.write("B\u0185\3\2\2\2D\u01b7\3\2\2\2F\u01bc\3\2\2\2H\u01c0\3")
        buf.write("\2\2\2J\u01c2\3\2\2\2L\u01d1\3\2\2\2N\u01d6\3\2\2\2P\u01dd")
        buf.write("\3\2\2\2R\u01e1\3\2\2\2T\u01ed\3\2\2\2V\u01ef\3\2\2\2")
        buf.write("X\u01f3\3\2\2\2Z\u01f7\3\2\2\2\\\u0200\3\2\2\2^\u020e")
        buf.write("\3\2\2\2`\u0219\3\2\2\2b\u0220\3\2\2\2d\u0228\3\2\2\2")
        buf.write("f\u022a\3\2\2\2hi\5\4\3\2im\7\f\2\2jl\5\6\4\2kj\3\2\2")
        buf.write("\2lo\3\2\2\2mk\3\2\2\2mn\3\2\2\2np\3\2\2\2om\3\2\2\2p")
        buf.write("q\7\r\2\2qs\3\2\2\2rh\3\2\2\2sv\3\2\2\2tr\3\2\2\2tu\3")
        buf.write("\2\2\2u\u0089\3\2\2\2vt\3\2\2\2wx\7\24\2\2xy\7\3\2\2y")
        buf.write("}\7\f\2\2z|\5\b\5\2{z\3\2\2\2|\177\3\2\2\2}{\3\2\2\2}")
        buf.write("~\3\2\2\2~\u0080\3\2\2\2\177}\3\2\2\2\u0080\u0084\5\n")
        buf.write("\6\2\u0081\u0083\5\b\5\2\u0082\u0081\3\2\2\2\u0083\u0086")
        buf.write("\3\2\2\2\u0084\u0082\3\2\2\2\u0084\u0085\3\2\2\2\u0085")
        buf.write("\u0087\3\2\2\2\u0086\u0084\3\2\2\2\u0087\u0088\7\r\2\2")
        buf.write("\u0088\u008a\3\2\2\2\u0089w\3\2\2\2\u0089\u008a\3\2\2")
        buf.write("\2\u008a\u008b\3\2\2\2\u008b\u008c\7\2\2\3\u008c\3\3\2")
        buf.write("\2\2\u008d\u008e\7\24\2\2\u008e\u0091\t\2\2\2\u008f\u0090")
        buf.write("\7\21\2\2\u0090\u0092\t\2\2\2\u0091\u008f\3\2\2\2\u0091")
        buf.write("\u0092\3\2\2\2\u0092\5\3\2\2\2\u0093\u0098\5\16\b\2\u0094")
        buf.write("\u0098\5\30\r\2\u0095\u0098\5\34\17\2\u0096\u0098\5\32")
        buf.write("\16\2\u0097\u0093\3\2\2\2\u0097\u0094\3\2\2\2\u0097\u0095")
        buf.write("\3\2\2\2\u0097\u0096\3\2\2\2\u0098\7\3\2\2\2\u0099\u009c")
        buf.write("\5\16\b\2\u009a\u009c\5\30\r\2\u009b\u0099\3\2\2\2\u009b")
        buf.write("\u009a\3\2\2\2\u009c\t\3\2\2\2\u009d\u009e\7\4\2\2\u009e")
        buf.write("\u009f\7\n\2\2\u009f\u00a0\7\13\2\2\u00a0\u00a1\5\36\20")
        buf.write("\2\u00a1\13\3\2\2\2\u00a2\u00a8\5 \21\2\u00a3\u00a8\5")
        buf.write("8\35\2\u00a4\u00a8\5\36\20\2\u00a5\u00a8\5\"\22\2\u00a6")
        buf.write("\u00a8\5\16\b\2\u00a7\u00a2\3\2\2\2\u00a7\u00a3\3\2\2")
        buf.write("\2\u00a7\u00a4\3\2\2\2\u00a7\u00a5\3\2\2\2\u00a7\u00a6")
        buf.write("\3\2\2\2\u00a8\r\3\2\2\2\u00a9\u00ac\7\25\2\2\u00aa\u00ad")
        buf.write("\5\22\n\2\u00ab\u00ad\5\20\t\2\u00ac\u00aa\3\2\2\2\u00ac")
        buf.write("\u00ab\3\2\2\2\u00ad\u00ae\3\2\2\2\u00ae\u00af\7\20\2")
        buf.write("\2\u00af\17\3\2\2\2\u00b0\u00b1\5\60\31\2\u00b1\u00b4")
        buf.write("\7\21\2\2\u00b2\u00b5\5\62\32\2\u00b3\u00b5\5N(\2\u00b4")
        buf.write("\u00b2\3\2\2\2\u00b4\u00b3\3\2\2\2\u00b5\21\3\2\2\2\u00b6")
        buf.write("\u00b7\5\26\f\2\u00b7\u00b8\7\23\2\2\u00b8\u00b9\5\22")
        buf.write("\n\2\u00b9\u00bc\7\23\2\2\u00ba\u00bd\5B\"\2\u00bb\u00bd")
        buf.write("\5H%\2\u00bc\u00ba\3\2\2\2\u00bc\u00bb\3\2\2\2\u00bd\u00c3")
        buf.write("\3\2\2\2\u00be\u00bf\5\26\f\2\u00bf\u00c0\7\21\2\2\u00c0")
        buf.write("\u00c1\5\24\13\2\u00c1\u00c3\3\2\2\2\u00c2\u00b6\3\2\2")
        buf.write("\2\u00c2\u00be\3\2\2\2\u00c3\23\3\2\2\2\u00c4\u00c7\5")
        buf.write("\62\32\2\u00c5\u00c7\5N(\2\u00c6\u00c4\3\2\2\2\u00c6\u00c5")
        buf.write("\3\2\2\2\u00c7\u00c8\3\2\2\2\u00c8\u00cb\7\67\2\2\u00c9")
        buf.write("\u00cc\5B\"\2\u00ca\u00cc\5H%\2\u00cb\u00c9\3\2\2\2\u00cb")
        buf.write("\u00ca\3\2\2\2\u00cc\u00d2\3\2\2\2\u00cd\u00d0\5\62\32")
        buf.write("\2\u00ce\u00d0\5N(\2\u00cf\u00cd\3\2\2\2\u00cf\u00ce\3")
        buf.write("\2\2\2\u00d0\u00d2\3\2\2\2\u00d1\u00c6\3\2\2\2\u00d1\u00cf")
        buf.write("\3\2\2\2\u00d2\25\3\2\2\2\u00d3\u00d4\t\3\2\2\u00d4\27")
        buf.write("\3\2\2\2\u00d5\u00d6\t\3\2\2\u00d6\u00d8\7\n\2\2\u00d7")
        buf.write("\u00d9\5(\25\2\u00d8\u00d7\3\2\2\2\u00d8\u00d9\3\2\2\2")
        buf.write("\u00d9\u00da\3\2\2\2\u00da\u00db\7\13\2\2\u00db\u00df")
        buf.write("\7\f\2\2\u00dc\u00de\5\f\7\2\u00dd\u00dc\3\2\2\2\u00de")
        buf.write("\u00e1\3\2\2\2\u00df\u00dd\3\2\2\2\u00df\u00e0\3\2\2\2")
        buf.write("\u00e0\u00e2\3\2\2\2\u00e1\u00df\3\2\2\2\u00e2\u00e3\7")
        buf.write("\r\2\2\u00e3\31\3\2\2\2\u00e4\u00e5\7\'\2\2\u00e5\u00e6")
        buf.write("\7\n\2\2\u00e6\u00e7\7\13\2\2\u00e7\u00e8\5\36\20\2\u00e8")
        buf.write("\33\3\2\2\2\u00e9\u00ea\7&\2\2\u00ea\u00ec\7\n\2\2\u00eb")
        buf.write("\u00ed\5(\25\2\u00ec\u00eb\3\2\2\2\u00ec\u00ed\3\2\2\2")
        buf.write("\u00ed\u00ee\3\2\2\2\u00ee\u00ef\7\13\2\2\u00ef\u00f0")
        buf.write("\5\36\20\2\u00f0\35\3\2\2\2\u00f1\u00f6\7\f\2\2\u00f2")
        buf.write("\u00f5\5 \21\2\u00f3\u00f5\5\36\20\2\u00f4\u00f2\3\2\2")
        buf.write("\2\u00f4\u00f3\3\2\2\2\u00f5\u00f8\3\2\2\2\u00f6\u00f4")
        buf.write("\3\2\2\2\u00f6\u00f7\3\2\2\2\u00f7\u00f9\3\2\2\2\u00f8")
        buf.write("\u00f6\3\2\2\2\u00f9\u00fa\7\r\2\2\u00fa\37\3\2\2\2\u00fb")
        buf.write("\u0106\5\"\22\2\u00fc\u0106\5\66\34\2\u00fd\u0106\5\16")
        buf.write("\b\2\u00fe\u0106\5:\36\2\u00ff\u0106\5<\37\2\u0100\u0106")
        buf.write("\5> \2\u0101\u0106\58\35\2\u0102\u0103\5T+\2\u0103\u0104")
        buf.write("\7\20\2\2\u0104\u0106\3\2\2\2\u0105\u00fb\3\2\2\2\u0105")
        buf.write("\u00fc\3\2\2\2\u0105\u00fd\3\2\2\2\u0105\u00fe\3\2\2\2")
        buf.write("\u0105\u00ff\3\2\2\2\u0105\u0100\3\2\2\2\u0105\u0101\3")
        buf.write("\2\2\2\u0105\u0102\3\2\2\2\u0106!\3\2\2\2\u0107\u0108")
        buf.write("\5$\23\2\u0108\u0109\7\20\2\2\u0109#\3\2\2\2\u010a\u010b")
        buf.write("\5B\"\2\u010b\u010c\7\67\2\2\u010c\u010d\5B\"\2\u010d")
        buf.write("%\3\2\2\2\u010e\u010f\7=\2\2\u010f\u0110\7\22\2\2\u0110")
        buf.write("\u0111\7>\2\2\u0111\u0113\7\n\2\2\u0112\u0114\5^\60\2")
        buf.write("\u0113\u0112\3\2\2\2\u0113\u0114\3\2\2\2\u0114\u0115\3")
        buf.write("\2\2\2\u0115\u0116\7\13\2\2\u0116\'\3\2\2\2\u0117\u011c")
        buf.write("\5*\26\2\u0118\u0119\7\20\2\2\u0119\u011b\5*\26\2\u011a")
        buf.write("\u0118\3\2\2\2\u011b\u011e\3\2\2\2\u011c\u011a\3\2\2\2")
        buf.write("\u011c\u011d\3\2\2\2\u011d)\3\2\2\2\u011e\u011c\3\2\2")
        buf.write("\2\u011f\u0129\5,\27\2\u0120\u0121\7\67\2\2\u0121\u0126")
        buf.write("\5B\"\2\u0122\u0123\7\23\2\2\u0123\u0125\5B\"\2\u0124")
        buf.write("\u0122\3\2\2\2\u0125\u0128\3\2\2\2\u0126\u0124\3\2\2\2")
        buf.write("\u0126\u0127\3\2\2\2\u0127\u012a\3\2\2\2\u0128\u0126\3")
        buf.write("\2\2\2\u0129\u0120\3\2\2\2\u0129\u012a\3\2\2\2\u012a\u0139")
        buf.write("\3\2\2\2\u012b\u0136\5.\30\2\u012c\u0132\7\67\2\2\u012d")
        buf.write("\u012e\5H%\2\u012e\u012f\7\23\2\2\u012f\u0131\3\2\2\2")
        buf.write("\u0130\u012d\3\2\2\2\u0131\u0134\3\2\2\2\u0132\u0130\3")
        buf.write("\2\2\2\u0132\u0133\3\2\2\2\u0133\u0135\3\2\2\2\u0134\u0132")
        buf.write("\3\2\2\2\u0135\u0137\5H%\2\u0136\u012c\3\2\2\2\u0136\u0137")
        buf.write("\3\2\2\2\u0137\u0139\3\2\2\2\u0138\u011f\3\2\2\2\u0138")
        buf.write("\u012b\3\2\2\2\u0139+\3\2\2\2\u013a\u013b\5\60\31\2\u013b")
        buf.write("\u013c\7\21\2\2\u013c\u013d\5\62\32\2\u013d-\3\2\2\2\u013e")
        buf.write("\u013f\5\60\31\2\u013f\u0140\7\21\2\2\u0140\u0141\5N(")
        buf.write("\2\u0141/\3\2\2\2\u0142\u0147\t\3\2\2\u0143\u0144\7\23")
        buf.write("\2\2\u0144\u0146\t\3\2\2\u0145\u0143\3\2\2\2\u0146\u0149")
        buf.write("\3\2\2\2\u0147\u0145\3\2\2\2\u0147\u0148\3\2\2\2\u0148")
        buf.write("\61\3\2\2\2\u0149\u0147\3\2\2\2\u014a\u014b\5\64\33\2")
        buf.write("\u014b\63\3\2\2\2\u014c\u014d\t\4\2\2\u014d\65\3\2\2\2")
        buf.write("\u014e\u014f\7\37\2\2\u014f\u0150\7\n\2\2\u0150\u0151")
        buf.write("\5B\"\2\u0151\u0152\7\13\2\2\u0152\u015b\5\36\20\2\u0153")
        buf.write("\u0154\7 \2\2\u0154\u0155\7\n\2\2\u0155\u0156\5B\"\2\u0156")
        buf.write("\u0157\7\13\2\2\u0157\u0158\5\36\20\2\u0158\u015a\3\2")
        buf.write("\2\2\u0159\u0153\3\2\2\2\u015a\u015d\3\2\2\2\u015b\u0159")
        buf.write("\3\2\2\2\u015b\u015c\3\2\2\2\u015c\u0160\3\2\2\2\u015d")
        buf.write("\u015b\3\2\2\2\u015e\u015f\7!\2\2\u015f\u0161\5\36\20")
        buf.write("\2\u0160\u015e\3\2\2\2\u0160\u0161\3\2\2\2\u0161\67\3")
        buf.write("\2\2\2\u0162\u0164\7#\2\2\u0163\u0165\5B\"\2\u0164\u0163")
        buf.write("\3\2\2\2\u0164\u0165\3\2\2\2\u0165\u0166\3\2\2\2\u0166")
        buf.write("\u0167\7\20\2\2\u01679\3\2\2\2\u0168\u0169\7\35\2\2\u0169")
        buf.write("\u016a\7\20\2\2\u016a;\3\2\2\2\u016b\u016c\7\36\2\2\u016c")
        buf.write("\u016d\7\20\2\2\u016d=\3\2\2\2\u016e\u016f\7\"\2\2\u016f")
        buf.write("\u0170\7\n\2\2\u0170\u0171\7=\2\2\u0171\u0172\7(\2\2\u0172")
        buf.write("\u0173\7\7\2\2\u0173\u0174\7+\2\2\u0174\u0177\7\7\2\2")
        buf.write("\u0175\u0176\7)\2\2\u0176\u0178\7\7\2\2\u0177\u0175\3")
        buf.write("\2\2\2\u0177\u0178\3\2\2\2\u0178\u0179\3\2\2\2\u0179\u017a")
        buf.write("\7\13\2\2\u017a\u017b\5\36\20\2\u017b?\3\2\2\2\u017c\u017d")
        buf.write("\5B\"\2\u017d\u017e\7\20\2\2\u017eA\3\2\2\2\u017f\u0180")
        buf.write("\b\"\1\2\u0180\u0186\5D#\2\u0181\u0182\7%\2\2\u0182\u0186")
        buf.write("\5B\"\f\u0183\u0184\t\5\2\2\u0184\u0186\5B\"\b\u0185\u017f")
        buf.write("\3\2\2\2\u0185\u0181\3\2\2\2\u0185\u0183\3\2\2\2\u0186")
        buf.write("\u01a4\3\2\2\2\u0187\u0188\f\13\2\2\u0188\u0189\7\22\2")
        buf.write("\2\u0189\u018a\7\5\2\2\u018a\u01a3\5B\"\f\u018b\u018c")
        buf.write("\f\n\2\2\u018c\u018d\7*\2\2\u018d\u01a3\5B\"\13\u018e")
        buf.write("\u018f\f\7\2\2\u018f\u0190\t\6\2\2\u0190\u01a3\5B\"\b")
        buf.write("\u0191\u0192\f\6\2\2\u0192\u0193\t\7\2\2\u0193\u01a3\5")
        buf.write("B\"\7\u0194\u0195\f\5\2\2\u0195\u0196\t\b\2\2\u0196\u01a3")
        buf.write("\5B\"\6\u0197\u0198\f\4\2\2\u0198\u0199\t\t\2\2\u0199")
        buf.write("\u01a3\5B\"\5\u019a\u019b\f\3\2\2\u019b\u019c\t\n\2\2")
        buf.write("\u019c\u01a3\5B\"\4\u019d\u019e\f\t\2\2\u019e\u019f\7")
        buf.write("\16\2\2\u019f\u01a0\5B\"\2\u01a0\u01a1\7\17\2\2\u01a1")
        buf.write("\u01a3\3\2\2\2\u01a2\u0187\3\2\2\2\u01a2\u018b\3\2\2\2")
        buf.write("\u01a2\u018e\3\2\2\2\u01a2\u0191\3\2\2\2\u01a2\u0194\3")
        buf.write("\2\2\2\u01a2\u0197\3\2\2\2\u01a2\u019a\3\2\2\2\u01a2\u019d")
        buf.write("\3\2\2\2\u01a3\u01a6\3\2\2\2\u01a4\u01a2\3\2\2\2\u01a4")
        buf.write("\u01a5\3\2\2\2\u01a5C\3\2\2\2\u01a6\u01a4\3\2\2\2\u01a7")
        buf.write("\u01a9\7=\2\2\u01a8\u01a7\3\2\2\2\u01a8\u01a9\3\2\2\2")
        buf.write("\u01a9\u01aa\3\2\2\2\u01aa\u01ab\7\n\2\2\u01ab\u01ac\5")
        buf.write("B\"\2\u01ac\u01ad\7\13\2\2\u01ad\u01b8\3\2\2\2\u01ae\u01b8")
        buf.write("\5d\63\2\u01af\u01b8\7=\2\2\u01b0\u01b8\5P)\2\u01b1\u01b8")
        buf.write("\5F$\2\u01b2\u01b8\5&\24\2\u01b3\u01b8\5T+\2\u01b4\u01b8")
        buf.write("\5R*\2\u01b5\u01b6\7\25\2\2\u01b6\u01b8\5,\27\2\u01b7")
        buf.write("\u01a8\3\2\2\2\u01b7\u01ae\3\2\2\2\u01b7\u01af\3\2\2\2")
        buf.write("\u01b7\u01b0\3\2\2\2\u01b7\u01b1\3\2\2\2\u01b7\u01b2\3")
        buf.write("\2\2\2\u01b7\u01b3\3\2\2\2\u01b7\u01b4\3\2\2\2\u01b7\u01b5")
        buf.write("\3\2\2\2\u01b8E\3\2\2\2\u01b9\u01bd\5J&\2\u01ba\u01bd")
        buf.write("\5L\'\2\u01bb\u01bd\5N(\2\u01bc\u01b9\3\2\2\2\u01bc\u01ba")
        buf.write("\3\2\2\2\u01bc\u01bb\3\2\2\2\u01bdG\3\2\2\2\u01be\u01c1")
        buf.write("\5J&\2\u01bf\u01c1\5L\'\2\u01c0\u01be\3\2\2\2\u01c0\u01bf")
        buf.write("\3\2\2\2\u01c1I\3\2\2\2\u01c2\u01c3\7\27\2\2\u01c3\u01c9")
        buf.write("\7\n\2\2\u01c4\u01c5\5L\'\2\u01c5\u01c6\7\23\2\2\u01c6")
        buf.write("\u01c8\3\2\2\2\u01c7\u01c4\3\2\2\2\u01c8\u01cb\3\2\2\2")
        buf.write("\u01c9\u01c7\3\2\2\2\u01c9\u01ca\3\2\2\2\u01ca\u01cd\3")
        buf.write("\2\2\2\u01cb\u01c9\3\2\2\2\u01cc\u01ce\5L\'\2\u01cd\u01cc")
        buf.write("\3\2\2\2\u01cd\u01ce\3\2\2\2\u01ce\u01cf\3\2\2\2\u01cf")
        buf.write("\u01d0\7\13\2\2\u01d0K\3\2\2\2\u01d1\u01d2\7\27\2\2\u01d2")
        buf.write("\u01d3\7\n\2\2\u01d3\u01d4\5b\62\2\u01d4\u01d5\7\13\2")
        buf.write("\2\u01d5M\3\2\2\2\u01d6\u01d7\7\27\2\2\u01d7\u01d8\7\16")
        buf.write("\2\2\u01d8\u01d9\5\64\33\2\u01d9\u01da\7\23\2\2\u01da")
        buf.write("\u01db\5d\63\2\u01db\u01dc\7\17\2\2\u01dcO\3\2\2\2\u01dd")
        buf.write("\u01de\7$\2\2\u01de\u01df\7*\2\2\u01df\u01e0\7=\2\2\u01e0")
        buf.write("Q\3\2\2\2\u01e1\u01e2\7%\2\2\u01e2\u01e3\7=\2\2\u01e3")
        buf.write("\u01e5\7\n\2\2\u01e4\u01e6\5b\62\2\u01e5\u01e4\3\2\2\2")
        buf.write("\u01e5\u01e6\3\2\2\2\u01e6\u01e7\3\2\2\2\u01e7\u01e8\7")
        buf.write("\13\2\2\u01e8S\3\2\2\2\u01e9\u01ee\5V,\2\u01ea\u01ee\5")
        buf.write("X-\2\u01eb\u01ee\5Z.\2\u01ec\u01ee\5\\/\2\u01ed\u01e9")
        buf.write("\3\2\2\2\u01ed\u01ea\3\2\2\2\u01ed\u01eb\3\2\2\2\u01ed")
        buf.write("\u01ec\3\2\2\2\u01eeU\3\2\2\2\u01ef\u01f0\7=\2\2\u01f0")
        buf.write("\u01f1\7*\2\2\u01f1\u01f2\7=\2\2\u01f2W\3\2\2\2\u01f3")
        buf.write("\u01f4\7=\2\2\u01f4\u01f5\7\22\2\2\u01f5\u01f6\7>\2\2")
        buf.write("\u01f6Y\3\2\2\2\u01f7\u01f8\7=\2\2\u01f8\u01f9\7*\2\2")
        buf.write("\u01f9\u01fa\7=\2\2\u01fa\u01fc\7\n\2\2\u01fb\u01fd\5")
        buf.write("^\60\2\u01fc\u01fb\3\2\2\2\u01fc\u01fd\3\2\2\2\u01fd\u01fe")
        buf.write("\3\2\2\2\u01fe\u01ff\7\13\2\2\u01ff[\3\2\2\2\u0200\u0201")
        buf.write("\7=\2\2\u0201\u0202\7\22\2\2\u0202\u0203\7>\2\2\u0203")
        buf.write("\u0205\7\n\2\2\u0204\u0206\5^\60\2\u0205\u0204\3\2\2\2")
        buf.write("\u0205\u0206\3\2\2\2\u0206\u0207\3\2\2\2\u0207\u0208\7")
        buf.write("\13\2\2\u0208]\3\2\2\2\u0209\u020a\5`\61\2\u020a\u020b")
        buf.write("\7\23\2\2\u020b\u020d\3\2\2\2\u020c\u0209\3\2\2\2\u020d")
        buf.write("\u0210\3\2\2\2\u020e\u020c\3\2\2\2\u020e\u020f\3\2\2\2")
        buf.write("\u020f\u0211\3\2\2\2\u0210\u020e\3\2\2\2\u0211\u0212\5")
        buf.write("`\61\2\u0212_\3\2\2\2\u0213\u021a\5B\"\2\u0214\u021a\5")
        buf.write("d\63\2\u0215\u021a\5X-\2\u0216\u021a\5Z.\2\u0217\u021a")
        buf.write("\5\\/\2\u0218\u021a\5V,\2\u0219\u0213\3\2\2\2\u0219\u0214")
        buf.write("\3\2\2\2\u0219\u0215\3\2\2\2\u0219\u0216\3\2\2\2\u0219")
        buf.write("\u0217\3\2\2\2\u0219\u0218\3\2\2\2\u021aa\3\2\2\2\u021b")
        buf.write("\u021c\5d\63\2\u021c\u021d\7\23\2\2\u021d\u021f\3\2\2")
        buf.write("\2\u021e\u021b\3\2\2\2\u021f\u0222\3\2\2\2\u0220\u021e")
        buf.write("\3\2\2\2\u0220\u0221\3\2\2\2\u0221\u0223\3\2\2\2\u0222")
        buf.write("\u0220\3\2\2\2\u0223\u0224\5d\63\2\u0224c\3\2\2\2\u0225")
        buf.write("\u0229\5f\64\2\u0226\u0229\7\t\2\2\u0227\u0229\7=\2\2")
        buf.write("\u0228\u0225\3\2\2\2\u0228\u0226\3\2\2\2\u0228\u0227\3")
        buf.write("\2\2\2\u0229e\3\2\2\2\u022a\u022b\t\13\2\2\u022bg\3\2")
        buf.write("\2\2\66mt}\u0084\u0089\u0091\u0097\u009b\u00a7\u00ac\u00b4")
        buf.write("\u00bc\u00c2\u00c6\u00cb\u00cf\u00d1\u00d8\u00df\u00ec")
        buf.write("\u00f4\u00f6\u0105\u0113\u011c\u0126\u0129\u0132\u0136")
        buf.write("\u0138\u0147\u015b\u0160\u0164\u0177\u0185\u01a2\u01a4")
        buf.write("\u01a8\u01b7\u01bc\u01c0\u01c9\u01cd\u01e5\u01ed\u01fc")
        buf.write("\u0205\u020e\u0219\u0220\u0228")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Program'", "'main'", "'$'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'('", "')'", 
                     "'{'", "'}'", "'['", "']'", "';'", "':'", "'::'", "','", 
                     "'Class'", "<INVALID>", "<INVALID>", "'Array'", "'Int'", 
                     "'Float'", "'Boolean'", "'String'", "'Null'", "'Break'", 
                     "'Continue'", "'If'", "'Elseif'", "'Else'", "'Foreach'", 
                     "'Return'", "'self'", "'New'", "'Constructor'", "'Destructor'", 
                     "'In'", "'By'", "'.'", "'..'", "'+'", "'-'", "'*'", 
                     "'/'", "'%'", "'!'", "'&&'", "'||'", "'<='", "'>='", 
                     "'!='", "'='", "'=='", "'<'", "'>'", "'==.'", "'+.'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "FLOAT_LITERAL", "INTEGER_LITERAL", "BOOLEAN_LITERAL", 
                      "STRING_LITERAL", "LB", "RB", "LP", "RP", "LSB", "RSB", 
                      "SEMI", "COL", "DCOL", "COM", "CLASS", "ATTR", "BLOCK_COMMENT", 
                      "ARRAY", "INT", "FLOAT", "BOOLEAN", "STRING", "NULL", 
                      "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", "FOREACH", 
                      "RETURN", "SELF", "NEW", "CONSTRUCTOR", "DESTRUCTOR", 
                      "IN", "BY", "DOT", "DDOT", "OP_ADD", "OP_SUB", "OP_MUL", 
                      "OP_DIV", "OP_MOD", "OP_NOT", "OP_AND", "OP_OR", "OP_LTE", 
                      "OP_GTE", "OP_NEQ", "OP_AS", "OP_EQ", "OP_LT", "OP_GT", 
                      "OP_EQ_STR", "OP_ADD_STR", "IDEN", "DOL_IDEN", "WS", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_class_decl = 1
    RULE_body_class = 2
    RULE_body_class_main = 3
    RULE_main_func = 4
    RULE_stmt = 5
    RULE_att_decl = 6
    RULE_para_list_nor = 7
    RULE_para_list_eq = 8
    RULE_rest_para = 9
    RULE_para = 10
    RULE_func_decl = 11
    RULE_destr_decl = 12
    RULE_constr_decl = 13
    RULE_block_stmt = 14
    RULE_block_items = 15
    RULE_assign_stmt = 16
    RULE_assign_lhs = 17
    RULE_method_invo_stmt = 18
    RULE_params_list_can = 19
    RULE_params_list = 20
    RULE_ids_list_with_type = 21
    RULE_ids_list_with_arr = 22
    RULE_ids_list = 23
    RULE_data_types = 24
    RULE_element_types = 25
    RULE_if_stmt = 26
    RULE_return_stmt = 27
    RULE_break_stmt = 28
    RULE_continue_stmt = 29
    RULE_forin_stmt = 30
    RULE_expr_stmt = 31
    RULE_expr = 32
    RULE_atom = 33
    RULE_array_declare = 34
    RULE_array = 35
    RULE_muldi_arr = 36
    RULE_indx_arr = 37
    RULE_arr_type = 38
    RULE_self_type = 39
    RULE_class_type = 40
    RULE_member_acc = 41
    RULE_inst_attr_acc = 42
    RULE_stat_attr_acc = 43
    RULE_inst_meth_invo = 44
    RULE_stat_meth_invo = 45
    RULE_list_expr_method = 46
    RULE_elem_expr_method = 47
    RULE_list_literal = 48
    RULE_literal = 49
    RULE_number_literal = 50

    ruleNames =  [ "program", "class_decl", "body_class", "body_class_main", 
                   "main_func", "stmt", "att_decl", "para_list_nor", "para_list_eq", 
                   "rest_para", "para", "func_decl", "destr_decl", "constr_decl", 
                   "block_stmt", "block_items", "assign_stmt", "assign_lhs", 
                   "method_invo_stmt", "params_list_can", "params_list", 
                   "ids_list_with_type", "ids_list_with_arr", "ids_list", 
                   "data_types", "element_types", "if_stmt", "return_stmt", 
                   "break_stmt", "continue_stmt", "forin_stmt", "expr_stmt", 
                   "expr", "atom", "array_declare", "array", "muldi_arr", 
                   "indx_arr", "arr_type", "self_type", "class_type", "member_acc", 
                   "inst_attr_acc", "stat_attr_acc", "inst_meth_invo", "stat_meth_invo", 
                   "list_expr_method", "elem_expr_method", "list_literal", 
                   "literal", "number_literal" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    FLOAT_LITERAL=4
    INTEGER_LITERAL=5
    BOOLEAN_LITERAL=6
    STRING_LITERAL=7
    LB=8
    RB=9
    LP=10
    RP=11
    LSB=12
    RSB=13
    SEMI=14
    COL=15
    DCOL=16
    COM=17
    CLASS=18
    ATTR=19
    BLOCK_COMMENT=20
    ARRAY=21
    INT=22
    FLOAT=23
    BOOLEAN=24
    STRING=25
    NULL=26
    BREAK=27
    CONTINUE=28
    IF=29
    ELSEIF=30
    ELSE=31
    FOREACH=32
    RETURN=33
    SELF=34
    NEW=35
    CONSTRUCTOR=36
    DESTRUCTOR=37
    IN=38
    BY=39
    DOT=40
    DDOT=41
    OP_ADD=42
    OP_SUB=43
    OP_MUL=44
    OP_DIV=45
    OP_MOD=46
    OP_NOT=47
    OP_AND=48
    OP_OR=49
    OP_LTE=50
    OP_GTE=51
    OP_NEQ=52
    OP_AS=53
    OP_EQ=54
    OP_LT=55
    OP_GT=56
    OP_EQ_STR=57
    OP_ADD_STR=58
    IDEN=59
    DOL_IDEN=60
    WS=61
    UNCLOSE_STRING=62
    ILLEGAL_ESCAPE=63
    ERROR_CHAR=64

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(D96Parser.EOF, 0)

        def class_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Class_declContext)
            else:
                return self.getTypedRuleContext(D96Parser.Class_declContext,i)


        def LP(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.LP)
            else:
                return self.getToken(D96Parser.LP, i)

        def RP(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.RP)
            else:
                return self.getToken(D96Parser.RP, i)

        def CLASS(self):
            return self.getToken(D96Parser.CLASS, 0)

        def main_func(self):
            return self.getTypedRuleContext(D96Parser.Main_funcContext,0)


        def body_class(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Body_classContext)
            else:
                return self.getTypedRuleContext(D96Parser.Body_classContext,i)


        def body_class_main(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Body_class_mainContext)
            else:
                return self.getTypedRuleContext(D96Parser.Body_class_mainContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = D96Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 102
                    self.class_decl()
                    self.state = 103
                    self.match(D96Parser.LP)
                    self.state = 107
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.ATTR) | (1 << D96Parser.CONSTRUCTOR) | (1 << D96Parser.DESTRUCTOR) | (1 << D96Parser.IDEN) | (1 << D96Parser.DOL_IDEN))) != 0):
                        self.state = 104
                        self.body_class()
                        self.state = 109
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 110
                    self.match(D96Parser.RP) 
                self.state = 116
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.CLASS:
                self.state = 117
                self.match(D96Parser.CLASS)
                self.state = 118
                self.match(D96Parser.T__0)
                self.state = 119
                self.match(D96Parser.LP)
                self.state = 123
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.ATTR) | (1 << D96Parser.IDEN) | (1 << D96Parser.DOL_IDEN))) != 0):
                    self.state = 120
                    self.body_class_main()
                    self.state = 125
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 126
                self.main_func()
                self.state = 130
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.ATTR) | (1 << D96Parser.IDEN) | (1 << D96Parser.DOL_IDEN))) != 0):
                    self.state = 127
                    self.body_class_main()
                    self.state = 132
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 133
                self.match(D96Parser.RP)


            self.state = 137
            self.match(D96Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(D96Parser.CLASS, 0)

        def IDEN(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.IDEN)
            else:
                return self.getToken(D96Parser.IDEN, i)

        def COL(self):
            return self.getToken(D96Parser.COL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_class_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_decl" ):
                return visitor.visitClass_decl(self)
            else:
                return visitor.visitChildren(self)




    def class_decl(self):

        localctx = D96Parser.Class_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_class_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.match(D96Parser.CLASS)
            self.state = 140
            _la = self._input.LA(1)
            if not(_la==D96Parser.T__1 or _la==D96Parser.IDEN):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 143
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.COL:
                self.state = 141
                self.match(D96Parser.COL)
                self.state = 142
                _la = self._input.LA(1)
                if not(_la==D96Parser.T__1 or _la==D96Parser.IDEN):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Body_classContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def att_decl(self):
            return self.getTypedRuleContext(D96Parser.Att_declContext,0)


        def func_decl(self):
            return self.getTypedRuleContext(D96Parser.Func_declContext,0)


        def constr_decl(self):
            return self.getTypedRuleContext(D96Parser.Constr_declContext,0)


        def destr_decl(self):
            return self.getTypedRuleContext(D96Parser.Destr_declContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_body_class

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody_class" ):
                return visitor.visitBody_class(self)
            else:
                return visitor.visitChildren(self)




    def body_class(self):

        localctx = D96Parser.Body_classContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_body_class)
        try:
            self.state = 149
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ATTR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 145
                self.att_decl()
                pass
            elif token in [D96Parser.IDEN, D96Parser.DOL_IDEN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 146
                self.func_decl()
                pass
            elif token in [D96Parser.CONSTRUCTOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 147
                self.constr_decl()
                pass
            elif token in [D96Parser.DESTRUCTOR]:
                self.enterOuterAlt(localctx, 4)
                self.state = 148
                self.destr_decl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Body_class_mainContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def att_decl(self):
            return self.getTypedRuleContext(D96Parser.Att_declContext,0)


        def func_decl(self):
            return self.getTypedRuleContext(D96Parser.Func_declContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_body_class_main

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody_class_main" ):
                return visitor.visitBody_class_main(self)
            else:
                return visitor.visitChildren(self)




    def body_class_main(self):

        localctx = D96Parser.Body_class_mainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_body_class_main)
        try:
            self.state = 153
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ATTR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 151
                self.att_decl()
                pass
            elif token in [D96Parser.IDEN, D96Parser.DOL_IDEN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 152
                self.func_decl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Main_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_main_func

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMain_func" ):
                return visitor.visitMain_func(self)
            else:
                return visitor.visitChildren(self)




    def main_func(self):

        localctx = D96Parser.Main_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_main_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.match(D96Parser.T__1)
            self.state = 156
            self.match(D96Parser.LB)
            self.state = 157
            self.match(D96Parser.RB)
            self.state = 158
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block_items(self):
            return self.getTypedRuleContext(D96Parser.Block_itemsContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(D96Parser.Return_stmtContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def assign_stmt(self):
            return self.getTypedRuleContext(D96Parser.Assign_stmtContext,0)


        def att_decl(self):
            return self.getTypedRuleContext(D96Parser.Att_declContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = D96Parser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_stmt)
        try:
            self.state = 165
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 160
                self.block_items()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 161
                self.return_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 162
                self.block_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 163
                self.assign_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 164
                self.att_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Att_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ATTR(self):
            return self.getToken(D96Parser.ATTR, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def para_list_eq(self):
            return self.getTypedRuleContext(D96Parser.Para_list_eqContext,0)


        def para_list_nor(self):
            return self.getTypedRuleContext(D96Parser.Para_list_norContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_att_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtt_decl" ):
                return visitor.visitAtt_decl(self)
            else:
                return visitor.visitChildren(self)




    def att_decl(self):

        localctx = D96Parser.Att_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_att_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.match(D96Parser.ATTR)
            self.state = 170
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 168
                self.para_list_eq()
                pass

            elif la_ == 2:
                self.state = 169
                self.para_list_nor()
                pass


            self.state = 172
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Para_list_norContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ids_list(self):
            return self.getTypedRuleContext(D96Parser.Ids_listContext,0)


        def COL(self):
            return self.getToken(D96Parser.COL, 0)

        def data_types(self):
            return self.getTypedRuleContext(D96Parser.Data_typesContext,0)


        def arr_type(self):
            return self.getTypedRuleContext(D96Parser.Arr_typeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_para_list_nor

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPara_list_nor" ):
                return visitor.visitPara_list_nor(self)
            else:
                return visitor.visitChildren(self)




    def para_list_nor(self):

        localctx = D96Parser.Para_list_norContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_para_list_nor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.ids_list()
            self.state = 175
            self.match(D96Parser.COL)
            self.state = 178
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT, D96Parser.FLOAT, D96Parser.BOOLEAN, D96Parser.STRING]:
                self.state = 176
                self.data_types()
                pass
            elif token in [D96Parser.ARRAY]:
                self.state = 177
                self.arr_type()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Para_list_eqContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def para(self):
            return self.getTypedRuleContext(D96Parser.ParaContext,0)


        def COM(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COM)
            else:
                return self.getToken(D96Parser.COM, i)

        def para_list_eq(self):
            return self.getTypedRuleContext(D96Parser.Para_list_eqContext,0)


        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def array(self):
            return self.getTypedRuleContext(D96Parser.ArrayContext,0)


        def COL(self):
            return self.getToken(D96Parser.COL, 0)

        def rest_para(self):
            return self.getTypedRuleContext(D96Parser.Rest_paraContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_para_list_eq

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPara_list_eq" ):
                return visitor.visitPara_list_eq(self)
            else:
                return visitor.visitChildren(self)




    def para_list_eq(self):

        localctx = D96Parser.Para_list_eqContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_para_list_eq)
        try:
            self.state = 192
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 180
                self.para()
                self.state = 181
                self.match(D96Parser.COM)

                self.state = 182
                self.para_list_eq()
                self.state = 183
                self.match(D96Parser.COM)
                self.state = 186
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                if la_ == 1:
                    self.state = 184
                    self.expr(0)
                    pass

                elif la_ == 2:
                    self.state = 185
                    self.array()
                    pass


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 188
                self.para()
                self.state = 189
                self.match(D96Parser.COL)
                self.state = 190
                self.rest_para()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Rest_paraContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_AS(self):
            return self.getToken(D96Parser.OP_AS, 0)

        def data_types(self):
            return self.getTypedRuleContext(D96Parser.Data_typesContext,0)


        def arr_type(self):
            return self.getTypedRuleContext(D96Parser.Arr_typeContext,0)


        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def array(self):
            return self.getTypedRuleContext(D96Parser.ArrayContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_rest_para

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRest_para" ):
                return visitor.visitRest_para(self)
            else:
                return visitor.visitChildren(self)




    def rest_para(self):

        localctx = D96Parser.Rest_paraContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_rest_para)
        try:
            self.state = 207
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 196
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.INT, D96Parser.FLOAT, D96Parser.BOOLEAN, D96Parser.STRING]:
                    self.state = 194
                    self.data_types()
                    pass
                elif token in [D96Parser.ARRAY]:
                    self.state = 195
                    self.arr_type()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 198
                self.match(D96Parser.OP_AS)
                self.state = 201
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                if la_ == 1:
                    self.state = 199
                    self.expr(0)
                    pass

                elif la_ == 2:
                    self.state = 200
                    self.array()
                    pass


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 205
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.INT, D96Parser.FLOAT, D96Parser.BOOLEAN, D96Parser.STRING]:
                    self.state = 203
                    self.data_types()
                    pass
                elif token in [D96Parser.ARRAY]:
                    self.state = 204
                    self.arr_type()
                    pass
                else:
                    raise NoViableAltException(self)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDEN(self):
            return self.getToken(D96Parser.IDEN, 0)

        def DOL_IDEN(self):
            return self.getToken(D96Parser.DOL_IDEN, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_para

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPara" ):
                return visitor.visitPara(self)
            else:
                return visitor.visitChildren(self)




    def para(self):

        localctx = D96Parser.ParaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_para)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            _la = self._input.LA(1)
            if not(_la==D96Parser.IDEN or _la==D96Parser.DOL_IDEN):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def IDEN(self):
            return self.getToken(D96Parser.IDEN, 0)

        def DOL_IDEN(self):
            return self.getToken(D96Parser.DOL_IDEN, 0)

        def params_list_can(self):
            return self.getTypedRuleContext(D96Parser.Params_list_canContext,0)


        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.StmtContext)
            else:
                return self.getTypedRuleContext(D96Parser.StmtContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_func_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_decl" ):
                return visitor.visitFunc_decl(self)
            else:
                return visitor.visitChildren(self)




    def func_decl(self):

        localctx = D96Parser.Func_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_func_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            _la = self._input.LA(1)
            if not(_la==D96Parser.IDEN or _la==D96Parser.DOL_IDEN):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 212
            self.match(D96Parser.LB)
            self.state = 214
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.IDEN or _la==D96Parser.DOL_IDEN:
                self.state = 213
                self.params_list_can()


            self.state = 216
            self.match(D96Parser.RB)
            self.state = 217
            self.match(D96Parser.LP)
            self.state = 221
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.LB) | (1 << D96Parser.LP) | (1 << D96Parser.ATTR) | (1 << D96Parser.ARRAY) | (1 << D96Parser.BREAK) | (1 << D96Parser.CONTINUE) | (1 << D96Parser.IF) | (1 << D96Parser.FOREACH) | (1 << D96Parser.RETURN) | (1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.OP_SUB) | (1 << D96Parser.OP_NOT) | (1 << D96Parser.IDEN))) != 0):
                self.state = 218
                self.stmt()
                self.state = 223
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 224
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Destr_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DESTRUCTOR(self):
            return self.getToken(D96Parser.DESTRUCTOR, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_destr_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDestr_decl" ):
                return visitor.visitDestr_decl(self)
            else:
                return visitor.visitChildren(self)




    def destr_decl(self):

        localctx = D96Parser.Destr_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_destr_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self.match(D96Parser.DESTRUCTOR)
            self.state = 227
            self.match(D96Parser.LB)
            self.state = 228
            self.match(D96Parser.RB)
            self.state = 229
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Constr_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONSTRUCTOR(self):
            return self.getToken(D96Parser.CONSTRUCTOR, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def params_list_can(self):
            return self.getTypedRuleContext(D96Parser.Params_list_canContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_constr_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstr_decl" ):
                return visitor.visitConstr_decl(self)
            else:
                return visitor.visitChildren(self)




    def constr_decl(self):

        localctx = D96Parser.Constr_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_constr_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self.match(D96Parser.CONSTRUCTOR)
            self.state = 232
            self.match(D96Parser.LB)
            self.state = 234
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.IDEN or _la==D96Parser.DOL_IDEN:
                self.state = 233
                self.params_list_can()


            self.state = 236
            self.match(D96Parser.RB)
            self.state = 237
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def block_items(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Block_itemsContext)
            else:
                return self.getTypedRuleContext(D96Parser.Block_itemsContext,i)


        def block_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Block_stmtContext)
            else:
                return self.getTypedRuleContext(D96Parser.Block_stmtContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_block_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_stmt" ):
                return visitor.visitBlock_stmt(self)
            else:
                return visitor.visitChildren(self)




    def block_stmt(self):

        localctx = D96Parser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_block_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.match(D96Parser.LP)
            self.state = 244
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.LB) | (1 << D96Parser.LP) | (1 << D96Parser.ATTR) | (1 << D96Parser.ARRAY) | (1 << D96Parser.BREAK) | (1 << D96Parser.CONTINUE) | (1 << D96Parser.IF) | (1 << D96Parser.FOREACH) | (1 << D96Parser.RETURN) | (1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.OP_SUB) | (1 << D96Parser.OP_NOT) | (1 << D96Parser.IDEN))) != 0):
                self.state = 242
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.FLOAT_LITERAL, D96Parser.INTEGER_LITERAL, D96Parser.BOOLEAN_LITERAL, D96Parser.STRING_LITERAL, D96Parser.LB, D96Parser.ATTR, D96Parser.ARRAY, D96Parser.BREAK, D96Parser.CONTINUE, D96Parser.IF, D96Parser.FOREACH, D96Parser.RETURN, D96Parser.SELF, D96Parser.NEW, D96Parser.OP_SUB, D96Parser.OP_NOT, D96Parser.IDEN]:
                    self.state = 240
                    self.block_items()
                    pass
                elif token in [D96Parser.LP]:
                    self.state = 241
                    self.block_stmt()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 246
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 247
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_itemsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_stmt(self):
            return self.getTypedRuleContext(D96Parser.Assign_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(D96Parser.If_stmtContext,0)


        def att_decl(self):
            return self.getTypedRuleContext(D96Parser.Att_declContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(D96Parser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(D96Parser.Continue_stmtContext,0)


        def forin_stmt(self):
            return self.getTypedRuleContext(D96Parser.Forin_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(D96Parser.Return_stmtContext,0)


        def member_acc(self):
            return self.getTypedRuleContext(D96Parser.Member_accContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_block_items

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_items" ):
                return visitor.visitBlock_items(self)
            else:
                return visitor.visitChildren(self)




    def block_items(self):

        localctx = D96Parser.Block_itemsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_block_items)
        try:
            self.state = 259
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 249
                self.assign_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 250
                self.if_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 251
                self.att_decl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 252
                self.break_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 253
                self.continue_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 254
                self.forin_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 255
                self.return_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 256
                self.member_acc()
                self.state = 257
                self.match(D96Parser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_lhs(self):
            return self.getTypedRuleContext(D96Parser.Assign_lhsContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_assign_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stmt" ):
                return visitor.visitAssign_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assign_stmt(self):

        localctx = D96Parser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self.assign_lhs()
            self.state = 262
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_lhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExprContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExprContext,i)


        def OP_AS(self):
            return self.getToken(D96Parser.OP_AS, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_assign_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_lhs" ):
                return visitor.visitAssign_lhs(self)
            else:
                return visitor.visitChildren(self)




    def assign_lhs(self):

        localctx = D96Parser.Assign_lhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_assign_lhs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self.expr(0)
            self.state = 265
            self.match(D96Parser.OP_AS)
            self.state = 266
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_invo_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDEN(self):
            return self.getToken(D96Parser.IDEN, 0)

        def DCOL(self):
            return self.getToken(D96Parser.DCOL, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def DOL_IDEN(self):
            return self.getToken(D96Parser.DOL_IDEN, 0)

        def list_expr_method(self):
            return self.getTypedRuleContext(D96Parser.List_expr_methodContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_method_invo_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_invo_stmt" ):
                return visitor.visitMethod_invo_stmt(self)
            else:
                return visitor.visitChildren(self)




    def method_invo_stmt(self):

        localctx = D96Parser.Method_invo_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_method_invo_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self.match(D96Parser.IDEN)
            self.state = 269
            self.match(D96Parser.DCOL)

            self.state = 270
            self.match(D96Parser.DOL_IDEN)
            self.state = 271
            self.match(D96Parser.LB)
            self.state = 273
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.LB) | (1 << D96Parser.ATTR) | (1 << D96Parser.ARRAY) | (1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.OP_SUB) | (1 << D96Parser.OP_NOT) | (1 << D96Parser.IDEN))) != 0):
                self.state = 272
                self.list_expr_method()


            self.state = 275
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Params_list_canContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def params_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Params_listContext)
            else:
                return self.getTypedRuleContext(D96Parser.Params_listContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.SEMI)
            else:
                return self.getToken(D96Parser.SEMI, i)

        def getRuleIndex(self):
            return D96Parser.RULE_params_list_can

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams_list_can" ):
                return visitor.visitParams_list_can(self)
            else:
                return visitor.visitChildren(self)




    def params_list_can(self):

        localctx = D96Parser.Params_list_canContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_params_list_can)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            self.params_list()
            self.state = 282
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.SEMI:
                self.state = 278
                self.match(D96Parser.SEMI)
                self.state = 279
                self.params_list()
                self.state = 284
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Params_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ids_list_with_type(self):
            return self.getTypedRuleContext(D96Parser.Ids_list_with_typeContext,0)


        def OP_AS(self):
            return self.getToken(D96Parser.OP_AS, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExprContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExprContext,i)


        def COM(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COM)
            else:
                return self.getToken(D96Parser.COM, i)

        def ids_list_with_arr(self):
            return self.getTypedRuleContext(D96Parser.Ids_list_with_arrContext,0)


        def array(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ArrayContext)
            else:
                return self.getTypedRuleContext(D96Parser.ArrayContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_params_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams_list" ):
                return visitor.visitParams_list(self)
            else:
                return visitor.visitChildren(self)




    def params_list(self):

        localctx = D96Parser.Params_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_params_list)
        self._la = 0 # Token type
        try:
            self.state = 310
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 285
                self.ids_list_with_type()
                self.state = 295
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==D96Parser.OP_AS:
                    self.state = 286
                    self.match(D96Parser.OP_AS)
                    self.state = 287
                    self.expr(0)
                    self.state = 292
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==D96Parser.COM:
                        self.state = 288
                        self.match(D96Parser.COM)
                        self.state = 289
                        self.expr(0)
                        self.state = 294
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 297
                self.ids_list_with_arr()
                self.state = 308
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==D96Parser.OP_AS:
                    self.state = 298
                    self.match(D96Parser.OP_AS)
                    self.state = 304
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt==1:
                            self.state = 299
                            self.array()
                            self.state = 300
                            self.match(D96Parser.COM) 
                        self.state = 306
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

                    self.state = 307
                    self.array()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ids_list_with_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ids_list(self):
            return self.getTypedRuleContext(D96Parser.Ids_listContext,0)


        def COL(self):
            return self.getToken(D96Parser.COL, 0)

        def data_types(self):
            return self.getTypedRuleContext(D96Parser.Data_typesContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_ids_list_with_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIds_list_with_type" ):
                return visitor.visitIds_list_with_type(self)
            else:
                return visitor.visitChildren(self)




    def ids_list_with_type(self):

        localctx = D96Parser.Ids_list_with_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_ids_list_with_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 312
            self.ids_list()
            self.state = 313
            self.match(D96Parser.COL)
            self.state = 314
            self.data_types()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ids_list_with_arrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ids_list(self):
            return self.getTypedRuleContext(D96Parser.Ids_listContext,0)


        def COL(self):
            return self.getToken(D96Parser.COL, 0)

        def arr_type(self):
            return self.getTypedRuleContext(D96Parser.Arr_typeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_ids_list_with_arr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIds_list_with_arr" ):
                return visitor.visitIds_list_with_arr(self)
            else:
                return visitor.visitChildren(self)




    def ids_list_with_arr(self):

        localctx = D96Parser.Ids_list_with_arrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_ids_list_with_arr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 316
            self.ids_list()
            self.state = 317
            self.match(D96Parser.COL)
            self.state = 318
            self.arr_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ids_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDEN(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.IDEN)
            else:
                return self.getToken(D96Parser.IDEN, i)

        def DOL_IDEN(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.DOL_IDEN)
            else:
                return self.getToken(D96Parser.DOL_IDEN, i)

        def COM(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COM)
            else:
                return self.getToken(D96Parser.COM, i)

        def getRuleIndex(self):
            return D96Parser.RULE_ids_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIds_list" ):
                return visitor.visitIds_list(self)
            else:
                return visitor.visitChildren(self)




    def ids_list(self):

        localctx = D96Parser.Ids_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_ids_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
            _la = self._input.LA(1)
            if not(_la==D96Parser.IDEN or _la==D96Parser.DOL_IDEN):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 325
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COM:
                self.state = 321
                self.match(D96Parser.COM)
                self.state = 322
                _la = self._input.LA(1)
                if not(_la==D96Parser.IDEN or _la==D96Parser.DOL_IDEN):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 327
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Data_typesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def element_types(self):
            return self.getTypedRuleContext(D96Parser.Element_typesContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_data_types

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitData_types" ):
                return visitor.visitData_types(self)
            else:
                return visitor.visitChildren(self)




    def data_types(self):

        localctx = D96Parser.Data_typesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_data_types)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 328
            self.element_types()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Element_typesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(D96Parser.INT, 0)

        def FLOAT(self):
            return self.getToken(D96Parser.FLOAT, 0)

        def STRING(self):
            return self.getToken(D96Parser.STRING, 0)

        def BOOLEAN(self):
            return self.getToken(D96Parser.BOOLEAN, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_element_types

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElement_types" ):
                return visitor.visitElement_types(self)
            else:
                return visitor.visitChildren(self)




    def element_types(self):

        localctx = D96Parser.Element_typesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_element_types)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 330
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.INT) | (1 << D96Parser.FLOAT) | (1 << D96Parser.BOOLEAN) | (1 << D96Parser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(D96Parser.IF, 0)

        def LB(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.LB)
            else:
                return self.getToken(D96Parser.LB, i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExprContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExprContext,i)


        def RB(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.RB)
            else:
                return self.getToken(D96Parser.RB, i)

        def block_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Block_stmtContext)
            else:
                return self.getTypedRuleContext(D96Parser.Block_stmtContext,i)


        def ELSEIF(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ELSEIF)
            else:
                return self.getToken(D96Parser.ELSEIF, i)

        def ELSE(self):
            return self.getToken(D96Parser.ELSE, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = D96Parser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 332
            self.match(D96Parser.IF)
            self.state = 333
            self.match(D96Parser.LB)
            self.state = 334
            self.expr(0)
            self.state = 335
            self.match(D96Parser.RB)
            self.state = 336
            self.block_stmt()
            self.state = 345
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.ELSEIF:
                self.state = 337
                self.match(D96Parser.ELSEIF)
                self.state = 338
                self.match(D96Parser.LB)
                self.state = 339
                self.expr(0)
                self.state = 340
                self.match(D96Parser.RB)
                self.state = 341
                self.block_stmt()
                self.state = 347
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 350
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ELSE:
                self.state = 348
                self.match(D96Parser.ELSE)
                self.state = 349
                self.block_stmt()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(D96Parser.RETURN, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_return_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = D96Parser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 352
            self.match(D96Parser.RETURN)
            self.state = 354
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.LB) | (1 << D96Parser.ATTR) | (1 << D96Parser.ARRAY) | (1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.OP_SUB) | (1 << D96Parser.OP_NOT) | (1 << D96Parser.IDEN))) != 0):
                self.state = 353
                self.expr(0)


            self.state = 356
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(D96Parser.BREAK, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_break_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = D96Parser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 358
            self.match(D96Parser.BREAK)
            self.state = 359
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(D96Parser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_continue_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stmt" ):
                return visitor.visitContinue_stmt(self)
            else:
                return visitor.visitChildren(self)




    def continue_stmt(self):

        localctx = D96Parser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 361
            self.match(D96Parser.CONTINUE)
            self.state = 362
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Forin_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOREACH(self):
            return self.getToken(D96Parser.FOREACH, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def IDEN(self):
            return self.getToken(D96Parser.IDEN, 0)

        def IN(self):
            return self.getToken(D96Parser.IN, 0)

        def INTEGER_LITERAL(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.INTEGER_LITERAL)
            else:
                return self.getToken(D96Parser.INTEGER_LITERAL, i)

        def DDOT(self):
            return self.getToken(D96Parser.DDOT, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def BY(self):
            return self.getToken(D96Parser.BY, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_forin_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForin_stmt" ):
                return visitor.visitForin_stmt(self)
            else:
                return visitor.visitChildren(self)




    def forin_stmt(self):

        localctx = D96Parser.Forin_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_forin_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 364
            self.match(D96Parser.FOREACH)
            self.state = 365
            self.match(D96Parser.LB)
            self.state = 366
            self.match(D96Parser.IDEN)
            self.state = 367
            self.match(D96Parser.IN)
            self.state = 368
            self.match(D96Parser.INTEGER_LITERAL)
            self.state = 369
            self.match(D96Parser.DDOT)
            self.state = 370
            self.match(D96Parser.INTEGER_LITERAL)
            self.state = 373
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.BY:
                self.state = 371
                self.match(D96Parser.BY)
                self.state = 372
                self.match(D96Parser.INTEGER_LITERAL)


            self.state = 375
            self.match(D96Parser.RB)
            self.state = 376
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_stmt" ):
                return visitor.visitExpr_stmt(self)
            else:
                return visitor.visitChildren(self)




    def expr_stmt(self):

        localctx = D96Parser.Expr_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_expr_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 378
            self.expr(0)
            self.state = 379
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom(self):
            return self.getTypedRuleContext(D96Parser.AtomContext,0)


        def NEW(self):
            return self.getToken(D96Parser.NEW, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExprContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExprContext,i)


        def OP_NOT(self):
            return self.getToken(D96Parser.OP_NOT, 0)

        def OP_SUB(self):
            return self.getToken(D96Parser.OP_SUB, 0)

        def DCOL(self):
            return self.getToken(D96Parser.DCOL, 0)

        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def OP_MUL(self):
            return self.getToken(D96Parser.OP_MUL, 0)

        def OP_DIV(self):
            return self.getToken(D96Parser.OP_DIV, 0)

        def OP_MOD(self):
            return self.getToken(D96Parser.OP_MOD, 0)

        def OP_ADD(self):
            return self.getToken(D96Parser.OP_ADD, 0)

        def OP_AND(self):
            return self.getToken(D96Parser.OP_AND, 0)

        def OP_OR(self):
            return self.getToken(D96Parser.OP_OR, 0)

        def OP_LTE(self):
            return self.getToken(D96Parser.OP_LTE, 0)

        def OP_GTE(self):
            return self.getToken(D96Parser.OP_GTE, 0)

        def OP_NEQ(self):
            return self.getToken(D96Parser.OP_NEQ, 0)

        def OP_LT(self):
            return self.getToken(D96Parser.OP_LT, 0)

        def OP_GT(self):
            return self.getToken(D96Parser.OP_GT, 0)

        def OP_EQ(self):
            return self.getToken(D96Parser.OP_EQ, 0)

        def OP_EQ_STR(self):
            return self.getToken(D96Parser.OP_EQ_STR, 0)

        def OP_ADD_STR(self):
            return self.getToken(D96Parser.OP_ADD_STR, 0)

        def LSB(self):
            return self.getToken(D96Parser.LSB, 0)

        def RSB(self):
            return self.getToken(D96Parser.RSB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 64
        self.enterRecursionRule(localctx, 64, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 387
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.state = 382
                self.atom()
                pass

            elif la_ == 2:
                self.state = 383
                self.match(D96Parser.NEW)
                self.state = 384
                self.expr(10)
                pass

            elif la_ == 3:
                self.state = 385
                _la = self._input.LA(1)
                if not(_la==D96Parser.OP_SUB or _la==D96Parser.OP_NOT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 386
                self.expr(6)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 418
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,37,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 416
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 389
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 390
                        self.match(D96Parser.DCOL)
                        self.state = 391
                        self.match(D96Parser.T__2)
                        self.state = 392
                        self.expr(10)
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 393
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")

                        self.state = 394
                        self.match(D96Parser.DOT)
                        self.state = 395
                        self.expr(9)
                        pass

                    elif la_ == 3:
                        localctx = D96Parser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 396
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 397
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.OP_MUL) | (1 << D96Parser.OP_DIV) | (1 << D96Parser.OP_MOD))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 398
                        self.expr(6)
                        pass

                    elif la_ == 4:
                        localctx = D96Parser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 399
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 400
                        _la = self._input.LA(1)
                        if not(_la==D96Parser.OP_ADD or _la==D96Parser.OP_SUB):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 401
                        self.expr(5)
                        pass

                    elif la_ == 5:
                        localctx = D96Parser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 402
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 403
                        _la = self._input.LA(1)
                        if not(_la==D96Parser.OP_AND or _la==D96Parser.OP_OR):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 404
                        self.expr(4)
                        pass

                    elif la_ == 6:
                        localctx = D96Parser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 405
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 406
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.OP_LTE) | (1 << D96Parser.OP_GTE) | (1 << D96Parser.OP_NEQ) | (1 << D96Parser.OP_EQ) | (1 << D96Parser.OP_LT) | (1 << D96Parser.OP_GT))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 407
                        self.expr(3)
                        pass

                    elif la_ == 7:
                        localctx = D96Parser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 408
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 409
                        _la = self._input.LA(1)
                        if not(_la==D96Parser.OP_EQ_STR or _la==D96Parser.OP_ADD_STR):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 410
                        self.expr(2)
                        pass

                    elif la_ == 8:
                        localctx = D96Parser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 411
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 412
                        self.match(D96Parser.LSB)
                        self.state = 413
                        self.expr(0)
                        self.state = 414
                        self.match(D96Parser.RSB)
                        pass

             
                self.state = 420
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,37,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def IDEN(self):
            return self.getToken(D96Parser.IDEN, 0)

        def literal(self):
            return self.getTypedRuleContext(D96Parser.LiteralContext,0)


        def self_type(self):
            return self.getTypedRuleContext(D96Parser.Self_typeContext,0)


        def array_declare(self):
            return self.getTypedRuleContext(D96Parser.Array_declareContext,0)


        def method_invo_stmt(self):
            return self.getTypedRuleContext(D96Parser.Method_invo_stmtContext,0)


        def member_acc(self):
            return self.getTypedRuleContext(D96Parser.Member_accContext,0)


        def class_type(self):
            return self.getTypedRuleContext(D96Parser.Class_typeContext,0)


        def ATTR(self):
            return self.getToken(D96Parser.ATTR, 0)

        def ids_list_with_type(self):
            return self.getTypedRuleContext(D96Parser.Ids_list_with_typeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_atom

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = D96Parser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_atom)
        self._la = 0 # Token type
        try:
            self.state = 437
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 422
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==D96Parser.IDEN:
                    self.state = 421
                    self.match(D96Parser.IDEN)


                self.state = 424
                self.match(D96Parser.LB)
                self.state = 425
                self.expr(0)
                self.state = 426
                self.match(D96Parser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 428
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 429
                self.match(D96Parser.IDEN)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 430
                self.self_type()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 431
                self.array_declare()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 432
                self.method_invo_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 433
                self.member_acc()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 434
                self.class_type()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 435
                self.match(D96Parser.ATTR)
                self.state = 436
                self.ids_list_with_type()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_declareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def muldi_arr(self):
            return self.getTypedRuleContext(D96Parser.Muldi_arrContext,0)


        def indx_arr(self):
            return self.getTypedRuleContext(D96Parser.Indx_arrContext,0)


        def arr_type(self):
            return self.getTypedRuleContext(D96Parser.Arr_typeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_array_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_declare" ):
                return visitor.visitArray_declare(self)
            else:
                return visitor.visitChildren(self)




    def array_declare(self):

        localctx = D96Parser.Array_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_array_declare)
        try:
            self.state = 442
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 439
                self.muldi_arr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 440
                self.indx_arr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 441
                self.arr_type()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def muldi_arr(self):
            return self.getTypedRuleContext(D96Parser.Muldi_arrContext,0)


        def indx_arr(self):
            return self.getTypedRuleContext(D96Parser.Indx_arrContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray" ):
                return visitor.visitArray(self)
            else:
                return visitor.visitChildren(self)




    def array(self):

        localctx = D96Parser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_array)
        try:
            self.state = 446
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 444
                self.muldi_arr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 445
                self.indx_arr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Muldi_arrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def indx_arr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Indx_arrContext)
            else:
                return self.getTypedRuleContext(D96Parser.Indx_arrContext,i)


        def COM(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COM)
            else:
                return self.getToken(D96Parser.COM, i)

        def getRuleIndex(self):
            return D96Parser.RULE_muldi_arr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMuldi_arr" ):
                return visitor.visitMuldi_arr(self)
            else:
                return visitor.visitChildren(self)




    def muldi_arr(self):

        localctx = D96Parser.Muldi_arrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_muldi_arr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 448
            self.match(D96Parser.ARRAY)
            self.state = 449
            self.match(D96Parser.LB)
            self.state = 455
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,42,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 450
                    self.indx_arr()
                    self.state = 451
                    self.match(D96Parser.COM) 
                self.state = 457
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,42,self._ctx)

            self.state = 459
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ARRAY:
                self.state = 458
                self.indx_arr()


            self.state = 461
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Indx_arrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def list_literal(self):
            return self.getTypedRuleContext(D96Parser.List_literalContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_indx_arr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndx_arr" ):
                return visitor.visitIndx_arr(self)
            else:
                return visitor.visitChildren(self)




    def indx_arr(self):

        localctx = D96Parser.Indx_arrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_indx_arr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 463
            self.match(D96Parser.ARRAY)
            self.state = 464
            self.match(D96Parser.LB)
            self.state = 465
            self.list_literal()
            self.state = 466
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arr_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LSB(self):
            return self.getToken(D96Parser.LSB, 0)

        def element_types(self):
            return self.getTypedRuleContext(D96Parser.Element_typesContext,0)


        def COM(self):
            return self.getToken(D96Parser.COM, 0)

        def literal(self):
            return self.getTypedRuleContext(D96Parser.LiteralContext,0)


        def RSB(self):
            return self.getToken(D96Parser.RSB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_arr_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr_type" ):
                return visitor.visitArr_type(self)
            else:
                return visitor.visitChildren(self)




    def arr_type(self):

        localctx = D96Parser.Arr_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_arr_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 468
            self.match(D96Parser.ARRAY)
            self.state = 469
            self.match(D96Parser.LSB)
            self.state = 470
            self.element_types()
            self.state = 471
            self.match(D96Parser.COM)
            self.state = 472
            self.literal()
            self.state = 473
            self.match(D96Parser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Self_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def IDEN(self):
            return self.getToken(D96Parser.IDEN, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_self_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelf_type" ):
                return visitor.visitSelf_type(self)
            else:
                return visitor.visitChildren(self)




    def self_type(self):

        localctx = D96Parser.Self_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_self_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 475
            self.match(D96Parser.SELF)
            self.state = 476
            self.match(D96Parser.DOT)
            self.state = 477
            self.match(D96Parser.IDEN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(D96Parser.NEW, 0)

        def IDEN(self):
            return self.getToken(D96Parser.IDEN, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def list_literal(self):
            return self.getTypedRuleContext(D96Parser.List_literalContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_class_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_type" ):
                return visitor.visitClass_type(self)
            else:
                return visitor.visitChildren(self)




    def class_type(self):

        localctx = D96Parser.Class_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_class_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 479
            self.match(D96Parser.NEW)
            self.state = 480
            self.match(D96Parser.IDEN)
            self.state = 481
            self.match(D96Parser.LB)
            self.state = 483
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.IDEN))) != 0):
                self.state = 482
                self.list_literal()


            self.state = 485
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Member_accContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def inst_attr_acc(self):
            return self.getTypedRuleContext(D96Parser.Inst_attr_accContext,0)


        def stat_attr_acc(self):
            return self.getTypedRuleContext(D96Parser.Stat_attr_accContext,0)


        def inst_meth_invo(self):
            return self.getTypedRuleContext(D96Parser.Inst_meth_invoContext,0)


        def stat_meth_invo(self):
            return self.getTypedRuleContext(D96Parser.Stat_meth_invoContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_member_acc

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMember_acc" ):
                return visitor.visitMember_acc(self)
            else:
                return visitor.visitChildren(self)




    def member_acc(self):

        localctx = D96Parser.Member_accContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_member_acc)
        try:
            self.state = 491
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 487
                self.inst_attr_acc()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 488
                self.stat_attr_acc()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 489
                self.inst_meth_invo()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 490
                self.stat_meth_invo()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Inst_attr_accContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDEN(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.IDEN)
            else:
                return self.getToken(D96Parser.IDEN, i)

        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_inst_attr_acc

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInst_attr_acc" ):
                return visitor.visitInst_attr_acc(self)
            else:
                return visitor.visitChildren(self)




    def inst_attr_acc(self):

        localctx = D96Parser.Inst_attr_accContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_inst_attr_acc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 493
            self.match(D96Parser.IDEN)
            self.state = 494
            self.match(D96Parser.DOT)

            self.state = 495
            self.match(D96Parser.IDEN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stat_attr_accContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDEN(self):
            return self.getToken(D96Parser.IDEN, 0)

        def DCOL(self):
            return self.getToken(D96Parser.DCOL, 0)

        def DOL_IDEN(self):
            return self.getToken(D96Parser.DOL_IDEN, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_stat_attr_acc

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStat_attr_acc" ):
                return visitor.visitStat_attr_acc(self)
            else:
                return visitor.visitChildren(self)




    def stat_attr_acc(self):

        localctx = D96Parser.Stat_attr_accContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_stat_attr_acc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 497
            self.match(D96Parser.IDEN)
            self.state = 498
            self.match(D96Parser.DCOL)

            self.state = 499
            self.match(D96Parser.DOL_IDEN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Inst_meth_invoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDEN(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.IDEN)
            else:
                return self.getToken(D96Parser.IDEN, i)

        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def list_expr_method(self):
            return self.getTypedRuleContext(D96Parser.List_expr_methodContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_inst_meth_invo

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInst_meth_invo" ):
                return visitor.visitInst_meth_invo(self)
            else:
                return visitor.visitChildren(self)




    def inst_meth_invo(self):

        localctx = D96Parser.Inst_meth_invoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_inst_meth_invo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 501
            self.match(D96Parser.IDEN)
            self.state = 502
            self.match(D96Parser.DOT)

            self.state = 503
            self.match(D96Parser.IDEN)
            self.state = 504
            self.match(D96Parser.LB)
            self.state = 506
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.LB) | (1 << D96Parser.ATTR) | (1 << D96Parser.ARRAY) | (1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.OP_SUB) | (1 << D96Parser.OP_NOT) | (1 << D96Parser.IDEN))) != 0):
                self.state = 505
                self.list_expr_method()


            self.state = 508
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stat_meth_invoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDEN(self):
            return self.getToken(D96Parser.IDEN, 0)

        def DCOL(self):
            return self.getToken(D96Parser.DCOL, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def DOL_IDEN(self):
            return self.getToken(D96Parser.DOL_IDEN, 0)

        def list_expr_method(self):
            return self.getTypedRuleContext(D96Parser.List_expr_methodContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_stat_meth_invo

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStat_meth_invo" ):
                return visitor.visitStat_meth_invo(self)
            else:
                return visitor.visitChildren(self)




    def stat_meth_invo(self):

        localctx = D96Parser.Stat_meth_invoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_stat_meth_invo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 510
            self.match(D96Parser.IDEN)
            self.state = 511
            self.match(D96Parser.DCOL)

            self.state = 512
            self.match(D96Parser.DOL_IDEN)
            self.state = 513
            self.match(D96Parser.LB)
            self.state = 515
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.LB) | (1 << D96Parser.ATTR) | (1 << D96Parser.ARRAY) | (1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.OP_SUB) | (1 << D96Parser.OP_NOT) | (1 << D96Parser.IDEN))) != 0):
                self.state = 514
                self.list_expr_method()


            self.state = 517
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_expr_methodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elem_expr_method(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Elem_expr_methodContext)
            else:
                return self.getTypedRuleContext(D96Parser.Elem_expr_methodContext,i)


        def COM(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COM)
            else:
                return self.getToken(D96Parser.COM, i)

        def getRuleIndex(self):
            return D96Parser.RULE_list_expr_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_expr_method" ):
                return visitor.visitList_expr_method(self)
            else:
                return visitor.visitChildren(self)




    def list_expr_method(self):

        localctx = D96Parser.List_expr_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_list_expr_method)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 524
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,48,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 519
                    self.elem_expr_method()
                    self.state = 520
                    self.match(D96Parser.COM) 
                self.state = 526
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,48,self._ctx)

            self.state = 527
            self.elem_expr_method()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elem_expr_methodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def literal(self):
            return self.getTypedRuleContext(D96Parser.LiteralContext,0)


        def stat_attr_acc(self):
            return self.getTypedRuleContext(D96Parser.Stat_attr_accContext,0)


        def inst_meth_invo(self):
            return self.getTypedRuleContext(D96Parser.Inst_meth_invoContext,0)


        def stat_meth_invo(self):
            return self.getTypedRuleContext(D96Parser.Stat_meth_invoContext,0)


        def inst_attr_acc(self):
            return self.getTypedRuleContext(D96Parser.Inst_attr_accContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_elem_expr_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElem_expr_method" ):
                return visitor.visitElem_expr_method(self)
            else:
                return visitor.visitChildren(self)




    def elem_expr_method(self):

        localctx = D96Parser.Elem_expr_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_elem_expr_method)
        try:
            self.state = 535
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 529
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 530
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 531
                self.stat_attr_acc()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 532
                self.inst_meth_invo()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 533
                self.stat_meth_invo()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 534
                self.inst_attr_acc()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.LiteralContext)
            else:
                return self.getTypedRuleContext(D96Parser.LiteralContext,i)


        def COM(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COM)
            else:
                return self.getToken(D96Parser.COM, i)

        def getRuleIndex(self):
            return D96Parser.RULE_list_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_literal" ):
                return visitor.visitList_literal(self)
            else:
                return visitor.visitChildren(self)




    def list_literal(self):

        localctx = D96Parser.List_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_list_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 542
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,50,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 537
                    self.literal()
                    self.state = 538
                    self.match(D96Parser.COM) 
                self.state = 544
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,50,self._ctx)

            self.state = 545
            self.literal()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def number_literal(self):
            return self.getTypedRuleContext(D96Parser.Number_literalContext,0)


        def STRING_LITERAL(self):
            return self.getToken(D96Parser.STRING_LITERAL, 0)

        def IDEN(self):
            return self.getToken(D96Parser.IDEN, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = D96Parser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_literal)
        try:
            self.state = 550
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.FLOAT_LITERAL, D96Parser.INTEGER_LITERAL, D96Parser.BOOLEAN_LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 547
                self.number_literal()
                pass
            elif token in [D96Parser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 548
                self.match(D96Parser.STRING_LITERAL)
                pass
            elif token in [D96Parser.IDEN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 549
                self.match(D96Parser.IDEN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Number_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER_LITERAL(self):
            return self.getToken(D96Parser.INTEGER_LITERAL, 0)

        def FLOAT_LITERAL(self):
            return self.getToken(D96Parser.FLOAT_LITERAL, 0)

        def BOOLEAN_LITERAL(self):
            return self.getToken(D96Parser.BOOLEAN_LITERAL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_number_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber_literal" ):
                return visitor.visitNumber_literal(self)
            else:
                return visitor.visitChildren(self)




    def number_literal(self):

        localctx = D96Parser.Number_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_number_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 552
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[32] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 1)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 7)
         




