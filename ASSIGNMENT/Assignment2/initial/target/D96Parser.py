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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3@")
        buf.write("\u022b\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\3\2\6\2h")
        buf.write("\n\2\r\2\16\2i\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\6\3v\n\3\r\3\16\3w\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\6\3\u0088\n\3\r\3\16\3\u0089\3")
        buf.write("\3\3\3\5\3\u008e\n\3\3\4\3\4\5\4\u0092\n\4\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\5\5\u009a\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u00a9\n\6\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u00b5\n\7\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\t\u00c3\n\t\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\n\5\n\u00cc\n\n\3\13\3\13\3\13\7\13")
        buf.write("\u00d1\n\13\f\13\16\13\u00d4\13\13\3\f\3\f\3\f\3\f\3\r")
        buf.write("\3\r\3\r\7\r\u00dd\n\r\f\r\16\r\u00e0\13\r\3\16\3\16\3")
        buf.write("\16\7\16\u00e5\n\16\f\16\16\16\u00e8\13\16\3\17\3\17\3")
        buf.write("\20\3\20\3\20\7\20\u00ef\n\20\f\20\16\20\u00f2\13\20\3")
        buf.write("\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\5\21")
        buf.write("\u00fe\n\21\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\24\3")
        buf.write("\24\3\24\5\24\u010a\n\24\3\25\3\25\3\25\3\25\3\25\5\25")
        buf.write("\u0111\n\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3")
        buf.write("\26\3\26\3\26\7\26\u011e\n\26\f\26\16\26\u0121\13\26\3")
        buf.write("\26\3\26\5\26\u0125\n\26\3\27\3\27\5\27\u0129\n\27\3\27")
        buf.write("\3\27\3\30\3\30\3\30\3\31\3\31\3\31\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\5\32\u013c\n\32\3\32\3\32\3")
        buf.write("\32\3\33\3\33\3\33\3\33\3\33\5\33\u0146\n\33\3\34\3\34")
        buf.write("\3\34\3\34\3\34\5\34\u014d\n\34\3\35\3\35\3\35\3\35\3")
        buf.write("\35\3\35\7\35\u0155\n\35\f\35\16\35\u0158\13\35\3\36\3")
        buf.write("\36\3\36\3\36\3\36\3\36\7\36\u0160\n\36\f\36\16\36\u0163")
        buf.write("\13\36\3\37\3\37\3\37\3\37\3\37\3\37\7\37\u016b\n\37\f")
        buf.write("\37\16\37\u016e\13\37\3 \3 \3 \5 \u0173\n \3!\3!\3!\5")
        buf.write("!\u0178\n!\3\"\3\"\3\"\3\"\5\"\u017e\n\"\3#\3#\3#\3#\3")
        buf.write("#\3#\3#\3#\3#\5#\u0189\n#\3$\3$\3$\3$\3$\3$\3$\3$\3$\3")
        buf.write("$\3$\3$\3$\3$\3$\3$\3$\3$\7$\u019d\n$\f$\16$\u01a0\13")
        buf.write("$\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3")
        buf.write("%\5%\u01b4\n%\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\5&\u01c1")
        buf.write("\n&\3\'\3\'\3\'\3\'\3\'\5\'\u01c8\n\'\3(\3(\3(\3(\5(\u01ce")
        buf.write("\n(\3)\3)\3)\7)\u01d3\n)\f)\16)\u01d6\13)\3)\3)\3*\3*")
        buf.write("\3*\3*\3*\5*\u01df\n*\3+\3+\3+\3+\3+\3,\3,\3,\3,\3,\3")
        buf.write(",\3,\3,\5,\u01ee\n,\3-\3-\3-\3.\3.\3.\3.\3.\3.\3.\3.\3")
        buf.write(".\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\5")
        buf.write(".\u020d\n.\3/\3/\5/\u0211\n/\3\60\3\60\3\60\3\60\3\60")
        buf.write("\3\61\3\61\3\61\3\61\3\61\5\61\u021d\n\61\3\62\3\62\3")
        buf.write("\62\3\62\3\62\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63")
        buf.write("\2\68:<F\64\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"")
        buf.write("$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bd\2\b\3\2;<\3")
        buf.write("\29:\4\2\62\64\668\3\2\60\61\3\2*+\3\2,.\2\u023c\2g\3")
        buf.write("\2\2\2\4\u008d\3\2\2\2\6\u0091\3\2\2\2\b\u0099\3\2\2\2")
        buf.write("\n\u00a8\3\2\2\2\f\u00b4\3\2\2\2\16\u00b6\3\2\2\2\20\u00c2")
        buf.write("\3\2\2\2\22\u00cb\3\2\2\2\24\u00cd\3\2\2\2\26\u00d5\3")
        buf.write("\2\2\2\30\u00d9\3\2\2\2\32\u00e1\3\2\2\2\34\u00e9\3\2")
        buf.write("\2\2\36\u00eb\3\2\2\2 \u00fd\3\2\2\2\"\u00ff\3\2\2\2$")
        buf.write("\u0102\3\2\2\2&\u0109\3\2\2\2(\u0110\3\2\2\2*\u0112\3")
        buf.write("\2\2\2,\u0126\3\2\2\2.\u012c\3\2\2\2\60\u012f\3\2\2\2")
        buf.write("\62\u0132\3\2\2\2\64\u0145\3\2\2\2\66\u014c\3\2\2\28\u014e")
        buf.write("\3\2\2\2:\u0159\3\2\2\2<\u0164\3\2\2\2>\u0172\3\2\2\2")
        buf.write("@\u0177\3\2\2\2B\u017d\3\2\2\2D\u0188\3\2\2\2F\u018a\3")
        buf.write("\2\2\2H\u01b3\3\2\2\2J\u01c0\3\2\2\2L\u01c7\3\2\2\2N\u01cd")
        buf.write("\3\2\2\2P\u01d4\3\2\2\2R\u01de\3\2\2\2T\u01e0\3\2\2\2")
        buf.write("V\u01ed\3\2\2\2X\u01ef\3\2\2\2Z\u020c\3\2\2\2\\\u0210")
        buf.write("\3\2\2\2^\u0212\3\2\2\2`\u021c\3\2\2\2b\u021e\3\2\2\2")
        buf.write("d\u0223\3\2\2\2fh\5\4\3\2gf\3\2\2\2hi\3\2\2\2ig\3\2\2")
        buf.write("\2ij\3\2\2\2jk\3\2\2\2kl\7\2\2\3l\3\3\2\2\2mn\7\21\2\2")
        buf.write("no\7;\2\2op\7\t\2\2p\u008e\7\n\2\2qr\7\21\2\2rs\7;\2\2")
        buf.write("su\7\t\2\2tv\5\6\4\2ut\3\2\2\2vw\3\2\2\2wu\3\2\2\2wx\3")
        buf.write("\2\2\2xy\3\2\2\2yz\7\n\2\2z\u008e\3\2\2\2{|\7\21\2\2|")
        buf.write("}\7;\2\2}~\7\16\2\2~\177\7;\2\2\177\u0080\7\t\2\2\u0080")
        buf.write("\u008e\7\n\2\2\u0081\u0082\7\21\2\2\u0082\u0083\7;\2\2")
        buf.write("\u0083\u0084\7\16\2\2\u0084\u0085\7;\2\2\u0085\u0087\7")
        buf.write("\t\2\2\u0086\u0088\5\6\4\2\u0087\u0086\3\2\2\2\u0088\u0089")
        buf.write("\3\2\2\2\u0089\u0087\3\2\2\2\u0089\u008a\3\2\2\2\u008a")
        buf.write("\u008b\3\2\2\2\u008b\u008c\7\n\2\2\u008c\u008e\3\2\2\2")
        buf.write("\u008dm\3\2\2\2\u008dq\3\2\2\2\u008d{\3\2\2\2\u008d\u0081")
        buf.write("\3\2\2\2\u008e\5\3\2\2\2\u008f\u0092\5\b\5\2\u0090\u0092")
        buf.write("\5\n\6\2\u0091\u008f\3\2\2\2\u0091\u0090\3\2\2\2\u0092")
        buf.write("\7\3\2\2\2\u0093\u0094\5\20\t\2\u0094\u0095\7\r\2\2\u0095")
        buf.write("\u009a\3\2\2\2\u0096\u0097\5\22\n\2\u0097\u0098\7\r\2")
        buf.write("\2\u0098\u009a\3\2\2\2\u0099\u0093\3\2\2\2\u0099\u0096")
        buf.write("\3\2\2\2\u009a\t\3\2\2\2\u009b\u00a9\5\f\7\2\u009c\u00a9")
        buf.write("\5\16\b\2\u009d\u009e\5\34\17\2\u009e\u009f\7\7\2\2\u009f")
        buf.write("\u00a0\7\b\2\2\u00a0\u00a1\5\36\20\2\u00a1\u00a9\3\2\2")
        buf.write("\2\u00a2\u00a3\5\34\17\2\u00a3\u00a4\7\7\2\2\u00a4\u00a5")
        buf.write("\5\24\13\2\u00a5\u00a6\7\b\2\2\u00a6\u00a7\5\36\20\2\u00a7")
        buf.write("\u00a9\3\2\2\2\u00a8\u009b\3\2\2\2\u00a8\u009c\3\2\2\2")
        buf.write("\u00a8\u009d\3\2\2\2\u00a8\u00a2\3\2\2\2\u00a9\13\3\2")
        buf.write("\2\2\u00aa\u00ab\7$\2\2\u00ab\u00ac\7\7\2\2\u00ac\u00ad")
        buf.write("\7\b\2\2\u00ad\u00b5\5\36\20\2\u00ae\u00af\7$\2\2\u00af")
        buf.write("\u00b0\7\7\2\2\u00b0\u00b1\5\24\13\2\u00b1\u00b2\7\b\2")
        buf.write("\2\u00b2\u00b3\5\36\20\2\u00b3\u00b5\3\2\2\2\u00b4\u00aa")
        buf.write("\3\2\2\2\u00b4\u00ae\3\2\2\2\u00b5\r\3\2\2\2\u00b6\u00b7")
        buf.write("\7%\2\2\u00b7\u00b8\7\7\2\2\u00b8\u00b9\7\b\2\2\u00b9")
        buf.write("\u00ba\5\36\20\2\u00ba\17\3\2\2\2\u00bb\u00bc\7\22\2\2")
        buf.write("\u00bc\u00bd\5\26\f\2\u00bd\u00be\7\65\2\2\u00be\u00bf")
        buf.write("\5\32\16\2\u00bf\u00c3\3\2\2\2\u00c0\u00c1\7\22\2\2\u00c1")
        buf.write("\u00c3\5\26\f\2\u00c2\u00bb\3\2\2\2\u00c2\u00c0\3\2\2")
        buf.write("\2\u00c3\21\3\2\2\2\u00c4\u00c5\7\23\2\2\u00c5\u00c6\5")
        buf.write("\26\f\2\u00c6\u00c7\7\65\2\2\u00c7\u00c8\5\32\16\2\u00c8")
        buf.write("\u00cc\3\2\2\2\u00c9\u00ca\7\23\2\2\u00ca\u00cc\5\26\f")
        buf.write("\2\u00cb\u00c4\3\2\2\2\u00cb\u00c9\3\2\2\2\u00cc\23\3")
        buf.write("\2\2\2\u00cd\u00d2\5\26\f\2\u00ce\u00cf\7\r\2\2\u00cf")
        buf.write("\u00d1\5\26\f\2\u00d0\u00ce\3\2\2\2\u00d1\u00d4\3\2\2")
        buf.write("\2\u00d2\u00d0\3\2\2\2\u00d2\u00d3\3\2\2\2\u00d3\25\3")
        buf.write("\2\2\2\u00d4\u00d2\3\2\2\2\u00d5\u00d6\5\30\r\2\u00d6")
        buf.write("\u00d7\7\16\2\2\u00d7\u00d8\5(\25\2\u00d8\27\3\2\2\2\u00d9")
        buf.write("\u00de\5\34\17\2\u00da\u00db\7\20\2\2\u00db\u00dd\5\34")
        buf.write("\17\2\u00dc\u00da\3\2\2\2\u00dd\u00e0\3\2\2\2\u00de\u00dc")
        buf.write("\3\2\2\2\u00de\u00df\3\2\2\2\u00df\31\3\2\2\2\u00e0\u00de")
        buf.write("\3\2\2\2\u00e1\u00e6\5\64\33\2\u00e2\u00e3\7\20\2\2\u00e3")
        buf.write("\u00e5\5\64\33\2\u00e4\u00e2\3\2\2\2\u00e5\u00e8\3\2\2")
        buf.write("\2\u00e6\u00e4\3\2\2\2\u00e6\u00e7\3\2\2\2\u00e7\33\3")
        buf.write("\2\2\2\u00e8\u00e6\3\2\2\2\u00e9\u00ea\t\2\2\2\u00ea\35")
        buf.write("\3\2\2\2\u00eb\u00f0\7\t\2\2\u00ec\u00ef\5 \21\2\u00ed")
        buf.write("\u00ef\5\36\20\2\u00ee\u00ec\3\2\2\2\u00ee\u00ed\3\2\2")
        buf.write("\2\u00ef\u00f2\3\2\2\2\u00f0\u00ee\3\2\2\2\u00f0\u00f1")
        buf.write("\3\2\2\2\u00f1\u00f3\3\2\2\2\u00f2\u00f0\3\2\2\2\u00f3")
        buf.write("\u00f4\7\n\2\2\u00f4\37\3\2\2\2\u00f5\u00fe\5\"\22\2\u00f6")
        buf.write("\u00fe\5*\26\2\u00f7\u00fe\5\b\5\2\u00f8\u00fe\5.\30\2")
        buf.write("\u00f9\u00fe\5\60\31\2\u00fa\u00fe\5\62\32\2\u00fb\u00fe")
        buf.write("\5,\27\2\u00fc\u00fe\5X-\2\u00fd\u00f5\3\2\2\2\u00fd\u00f6")
        buf.write("\3\2\2\2\u00fd\u00f7\3\2\2\2\u00fd\u00f8\3\2\2\2\u00fd")
        buf.write("\u00f9\3\2\2\2\u00fd\u00fa\3\2\2\2\u00fd\u00fb\3\2\2\2")
        buf.write("\u00fd\u00fc\3\2\2\2\u00fe!\3\2\2\2\u00ff\u0100\5$\23")
        buf.write("\2\u0100\u0101\7\r\2\2\u0101#\3\2\2\2\u0102\u0103\5&\24")
        buf.write("\2\u0103\u0104\7\65\2\2\u0104\u0105\5\64\33\2\u0105%\3")
        buf.write("\2\2\2\u0106\u010a\7;\2\2\u0107\u010a\5T+\2\u0108\u010a")
        buf.write("\5V,\2\u0109\u0106\3\2\2\2\u0109\u0107\3\2\2\2\u0109\u0108")
        buf.write("\3\2\2\2\u010a\'\3\2\2\2\u010b\u0111\7\26\2\2\u010c\u0111")
        buf.write("\7\27\2\2\u010d\u0111\7\31\2\2\u010e\u0111\7\30\2\2\u010f")
        buf.write("\u0111\5d\63\2\u0110\u010b\3\2\2\2\u0110\u010c\3\2\2\2")
        buf.write("\u0110\u010d\3\2\2\2\u0110\u010e\3\2\2\2\u0110\u010f\3")
        buf.write("\2\2\2\u0111)\3\2\2\2\u0112\u0113\7\35\2\2\u0113\u0114")
        buf.write("\7\7\2\2\u0114\u0115\5\64\33\2\u0115\u0116\7\b\2\2\u0116")
        buf.write("\u011f\5\36\20\2\u0117\u0118\7\36\2\2\u0118\u0119\7\7")
        buf.write("\2\2\u0119\u011a\5\64\33\2\u011a\u011b\7\b\2\2\u011b\u011c")
        buf.write("\5\36\20\2\u011c\u011e\3\2\2\2\u011d\u0117\3\2\2\2\u011e")
        buf.write("\u0121\3\2\2\2\u011f\u011d\3\2\2\2\u011f\u0120\3\2\2\2")
        buf.write("\u0120\u0124\3\2\2\2\u0121\u011f\3\2\2\2\u0122\u0123\7")
        buf.write("\37\2\2\u0123\u0125\5\36\20\2\u0124\u0122\3\2\2\2\u0124")
        buf.write("\u0125\3\2\2\2\u0125+\3\2\2\2\u0126\u0128\7!\2\2\u0127")
        buf.write("\u0129\5\64\33\2\u0128\u0127\3\2\2\2\u0128\u0129\3\2\2")
        buf.write("\2\u0129\u012a\3\2\2\2\u012a\u012b\7\r\2\2\u012b-\3\2")
        buf.write("\2\2\u012c\u012d\7\33\2\2\u012d\u012e\7\r\2\2\u012e/\3")
        buf.write("\2\2\2\u012f\u0130\7\34\2\2\u0130\u0131\7\r\2\2\u0131")
        buf.write("\61\3\2\2\2\u0132\u0133\7 \2\2\u0133\u0134\7\7\2\2\u0134")
        buf.write("\u0135\7;\2\2\u0135\u0136\7&\2\2\u0136\u0137\7\4\2\2\u0137")
        buf.write("\u0138\7)\2\2\u0138\u013b\7\4\2\2\u0139\u013a\7\'\2\2")
        buf.write("\u013a\u013c\7\4\2\2\u013b\u0139\3\2\2\2\u013b\u013c\3")
        buf.write("\2\2\2\u013c\u013d\3\2\2\2\u013d\u013e\7\b\2\2\u013e\u013f")
        buf.write("\5\36\20\2\u013f\63\3\2\2\2\u0140\u0141\5\66\34\2\u0141")
        buf.write("\u0142\t\3\2\2\u0142\u0143\5\66\34\2\u0143\u0146\3\2\2")
        buf.write("\2\u0144\u0146\5\66\34\2\u0145\u0140\3\2\2\2\u0145\u0144")
        buf.write("\3\2\2\2\u0146\65\3\2\2\2\u0147\u0148\58\35\2\u0148\u0149")
        buf.write("\t\4\2\2\u0149\u014a\58\35\2\u014a\u014d\3\2\2\2\u014b")
        buf.write("\u014d\58\35\2\u014c\u0147\3\2\2\2\u014c\u014b\3\2\2\2")
        buf.write("\u014d\67\3\2\2\2\u014e\u014f\b\35\1\2\u014f\u0150\5:")
        buf.write("\36\2\u0150\u0156\3\2\2\2\u0151\u0152\f\4\2\2\u0152\u0153")
        buf.write("\t\5\2\2\u0153\u0155\5:\36\2\u0154\u0151\3\2\2\2\u0155")
        buf.write("\u0158\3\2\2\2\u0156\u0154\3\2\2\2\u0156\u0157\3\2\2\2")
        buf.write("\u01579\3\2\2\2\u0158\u0156\3\2\2\2\u0159\u015a\b\36\1")
        buf.write("\2\u015a\u015b\5<\37\2\u015b\u0161\3\2\2\2\u015c\u015d")
        buf.write("\f\4\2\2\u015d\u015e\t\6\2\2\u015e\u0160\5<\37\2\u015f")
        buf.write("\u015c\3\2\2\2\u0160\u0163\3\2\2\2\u0161\u015f\3\2\2\2")
        buf.write("\u0161\u0162\3\2\2\2\u0162;\3\2\2\2\u0163\u0161\3\2\2")
        buf.write("\2\u0164\u0165\b\37\1\2\u0165\u0166\5> \2\u0166\u016c")
        buf.write("\3\2\2\2\u0167\u0168\f\4\2\2\u0168\u0169\t\7\2\2\u0169")
        buf.write("\u016b\5> \2\u016a\u0167\3\2\2\2\u016b\u016e\3\2\2\2\u016c")
        buf.write("\u016a\3\2\2\2\u016c\u016d\3\2\2\2\u016d=\3\2\2\2\u016e")
        buf.write("\u016c\3\2\2\2\u016f\u0170\7/\2\2\u0170\u0173\5> \2\u0171")
        buf.write("\u0173\5@!\2\u0172\u016f\3\2\2\2\u0172\u0171\3\2\2\2\u0173")
        buf.write("?\3\2\2\2\u0174\u0175\7+\2\2\u0175\u0178\5@!\2\u0176\u0178")
        buf.write("\5B\"\2\u0177\u0174\3\2\2\2\u0177\u0176\3\2\2\2\u0178")
        buf.write("A\3\2\2\2\u0179\u017a\5F$\2\u017a\u017b\5D#\2\u017b\u017e")
        buf.write("\3\2\2\2\u017c\u017e\5F$\2\u017d\u0179\3\2\2\2\u017d\u017c")
        buf.write("\3\2\2\2\u017eC\3\2\2\2\u017f\u0180\7\13\2\2\u0180\u0181")
        buf.write("\5\64\33\2\u0181\u0182\7\f\2\2\u0182\u0183\5D#\2\u0183")
        buf.write("\u0189\3\2\2\2\u0184\u0185\7\13\2\2\u0185\u0186\5\64\33")
        buf.write("\2\u0186\u0187\7\f\2\2\u0187\u0189\3\2\2\2\u0188\u017f")
        buf.write("\3\2\2\2\u0188\u0184\3\2\2\2\u0189E\3\2\2\2\u018a\u018b")
        buf.write("\b$\1\2\u018b\u018c\5H%\2\u018c\u019e\3\2\2\2\u018d\u018e")
        buf.write("\f\6\2\2\u018e\u018f\7(\2\2\u018f\u019d\7;\2\2\u0190\u0191")
        buf.write("\f\5\2\2\u0191\u0192\7(\2\2\u0192\u0193\7;\2\2\u0193\u0194")
        buf.write("\7\7\2\2\u0194\u019d\7\b\2\2\u0195\u0196\f\4\2\2\u0196")
        buf.write("\u0197\7(\2\2\u0197\u0198\7;\2\2\u0198\u0199\7\7\2\2\u0199")
        buf.write("\u019a\5\32\16\2\u019a\u019b\7\b\2\2\u019b\u019d\3\2\2")
        buf.write("\2\u019c\u018d\3\2\2\2\u019c\u0190\3\2\2\2\u019c\u0195")
        buf.write("\3\2\2\2\u019d\u01a0\3\2\2\2\u019e\u019c\3\2\2\2\u019e")
        buf.write("\u019f\3\2\2\2\u019fG\3\2\2\2\u01a0\u019e\3\2\2\2\u01a1")
        buf.write("\u01a2\5J&\2\u01a2\u01a3\7\17\2\2\u01a3\u01a4\7<\2\2\u01a4")
        buf.write("\u01b4\3\2\2\2\u01a5\u01a6\5J&\2\u01a6\u01a7\7\17\2\2")
        buf.write("\u01a7\u01a8\7<\2\2\u01a8\u01a9\7\7\2\2\u01a9\u01aa\7")
        buf.write("\b\2\2\u01aa\u01b4\3\2\2\2\u01ab\u01ac\5J&\2\u01ac\u01ad")
        buf.write("\7\17\2\2\u01ad\u01ae\7<\2\2\u01ae\u01af\7\7\2\2\u01af")
        buf.write("\u01b0\5\32\16\2\u01b0\u01b1\7\b\2\2\u01b1\u01b4\3\2\2")
        buf.write("\2\u01b2\u01b4\5J&\2\u01b3\u01a1\3\2\2\2\u01b3\u01a5\3")
        buf.write("\2\2\2\u01b3\u01ab\3\2\2\2\u01b3\u01b2\3\2\2\2\u01b4I")
        buf.write("\3\2\2\2\u01b5\u01b6\7#\2\2\u01b6\u01b7\7;\2\2\u01b7\u01b8")
        buf.write("\7\7\2\2\u01b8\u01c1\7\b\2\2\u01b9\u01ba\7#\2\2\u01ba")
        buf.write("\u01bb\7;\2\2\u01bb\u01bc\7\7\2\2\u01bc\u01bd\5\32\16")
        buf.write("\2\u01bd\u01be\7\b\2\2\u01be\u01c1\3\2\2\2\u01bf\u01c1")
        buf.write("\5L\'\2\u01c0\u01b5\3\2\2\2\u01c0\u01b9\3\2\2\2\u01c0")
        buf.write("\u01bf\3\2\2\2\u01c1K\3\2\2\2\u01c2\u01c3\7\7\2\2\u01c3")
        buf.write("\u01c4\5\64\33\2\u01c4\u01c5\7\b\2\2\u01c5\u01c8\3\2\2")
        buf.write("\2\u01c6\u01c8\5N(\2\u01c7\u01c2\3\2\2\2\u01c7\u01c6\3")
        buf.write("\2\2\2\u01c8M\3\2\2\2\u01c9\u01ce\7;\2\2\u01ca\u01ce\5")
        buf.write("R*\2\u01cb\u01ce\7\"\2\2\u01cc\u01ce\7\32\2\2\u01cd\u01c9")
        buf.write("\3\2\2\2\u01cd\u01ca\3\2\2\2\u01cd\u01cb\3\2\2\2\u01cd")
        buf.write("\u01cc\3\2\2\2\u01ceO\3\2\2\2\u01cf\u01d0\5R*\2\u01d0")
        buf.write("\u01d1\7\20\2\2\u01d1\u01d3\3\2\2\2\u01d2\u01cf\3\2\2")
        buf.write("\2\u01d3\u01d6\3\2\2\2\u01d4\u01d2\3\2\2\2\u01d4\u01d5")
        buf.write("\3\2\2\2\u01d5\u01d7\3\2\2\2\u01d6\u01d4\3\2\2\2\u01d7")
        buf.write("\u01d8\5R*\2\u01d8Q\3\2\2\2\u01d9\u01df\7\4\2\2\u01da")
        buf.write("\u01df\7\3\2\2\u01db\u01df\7\5\2\2\u01dc\u01df\7\6\2\2")
        buf.write("\u01dd\u01df\5\\/\2\u01de\u01d9\3\2\2\2\u01de\u01da\3")
        buf.write("\2\2\2\u01de\u01db\3\2\2\2\u01de\u01dc\3\2\2\2\u01de\u01dd")
        buf.write("\3\2\2\2\u01dfS\3\2\2\2\u01e0\u01e1\5F$\2\u01e1\u01e2")
        buf.write("\7\13\2\2\u01e2\u01e3\5\64\33\2\u01e3\u01e4\7\f\2\2\u01e4")
        buf.write("U\3\2\2\2\u01e5\u01e6\5\64\33\2\u01e6\u01e7\7(\2\2\u01e7")
        buf.write("\u01e8\7;\2\2\u01e8\u01ee\3\2\2\2\u01e9\u01ea\5\64\33")
        buf.write("\2\u01ea\u01eb\7\17\2\2\u01eb\u01ec\7;\2\2\u01ec\u01ee")
        buf.write("\3\2\2\2\u01ed\u01e5\3\2\2\2\u01ed\u01e9\3\2\2\2\u01ee")
        buf.write("W\3\2\2\2\u01ef\u01f0\5Z.\2\u01f0\u01f1\7\r\2\2\u01f1")
        buf.write("Y\3\2\2\2\u01f2\u01f3\5\64\33\2\u01f3\u01f4\7(\2\2\u01f4")
        buf.write("\u01f5\7;\2\2\u01f5\u01f6\7\7\2\2\u01f6\u01f7\7\b\2\2")
        buf.write("\u01f7\u020d\3\2\2\2\u01f8\u01f9\5\64\33\2\u01f9\u01fa")
        buf.write("\7(\2\2\u01fa\u01fb\7;\2\2\u01fb\u01fc\7\7\2\2\u01fc\u01fd")
        buf.write("\5\32\16\2\u01fd\u01fe\7\b\2\2\u01fe\u020d\3\2\2\2\u01ff")
        buf.write("\u0200\5\64\33\2\u0200\u0201\7\17\2\2\u0201\u0202\7<\2")
        buf.write("\2\u0202\u0203\7\7\2\2\u0203\u0204\7\b\2\2\u0204\u020d")
        buf.write("\3\2\2\2\u0205\u0206\5\64\33\2\u0206\u0207\7\17\2\2\u0207")
        buf.write("\u0208\7<\2\2\u0208\u0209\7\7\2\2\u0209\u020a\5\32\16")
        buf.write("\2\u020a\u020b\7\b\2\2\u020b\u020d\3\2\2\2\u020c\u01f2")
        buf.write("\3\2\2\2\u020c\u01f8\3\2\2\2\u020c\u01ff\3\2\2\2\u020c")
        buf.write("\u0205\3\2\2\2\u020d[\3\2\2\2\u020e\u0211\5^\60\2\u020f")
        buf.write("\u0211\5b\62\2\u0210\u020e\3\2\2\2\u0210\u020f\3\2\2\2")
        buf.write("\u0211]\3\2\2\2\u0212\u0213\7\25\2\2\u0213\u0214\7\7\2")
        buf.write("\2\u0214\u0215\5`\61\2\u0215\u0216\7\b\2\2\u0216_\3\2")
        buf.write("\2\2\u0217\u0218\5b\62\2\u0218\u0219\7\20\2\2\u0219\u021a")
        buf.write("\5`\61\2\u021a\u021d\3\2\2\2\u021b\u021d\5b\62\2\u021c")
        buf.write("\u0217\3\2\2\2\u021c\u021b\3\2\2\2\u021da\3\2\2\2\u021e")
        buf.write("\u021f\7\25\2\2\u021f\u0220\7\7\2\2\u0220\u0221\5\32\16")
        buf.write("\2\u0221\u0222\7\b\2\2\u0222c\3\2\2\2\u0223\u0224\7\25")
        buf.write("\2\2\u0224\u0225\7\13\2\2\u0225\u0226\5(\25\2\u0226\u0227")
        buf.write("\7\20\2\2\u0227\u0228\5R*\2\u0228\u0229\7\f\2\2\u0229")
        buf.write("e\3\2\2\2-iw\u0089\u008d\u0091\u0099\u00a8\u00b4\u00c2")
        buf.write("\u00cb\u00d2\u00de\u00e6\u00ee\u00f0\u00fd\u0109\u0110")
        buf.write("\u011f\u0124\u0128\u013b\u0145\u014c\u0156\u0161\u016c")
        buf.write("\u0172\u0177\u017d\u0188\u019c\u019e\u01b3\u01c0\u01c7")
        buf.write("\u01cd\u01d4\u01de\u01ed\u020c\u0210\u021c")
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
    RULE_index_operators = 33
    RULE_expr8 = 34
    RULE_expr9 = 35
    RULE_expr10 = 36
    RULE_expr11 = 37
    RULE_operands = 38
    RULE_list_literal = 39
    RULE_literal = 40
    RULE_array_operator = 41
    RULE_field_access = 42
    RULE_method_invocation_stmt = 43
    RULE_method_invocation = 44
    RULE_array = 45
    RULE_muldi_arr = 46
    RULE_array_list = 47
    RULE_indx_arr = 48
    RULE_array_type = 49

    ruleNames =  [ "program", "class_decl", "mem_decl", "attr_decl", "method_decl", 
                   "constr_decl", "destr_decl", "immutable_attr", "mutable_attr", 
                   "params_list", "id_list_type", "id_list", "expr_list", 
                   "iden_dol", "block_stmt", "block_items", "assign_stmt", 
                   "assign_lhs", "lhs", "data_type", "if_stmt", "return_stmt", 
                   "break_stmt", "continue_stmt", "forin_stmt", "expr", 
                   "expr1", "expr2", "expr3", "expr4", "expr5", "expr6", 
                   "expr7", "index_operators", "expr8", "expr9", "expr10", 
                   "expr11", "operands", "list_literal", "literal", "array_operator", 
                   "field_access", "method_invocation_stmt", "method_invocation", 
                   "array", "muldi_arr", "array_list", "indx_arr", "array_type" ]

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
            self.state = 101 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 100
                self.class_decl()
                self.state = 103 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==D96Parser.CLASS):
                    break

            self.state = 105
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
            self.state = 139
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 107
                self.match(D96Parser.CLASS)
                self.state = 108
                self.match(D96Parser.IDEN)
                self.state = 109
                self.match(D96Parser.LP)
                self.state = 110
                self.match(D96Parser.RP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 111
                self.match(D96Parser.CLASS)
                self.state = 112
                self.match(D96Parser.IDEN)
                self.state = 113
                self.match(D96Parser.LP)
                self.state = 115 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 114
                    self.mem_decl()
                    self.state = 117 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.VAL) | (1 << D96Parser.VAR) | (1 << D96Parser.CONSTRUCTOR) | (1 << D96Parser.DESTRUCTOR) | (1 << D96Parser.IDEN) | (1 << D96Parser.DOL_IDEN))) != 0)):
                        break

                self.state = 119
                self.match(D96Parser.RP)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 121
                self.match(D96Parser.CLASS)
                self.state = 122
                self.match(D96Parser.IDEN)
                self.state = 123
                self.match(D96Parser.COL)
                self.state = 124
                self.match(D96Parser.IDEN)
                self.state = 125
                self.match(D96Parser.LP)
                self.state = 126
                self.match(D96Parser.RP)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 127
                self.match(D96Parser.CLASS)
                self.state = 128
                self.match(D96Parser.IDEN)
                self.state = 129
                self.match(D96Parser.COL)
                self.state = 130
                self.match(D96Parser.IDEN)
                self.state = 131
                self.match(D96Parser.LP)
                self.state = 133 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 132
                    self.mem_decl()
                    self.state = 135 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.VAL) | (1 << D96Parser.VAR) | (1 << D96Parser.CONSTRUCTOR) | (1 << D96Parser.DESTRUCTOR) | (1 << D96Parser.IDEN) | (1 << D96Parser.DOL_IDEN))) != 0)):
                        break

                self.state = 137
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attr_decl(self):
            return self.getTypedRuleContext(D96Parser.Attr_declContext,0)


        def method_decl(self):
            return self.getTypedRuleContext(D96Parser.Method_declContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_mem_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMem_decl" ):
                return visitor.visitMem_decl(self)
            else:
                return visitor.visitChildren(self)




    def mem_decl(self):

        localctx = D96Parser.Mem_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_mem_decl)
        try:
            self.state = 143
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAL, D96Parser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 141
                self.attr_decl()
                pass
            elif token in [D96Parser.CONSTRUCTOR, D96Parser.DESTRUCTOR, D96Parser.IDEN, D96Parser.DOL_IDEN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 142
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttr_decl" ):
                return visitor.visitAttr_decl(self)
            else:
                return visitor.visitChildren(self)




    def attr_decl(self):

        localctx = D96Parser.Attr_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_attr_decl)
        try:
            self.state = 151
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 145
                self.immutable_attr()
                self.state = 146
                self.match(D96Parser.SEMI)
                pass
            elif token in [D96Parser.VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 148
                self.mutable_attr()
                self.state = 149
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_decl" ):
                return visitor.visitMethod_decl(self)
            else:
                return visitor.visitChildren(self)




    def method_decl(self):

        localctx = D96Parser.Method_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_method_decl)
        try:
            self.state = 166
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 153
                self.constr_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 154
                self.destr_decl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 155
                self.iden_dol()
                self.state = 156
                self.match(D96Parser.LB)
                self.state = 157
                self.match(D96Parser.RB)
                self.state = 158
                self.block_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 160
                self.iden_dol()
                self.state = 161
                self.match(D96Parser.LB)
                self.state = 162
                self.params_list()
                self.state = 163
                self.match(D96Parser.RB)
                self.state = 164
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


        def params_list(self):
            return self.getTypedRuleContext(D96Parser.Params_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_constr_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstr_decl" ):
                return visitor.visitConstr_decl(self)
            else:
                return visitor.visitChildren(self)




    def constr_decl(self):

        localctx = D96Parser.Constr_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_constr_decl)
        try:
            self.state = 178
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 168
                self.match(D96Parser.CONSTRUCTOR)
                self.state = 169
                self.match(D96Parser.LB)
                self.state = 170
                self.match(D96Parser.RB)
                self.state = 171
                self.block_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 172
                self.match(D96Parser.CONSTRUCTOR)
                self.state = 173
                self.match(D96Parser.LB)
                self.state = 174
                self.params_list()
                self.state = 175
                self.match(D96Parser.RB)
                self.state = 176
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
        self.enterRule(localctx, 12, self.RULE_destr_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.match(D96Parser.DESTRUCTOR)
            self.state = 181
            self.match(D96Parser.LB)
            self.state = 182
            self.match(D96Parser.RB)
            self.state = 183
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Immutable_attrContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImmutable_attr" ):
                return visitor.visitImmutable_attr(self)
            else:
                return visitor.visitChildren(self)




    def immutable_attr(self):

        localctx = D96Parser.Immutable_attrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_immutable_attr)
        try:
            self.state = 192
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 185
                self.match(D96Parser.VAL)
                self.state = 186
                self.id_list_type()
                self.state = 187
                self.match(D96Parser.OP_AS)
                self.state = 188
                self.expr_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 190
                self.match(D96Parser.VAL)
                self.state = 191
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMutable_attr" ):
                return visitor.visitMutable_attr(self)
            else:
                return visitor.visitChildren(self)




    def mutable_attr(self):

        localctx = D96Parser.Mutable_attrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_mutable_attr)
        try:
            self.state = 201
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 194
                self.match(D96Parser.VAR)
                self.state = 195
                self.id_list_type()
                self.state = 196
                self.match(D96Parser.OP_AS)
                self.state = 197
                self.expr_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 199
                self.match(D96Parser.VAR)
                self.state = 200
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams_list" ):
                return visitor.visitParams_list(self)
            else:
                return visitor.visitChildren(self)




    def params_list(self):

        localctx = D96Parser.Params_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_params_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.id_list_type()
            self.state = 208
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.SEMI:
                self.state = 204
                self.match(D96Parser.SEMI)
                self.state = 205
                self.id_list_type()
                self.state = 210
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId_list_type" ):
                return visitor.visitId_list_type(self)
            else:
                return visitor.visitChildren(self)




    def id_list_type(self):

        localctx = D96Parser.Id_list_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_id_list_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self.id_list()
            self.state = 212
            self.match(D96Parser.COL)
            self.state = 213
            self.data_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Id_listContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId_list" ):
                return visitor.visitId_list(self)
            else:
                return visitor.visitChildren(self)




    def id_list(self):

        localctx = D96Parser.Id_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_id_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self.iden_dol()
            self.state = 220
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COM:
                self.state = 216
                self.match(D96Parser.COM)
                self.state = 217
                self.iden_dol()
                self.state = 222
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_list" ):
                return visitor.visitExpr_list(self)
            else:
                return visitor.visitChildren(self)




    def expr_list(self):

        localctx = D96Parser.Expr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_expr_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self.expr()
            self.state = 228
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COM:
                self.state = 224
                self.match(D96Parser.COM)
                self.state = 225
                self.expr()
                self.state = 230
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDEN(self):
            return self.getToken(D96Parser.IDEN, 0)

        def DOL_IDEN(self):
            return self.getToken(D96Parser.DOL_IDEN, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_iden_dol

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIden_dol" ):
                return visitor.visitIden_dol(self)
            else:
                return visitor.visitChildren(self)




    def iden_dol(self):

        localctx = D96Parser.Iden_dolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_iden_dol)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
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
            self.state = 233
            self.match(D96Parser.LP)
            self.state = 238
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.LB) | (1 << D96Parser.LP) | (1 << D96Parser.VAL) | (1 << D96Parser.VAR) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NULL) | (1 << D96Parser.BREAK) | (1 << D96Parser.CONTINUE) | (1 << D96Parser.IF) | (1 << D96Parser.FOREACH) | (1 << D96Parser.RETURN) | (1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.OP_SUB) | (1 << D96Parser.OP_NOT) | (1 << D96Parser.IDEN))) != 0):
                self.state = 236
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.FLOAT_LITERAL, D96Parser.INTEGER_LITERAL, D96Parser.BOOLEAN_LITERAL, D96Parser.STRING_LITERAL, D96Parser.LB, D96Parser.VAL, D96Parser.VAR, D96Parser.ARRAY, D96Parser.NULL, D96Parser.BREAK, D96Parser.CONTINUE, D96Parser.IF, D96Parser.FOREACH, D96Parser.RETURN, D96Parser.SELF, D96Parser.NEW, D96Parser.OP_SUB, D96Parser.OP_NOT, D96Parser.IDEN]:
                    self.state = 234
                    self.block_items()
                    pass
                elif token in [D96Parser.LP]:
                    self.state = 235
                    self.block_stmt()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 240
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 241
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_items" ):
                return visitor.visitBlock_items(self)
            else:
                return visitor.visitChildren(self)




    def block_items(self):

        localctx = D96Parser.Block_itemsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_block_items)
        try:
            self.state = 251
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 243
                self.assign_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 244
                self.if_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 245
                self.attr_decl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 246
                self.break_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 247
                self.continue_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 248
                self.forin_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 249
                self.return_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 250
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
            self.state = 253
            self.assign_lhs()
            self.state = 254
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

        def lhs(self):
            return self.getTypedRuleContext(D96Parser.LhsContext,0)


        def OP_AS(self):
            return self.getToken(D96Parser.OP_AS, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


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
            self.state = 256
            self.lhs()
            self.state = 257
            self.match(D96Parser.OP_AS)
            self.state = 258
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = D96Parser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_lhs)
        try:
            self.state = 263
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 260
                self.match(D96Parser.IDEN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 261
                self.array_operator()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 262
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

        def array_type(self):
            return self.getTypedRuleContext(D96Parser.Array_typeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_data_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitData_type" ):
                return visitor.visitData_type(self)
            else:
                return visitor.visitChildren(self)




    def data_type(self):

        localctx = D96Parser.Data_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_data_type)
        try:
            self.state = 270
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 265
                self.match(D96Parser.INT)
                pass
            elif token in [D96Parser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 266
                self.match(D96Parser.FLOAT)
                pass
            elif token in [D96Parser.STRING]:
                self.enterOuterAlt(localctx, 3)
                self.state = 267
                self.match(D96Parser.STRING)
                pass
            elif token in [D96Parser.BOOLEAN]:
                self.enterOuterAlt(localctx, 4)
                self.state = 268
                self.match(D96Parser.BOOLEAN)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 5)
                self.state = 269
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
        self.enterRule(localctx, 40, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.match(D96Parser.IF)
            self.state = 273
            self.match(D96Parser.LB)
            self.state = 274
            self.expr()
            self.state = 275
            self.match(D96Parser.RB)
            self.state = 276
            self.block_stmt()
            self.state = 285
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.ELSEIF:
                self.state = 277
                self.match(D96Parser.ELSEIF)
                self.state = 278
                self.match(D96Parser.LB)
                self.state = 279
                self.expr()
                self.state = 280
                self.match(D96Parser.RB)
                self.state = 281
                self.block_stmt()
                self.state = 287
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 290
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ELSE:
                self.state = 288
                self.match(D96Parser.ELSE)
                self.state = 289
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
        self.enterRule(localctx, 42, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 292
            self.match(D96Parser.RETURN)
            self.state = 294
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.LB) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NULL) | (1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.OP_SUB) | (1 << D96Parser.OP_NOT) | (1 << D96Parser.IDEN))) != 0):
                self.state = 293
                self.expr()


            self.state = 296
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
        self.enterRule(localctx, 44, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            self.match(D96Parser.BREAK)
            self.state = 299
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
        self.enterRule(localctx, 46, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
            self.match(D96Parser.CONTINUE)
            self.state = 302
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
        self.enterRule(localctx, 48, self.RULE_forin_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 304
            self.match(D96Parser.FOREACH)
            self.state = 305
            self.match(D96Parser.LB)
            self.state = 306
            self.match(D96Parser.IDEN)
            self.state = 307
            self.match(D96Parser.IN)
            self.state = 308
            self.match(D96Parser.INTEGER_LITERAL)
            self.state = 309
            self.match(D96Parser.DDOT)
            self.state = 310
            self.match(D96Parser.INTEGER_LITERAL)
            self.state = 313
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.BY:
                self.state = 311
                self.match(D96Parser.BY)
                self.state = 312
                self.match(D96Parser.INTEGER_LITERAL)


            self.state = 315
            self.match(D96Parser.RB)
            self.state = 316
            self.block_stmt()
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

        def expr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Expr1Context)
            else:
                return self.getTypedRuleContext(D96Parser.Expr1Context,i)


        def OP_EQ_STR(self):
            return self.getToken(D96Parser.OP_EQ_STR, 0)

        def OP_ADD_STR(self):
            return self.getToken(D96Parser.OP_ADD_STR, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = D96Parser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.state = 323
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 318
                self.expr1()
                self.state = 319
                _la = self._input.LA(1)
                if not(_la==D96Parser.OP_EQ_STR or _la==D96Parser.OP_ADD_STR):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 320
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 322
                self.expr1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Expr2Context)
            else:
                return self.getTypedRuleContext(D96Parser.Expr2Context,i)


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)




    def expr1(self):

        localctx = D96Parser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_expr1)
        self._la = 0 # Token type
        try:
            self.state = 330
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 325
                self.expr2(0)
                self.state = 326
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.OP_LTE) | (1 << D96Parser.OP_GTE) | (1 << D96Parser.OP_NEQ) | (1 << D96Parser.OP_EQ) | (1 << D96Parser.OP_LT) | (1 << D96Parser.OP_GT))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 327
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 329
                self.expr2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)



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
            self.state = 333
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 340
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 335
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 336
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.OP_AND or _la==D96Parser.OP_OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 337
                    self.expr3(0) 
                self.state = 342
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)



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
            self.state = 344
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 351
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 346
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 347
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.OP_ADD or _la==D96Parser.OP_SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 348
                    self.expr4(0) 
                self.state = 353
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr4" ):
                return visitor.visitExpr4(self)
            else:
                return visitor.visitChildren(self)



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
            self.state = 355
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 362
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 357
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 358
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.OP_MUL) | (1 << D96Parser.OP_DIV) | (1 << D96Parser.OP_MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 359
                    self.expr5() 
                self.state = 364
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)




    def expr5(self):

        localctx = D96Parser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_expr5)
        try:
            self.state = 368
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.OP_NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 365
                self.match(D96Parser.OP_NOT)
                self.state = 366
                self.expr5()
                pass
            elif token in [D96Parser.FLOAT_LITERAL, D96Parser.INTEGER_LITERAL, D96Parser.BOOLEAN_LITERAL, D96Parser.STRING_LITERAL, D96Parser.LB, D96Parser.ARRAY, D96Parser.NULL, D96Parser.SELF, D96Parser.NEW, D96Parser.OP_SUB, D96Parser.IDEN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 367
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr6" ):
                return visitor.visitExpr6(self)
            else:
                return visitor.visitChildren(self)




    def expr6(self):

        localctx = D96Parser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_expr6)
        try:
            self.state = 373
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.OP_SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 370
                self.match(D96Parser.OP_SUB)
                self.state = 371
                self.expr6()
                pass
            elif token in [D96Parser.FLOAT_LITERAL, D96Parser.INTEGER_LITERAL, D96Parser.BOOLEAN_LITERAL, D96Parser.STRING_LITERAL, D96Parser.LB, D96Parser.ARRAY, D96Parser.NULL, D96Parser.SELF, D96Parser.NEW, D96Parser.IDEN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 372
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr8(self):
            return self.getTypedRuleContext(D96Parser.Expr8Context,0)


        def index_operators(self):
            return self.getTypedRuleContext(D96Parser.Index_operatorsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr7" ):
                return visitor.visitExpr7(self)
            else:
                return visitor.visitChildren(self)




    def expr7(self):

        localctx = D96Parser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_expr7)
        try:
            self.state = 379
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 375
                self.expr8(0)
                self.state = 376
                self.index_operators()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 378
                self.expr8(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_operatorsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(D96Parser.LSB, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def RSB(self):
            return self.getToken(D96Parser.RSB, 0)

        def index_operators(self):
            return self.getTypedRuleContext(D96Parser.Index_operatorsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_index_operators

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_operators" ):
                return visitor.visitIndex_operators(self)
            else:
                return visitor.visitChildren(self)




    def index_operators(self):

        localctx = D96Parser.Index_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_index_operators)
        try:
            self.state = 390
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 381
                self.match(D96Parser.LSB)
                self.state = 382
                self.expr()
                self.state = 383
                self.match(D96Parser.RSB)
                self.state = 384
                self.index_operators()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 386
                self.match(D96Parser.LSB)
                self.state = 387
                self.expr()
                self.state = 388
                self.match(D96Parser.RSB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr8Context(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr8" ):
                return visitor.visitExpr8(self)
            else:
                return visitor.visitChildren(self)



    def expr8(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr8Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_expr8, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 393
            self.expr9()
            self._ctx.stop = self._input.LT(-1)
            self.state = 412
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 410
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Expr8Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr8)
                        self.state = 395
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 396
                        self.match(D96Parser.DOT)
                        self.state = 397
                        self.match(D96Parser.IDEN)
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Expr8Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr8)
                        self.state = 398
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 399
                        self.match(D96Parser.DOT)
                        self.state = 400
                        self.match(D96Parser.IDEN)
                        self.state = 401
                        self.match(D96Parser.LB)
                        self.state = 402
                        self.match(D96Parser.RB)
                        pass

                    elif la_ == 3:
                        localctx = D96Parser.Expr8Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr8)
                        self.state = 403
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 404
                        self.match(D96Parser.DOT)
                        self.state = 405
                        self.match(D96Parser.IDEN)
                        self.state = 406
                        self.match(D96Parser.LB)
                        self.state = 407
                        self.expr_list()
                        self.state = 408
                        self.match(D96Parser.RB)
                        pass

             
                self.state = 414
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr9Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr10(self):
            return self.getTypedRuleContext(D96Parser.Expr10Context,0)


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr9" ):
                return visitor.visitExpr9(self)
            else:
                return visitor.visitChildren(self)




    def expr9(self):

        localctx = D96Parser.Expr9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_expr9)
        try:
            self.state = 433
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 415
                self.expr10()
                self.state = 416
                self.match(D96Parser.DCOL)
                self.state = 417
                self.match(D96Parser.DOL_IDEN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 419
                self.expr10()
                self.state = 420
                self.match(D96Parser.DCOL)
                self.state = 421
                self.match(D96Parser.DOL_IDEN)
                self.state = 422
                self.match(D96Parser.LB)
                self.state = 423
                self.match(D96Parser.RB)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 425
                self.expr10()
                self.state = 426
                self.match(D96Parser.DCOL)
                self.state = 427
                self.match(D96Parser.DOL_IDEN)
                self.state = 428
                self.match(D96Parser.LB)
                self.state = 429
                self.expr_list()
                self.state = 430
                self.match(D96Parser.RB)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 432
                self.expr10()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr10Context(ParserRuleContext):
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

        def expr_list(self):
            return self.getTypedRuleContext(D96Parser.Expr_listContext,0)


        def expr11(self):
            return self.getTypedRuleContext(D96Parser.Expr11Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr10

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr10" ):
                return visitor.visitExpr10(self)
            else:
                return visitor.visitChildren(self)




    def expr10(self):

        localctx = D96Parser.Expr10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_expr10)
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

        def operands(self):
            return self.getTypedRuleContext(D96Parser.OperandsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr11

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr11" ):
                return visitor.visitExpr11(self)
            else:
                return visitor.visitChildren(self)




    def expr11(self):

        localctx = D96Parser.Expr11Context(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_expr11)
        try:
            self.state = 453
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.LB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 448
                self.match(D96Parser.LB)
                self.state = 449
                self.expr()
                self.state = 450
                self.match(D96Parser.RB)
                pass
            elif token in [D96Parser.FLOAT_LITERAL, D96Parser.INTEGER_LITERAL, D96Parser.BOOLEAN_LITERAL, D96Parser.STRING_LITERAL, D96Parser.ARRAY, D96Parser.NULL, D96Parser.SELF, D96Parser.IDEN]:
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDEN(self):
            return self.getToken(D96Parser.IDEN, 0)

        def literal(self):
            return self.getTypedRuleContext(D96Parser.LiteralContext,0)


        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def NULL(self):
            return self.getToken(D96Parser.NULL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_operands

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperands" ):
                return visitor.visitOperands(self)
            else:
                return visitor.visitChildren(self)




    def operands(self):

        localctx = D96Parser.OperandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_operands)
        try:
            self.state = 459
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.IDEN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 455
                self.match(D96Parser.IDEN)
                pass
            elif token in [D96Parser.FLOAT_LITERAL, D96Parser.INTEGER_LITERAL, D96Parser.BOOLEAN_LITERAL, D96Parser.STRING_LITERAL, D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 456
                self.literal()
                pass
            elif token in [D96Parser.SELF]:
                self.enterOuterAlt(localctx, 3)
                self.state = 457
                self.match(D96Parser.SELF)
                pass
            elif token in [D96Parser.NULL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 458
                self.match(D96Parser.NULL)
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
        self.enterRule(localctx, 78, self.RULE_list_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 466
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,37,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 461
                    self.literal()
                    self.state = 462
                    self.match(D96Parser.COM) 
                self.state = 468
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,37,self._ctx)

            self.state = 469
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = D96Parser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_literal)
        try:
            self.state = 476
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INTEGER_LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 471
                self.match(D96Parser.INTEGER_LITERAL)
                pass
            elif token in [D96Parser.FLOAT_LITERAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 472
                self.match(D96Parser.FLOAT_LITERAL)
                pass
            elif token in [D96Parser.BOOLEAN_LITERAL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 473
                self.match(D96Parser.BOOLEAN_LITERAL)
                pass
            elif token in [D96Parser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 474
                self.match(D96Parser.STRING_LITERAL)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 5)
                self.state = 475
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


    class Array_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_operator" ):
                return visitor.visitArray_operator(self)
            else:
                return visitor.visitChildren(self)




    def array_operator(self):

        localctx = D96Parser.Array_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_array_operator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 478
            self.expr8(0)
            self.state = 479
            self.match(D96Parser.LSB)
            self.state = 480
            self.expr()
            self.state = 481
            self.match(D96Parser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_accessContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitField_access" ):
                return visitor.visitField_access(self)
            else:
                return visitor.visitChildren(self)




    def field_access(self):

        localctx = D96Parser.Field_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_field_access)
        try:
            self.state = 491
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 483
                self.expr()
                self.state = 484
                self.match(D96Parser.DOT)
                self.state = 485
                self.match(D96Parser.IDEN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 487
                self.expr()
                self.state = 488
                self.match(D96Parser.DCOL)
                self.state = 489
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def method_invocation(self):
            return self.getTypedRuleContext(D96Parser.Method_invocationContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_method_invocation_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_invocation_stmt" ):
                return visitor.visitMethod_invocation_stmt(self)
            else:
                return visitor.visitChildren(self)




    def method_invocation_stmt(self):

        localctx = D96Parser.Method_invocation_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_method_invocation_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 493
            self.method_invocation()
            self.state = 494
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_invocationContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_invocation" ):
                return visitor.visitMethod_invocation(self)
            else:
                return visitor.visitChildren(self)




    def method_invocation(self):

        localctx = D96Parser.Method_invocationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_method_invocation)
        try:
            self.state = 522
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 496
                self.expr()
                self.state = 497
                self.match(D96Parser.DOT)
                self.state = 498
                self.match(D96Parser.IDEN)
                self.state = 499
                self.match(D96Parser.LB)
                self.state = 500
                self.match(D96Parser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 502
                self.expr()
                self.state = 503
                self.match(D96Parser.DOT)
                self.state = 504
                self.match(D96Parser.IDEN)
                self.state = 505
                self.match(D96Parser.LB)
                self.state = 506
                self.expr_list()
                self.state = 507
                self.match(D96Parser.RB)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 509
                self.expr()
                self.state = 510
                self.match(D96Parser.DCOL)
                self.state = 511
                self.match(D96Parser.DOL_IDEN)
                self.state = 512
                self.match(D96Parser.LB)
                self.state = 513
                self.match(D96Parser.RB)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 515
                self.expr()
                self.state = 516
                self.match(D96Parser.DCOL)
                self.state = 517
                self.match(D96Parser.DOL_IDEN)
                self.state = 518
                self.match(D96Parser.LB)
                self.state = 519
                self.expr_list()
                self.state = 520
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
        self.enterRule(localctx, 90, self.RULE_array)
        try:
            self.state = 526
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 524
                self.muldi_arr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 525
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

        def array_list(self):
            return self.getTypedRuleContext(D96Parser.Array_listContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_muldi_arr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMuldi_arr" ):
                return visitor.visitMuldi_arr(self)
            else:
                return visitor.visitChildren(self)




    def muldi_arr(self):

        localctx = D96Parser.Muldi_arrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_muldi_arr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 528
            self.match(D96Parser.ARRAY)
            self.state = 529
            self.match(D96Parser.LB)
            self.state = 530
            self.array_list()
            self.state = 531
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_listContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_list" ):
                return visitor.visitArray_list(self)
            else:
                return visitor.visitChildren(self)




    def array_list(self):

        localctx = D96Parser.Array_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_array_list)
        try:
            self.state = 538
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 533
                self.indx_arr()
                self.state = 534
                self.match(D96Parser.COM)
                self.state = 535
                self.array_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 537
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndx_arr" ):
                return visitor.visitIndx_arr(self)
            else:
                return visitor.visitChildren(self)




    def indx_arr(self):

        localctx = D96Parser.Indx_arrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_indx_arr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 540
            self.match(D96Parser.ARRAY)
            self.state = 541
            self.match(D96Parser.LB)
            self.state = 542
            self.expr_list()
            self.state = 543
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_typeContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type" ):
                return visitor.visitArray_type(self)
            else:
                return visitor.visitChildren(self)




    def array_type(self):

        localctx = D96Parser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 545
            self.match(D96Parser.ARRAY)
            self.state = 546
            self.match(D96Parser.LSB)
            self.state = 547
            self.data_type()
            self.state = 548
            self.match(D96Parser.COM)
            self.state = 549
            self.literal()
            self.state = 550
            self.match(D96Parser.RSB)
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
        self._predicates[27] = self.expr2_sempred
        self._predicates[28] = self.expr3_sempred
        self._predicates[29] = self.expr4_sempred
        self._predicates[34] = self.expr8_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr8_sempred(self, localctx:Expr8Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         




