# Generated from d:\BK COURSE\HK212\PPL\Assignment\Assignment2\initial\src\main\d96\parser\D96.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3@")
        buf.write("\u022f\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\3\2\6\2f\n\2\r\2\16")
        buf.write("\2g\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\6\3t\n\3\r")
        buf.write("\3\16\3u\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\6\3\u0086\n\3\r\3\16\3\u0087\3\3\3\3\5\3\u008c")
        buf.write("\n\3\3\4\3\4\5\4\u0090\n\4\3\5\3\5\3\5\3\5\3\5\3\5\5\5")
        buf.write("\u0098\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\5\6\u00a7\n\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\5\7\u00b3\n\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\5\t\u00c1\n\t\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\5\n\u00ca\n\n\3\13\3\13\3\13\7\13\u00cf\n\13\f\13")
        buf.write("\16\13\u00d2\13\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r\7\r\u00db")
        buf.write("\n\r\f\r\16\r\u00de\13\r\3\16\3\16\3\16\7\16\u00e3\n\16")
        buf.write("\f\16\16\16\u00e6\13\16\3\17\3\17\3\20\3\20\3\20\7\20")
        buf.write("\u00ed\n\20\f\20\16\20\u00f0\13\20\3\20\3\20\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\5\21\u00fc\n\21\3\22\3")
        buf.write("\22\3\22\3\23\3\23\3\23\3\23\3\24\3\24\3\24\5\24\u0108")
        buf.write("\n\24\3\25\3\25\3\25\3\25\3\25\5\25\u010f\n\25\3\26\3")
        buf.write("\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\7\26")
        buf.write("\u011c\n\26\f\26\16\26\u011f\13\26\3\26\3\26\5\26\u0123")
        buf.write("\n\26\3\27\3\27\5\27\u0127\n\27\3\27\3\27\3\30\3\30\3")
        buf.write("\30\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\5\32\u013a\n\32\3\32\3\32\3\32\3\33\3\33\3")
        buf.write("\33\3\33\3\33\3\33\7\33\u0145\n\33\f\33\16\33\u0148\13")
        buf.write("\33\3\34\3\34\3\34\3\34\3\34\3\34\7\34\u0150\n\34\f\34")
        buf.write("\16\34\u0153\13\34\3\35\3\35\3\35\3\35\3\35\3\35\7\35")
        buf.write("\u015b\n\35\f\35\16\35\u015e\13\35\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\7\36\u0166\n\36\f\36\16\36\u0169\13\36\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\7\37\u0171\n\37\f\37\16\37\u0174")
        buf.write("\13\37\3 \3 \3 \5 \u0179\n \3!\3!\3!\5!\u017e\n!\3\"\3")
        buf.write("\"\3\"\3\"\3\"\3\"\5\"\u0186\n\"\3#\3#\3#\3#\3#\3#\3#")
        buf.write("\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\7#\u019a\n#\f#\16#\u019d")
        buf.write("\13#\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3")
        buf.write("$\3$\7$\u01b1\n$\f$\16$\u01b4\13$\3%\3%\3%\3%\3%\3%\3")
        buf.write("%\3%\3%\3%\3%\5%\u01c1\n%\3&\3&\3&\3&\3&\5&\u01c8\n&\3")
        buf.write("\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\5\'\u01d2\n\'\3(\3(\3(")
        buf.write("\3(\3(\3)\3)\3)\3)\3)\3)\3)\3)\5)\u01e1\n)\3*\3*\3*\3")
        buf.write("+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3")
        buf.write("+\3+\3+\3+\3+\3+\3+\3+\5+\u0200\n+\3,\3,\5,\u0204\n,\3")
        buf.write("-\3-\3-\3-\3-\3.\3.\3.\3.\3.\5.\u0210\n.\3/\3/\3/\3/\3")
        buf.write("/\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\61\3\61\3\61\7")
        buf.write("\61\u0221\n\61\f\61\16\61\u0224\13\61\3\61\3\61\3\62\3")
        buf.write("\62\3\62\3\62\3\62\5\62\u022d\n\62\3\62\2\t\64\668:<D")
        buf.write("F\63\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60")
        buf.write("\62\64\668:<>@BDFHJLNPRTVXZ\\^`b\2\b\3\2;<\3\29:\4\2\62")
        buf.write("\64\668\3\2\60\61\3\2*+\3\2,.\2\u0240\2e\3\2\2\2\4\u008b")
        buf.write("\3\2\2\2\6\u008f\3\2\2\2\b\u0097\3\2\2\2\n\u00a6\3\2\2")
        buf.write("\2\f\u00b2\3\2\2\2\16\u00b4\3\2\2\2\20\u00c0\3\2\2\2\22")
        buf.write("\u00c9\3\2\2\2\24\u00cb\3\2\2\2\26\u00d3\3\2\2\2\30\u00d7")
        buf.write("\3\2\2\2\32\u00df\3\2\2\2\34\u00e7\3\2\2\2\36\u00e9\3")
        buf.write("\2\2\2 \u00fb\3\2\2\2\"\u00fd\3\2\2\2$\u0100\3\2\2\2&")
        buf.write("\u0107\3\2\2\2(\u010e\3\2\2\2*\u0110\3\2\2\2,\u0124\3")
        buf.write("\2\2\2.\u012a\3\2\2\2\60\u012d\3\2\2\2\62\u0130\3\2\2")
        buf.write("\2\64\u013e\3\2\2\2\66\u0149\3\2\2\28\u0154\3\2\2\2:\u015f")
        buf.write("\3\2\2\2<\u016a\3\2\2\2>\u0178\3\2\2\2@\u017d\3\2\2\2")
        buf.write("B\u0185\3\2\2\2D\u0187\3\2\2\2F\u019e\3\2\2\2H\u01c0\3")
        buf.write("\2\2\2J\u01c7\3\2\2\2L\u01d1\3\2\2\2N\u01d3\3\2\2\2P\u01e0")
        buf.write("\3\2\2\2R\u01e2\3\2\2\2T\u01ff\3\2\2\2V\u0203\3\2\2\2")
        buf.write("X\u0205\3\2\2\2Z\u020f\3\2\2\2\\\u0211\3\2\2\2^\u0216")
        buf.write("\3\2\2\2`\u0222\3\2\2\2b\u022c\3\2\2\2df\5\4\3\2ed\3\2")
        buf.write("\2\2fg\3\2\2\2ge\3\2\2\2gh\3\2\2\2hi\3\2\2\2ij\7\2\2\3")
        buf.write("j\3\3\2\2\2kl\7\21\2\2lm\7;\2\2mn\7\t\2\2n\u008c\7\n\2")
        buf.write("\2op\7\21\2\2pq\7;\2\2qs\7\t\2\2rt\5\6\4\2sr\3\2\2\2t")
        buf.write("u\3\2\2\2us\3\2\2\2uv\3\2\2\2vw\3\2\2\2wx\7\n\2\2x\u008c")
        buf.write("\3\2\2\2yz\7\21\2\2z{\7;\2\2{|\7\16\2\2|}\7;\2\2}~\7\t")
        buf.write("\2\2~\u008c\7\n\2\2\177\u0080\7\21\2\2\u0080\u0081\7;")
        buf.write("\2\2\u0081\u0082\7\16\2\2\u0082\u0083\7;\2\2\u0083\u0085")
        buf.write("\7\t\2\2\u0084\u0086\5\6\4\2\u0085\u0084\3\2\2\2\u0086")
        buf.write("\u0087\3\2\2\2\u0087\u0085\3\2\2\2\u0087\u0088\3\2\2\2")
        buf.write("\u0088\u0089\3\2\2\2\u0089\u008a\7\n\2\2\u008a\u008c\3")
        buf.write("\2\2\2\u008bk\3\2\2\2\u008bo\3\2\2\2\u008by\3\2\2\2\u008b")
        buf.write("\177\3\2\2\2\u008c\5\3\2\2\2\u008d\u0090\5\b\5\2\u008e")
        buf.write("\u0090\5\n\6\2\u008f\u008d\3\2\2\2\u008f\u008e\3\2\2\2")
        buf.write("\u0090\7\3\2\2\2\u0091\u0092\5\20\t\2\u0092\u0093\7\r")
        buf.write("\2\2\u0093\u0098\3\2\2\2\u0094\u0095\5\22\n\2\u0095\u0096")
        buf.write("\7\r\2\2\u0096\u0098\3\2\2\2\u0097\u0091\3\2\2\2\u0097")
        buf.write("\u0094\3\2\2\2\u0098\t\3\2\2\2\u0099\u00a7\5\f\7\2\u009a")
        buf.write("\u00a7\5\16\b\2\u009b\u009c\5\34\17\2\u009c\u009d\7\7")
        buf.write("\2\2\u009d\u009e\7\b\2\2\u009e\u009f\5\36\20\2\u009f\u00a7")
        buf.write("\3\2\2\2\u00a0\u00a1\5\34\17\2\u00a1\u00a2\7\7\2\2\u00a2")
        buf.write("\u00a3\5\24\13\2\u00a3\u00a4\7\b\2\2\u00a4\u00a5\5\36")
        buf.write("\20\2\u00a5\u00a7\3\2\2\2\u00a6\u0099\3\2\2\2\u00a6\u009a")
        buf.write("\3\2\2\2\u00a6\u009b\3\2\2\2\u00a6\u00a0\3\2\2\2\u00a7")
        buf.write("\13\3\2\2\2\u00a8\u00a9\7$\2\2\u00a9\u00aa\7\7\2\2\u00aa")
        buf.write("\u00ab\7\b\2\2\u00ab\u00b3\5\36\20\2\u00ac\u00ad\7$\2")
        buf.write("\2\u00ad\u00ae\7\7\2\2\u00ae\u00af\5\24\13\2\u00af\u00b0")
        buf.write("\7\b\2\2\u00b0\u00b1\5\36\20\2\u00b1\u00b3\3\2\2\2\u00b2")
        buf.write("\u00a8\3\2\2\2\u00b2\u00ac\3\2\2\2\u00b3\r\3\2\2\2\u00b4")
        buf.write("\u00b5\7%\2\2\u00b5\u00b6\7\7\2\2\u00b6\u00b7\7\b\2\2")
        buf.write("\u00b7\u00b8\5\36\20\2\u00b8\17\3\2\2\2\u00b9\u00ba\7")
        buf.write("\22\2\2\u00ba\u00bb\5\26\f\2\u00bb\u00bc\7\65\2\2\u00bc")
        buf.write("\u00bd\5\32\16\2\u00bd\u00c1\3\2\2\2\u00be\u00bf\7\22")
        buf.write("\2\2\u00bf\u00c1\5\26\f\2\u00c0\u00b9\3\2\2\2\u00c0\u00be")
        buf.write("\3\2\2\2\u00c1\21\3\2\2\2\u00c2\u00c3\7\23\2\2\u00c3\u00c4")
        buf.write("\5\26\f\2\u00c4\u00c5\7\65\2\2\u00c5\u00c6\5\32\16\2\u00c6")
        buf.write("\u00ca\3\2\2\2\u00c7\u00c8\7\23\2\2\u00c8\u00ca\5\26\f")
        buf.write("\2\u00c9\u00c2\3\2\2\2\u00c9\u00c7\3\2\2\2\u00ca\23\3")
        buf.write("\2\2\2\u00cb\u00d0\5\26\f\2\u00cc\u00cd\7\r\2\2\u00cd")
        buf.write("\u00cf\5\26\f\2\u00ce\u00cc\3\2\2\2\u00cf\u00d2\3\2\2")
        buf.write("\2\u00d0\u00ce\3\2\2\2\u00d0\u00d1\3\2\2\2\u00d1\25\3")
        buf.write("\2\2\2\u00d2\u00d0\3\2\2\2\u00d3\u00d4\5\30\r\2\u00d4")
        buf.write("\u00d5\7\16\2\2\u00d5\u00d6\5(\25\2\u00d6\27\3\2\2\2\u00d7")
        buf.write("\u00dc\5\34\17\2\u00d8\u00d9\7\20\2\2\u00d9\u00db\5\34")
        buf.write("\17\2\u00da\u00d8\3\2\2\2\u00db\u00de\3\2\2\2\u00dc\u00da")
        buf.write("\3\2\2\2\u00dc\u00dd\3\2\2\2\u00dd\31\3\2\2\2\u00de\u00dc")
        buf.write("\3\2\2\2\u00df\u00e4\5\64\33\2\u00e0\u00e1\7\20\2\2\u00e1")
        buf.write("\u00e3\5\64\33\2\u00e2\u00e0\3\2\2\2\u00e3\u00e6\3\2\2")
        buf.write("\2\u00e4\u00e2\3\2\2\2\u00e4\u00e5\3\2\2\2\u00e5\33\3")
        buf.write("\2\2\2\u00e6\u00e4\3\2\2\2\u00e7\u00e8\t\2\2\2\u00e8\35")
        buf.write("\3\2\2\2\u00e9\u00ee\7\t\2\2\u00ea\u00ed\5 \21\2\u00eb")
        buf.write("\u00ed\5\36\20\2\u00ec\u00ea\3\2\2\2\u00ec\u00eb\3\2\2")
        buf.write("\2\u00ed\u00f0\3\2\2\2\u00ee\u00ec\3\2\2\2\u00ee\u00ef")
        buf.write("\3\2\2\2\u00ef\u00f1\3\2\2\2\u00f0\u00ee\3\2\2\2\u00f1")
        buf.write("\u00f2\7\n\2\2\u00f2\37\3\2\2\2\u00f3\u00fc\5\"\22\2\u00f4")
        buf.write("\u00fc\5*\26\2\u00f5\u00fc\5\b\5\2\u00f6\u00fc\5.\30\2")
        buf.write("\u00f7\u00fc\5\60\31\2\u00f8\u00fc\5\62\32\2\u00f9\u00fc")
        buf.write("\5,\27\2\u00fa\u00fc\5R*\2\u00fb\u00f3\3\2\2\2\u00fb\u00f4")
        buf.write("\3\2\2\2\u00fb\u00f5\3\2\2\2\u00fb\u00f6\3\2\2\2\u00fb")
        buf.write("\u00f7\3\2\2\2\u00fb\u00f8\3\2\2\2\u00fb\u00f9\3\2\2\2")
        buf.write("\u00fb\u00fa\3\2\2\2\u00fc!\3\2\2\2\u00fd\u00fe\5$\23")
        buf.write("\2\u00fe\u00ff\7\r\2\2\u00ff#\3\2\2\2\u0100\u0101\5&\24")
        buf.write("\2\u0101\u0102\7\65\2\2\u0102\u0103\5\64\33\2\u0103%\3")
        buf.write("\2\2\2\u0104\u0108\7;\2\2\u0105\u0108\5N(\2\u0106\u0108")
        buf.write("\5P)\2\u0107\u0104\3\2\2\2\u0107\u0105\3\2\2\2\u0107\u0106")
        buf.write("\3\2\2\2\u0108\'\3\2\2\2\u0109\u010f\7\26\2\2\u010a\u010f")
        buf.write("\7\27\2\2\u010b\u010f\7\31\2\2\u010c\u010f\7\30\2\2\u010d")
        buf.write("\u010f\5^\60\2\u010e\u0109\3\2\2\2\u010e\u010a\3\2\2\2")
        buf.write("\u010e\u010b\3\2\2\2\u010e\u010c\3\2\2\2\u010e\u010d\3")
        buf.write("\2\2\2\u010f)\3\2\2\2\u0110\u0111\7\35\2\2\u0111\u0112")
        buf.write("\7\7\2\2\u0112\u0113\5\64\33\2\u0113\u0114\7\b\2\2\u0114")
        buf.write("\u011d\5\36\20\2\u0115\u0116\7\36\2\2\u0116\u0117\7\7")
        buf.write("\2\2\u0117\u0118\5\64\33\2\u0118\u0119\7\b\2\2\u0119\u011a")
        buf.write("\5\36\20\2\u011a\u011c\3\2\2\2\u011b\u0115\3\2\2\2\u011c")
        buf.write("\u011f\3\2\2\2\u011d\u011b\3\2\2\2\u011d\u011e\3\2\2\2")
        buf.write("\u011e\u0122\3\2\2\2\u011f\u011d\3\2\2\2\u0120\u0121\7")
        buf.write("\37\2\2\u0121\u0123\5\36\20\2\u0122\u0120\3\2\2\2\u0122")
        buf.write("\u0123\3\2\2\2\u0123+\3\2\2\2\u0124\u0126\7!\2\2\u0125")
        buf.write("\u0127\5\64\33\2\u0126\u0125\3\2\2\2\u0126\u0127\3\2\2")
        buf.write("\2\u0127\u0128\3\2\2\2\u0128\u0129\7\r\2\2\u0129-\3\2")
        buf.write("\2\2\u012a\u012b\7\33\2\2\u012b\u012c\7\r\2\2\u012c/\3")
        buf.write("\2\2\2\u012d\u012e\7\34\2\2\u012e\u012f\7\r\2\2\u012f")
        buf.write("\61\3\2\2\2\u0130\u0131\7 \2\2\u0131\u0132\7\7\2\2\u0132")
        buf.write("\u0133\7;\2\2\u0133\u0134\7&\2\2\u0134\u0135\7\4\2\2\u0135")
        buf.write("\u0136\7)\2\2\u0136\u0139\7\4\2\2\u0137\u0138\7\'\2\2")
        buf.write("\u0138\u013a\7\4\2\2\u0139\u0137\3\2\2\2\u0139\u013a\3")
        buf.write("\2\2\2\u013a\u013b\3\2\2\2\u013b\u013c\7\b\2\2\u013c\u013d")
        buf.write("\5\36\20\2\u013d\63\3\2\2\2\u013e\u013f\b\33\1\2\u013f")
        buf.write("\u0140\5\66\34\2\u0140\u0146\3\2\2\2\u0141\u0142\f\4\2")
        buf.write("\2\u0142\u0143\t\3\2\2\u0143\u0145\5\66\34\2\u0144\u0141")
        buf.write("\3\2\2\2\u0145\u0148\3\2\2\2\u0146\u0144\3\2\2\2\u0146")
        buf.write("\u0147\3\2\2\2\u0147\65\3\2\2\2\u0148\u0146\3\2\2\2\u0149")
        buf.write("\u014a\b\34\1\2\u014a\u014b\58\35\2\u014b\u0151\3\2\2")
        buf.write("\2\u014c\u014d\f\4\2\2\u014d\u014e\t\4\2\2\u014e\u0150")
        buf.write("\58\35\2\u014f\u014c\3\2\2\2\u0150\u0153\3\2\2\2\u0151")
        buf.write("\u014f\3\2\2\2\u0151\u0152\3\2\2\2\u0152\67\3\2\2\2\u0153")
        buf.write("\u0151\3\2\2\2\u0154\u0155\b\35\1\2\u0155\u0156\5:\36")
        buf.write("\2\u0156\u015c\3\2\2\2\u0157\u0158\f\4\2\2\u0158\u0159")
        buf.write("\t\5\2\2\u0159\u015b\5:\36\2\u015a\u0157\3\2\2\2\u015b")
        buf.write("\u015e\3\2\2\2\u015c\u015a\3\2\2\2\u015c\u015d\3\2\2\2")
        buf.write("\u015d9\3\2\2\2\u015e\u015c\3\2\2\2\u015f\u0160\b\36\1")
        buf.write("\2\u0160\u0161\5<\37\2\u0161\u0167\3\2\2\2\u0162\u0163")
        buf.write("\f\4\2\2\u0163\u0164\t\6\2\2\u0164\u0166\5<\37\2\u0165")
        buf.write("\u0162\3\2\2\2\u0166\u0169\3\2\2\2\u0167\u0165\3\2\2\2")
        buf.write("\u0167\u0168\3\2\2\2\u0168;\3\2\2\2\u0169\u0167\3\2\2")
        buf.write("\2\u016a\u016b\b\37\1\2\u016b\u016c\5> \2\u016c\u0172")
        buf.write("\3\2\2\2\u016d\u016e\f\4\2\2\u016e\u016f\t\7\2\2\u016f")
        buf.write("\u0171\5> \2\u0170\u016d\3\2\2\2\u0171\u0174\3\2\2\2\u0172")
        buf.write("\u0170\3\2\2\2\u0172\u0173\3\2\2\2\u0173=\3\2\2\2\u0174")
        buf.write("\u0172\3\2\2\2\u0175\u0176\7/\2\2\u0176\u0179\5> \2\u0177")
        buf.write("\u0179\5@!\2\u0178\u0175\3\2\2\2\u0178\u0177\3\2\2\2\u0179")
        buf.write("?\3\2\2\2\u017a\u017b\7+\2\2\u017b\u017e\5@!\2\u017c\u017e")
        buf.write("\5B\"\2\u017d\u017a\3\2\2\2\u017d\u017c\3\2\2\2\u017e")
        buf.write("A\3\2\2\2\u017f\u0180\5D#\2\u0180\u0181\7\13\2\2\u0181")
        buf.write("\u0182\5\64\33\2\u0182\u0183\7\f\2\2\u0183\u0186\3\2\2")
        buf.write("\2\u0184\u0186\5D#\2\u0185\u017f\3\2\2\2\u0185\u0184\3")
        buf.write("\2\2\2\u0186C\3\2\2\2\u0187\u0188\b#\1\2\u0188\u0189\5")
        buf.write("F$\2\u0189\u019b\3\2\2\2\u018a\u018b\f\6\2\2\u018b\u018c")
        buf.write("\7(\2\2\u018c\u019a\7;\2\2\u018d\u018e\f\5\2\2\u018e\u018f")
        buf.write("\7(\2\2\u018f\u0190\7;\2\2\u0190\u0191\7\7\2\2\u0191\u019a")
        buf.write("\7\b\2\2\u0192\u0193\f\4\2\2\u0193\u0194\7(\2\2\u0194")
        buf.write("\u0195\7;\2\2\u0195\u0196\7\7\2\2\u0196\u0197\5\32\16")
        buf.write("\2\u0197\u0198\7\b\2\2\u0198\u019a\3\2\2\2\u0199\u018a")
        buf.write("\3\2\2\2\u0199\u018d\3\2\2\2\u0199\u0192\3\2\2\2\u019a")
        buf.write("\u019d\3\2\2\2\u019b\u0199\3\2\2\2\u019b\u019c\3\2\2\2")
        buf.write("\u019cE\3\2\2\2\u019d\u019b\3\2\2\2\u019e\u019f\b$\1\2")
        buf.write("\u019f\u01a0\5H%\2\u01a0\u01b2\3\2\2\2\u01a1\u01a2\f\6")
        buf.write("\2\2\u01a2\u01a3\7\17\2\2\u01a3\u01b1\7<\2\2\u01a4\u01a5")
        buf.write("\f\5\2\2\u01a5\u01a6\7\17\2\2\u01a6\u01a7\7<\2\2\u01a7")
        buf.write("\u01a8\7\7\2\2\u01a8\u01b1\7\b\2\2\u01a9\u01aa\f\4\2\2")
        buf.write("\u01aa\u01ab\7\17\2\2\u01ab\u01ac\7<\2\2\u01ac\u01ad\7")
        buf.write("\7\2\2\u01ad\u01ae\5\32\16\2\u01ae\u01af\7\b\2\2\u01af")
        buf.write("\u01b1\3\2\2\2\u01b0\u01a1\3\2\2\2\u01b0\u01a4\3\2\2\2")
        buf.write("\u01b0\u01a9\3\2\2\2\u01b1\u01b4\3\2\2\2\u01b2\u01b0\3")
        buf.write("\2\2\2\u01b2\u01b3\3\2\2\2\u01b3G\3\2\2\2\u01b4\u01b2")
        buf.write("\3\2\2\2\u01b5\u01b6\7#\2\2\u01b6\u01b7\7;\2\2\u01b7\u01b8")
        buf.write("\7\7\2\2\u01b8\u01c1\7\b\2\2\u01b9\u01ba\7#\2\2\u01ba")
        buf.write("\u01bb\7;\2\2\u01bb\u01bc\7\7\2\2\u01bc\u01bd\5\32\16")
        buf.write("\2\u01bd\u01be\7\b\2\2\u01be\u01c1\3\2\2\2\u01bf\u01c1")
        buf.write("\5J&\2\u01c0\u01b5\3\2\2\2\u01c0\u01b9\3\2\2\2\u01c0\u01bf")
        buf.write("\3\2\2\2\u01c1I\3\2\2\2\u01c2\u01c3\7\7\2\2\u01c3\u01c4")
        buf.write("\5\64\33\2\u01c4\u01c5\7\b\2\2\u01c5\u01c8\3\2\2\2\u01c6")
        buf.write("\u01c8\5L\'\2\u01c7\u01c2\3\2\2\2\u01c7\u01c6\3\2\2\2")
        buf.write("\u01c8K\3\2\2\2\u01c9\u01d2\7;\2\2\u01ca\u01d2\5b\62\2")
        buf.write("\u01cb\u01cc\7\"\2\2\u01cc\u01cd\7(\2\2\u01cd\u01d2\7")
        buf.write(";\2\2\u01ce\u01cf\7\"\2\2\u01cf\u01d0\7\17\2\2\u01d0\u01d2")
        buf.write("\7;\2\2\u01d1\u01c9\3\2\2\2\u01d1\u01ca\3\2\2\2\u01d1")
        buf.write("\u01cb\3\2\2\2\u01d1\u01ce\3\2\2\2\u01d2M\3\2\2\2\u01d3")
        buf.write("\u01d4\5D#\2\u01d4\u01d5\7\13\2\2\u01d5\u01d6\5\64\33")
        buf.write("\2\u01d6\u01d7\7\f\2\2\u01d7O\3\2\2\2\u01d8\u01d9\5\64")
        buf.write("\33\2\u01d9\u01da\7(\2\2\u01da\u01db\7;\2\2\u01db\u01e1")
        buf.write("\3\2\2\2\u01dc\u01dd\5\64\33\2\u01dd\u01de\7\17\2\2\u01de")
        buf.write("\u01df\7;\2\2\u01df\u01e1\3\2\2\2\u01e0\u01d8\3\2\2\2")
        buf.write("\u01e0\u01dc\3\2\2\2\u01e1Q\3\2\2\2\u01e2\u01e3\5T+\2")
        buf.write("\u01e3\u01e4\7\r\2\2\u01e4S\3\2\2\2\u01e5\u01e6\5\64\33")
        buf.write("\2\u01e6\u01e7\7(\2\2\u01e7\u01e8\7;\2\2\u01e8\u01e9\7")
        buf.write("\7\2\2\u01e9\u01ea\7\b\2\2\u01ea\u0200\3\2\2\2\u01eb\u01ec")
        buf.write("\5\64\33\2\u01ec\u01ed\7(\2\2\u01ed\u01ee\7;\2\2\u01ee")
        buf.write("\u01ef\7\7\2\2\u01ef\u01f0\5\32\16\2\u01f0\u01f1\7\b\2")
        buf.write("\2\u01f1\u0200\3\2\2\2\u01f2\u01f3\5\64\33\2\u01f3\u01f4")
        buf.write("\7\17\2\2\u01f4\u01f5\7<\2\2\u01f5\u01f6\7\7\2\2\u01f6")
        buf.write("\u01f7\7\b\2\2\u01f7\u0200\3\2\2\2\u01f8\u01f9\5\64\33")
        buf.write("\2\u01f9\u01fa\7\17\2\2\u01fa\u01fb\7<\2\2\u01fb\u01fc")
        buf.write("\7\7\2\2\u01fc\u01fd\5\32\16\2\u01fd\u01fe\7\b\2\2\u01fe")
        buf.write("\u0200\3\2\2\2\u01ff\u01e5\3\2\2\2\u01ff\u01eb\3\2\2\2")
        buf.write("\u01ff\u01f2\3\2\2\2\u01ff\u01f8\3\2\2\2\u0200U\3\2\2")
        buf.write("\2\u0201\u0204\5X-\2\u0202\u0204\5\\/\2\u0203\u0201\3")
        buf.write("\2\2\2\u0203\u0202\3\2\2\2\u0204W\3\2\2\2\u0205\u0206")
        buf.write("\7\25\2\2\u0206\u0207\7\7\2\2\u0207\u0208\5Z.\2\u0208")
        buf.write("\u0209\7\b\2\2\u0209Y\3\2\2\2\u020a\u020b\5\\/\2\u020b")
        buf.write("\u020c\7\20\2\2\u020c\u020d\5Z.\2\u020d\u0210\3\2\2\2")
        buf.write("\u020e\u0210\5\\/\2\u020f\u020a\3\2\2\2\u020f\u020e\3")
        buf.write("\2\2\2\u0210[\3\2\2\2\u0211\u0212\7\25\2\2\u0212\u0213")
        buf.write("\7\7\2\2\u0213\u0214\5\32\16\2\u0214\u0215\7\b\2\2\u0215")
        buf.write("]\3\2\2\2\u0216\u0217\7\25\2\2\u0217\u0218\7\13\2\2\u0218")
        buf.write("\u0219\5(\25\2\u0219\u021a\7\20\2\2\u021a\u021b\5b\62")
        buf.write("\2\u021b\u021c\7\f\2\2\u021c_\3\2\2\2\u021d\u021e\5b\62")
        buf.write("\2\u021e\u021f\7\20\2\2\u021f\u0221\3\2\2\2\u0220\u021d")
        buf.write("\3\2\2\2\u0221\u0224\3\2\2\2\u0222\u0220\3\2\2\2\u0222")
        buf.write("\u0223\3\2\2\2\u0223\u0225\3\2\2\2\u0224\u0222\3\2\2\2")
        buf.write("\u0225\u0226\5b\62\2\u0226a\3\2\2\2\u0227\u022d\7\4\2")
        buf.write("\2\u0228\u022d\7\3\2\2\u0229\u022d\7\5\2\2\u022a\u022d")
        buf.write("\7\6\2\2\u022b\u022d\5V,\2\u022c\u0227\3\2\2\2\u022c\u0228")
        buf.write("\3\2\2\2\u022c\u0229\3\2\2\2\u022c\u022a\3\2\2\2\u022c")
        buf.write("\u022b\3\2\2\2\u022dc\3\2\2\2-gu\u0087\u008b\u008f\u0097")
        buf.write("\u00a6\u00b2\u00c0\u00c9\u00d0\u00dc\u00e4\u00ec\u00ee")
        buf.write("\u00fb\u0107\u010e\u011d\u0122\u0126\u0139\u0146\u0151")
        buf.write("\u015c\u0167\u0172\u0178\u017d\u0185\u0199\u019b\u01b0")
        buf.write("\u01b2\u01c0\u01c7\u01d1\u01e0\u01ff\u0203\u020f\u0222")
        buf.write("\u022c")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'('", "')'", "'{'", "'}'", "'['", "']'", 
                     "';'", "':'", "'::'", "','", "'Class'", "'Val'", "'Var'", 
                     "<INVALID>", "'Array'", "'Int'", "'Float'", "'Boolean'", 
                     "'String'", "'Null'", "'Break'", "'Continue'", "'If'", 
                     "'Elseif'", "'Else'", "'Foreach'", "'Return'", "'self'", 
                     "'New'", "'Constructor'", "'Destructor'", "'In'", "'By'", 
                     "'.'", "'..'", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", 
                     "'&&'", "'||'", "'<='", "'>='", "'!='", "'='", "'=='", 
                     "'<'", "'>'", "'==.'", "'+.'" ]

    symbolicNames = [ "<INVALID>", "FLOAT_LITERAL", "INTEGER_LITERAL", "BOOLEAN_LITERAL", 
                      "STRING_LITERAL", "LB", "RB", "LP", "RP", "LSB", "RSB", 
                      "SEMI", "COL", "DCOL", "COM", "CLASS", "VAL", "VAR", 
                      "BLOCK_COMMENT", "ARRAY", "INT", "FLOAT", "BOOLEAN", 
                      "STRING", "NULL", "BREAK", "CONTINUE", "IF", "ELSEIF", 
                      "ELSE", "FOREACH", "RETURN", "SELF", "NEW", "CONSTRUCTOR", 
                      "DESTRUCTOR", "IN", "BY", "DOT", "DDOT", "OP_ADD", 
                      "OP_SUB", "OP_MUL", "OP_DIV", "OP_MOD", "OP_NOT", 
                      "OP_AND", "OP_OR", "OP_LTE", "OP_GTE", "OP_NEQ", "OP_AS", 
                      "OP_EQ", "OP_LT", "OP_GT", "OP_EQ_STR", "OP_ADD_STR", 
                      "IDEN", "DOL_IDEN", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "ERROR_CHAR" ]

    RULE_program = 0
    RULE_class_decl = 1
    RULE_mem_decl = 2
    RULE_attr_decl = 3
    RULE_method_decl = 4
    RULE_constr_decl = 5
    RULE_destr_decl = 6
    RULE_immutable_attr = 7
    RULE_mutable_attr = 8
    RULE_params_list = 9
    RULE_id_list_type = 10
    RULE_id_list = 11
    RULE_expr_list = 12
    RULE_iden_dol = 13
    RULE_block_stmt = 14
    RULE_block_items = 15
    RULE_assign_stmt = 16
    RULE_assign_lhs = 17
    RULE_lhs = 18
    RULE_data_type = 19
    RULE_if_stmt = 20
    RULE_return_stmt = 21
    RULE_break_stmt = 22
    RULE_continue_stmt = 23
    RULE_forin_stmt = 24
    RULE_expr = 25
    RULE_expr1 = 26
    RULE_expr2 = 27
    RULE_expr3 = 28
    RULE_expr4 = 29
    RULE_expr5 = 30
    RULE_expr6 = 31
    RULE_expr7 = 32
    RULE_expr8 = 33
    RULE_expr9 = 34
    RULE_expr10 = 35
    RULE_expr11 = 36
    RULE_operands = 37
    RULE_array_operator = 38
    RULE_field_access = 39
    RULE_method_invocation_stmt = 40
    RULE_method_invocation = 41
    RULE_array = 42
    RULE_muldi_arr = 43
    RULE_array_list = 44
    RULE_indx_arr = 45
    RULE_array_type = 46
    RULE_list_literal = 47
    RULE_literal = 48

    ruleNames =  [ "program", "class_decl", "mem_decl", "attr_decl", "method_decl", 
                   "constr_decl", "destr_decl", "immutable_attr", "mutable_attr", 
                   "params_list", "id_list_type", "id_list", "expr_list", 
                   "iden_dol", "block_stmt", "block_items", "assign_stmt", 
                   "assign_lhs", "lhs", "data_type", "if_stmt", "return_stmt", 
                   "break_stmt", "continue_stmt", "forin_stmt", "expr", 
                   "expr1", "expr2", "expr3", "expr4", "expr5", "expr6", 
                   "expr7", "expr8", "expr9", "expr10", "expr11", "operands", 
                   "array_operator", "field_access", "method_invocation_stmt", 
                   "method_invocation", "array", "muldi_arr", "array_list", 
                   "indx_arr", "array_type", "list_literal", "literal" ]

    EOF = Token.EOF
    FLOAT_LITERAL=1
    INTEGER_LITERAL=2
    BOOLEAN_LITERAL=3
    STRING_LITERAL=4
    LB=5
    RB=6
    LP=7
    RP=8
    LSB=9
    RSB=10
    SEMI=11
    COL=12
    DCOL=13
    COM=14
    CLASS=15
    VAL=16
    VAR=17
    BLOCK_COMMENT=18
    ARRAY=19
    INT=20
    FLOAT=21
    BOOLEAN=22
    STRING=23
    NULL=24
    BREAK=25
    CONTINUE=26
    IF=27
    ELSEIF=28
    ELSE=29
    FOREACH=30
    RETURN=31
    SELF=32
    NEW=33
    CONSTRUCTOR=34
    DESTRUCTOR=35
    IN=36
    BY=37
    DOT=38
    DDOT=39
    OP_ADD=40
    OP_SUB=41
    OP_MUL=42
    OP_DIV=43
    OP_MOD=44
    OP_NOT=45
    OP_AND=46
    OP_OR=47
    OP_LTE=48
    OP_GTE=49
    OP_NEQ=50
    OP_AS=51
    OP_EQ=52
    OP_LT=53
    OP_GT=54
    OP_EQ_STR=55
    OP_ADD_STR=56
    IDEN=57
    DOL_IDEN=58
    WS=59
    UNCLOSE_STRING=60
    ILLEGAL_ESCAPE=61
    ERROR_CHAR=62

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgramContext(ParserRuleContext):

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


        def getRuleIndex(self):
            return D96Parser.RULE_program




    def program(self):

        localctx = D96Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 98
                self.class_decl()
                self.state = 101 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==D96Parser.CLASS):
                    break

            self.state = 103
            self.match(D96Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Class_declContext(ParserRuleContext):

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

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def mem_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Mem_declContext)
            else:
                return self.getTypedRuleContext(D96Parser.Mem_declContext,i)


        def COL(self):
            return self.getToken(D96Parser.COL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_class_decl




    def class_decl(self):

        localctx = D96Parser.Class_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_class_decl)
        self._la = 0 # Token type
        try:
            self.state = 137
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 105
                self.match(D96Parser.CLASS)
                self.state = 106
                self.match(D96Parser.IDEN)
                self.state = 107
                self.match(D96Parser.LP)
                self.state = 108
                self.match(D96Parser.RP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 109
                self.match(D96Parser.CLASS)
                self.state = 110
                self.match(D96Parser.IDEN)
                self.state = 111
                self.match(D96Parser.LP)
                self.state = 113 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 112
                    self.mem_decl()
                    self.state = 115 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.VAL) | (1 << D96Parser.VAR) | (1 << D96Parser.CONSTRUCTOR) | (1 << D96Parser.DESTRUCTOR) | (1 << D96Parser.IDEN) | (1 << D96Parser.DOL_IDEN))) != 0)):
                        break

                self.state = 117
                self.match(D96Parser.RP)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 119
                self.match(D96Parser.CLASS)
                self.state = 120
                self.match(D96Parser.IDEN)
                self.state = 121
                self.match(D96Parser.COL)
                self.state = 122
                self.match(D96Parser.IDEN)
                self.state = 123
                self.match(D96Parser.LP)
                self.state = 124
                self.match(D96Parser.RP)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 125
                self.match(D96Parser.CLASS)
                self.state = 126
                self.match(D96Parser.IDEN)
                self.state = 127
                self.match(D96Parser.COL)
                self.state = 128
                self.match(D96Parser.IDEN)
                self.state = 129
                self.match(D96Parser.LP)
                self.state = 131 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 130
                    self.mem_decl()
                    self.state = 133 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.VAL) | (1 << D96Parser.VAR) | (1 << D96Parser.CONSTRUCTOR) | (1 << D96Parser.DESTRUCTOR) | (1 << D96Parser.IDEN) | (1 << D96Parser.DOL_IDEN))) != 0)):
                        break

                self.state = 135
                self.match(D96Parser.RP)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Mem_declContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attr_decl(self):
            return self.getTypedRuleContext(D96Parser.Attr_declContext,0)


        def method_decl(self):
            return self.getTypedRuleContext(D96Parser.Method_declContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_mem_decl




    def mem_decl(self):

        localctx = D96Parser.Mem_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_mem_decl)
        try:
            self.state = 141
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAL, D96Parser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 139
                self.attr_decl()
                pass
            elif token in [D96Parser.CONSTRUCTOR, D96Parser.DESTRUCTOR, D96Parser.IDEN, D96Parser.DOL_IDEN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 140
                self.method_decl()
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

    class Attr_declContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def immutable_attr(self):
            return self.getTypedRuleContext(D96Parser.Immutable_attrContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def mutable_attr(self):
            return self.getTypedRuleContext(D96Parser.Mutable_attrContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_attr_decl




    def attr_decl(self):

        localctx = D96Parser.Attr_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_attr_decl)
        try:
            self.state = 149
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 143
                self.immutable_attr()
                self.state = 144
                self.match(D96Parser.SEMI)
                pass
            elif token in [D96Parser.VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 146
                self.mutable_attr()
                self.state = 147
                self.match(D96Parser.SEMI)
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

    class Method_declContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def constr_decl(self):
            return self.getTypedRuleContext(D96Parser.Constr_declContext,0)


        def destr_decl(self):
            return self.getTypedRuleContext(D96Parser.Destr_declContext,0)


        def iden_dol(self):
            return self.getTypedRuleContext(D96Parser.Iden_dolContext,0)


        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def params_list(self):
            return self.getTypedRuleContext(D96Parser.Params_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_method_decl




    def method_decl(self):

        localctx = D96Parser.Method_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_method_decl)
        try:
            self.state = 164
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 151
                self.constr_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 152
                self.destr_decl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 153
                self.iden_dol()
                self.state = 154
                self.match(D96Parser.LB)
                self.state = 155
                self.match(D96Parser.RB)
                self.state = 156
                self.block_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 158
                self.iden_dol()
                self.state = 159
                self.match(D96Parser.LB)
                self.state = 160
                self.params_list()
                self.state = 161
                self.match(D96Parser.RB)
                self.state = 162
                self.block_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Constr_declContext(ParserRuleContext):

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


        def params_list(self):
            return self.getTypedRuleContext(D96Parser.Params_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_constr_decl




    def constr_decl(self):

        localctx = D96Parser.Constr_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_constr_decl)
        try:
            self.state = 176
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 166
                self.match(D96Parser.CONSTRUCTOR)
                self.state = 167
                self.match(D96Parser.LB)
                self.state = 168
                self.match(D96Parser.RB)
                self.state = 169
                self.block_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 170
                self.match(D96Parser.CONSTRUCTOR)
                self.state = 171
                self.match(D96Parser.LB)
                self.state = 172
                self.params_list()
                self.state = 173
                self.match(D96Parser.RB)
                self.state = 174
                self.block_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Destr_declContext(ParserRuleContext):

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




    def destr_decl(self):

        localctx = D96Parser.Destr_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_destr_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.match(D96Parser.DESTRUCTOR)
            self.state = 179
            self.match(D96Parser.LB)
            self.state = 180
            self.match(D96Parser.RB)
            self.state = 181
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Immutable_attrContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def id_list_type(self):
            return self.getTypedRuleContext(D96Parser.Id_list_typeContext,0)


        def OP_AS(self):
            return self.getToken(D96Parser.OP_AS, 0)

        def expr_list(self):
            return self.getTypedRuleContext(D96Parser.Expr_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_immutable_attr




    def immutable_attr(self):

        localctx = D96Parser.Immutable_attrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_immutable_attr)
        try:
            self.state = 190
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 183
                self.match(D96Parser.VAL)
                self.state = 184
                self.id_list_type()
                self.state = 185
                self.match(D96Parser.OP_AS)
                self.state = 186
                self.expr_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 188
                self.match(D96Parser.VAL)
                self.state = 189
                self.id_list_type()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Mutable_attrContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def id_list_type(self):
            return self.getTypedRuleContext(D96Parser.Id_list_typeContext,0)


        def OP_AS(self):
            return self.getToken(D96Parser.OP_AS, 0)

        def expr_list(self):
            return self.getTypedRuleContext(D96Parser.Expr_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_mutable_attr




    def mutable_attr(self):

        localctx = D96Parser.Mutable_attrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_mutable_attr)
        try:
            self.state = 199
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 192
                self.match(D96Parser.VAR)
                self.state = 193
                self.id_list_type()
                self.state = 194
                self.match(D96Parser.OP_AS)
                self.state = 195
                self.expr_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 197
                self.match(D96Parser.VAR)
                self.state = 198
                self.id_list_type()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Params_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_list_type(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Id_list_typeContext)
            else:
                return self.getTypedRuleContext(D96Parser.Id_list_typeContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.SEMI)
            else:
                return self.getToken(D96Parser.SEMI, i)

        def getRuleIndex(self):
            return D96Parser.RULE_params_list




    def params_list(self):

        localctx = D96Parser.Params_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_params_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self.id_list_type()
            self.state = 206
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.SEMI:
                self.state = 202
                self.match(D96Parser.SEMI)
                self.state = 203
                self.id_list_type()
                self.state = 208
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Id_list_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_list(self):
            return self.getTypedRuleContext(D96Parser.Id_listContext,0)


        def COL(self):
            return self.getToken(D96Parser.COL, 0)

        def data_type(self):
            return self.getTypedRuleContext(D96Parser.Data_typeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_id_list_type




    def id_list_type(self):

        localctx = D96Parser.Id_list_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_id_list_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.id_list()
            self.state = 210
            self.match(D96Parser.COL)
            self.state = 211
            self.data_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Id_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def iden_dol(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Iden_dolContext)
            else:
                return self.getTypedRuleContext(D96Parser.Iden_dolContext,i)


        def COM(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COM)
            else:
                return self.getToken(D96Parser.COM, i)

        def getRuleIndex(self):
            return D96Parser.RULE_id_list




    def id_list(self):

        localctx = D96Parser.Id_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_id_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.iden_dol()
            self.state = 218
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COM:
                self.state = 214
                self.match(D96Parser.COM)
                self.state = 215
                self.iden_dol()
                self.state = 220
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Expr_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

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

        def getRuleIndex(self):
            return D96Parser.RULE_expr_list




    def expr_list(self):

        localctx = D96Parser.Expr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_expr_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.expr(0)
            self.state = 226
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COM:
                self.state = 222
                self.match(D96Parser.COM)
                self.state = 223
                self.expr(0)
                self.state = 228
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Iden_dolContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDEN(self):
            return self.getToken(D96Parser.IDEN, 0)

        def DOL_IDEN(self):
            return self.getToken(D96Parser.DOL_IDEN, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_iden_dol




    def iden_dol(self):

        localctx = D96Parser.Iden_dolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_iden_dol)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
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

    class Block_stmtContext(ParserRuleContext):

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




    def block_stmt(self):

        localctx = D96Parser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_block_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self.match(D96Parser.LP)
            self.state = 236
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.LB) | (1 << D96Parser.LP) | (1 << D96Parser.VAL) | (1 << D96Parser.VAR) | (1 << D96Parser.ARRAY) | (1 << D96Parser.BREAK) | (1 << D96Parser.CONTINUE) | (1 << D96Parser.IF) | (1 << D96Parser.FOREACH) | (1 << D96Parser.RETURN) | (1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.OP_SUB) | (1 << D96Parser.OP_NOT) | (1 << D96Parser.IDEN))) != 0):
                self.state = 234
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.FLOAT_LITERAL, D96Parser.INTEGER_LITERAL, D96Parser.BOOLEAN_LITERAL, D96Parser.STRING_LITERAL, D96Parser.LB, D96Parser.VAL, D96Parser.VAR, D96Parser.ARRAY, D96Parser.BREAK, D96Parser.CONTINUE, D96Parser.IF, D96Parser.FOREACH, D96Parser.RETURN, D96Parser.SELF, D96Parser.NEW, D96Parser.OP_SUB, D96Parser.OP_NOT, D96Parser.IDEN]:
                    self.state = 232
                    self.block_items()
                    pass
                elif token in [D96Parser.LP]:
                    self.state = 233
                    self.block_stmt()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 238
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 239
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Block_itemsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_stmt(self):
            return self.getTypedRuleContext(D96Parser.Assign_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(D96Parser.If_stmtContext,0)


        def attr_decl(self):
            return self.getTypedRuleContext(D96Parser.Attr_declContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(D96Parser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(D96Parser.Continue_stmtContext,0)


        def forin_stmt(self):
            return self.getTypedRuleContext(D96Parser.Forin_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(D96Parser.Return_stmtContext,0)


        def method_invocation_stmt(self):
            return self.getTypedRuleContext(D96Parser.Method_invocation_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_block_items




    def block_items(self):

        localctx = D96Parser.Block_itemsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_block_items)
        try:
            self.state = 249
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 241
                self.assign_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 242
                self.if_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 243
                self.attr_decl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 244
                self.break_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 245
                self.continue_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 246
                self.forin_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 247
                self.return_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 248
                self.method_invocation_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Assign_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_lhs(self):
            return self.getTypedRuleContext(D96Parser.Assign_lhsContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_assign_stmt




    def assign_stmt(self):

        localctx = D96Parser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self.assign_lhs()
            self.state = 252
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Assign_lhsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(D96Parser.LhsContext,0)


        def OP_AS(self):
            return self.getToken(D96Parser.OP_AS, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_assign_lhs




    def assign_lhs(self):

        localctx = D96Parser.Assign_lhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_assign_lhs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.lhs()
            self.state = 255
            self.match(D96Parser.OP_AS)
            self.state = 256
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LhsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDEN(self):
            return self.getToken(D96Parser.IDEN, 0)

        def array_operator(self):
            return self.getTypedRuleContext(D96Parser.Array_operatorContext,0)


        def field_access(self):
            return self.getTypedRuleContext(D96Parser.Field_accessContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_lhs




    def lhs(self):

        localctx = D96Parser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_lhs)
        try:
            self.state = 261
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 258
                self.match(D96Parser.IDEN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 259
                self.array_operator()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 260
                self.field_access()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Data_typeContext(ParserRuleContext):

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

        def array_type(self):
            return self.getTypedRuleContext(D96Parser.Array_typeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_data_type




    def data_type(self):

        localctx = D96Parser.Data_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_data_type)
        try:
            self.state = 268
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 263
                self.match(D96Parser.INT)
                pass
            elif token in [D96Parser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 264
                self.match(D96Parser.FLOAT)
                pass
            elif token in [D96Parser.STRING]:
                self.enterOuterAlt(localctx, 3)
                self.state = 265
                self.match(D96Parser.STRING)
                pass
            elif token in [D96Parser.BOOLEAN]:
                self.enterOuterAlt(localctx, 4)
                self.state = 266
                self.match(D96Parser.BOOLEAN)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 5)
                self.state = 267
                self.array_type()
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

    class If_stmtContext(ParserRuleContext):

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




    def if_stmt(self):

        localctx = D96Parser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self.match(D96Parser.IF)
            self.state = 271
            self.match(D96Parser.LB)
            self.state = 272
            self.expr(0)
            self.state = 273
            self.match(D96Parser.RB)
            self.state = 274
            self.block_stmt()
            self.state = 283
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.ELSEIF:
                self.state = 275
                self.match(D96Parser.ELSEIF)
                self.state = 276
                self.match(D96Parser.LB)
                self.state = 277
                self.expr(0)
                self.state = 278
                self.match(D96Parser.RB)
                self.state = 279
                self.block_stmt()
                self.state = 285
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 288
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ELSE:
                self.state = 286
                self.match(D96Parser.ELSE)
                self.state = 287
                self.block_stmt()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Return_stmtContext(ParserRuleContext):

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




    def return_stmt(self):

        localctx = D96Parser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 290
            self.match(D96Parser.RETURN)
            self.state = 292
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.LB) | (1 << D96Parser.ARRAY) | (1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.OP_SUB) | (1 << D96Parser.OP_NOT) | (1 << D96Parser.IDEN))) != 0):
                self.state = 291
                self.expr(0)


            self.state = 294
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Break_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(D96Parser.BREAK, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_break_stmt




    def break_stmt(self):

        localctx = D96Parser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296
            self.match(D96Parser.BREAK)
            self.state = 297
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Continue_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(D96Parser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_continue_stmt




    def continue_stmt(self):

        localctx = D96Parser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            self.match(D96Parser.CONTINUE)
            self.state = 300
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Forin_stmtContext(ParserRuleContext):

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




    def forin_stmt(self):

        localctx = D96Parser.Forin_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_forin_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            self.match(D96Parser.FOREACH)
            self.state = 303
            self.match(D96Parser.LB)
            self.state = 304
            self.match(D96Parser.IDEN)
            self.state = 305
            self.match(D96Parser.IN)
            self.state = 306
            self.match(D96Parser.INTEGER_LITERAL)
            self.state = 307
            self.match(D96Parser.DDOT)
            self.state = 308
            self.match(D96Parser.INTEGER_LITERAL)
            self.state = 311
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.BY:
                self.state = 309
                self.match(D96Parser.BY)
                self.state = 310
                self.match(D96Parser.INTEGER_LITERAL)


            self.state = 313
            self.match(D96Parser.RB)
            self.state = 314
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self):
            return self.getTypedRuleContext(D96Parser.Expr1Context,0)


        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def OP_EQ_STR(self):
            return self.getToken(D96Parser.OP_EQ_STR, 0)

        def OP_ADD_STR(self):
            return self.getToken(D96Parser.OP_ADD_STR, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 50
        self.enterRecursionRule(localctx, 50, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 317
            self.expr1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 324
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 319
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 320
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.OP_EQ_STR or _la==D96Parser.OP_ADD_STR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 321
                    self.expr1(0) 
                self.state = 326
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Expr1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self):
            return self.getTypedRuleContext(D96Parser.Expr2Context,0)


        def expr1(self):
            return self.getTypedRuleContext(D96Parser.Expr1Context,0)


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

        def getRuleIndex(self):
            return D96Parser.RULE_expr1



    def expr1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_expr1, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 328
            self.expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 335
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                    self.state = 330
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 331
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.OP_LTE) | (1 << D96Parser.OP_GTE) | (1 << D96Parser.OP_NEQ) | (1 << D96Parser.OP_EQ) | (1 << D96Parser.OP_LT) | (1 << D96Parser.OP_GT))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 332
                    self.expr2(0) 
                self.state = 337
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Expr2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(D96Parser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(D96Parser.Expr2Context,0)


        def OP_AND(self):
            return self.getToken(D96Parser.OP_AND, 0)

        def OP_OR(self):
            return self.getToken(D96Parser.OP_OR, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr2



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 339
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 346
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 341
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 342
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.OP_AND or _la==D96Parser.OP_OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 343
                    self.expr3(0) 
                self.state = 348
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Expr3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(D96Parser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(D96Parser.Expr3Context,0)


        def OP_ADD(self):
            return self.getToken(D96Parser.OP_ADD, 0)

        def OP_SUB(self):
            return self.getToken(D96Parser.OP_SUB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr3



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 56
        self.enterRecursionRule(localctx, 56, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 350
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 357
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 352
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 353
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.OP_ADD or _la==D96Parser.OP_SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 354
                    self.expr4(0) 
                self.state = 359
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Expr4Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(D96Parser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(D96Parser.Expr4Context,0)


        def OP_MUL(self):
            return self.getToken(D96Parser.OP_MUL, 0)

        def OP_DIV(self):
            return self.getToken(D96Parser.OP_DIV, 0)

        def OP_MOD(self):
            return self.getToken(D96Parser.OP_MOD, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr4



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 58
        self.enterRecursionRule(localctx, 58, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 361
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 368
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 363
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 364
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.OP_MUL) | (1 << D96Parser.OP_DIV) | (1 << D96Parser.OP_MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 365
                    self.expr5() 
                self.state = 370
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Expr5Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_NOT(self):
            return self.getToken(D96Parser.OP_NOT, 0)

        def expr5(self):
            return self.getTypedRuleContext(D96Parser.Expr5Context,0)


        def expr6(self):
            return self.getTypedRuleContext(D96Parser.Expr6Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr5




    def expr5(self):

        localctx = D96Parser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_expr5)
        try:
            self.state = 374
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.OP_NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 371
                self.match(D96Parser.OP_NOT)
                self.state = 372
                self.expr5()
                pass
            elif token in [D96Parser.FLOAT_LITERAL, D96Parser.INTEGER_LITERAL, D96Parser.BOOLEAN_LITERAL, D96Parser.STRING_LITERAL, D96Parser.LB, D96Parser.ARRAY, D96Parser.SELF, D96Parser.NEW, D96Parser.OP_SUB, D96Parser.IDEN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 373
                self.expr6()
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

    class Expr6Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_SUB(self):
            return self.getToken(D96Parser.OP_SUB, 0)

        def expr6(self):
            return self.getTypedRuleContext(D96Parser.Expr6Context,0)


        def expr7(self):
            return self.getTypedRuleContext(D96Parser.Expr7Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr6




    def expr6(self):

        localctx = D96Parser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_expr6)
        try:
            self.state = 379
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.OP_SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 376
                self.match(D96Parser.OP_SUB)
                self.state = 377
                self.expr6()
                pass
            elif token in [D96Parser.FLOAT_LITERAL, D96Parser.INTEGER_LITERAL, D96Parser.BOOLEAN_LITERAL, D96Parser.STRING_LITERAL, D96Parser.LB, D96Parser.ARRAY, D96Parser.SELF, D96Parser.NEW, D96Parser.IDEN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 378
                self.expr7()
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

    class Expr7Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr8(self):
            return self.getTypedRuleContext(D96Parser.Expr8Context,0)


        def LSB(self):
            return self.getToken(D96Parser.LSB, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def RSB(self):
            return self.getToken(D96Parser.RSB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr7




    def expr7(self):

        localctx = D96Parser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_expr7)
        try:
            self.state = 387
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 381
                self.expr8(0)
                self.state = 382
                self.match(D96Parser.LSB)
                self.state = 383
                self.expr(0)
                self.state = 384
                self.match(D96Parser.RSB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 386
                self.expr8(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Expr8Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr9(self):
            return self.getTypedRuleContext(D96Parser.Expr9Context,0)


        def expr8(self):
            return self.getTypedRuleContext(D96Parser.Expr8Context,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def IDEN(self):
            return self.getToken(D96Parser.IDEN, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def expr_list(self):
            return self.getTypedRuleContext(D96Parser.Expr_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr8



    def expr8(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr8Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 66
        self.enterRecursionRule(localctx, 66, self.RULE_expr8, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 390
            self.expr9(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 409
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 407
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Expr8Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr8)
                        self.state = 392
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 393
                        self.match(D96Parser.DOT)
                        self.state = 394
                        self.match(D96Parser.IDEN)
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Expr8Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr8)
                        self.state = 395
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 396
                        self.match(D96Parser.DOT)
                        self.state = 397
                        self.match(D96Parser.IDEN)
                        self.state = 398
                        self.match(D96Parser.LB)
                        self.state = 399
                        self.match(D96Parser.RB)
                        pass

                    elif la_ == 3:
                        localctx = D96Parser.Expr8Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr8)
                        self.state = 400
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 401
                        self.match(D96Parser.DOT)
                        self.state = 402
                        self.match(D96Parser.IDEN)
                        self.state = 403
                        self.match(D96Parser.LB)
                        self.state = 404
                        self.expr_list()
                        self.state = 405
                        self.match(D96Parser.RB)
                        pass

             
                self.state = 411
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Expr9Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr10(self):
            return self.getTypedRuleContext(D96Parser.Expr10Context,0)


        def expr9(self):
            return self.getTypedRuleContext(D96Parser.Expr9Context,0)


        def DCOL(self):
            return self.getToken(D96Parser.DCOL, 0)

        def DOL_IDEN(self):
            return self.getToken(D96Parser.DOL_IDEN, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def expr_list(self):
            return self.getTypedRuleContext(D96Parser.Expr_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr9



    def expr9(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr9Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_expr9, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 413
            self.expr10()
            self._ctx.stop = self._input.LT(-1)
            self.state = 432
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 430
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Expr9Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr9)
                        self.state = 415
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 416
                        self.match(D96Parser.DCOL)
                        self.state = 417
                        self.match(D96Parser.DOL_IDEN)
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Expr9Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr9)
                        self.state = 418
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 419
                        self.match(D96Parser.DCOL)
                        self.state = 420
                        self.match(D96Parser.DOL_IDEN)
                        self.state = 421
                        self.match(D96Parser.LB)
                        self.state = 422
                        self.match(D96Parser.RB)
                        pass

                    elif la_ == 3:
                        localctx = D96Parser.Expr9Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr9)
                        self.state = 423
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 424
                        self.match(D96Parser.DCOL)
                        self.state = 425
                        self.match(D96Parser.DOL_IDEN)
                        self.state = 426
                        self.match(D96Parser.LB)
                        self.state = 427
                        self.expr_list()
                        self.state = 428
                        self.match(D96Parser.RB)
                        pass

             
                self.state = 434
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Expr10Context(ParserRuleContext):

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

        def expr_list(self):
            return self.getTypedRuleContext(D96Parser.Expr_listContext,0)


        def expr11(self):
            return self.getTypedRuleContext(D96Parser.Expr11Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr10




    def expr10(self):

        localctx = D96Parser.Expr10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_expr10)
        try:
            self.state = 446
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 435
                self.match(D96Parser.NEW)
                self.state = 436
                self.match(D96Parser.IDEN)
                self.state = 437
                self.match(D96Parser.LB)
                self.state = 438
                self.match(D96Parser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 439
                self.match(D96Parser.NEW)
                self.state = 440
                self.match(D96Parser.IDEN)
                self.state = 441
                self.match(D96Parser.LB)
                self.state = 442
                self.expr_list()
                self.state = 443
                self.match(D96Parser.RB)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 445
                self.expr11()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Expr11Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def operands(self):
            return self.getTypedRuleContext(D96Parser.OperandsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr11




    def expr11(self):

        localctx = D96Parser.Expr11Context(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_expr11)
        try:
            self.state = 453
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.LB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 448
                self.match(D96Parser.LB)
                self.state = 449
                self.expr(0)
                self.state = 450
                self.match(D96Parser.RB)
                pass
            elif token in [D96Parser.FLOAT_LITERAL, D96Parser.INTEGER_LITERAL, D96Parser.BOOLEAN_LITERAL, D96Parser.STRING_LITERAL, D96Parser.ARRAY, D96Parser.SELF, D96Parser.IDEN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 452
                self.operands()
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

    class OperandsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDEN(self):
            return self.getToken(D96Parser.IDEN, 0)

        def literal(self):
            return self.getTypedRuleContext(D96Parser.LiteralContext,0)


        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def DCOL(self):
            return self.getToken(D96Parser.DCOL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_operands




    def operands(self):

        localctx = D96Parser.OperandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_operands)
        try:
            self.state = 463
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 455
                self.match(D96Parser.IDEN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 456
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 457
                self.match(D96Parser.SELF)
                self.state = 458
                self.match(D96Parser.DOT)
                self.state = 459
                self.match(D96Parser.IDEN)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 460
                self.match(D96Parser.SELF)
                self.state = 461
                self.match(D96Parser.DCOL)
                self.state = 462
                self.match(D96Parser.IDEN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Array_operatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr8(self):
            return self.getTypedRuleContext(D96Parser.Expr8Context,0)


        def LSB(self):
            return self.getToken(D96Parser.LSB, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def RSB(self):
            return self.getToken(D96Parser.RSB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_array_operator




    def array_operator(self):

        localctx = D96Parser.Array_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_array_operator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 465
            self.expr8(0)
            self.state = 466
            self.match(D96Parser.LSB)
            self.state = 467
            self.expr(0)
            self.state = 468
            self.match(D96Parser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Field_accessContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def IDEN(self):
            return self.getToken(D96Parser.IDEN, 0)

        def DCOL(self):
            return self.getToken(D96Parser.DCOL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_field_access




    def field_access(self):

        localctx = D96Parser.Field_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_field_access)
        try:
            self.state = 478
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 470
                self.expr(0)
                self.state = 471
                self.match(D96Parser.DOT)
                self.state = 472
                self.match(D96Parser.IDEN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 474
                self.expr(0)
                self.state = 475
                self.match(D96Parser.DCOL)
                self.state = 476
                self.match(D96Parser.IDEN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Method_invocation_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def method_invocation(self):
            return self.getTypedRuleContext(D96Parser.Method_invocationContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_method_invocation_stmt




    def method_invocation_stmt(self):

        localctx = D96Parser.Method_invocation_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_method_invocation_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 480
            self.method_invocation()
            self.state = 481
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Method_invocationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def IDEN(self):
            return self.getToken(D96Parser.IDEN, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def expr_list(self):
            return self.getTypedRuleContext(D96Parser.Expr_listContext,0)


        def DCOL(self):
            return self.getToken(D96Parser.DCOL, 0)

        def DOL_IDEN(self):
            return self.getToken(D96Parser.DOL_IDEN, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_method_invocation




    def method_invocation(self):

        localctx = D96Parser.Method_invocationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_method_invocation)
        try:
            self.state = 509
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 483
                self.expr(0)
                self.state = 484
                self.match(D96Parser.DOT)
                self.state = 485
                self.match(D96Parser.IDEN)
                self.state = 486
                self.match(D96Parser.LB)
                self.state = 487
                self.match(D96Parser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 489
                self.expr(0)
                self.state = 490
                self.match(D96Parser.DOT)
                self.state = 491
                self.match(D96Parser.IDEN)
                self.state = 492
                self.match(D96Parser.LB)
                self.state = 493
                self.expr_list()
                self.state = 494
                self.match(D96Parser.RB)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 496
                self.expr(0)
                self.state = 497
                self.match(D96Parser.DCOL)
                self.state = 498
                self.match(D96Parser.DOL_IDEN)
                self.state = 499
                self.match(D96Parser.LB)
                self.state = 500
                self.match(D96Parser.RB)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 502
                self.expr(0)
                self.state = 503
                self.match(D96Parser.DCOL)
                self.state = 504
                self.match(D96Parser.DOL_IDEN)
                self.state = 505
                self.match(D96Parser.LB)
                self.state = 506
                self.expr_list()
                self.state = 507
                self.match(D96Parser.RB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArrayContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def muldi_arr(self):
            return self.getTypedRuleContext(D96Parser.Muldi_arrContext,0)


        def indx_arr(self):
            return self.getTypedRuleContext(D96Parser.Indx_arrContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_array




    def array(self):

        localctx = D96Parser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_array)
        try:
            self.state = 513
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 511
                self.muldi_arr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 512
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def array_list(self):
            return self.getTypedRuleContext(D96Parser.Array_listContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_muldi_arr




    def muldi_arr(self):

        localctx = D96Parser.Muldi_arrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_muldi_arr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 515
            self.match(D96Parser.ARRAY)
            self.state = 516
            self.match(D96Parser.LB)
            self.state = 517
            self.array_list()
            self.state = 518
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Array_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def indx_arr(self):
            return self.getTypedRuleContext(D96Parser.Indx_arrContext,0)


        def COM(self):
            return self.getToken(D96Parser.COM, 0)

        def array_list(self):
            return self.getTypedRuleContext(D96Parser.Array_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_array_list




    def array_list(self):

        localctx = D96Parser.Array_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_array_list)
        try:
            self.state = 525
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 520
                self.indx_arr()
                self.state = 521
                self.match(D96Parser.COM)
                self.state = 522
                self.array_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 524
                self.indx_arr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Indx_arrContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def expr_list(self):
            return self.getTypedRuleContext(D96Parser.Expr_listContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_indx_arr




    def indx_arr(self):

        localctx = D96Parser.Indx_arrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_indx_arr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 527
            self.match(D96Parser.ARRAY)
            self.state = 528
            self.match(D96Parser.LB)
            self.state = 529
            self.expr_list()
            self.state = 530
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Array_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LSB(self):
            return self.getToken(D96Parser.LSB, 0)

        def data_type(self):
            return self.getTypedRuleContext(D96Parser.Data_typeContext,0)


        def COM(self):
            return self.getToken(D96Parser.COM, 0)

        def literal(self):
            return self.getTypedRuleContext(D96Parser.LiteralContext,0)


        def RSB(self):
            return self.getToken(D96Parser.RSB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_array_type




    def array_type(self):

        localctx = D96Parser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 532
            self.match(D96Parser.ARRAY)
            self.state = 533
            self.match(D96Parser.LSB)
            self.state = 534
            self.data_type()
            self.state = 535
            self.match(D96Parser.COM)
            self.state = 536
            self.literal()
            self.state = 537
            self.match(D96Parser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class List_literalContext(ParserRuleContext):

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




    def list_literal(self):

        localctx = D96Parser.List_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_list_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 544
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,41,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 539
                    self.literal()
                    self.state = 540
                    self.match(D96Parser.COM) 
                self.state = 546
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,41,self._ctx)

            self.state = 547
            self.literal()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER_LITERAL(self):
            return self.getToken(D96Parser.INTEGER_LITERAL, 0)

        def FLOAT_LITERAL(self):
            return self.getToken(D96Parser.FLOAT_LITERAL, 0)

        def BOOLEAN_LITERAL(self):
            return self.getToken(D96Parser.BOOLEAN_LITERAL, 0)

        def STRING_LITERAL(self):
            return self.getToken(D96Parser.STRING_LITERAL, 0)

        def array(self):
            return self.getTypedRuleContext(D96Parser.ArrayContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_literal




    def literal(self):

        localctx = D96Parser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_literal)
        try:
            self.state = 554
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INTEGER_LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 549
                self.match(D96Parser.INTEGER_LITERAL)
                pass
            elif token in [D96Parser.FLOAT_LITERAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 550
                self.match(D96Parser.FLOAT_LITERAL)
                pass
            elif token in [D96Parser.BOOLEAN_LITERAL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 551
                self.match(D96Parser.BOOLEAN_LITERAL)
                pass
            elif token in [D96Parser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 552
                self.match(D96Parser.STRING_LITERAL)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 5)
                self.state = 553
                self.array()
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[25] = self.expr_sempred
        self._predicates[26] = self.expr1_sempred
        self._predicates[27] = self.expr2_sempred
        self._predicates[28] = self.expr3_sempred
        self._predicates[29] = self.expr4_sempred
        self._predicates[33] = self.expr8_sempred
        self._predicates[34] = self.expr9_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr1_sempred(self, localctx:Expr1Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def expr8_sempred(self, localctx:Expr8Context, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 2)
         

    def expr9_sempred(self, localctx:Expr9Context, predIndex:int):
            if predIndex == 8:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 2)
         




