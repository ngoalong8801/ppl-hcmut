# Generated from main/d95/parser/D95.g4 by ANTLR 4.8
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3A")
        buf.write("\u01b0\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\3\2\3\2\7\2o\n\2\f\2\16\2r\13\2\3")
        buf.write("\2\3\2\3\3\3\3\5\3x\n\3\3\4\3\4\3\4\3\4\5\4~\n\4\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5\u0088\n\5\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\5\7\u0098\n")
        buf.write("\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\n\3\n\5\n\u00a9\n\n\3\13\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\5\f\u00bf\n\f\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00c7\n")
        buf.write("\r\3\16\3\16\3\16\3\16\3\16\5\16\u00ce\n\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\20\3\20")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22")
        buf.write("\3\23\3\23\3\23\3\24\3\24\3\24\3\25\3\25\3\25\5\25\u00f1")
        buf.write("\n\25\3\25\3\25\3\26\3\26\5\26\u00f7\n\26\3\27\3\27\3")
        buf.write("\27\3\27\3\27\5\27\u00fe\n\27\3\30\3\30\3\30\3\30\3\30")
        buf.write("\5\30\u0105\n\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\7")
        buf.write("\31\u010e\n\31\f\31\16\31\u0111\13\31\3\32\3\32\3\32\3")
        buf.write("\32\3\32\3\32\3\32\7\32\u011a\n\32\f\32\16\32\u011d\13")
        buf.write("\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\7\33\u0126\n\33")
        buf.write("\f\33\16\33\u0129\13\33\3\34\3\34\3\34\5\34\u012e\n\34")
        buf.write("\3\35\3\35\3\35\5\35\u0133\n\35\3\36\3\36\3\36\3\36\5")
        buf.write("\36\u0139\n\36\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3 \3 \5")
        buf.write(" \u0146\n \3!\3!\3!\3!\3!\3!\3!\3!\5!\u0150\n!\3\"\3\"")
        buf.write("\5\"\u0154\n\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\5#\u0160")
        buf.write("\n#\3$\3$\3$\5$\u0165\n$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)")
        buf.write("\3)\3*\3*\3+\3+\3+\3+\3+\5+\u0178\n+\3,\3,\3,\5,\u017d")
        buf.write("\n,\3-\3-\3-\3-\3-\3.\3.\3.\3.\3.\3/\3/\3/\3/\3/\3\60")
        buf.write("\3\60\3\60\3\60\3\60\5\60\u0193\n\60\3\61\3\61\3\61\3")
        buf.write("\61\3\62\3\62\3\62\5\62\u019c\n\62\3\63\3\63\3\63\3\63")
        buf.write("\3\63\3\63\5\63\u01a4\n\63\3\64\3\64\3\64\3\64\5\64\u01aa")
        buf.write("\n\64\3\65\3\65\3\66\3\66\3\66\2\5\60\62\64\67\2\4\6\b")
        buf.write("\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668")
        buf.write(":<>@BDFHJLNPRTVXZ\\^`bdfhj\2\13\3\2\t\n\3\2\3\b\3\2\60")
        buf.write("\61\4\2!%..\3\2,-\3\2&\'\3\2(*\3\2\f\17\3\2\32\33\2\u01ab")
        buf.write("\2p\3\2\2\2\4w\3\2\2\2\6}\3\2\2\2\b\u0087\3\2\2\2\n\u0089")
        buf.write("\3\2\2\2\f\u0097\3\2\2\2\16\u0099\3\2\2\2\20\u00a1\3\2")
        buf.write("\2\2\22\u00a8\3\2\2\2\24\u00aa\3\2\2\2\26\u00be\3\2\2")
        buf.write("\2\30\u00c6\3\2\2\2\32\u00c8\3\2\2\2\34\u00d8\3\2\2\2")
        buf.write("\36\u00da\3\2\2\2 \u00dc\3\2\2\2\"\u00e4\3\2\2\2$\u00e7")
        buf.write("\3\2\2\2&\u00ea\3\2\2\2(\u00ed\3\2\2\2*\u00f6\3\2\2\2")
        buf.write(",\u00fd\3\2\2\2.\u0104\3\2\2\2\60\u0106\3\2\2\2\62\u0112")
        buf.write("\3\2\2\2\64\u011e\3\2\2\2\66\u012d\3\2\2\28\u0132\3\2")
        buf.write("\2\2:\u0138\3\2\2\2<\u013a\3\2\2\2>\u0145\3\2\2\2@\u014f")
        buf.write("\3\2\2\2B\u0153\3\2\2\2D\u015f\3\2\2\2F\u0164\3\2\2\2")
        buf.write("H\u0166\3\2\2\2J\u0168\3\2\2\2L\u016a\3\2\2\2N\u016c\3")
        buf.write("\2\2\2P\u016e\3\2\2\2R\u0170\3\2\2\2T\u0177\3\2\2\2V\u017c")
        buf.write("\3\2\2\2X\u017e\3\2\2\2Z\u0183\3\2\2\2\\\u0188\3\2\2\2")
        buf.write("^\u0192\3\2\2\2`\u0194\3\2\2\2b\u019b\3\2\2\2d\u01a3\3")
        buf.write("\2\2\2f\u01a9\3\2\2\2h\u01ab\3\2\2\2j\u01ad\3\2\2\2lo")
        buf.write("\5\4\3\2mo\5\16\b\2nl\3\2\2\2nm\3\2\2\2or\3\2\2\2pn\3")
        buf.write("\2\2\2pq\3\2\2\2qs\3\2\2\2rp\3\2\2\2st\7\2\2\3t\3\3\2")
        buf.write("\2\2ux\5\20\t\2vx\5\n\6\2wu\3\2\2\2wv\3\2\2\2x\5\3\2\2")
        buf.write("\2yz\5\b\5\2z{\5\6\4\2{~\3\2\2\2|~\3\2\2\2}y\3\2\2\2}")
        buf.write("|\3\2\2\2~\7\3\2\2\2\177\u0088\5\24\13\2\u0080\u0088\5")
        buf.write("\20\t\2\u0081\u0088\5\32\16\2\u0082\u0088\5 \21\2\u0083")
        buf.write("\u0088\5\"\22\2\u0084\u0088\5$\23\2\u0085\u0088\5&\24")
        buf.write("\2\u0086\u0088\5(\25\2\u0087\177\3\2\2\2\u0087\u0080\3")
        buf.write("\2\2\2\u0087\u0081\3\2\2\2\u0087\u0082\3\2\2\2\u0087\u0083")
        buf.write("\3\2\2\2\u0087\u0084\3\2\2\2\u0087\u0085\3\2\2\2\u0087")
        buf.write("\u0086\3\2\2\2\u0088\t\3\2\2\2\u0089\u008a\7\31\2\2\u008a")
        buf.write("\u008b\7\13\2\2\u008b\u008c\7\67\2\2\u008c\u008d\5\f\7")
        buf.write("\2\u008d\u008e\78\2\2\u008e\u008f\7;\2\2\u008f\u0090\5")
        buf.write("\6\4\2\u0090\u0091\7<\2\2\u0091\13\3\2\2\2\u0092\u0093")
        buf.write("\7\t\2\2\u0093\u0094\7\64\2\2\u0094\u0098\5\f\7\2\u0095")
        buf.write("\u0098\7\t\2\2\u0096\u0098\3\2\2\2\u0097\u0092\3\2\2\2")
        buf.write("\u0097\u0095\3\2\2\2\u0097\u0096\3\2\2\2\u0098\r\3\2\2")
        buf.write("\2\u0099\u009a\7\35\2\2\u009a\u009b\7\67\2\2\u009b\u009c")
        buf.write("\7\n\2\2\u009c\u009d\7\64\2\2\u009d\u009e\5*\26\2\u009e")
        buf.write("\u009f\78\2\2\u009f\u00a0\7\65\2\2\u00a0\17\3\2\2\2\u00a1")
        buf.write("\u00a2\5\22\n\2\u00a2\u00a3\7/\2\2\u00a3\u00a4\5*\26\2")
        buf.write("\u00a4\u00a5\7\65\2\2\u00a5\21\3\2\2\2\u00a6\u00a9\7\t")
        buf.write("\2\2\u00a7\u00a9\5:\36\2\u00a8\u00a6\3\2\2\2\u00a8\u00a7")
        buf.write("\3\2\2\2\u00a9\23\3\2\2\2\u00aa\u00ab\7\23\2\2\u00ab\u00ac")
        buf.write("\7\67\2\2\u00ac\u00ad\5*\26\2\u00ad\u00ae\78\2\2\u00ae")
        buf.write("\u00af\7;\2\2\u00af\u00b0\5\6\4\2\u00b0\u00b1\7<\2\2\u00b1")
        buf.write("\u00b2\5\26\f\2\u00b2\u00b3\5\30\r\2\u00b3\25\3\2\2\2")
        buf.write("\u00b4\u00b5\7\24\2\2\u00b5\u00b6\7\67\2\2\u00b6\u00b7")
        buf.write("\5*\26\2\u00b7\u00b8\78\2\2\u00b8\u00b9\7;\2\2\u00b9\u00ba")
        buf.write("\5\6\4\2\u00ba\u00bb\7<\2\2\u00bb\u00bc\5\26\f\2\u00bc")
        buf.write("\u00bf\3\2\2\2\u00bd\u00bf\3\2\2\2\u00be\u00b4\3\2\2\2")
        buf.write("\u00be\u00bd\3\2\2\2\u00bf\27\3\2\2\2\u00c0\u00c1\7\25")
        buf.write("\2\2\u00c1\u00c2\7;\2\2\u00c2\u00c3\5\6\4\2\u00c3\u00c4")
        buf.write("\7<\2\2\u00c4\u00c7\3\2\2\2\u00c5\u00c7\3\2\2\2\u00c6")
        buf.write("\u00c0\3\2\2\2\u00c6\u00c5\3\2\2\2\u00c7\31\3\2\2\2\u00c8")
        buf.write("\u00c9\7\27\2\2\u00c9\u00cd\7\67\2\2\u00ca\u00ce\7\t\2")
        buf.write("\2\u00cb\u00ce\7\n\2\2\u00cc\u00ce\5V,\2\u00cd\u00ca\3")
        buf.write("\2\2\2\u00cd\u00cb\3\2\2\2\u00cd\u00cc\3\2\2\2\u00ce\u00cf")
        buf.write("\3\2\2\2\u00cf\u00d0\7\30\2\2\u00d0\u00d1\5\34\17\2\u00d1")
        buf.write("\u00d2\7\62\2\2\u00d2\u00d3\5\36\20\2\u00d3\u00d4\78\2")
        buf.write("\2\u00d4\u00d5\7;\2\2\u00d5\u00d6\5\6\4\2\u00d6\u00d7")
        buf.write("\7<\2\2\u00d7\33\3\2\2\2\u00d8\u00d9\t\2\2\2\u00d9\35")
        buf.write("\3\2\2\2\u00da\u00db\t\2\2\2\u00db\37\3\2\2\2\u00dc\u00dd")
        buf.write("\7\26\2\2\u00dd\u00de\7\67\2\2\u00de\u00df\5*\26\2\u00df")
        buf.write("\u00e0\78\2\2\u00e0\u00e1\7;\2\2\u00e1\u00e2\5\6\4\2\u00e2")
        buf.write("\u00e3\7<\2\2\u00e3!\3\2\2\2\u00e4\u00e5\7\21\2\2\u00e5")
        buf.write("\u00e6\7\65\2\2\u00e6#\3\2\2\2\u00e7\u00e8\7\22\2\2\u00e8")
        buf.write("\u00e9\7\65\2\2\u00e9%\3\2\2\2\u00ea\u00eb\5B\"\2\u00eb")
        buf.write("\u00ec\7\65\2\2\u00ec\'\3\2\2\2\u00ed\u00f0\7\36\2\2\u00ee")
        buf.write("\u00f1\5*\26\2\u00ef\u00f1\3\2\2\2\u00f0\u00ee\3\2\2\2")
        buf.write("\u00f0\u00ef\3\2\2\2\u00f1\u00f2\3\2\2\2\u00f2\u00f3\7")
        buf.write("\65\2\2\u00f3)\3\2\2\2\u00f4\u00f7\5,\27\2\u00f5\u00f7")
        buf.write("\5V,\2\u00f6\u00f4\3\2\2\2\u00f6\u00f5\3\2\2\2\u00f7+")
        buf.write("\3\2\2\2\u00f8\u00f9\5.\30\2\u00f9\u00fa\5J&\2\u00fa\u00fb")
        buf.write("\5.\30\2\u00fb\u00fe\3\2\2\2\u00fc\u00fe\5.\30\2\u00fd")
        buf.write("\u00f8\3\2\2\2\u00fd\u00fc\3\2\2\2\u00fe-\3\2\2\2\u00ff")
        buf.write("\u0100\5\60\31\2\u0100\u0101\5L\'\2\u0101\u0102\5\60\31")
        buf.write("\2\u0102\u0105\3\2\2\2\u0103\u0105\5\60\31\2\u0104\u00ff")
        buf.write("\3\2\2\2\u0104\u0103\3\2\2\2\u0105/\3\2\2\2\u0106\u0107")
        buf.write("\b\31\1\2\u0107\u0108\5\62\32\2\u0108\u010f\3\2\2\2\u0109")
        buf.write("\u010a\f\4\2\2\u010a\u010b\5N(\2\u010b\u010c\5\62\32\2")
        buf.write("\u010c\u010e\3\2\2\2\u010d\u0109\3\2\2\2\u010e\u0111\3")
        buf.write("\2\2\2\u010f\u010d\3\2\2\2\u010f\u0110\3\2\2\2\u0110\61")
        buf.write("\3\2\2\2\u0111\u010f\3\2\2\2\u0112\u0113\b\32\1\2\u0113")
        buf.write("\u0114\5\64\33\2\u0114\u011b\3\2\2\2\u0115\u0116\f\4\2")
        buf.write("\2\u0116\u0117\5P)\2\u0117\u0118\5\64\33\2\u0118\u011a")
        buf.write("\3\2\2\2\u0119\u0115\3\2\2\2\u011a\u011d\3\2\2\2\u011b")
        buf.write("\u0119\3\2\2\2\u011b\u011c\3\2\2\2\u011c\63\3\2\2\2\u011d")
        buf.write("\u011b\3\2\2\2\u011e\u011f\b\33\1\2\u011f\u0120\5\66\34")
        buf.write("\2\u0120\u0127\3\2\2\2\u0121\u0122\f\4\2\2\u0122\u0123")
        buf.write("\5R*\2\u0123\u0124\5\66\34\2\u0124\u0126\3\2\2\2\u0125")
        buf.write("\u0121\3\2\2\2\u0126\u0129\3\2\2\2\u0127\u0125\3\2\2\2")
        buf.write("\u0127\u0128\3\2\2\2\u0128\65\3\2\2\2\u0129\u0127\3\2")
        buf.write("\2\2\u012a\u012b\7+\2\2\u012b\u012e\5\66\34\2\u012c\u012e")
        buf.write("\58\35\2\u012d\u012a\3\2\2\2\u012d\u012c\3\2\2\2\u012e")
        buf.write("\67\3\2\2\2\u012f\u0130\7\'\2\2\u0130\u0133\58\35\2\u0131")
        buf.write("\u0133\5:\36\2\u0132\u012f\3\2\2\2\u0132\u0131\3\2\2\2")
        buf.write("\u01339\3\2\2\2\u0134\u0135\5<\37\2\u0135\u0136\5> \2")
        buf.write("\u0136\u0139\3\2\2\2\u0137\u0139\5@!\2\u0138\u0134\3\2")
        buf.write("\2\2\u0138\u0137\3\2\2\2\u0139;\3\2\2\2\u013a\u013b\t")
        buf.write("\2\2\2\u013b=\3\2\2\2\u013c\u013d\79\2\2\u013d\u013e\5")
        buf.write(",\27\2\u013e\u013f\7:\2\2\u013f\u0146\3\2\2\2\u0140\u0141")
        buf.write("\79\2\2\u0141\u0142\5,\27\2\u0142\u0143\7:\2\2\u0143\u0144")
        buf.write("\5> \2\u0144\u0146\3\2\2\2\u0145\u013c\3\2\2\2\u0145\u0140")
        buf.write("\3\2\2\2\u0146?\3\2\2\2\u0147\u0150\5f\64\2\u0148\u0150")
        buf.write("\7\t\2\2\u0149\u0150\7\n\2\2\u014a\u0150\5B\"\2\u014b")
        buf.write("\u014c\7\67\2\2\u014c\u014d\5*\26\2\u014d\u014e\78\2\2")
        buf.write("\u014e\u0150\3\2\2\2\u014f\u0147\3\2\2\2\u014f\u0148\3")
        buf.write("\2\2\2\u014f\u0149\3\2\2\2\u014f\u014a\3\2\2\2\u014f\u014b")
        buf.write("\3\2\2\2\u0150A\3\2\2\2\u0151\u0154\7\13\2\2\u0152\u0154")
        buf.write("\5H%\2\u0153\u0151\3\2\2\2\u0153\u0152\3\2\2\2\u0154\u0155")
        buf.write("\3\2\2\2\u0155\u0156\7\67\2\2\u0156\u0157\5D#\2\u0157")
        buf.write("\u0158\78\2\2\u0158C\3\2\2\2\u0159\u015a\5F$\2\u015a\u015b")
        buf.write("\7\64\2\2\u015b\u015c\5D#\2\u015c\u0160\3\2\2\2\u015d")
        buf.write("\u0160\5F$\2\u015e\u0160\3\2\2\2\u015f\u0159\3\2\2\2\u015f")
        buf.write("\u015d\3\2\2\2\u015f\u015e\3\2\2\2\u0160E\3\2\2\2\u0161")
        buf.write("\u0165\5f\64\2\u0162\u0165\7\t\2\2\u0163\u0165\5*\26\2")
        buf.write("\u0164\u0161\3\2\2\2\u0164\u0162\3\2\2\2\u0164\u0163\3")
        buf.write("\2\2\2\u0165G\3\2\2\2\u0166\u0167\t\3\2\2\u0167I\3\2\2")
        buf.write("\2\u0168\u0169\t\4\2\2\u0169K\3\2\2\2\u016a\u016b\t\5")
        buf.write("\2\2\u016bM\3\2\2\2\u016c\u016d\t\6\2\2\u016dO\3\2\2\2")
        buf.write("\u016e\u016f\t\7\2\2\u016fQ\3\2\2\2\u0170\u0171\t\b\2")
        buf.write("\2\u0171S\3\2\2\2\u0172\u0173\5V,\2\u0173\u0174\7\64\2")
        buf.write("\2\u0174\u0175\5T+\2\u0175\u0178\3\2\2\2\u0176\u0178\5")
        buf.write("V,\2\u0177\u0172\3\2\2\2\u0177\u0176\3\2\2\2\u0178U\3")
        buf.write("\2\2\2\u0179\u017d\5X-\2\u017a\u017d\5Z.\2\u017b\u017d")
        buf.write("\5\\/\2\u017c\u0179\3\2\2\2\u017c\u017a\3\2\2\2\u017c")
        buf.write("\u017b\3\2\2\2\u017dW\3\2\2\2\u017e\u017f\7\34\2\2\u017f")
        buf.write("\u0180\7\67\2\2\u0180\u0181\5d\63\2\u0181\u0182\78\2\2")
        buf.write("\u0182Y\3\2\2\2\u0183\u0184\7\34\2\2\u0184\u0185\7\67")
        buf.write("\2\2\u0185\u0186\5^\60\2\u0186\u0187\78\2\2\u0187[\3\2")
        buf.write("\2\2\u0188\u0189\7\34\2\2\u0189\u018a\7\67\2\2\u018a\u018b")
        buf.write("\5T+\2\u018b\u018c\78\2\2\u018c]\3\2\2\2\u018d\u018e\5")
        buf.write("`\61\2\u018e\u018f\7\64\2\2\u018f\u0190\5^\60\2\u0190")
        buf.write("\u0193\3\2\2\2\u0191\u0193\5`\61\2\u0192\u018d\3\2\2\2")
        buf.write("\u0192\u0191\3\2\2\2\u0193_\3\2\2\2\u0194\u0195\5b\62")
        buf.write("\2\u0195\u0196\7\62\2\2\u0196\u0197\5*\26\2\u0197a\3\2")
        buf.write("\2\2\u0198\u019c\5h\65\2\u0199\u019c\7 \2\2\u019a\u019c")
        buf.write("\7\t\2\2\u019b\u0198\3\2\2\2\u019b\u0199\3\2\2\2\u019b")
        buf.write("\u019a\3\2\2\2\u019cc\3\2\2\2\u019d\u019e\5f\64\2\u019e")
        buf.write("\u019f\7\64\2\2\u019f\u01a0\5d\63\2\u01a0\u01a4\3\2\2")
        buf.write("\2\u01a1\u01a4\5f\64\2\u01a2\u01a4\3\2\2\2\u01a3\u019d")
        buf.write("\3\2\2\2\u01a3\u01a1\3\2\2\2\u01a3\u01a2\3\2\2\2\u01a4")
        buf.write("e\3\2\2\2\u01a5\u01aa\5h\65\2\u01a6\u01aa\7\20\2\2\u01a7")
        buf.write("\u01aa\5j\66\2\u01a8\u01aa\7 \2\2\u01a9\u01a5\3\2\2\2")
        buf.write("\u01a9\u01a6\3\2\2\2\u01a9\u01a7\3\2\2\2\u01a9\u01a8\3")
        buf.write("\2\2\2\u01aag\3\2\2\2\u01ab\u01ac\t\t\2\2\u01aci\3\2\2")
        buf.write("\2\u01ad\u01ae\t\n\2\2\u01aek\3\2\2\2!npw}\u0087\u0097")
        buf.write("\u00a8\u00be\u00c6\u00cd\u00f0\u00f6\u00fd\u0104\u010f")
        buf.write("\u011b\u0127\u012d\u0132\u0138\u0145\u014f\u0153\u015f")
        buf.write("\u0164\u0177\u017c\u0192\u019b\u01a3\u01a9")
        return buf.getvalue()


class D95Parser ( Parser ):

    grammarFileName = "D95.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'str2int'", "'int2str'", "'str2float'", 
                     "'float2str'", "'str2bool'", "'bool2str'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'break'", "'continue'", 
                     "'if'", "'elseif'", "'else'", "'while'", "'foreach'", 
                     "'as'", "'function'", "'true'", "'false'", "'array'", 
                     "'define'", "'return'", "<INVALID>", "<INVALID>", "'!='", 
                     "'>'", "'>='", "'<'", "'<='", "'+'", "'-'", "'*'", 
                     "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", "'='", 
                     "'==.'", "'+.'", "'=>'", "'.'", "','", "';'", "':'", 
                     "'('", "')'", "'['", "']'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "STR2INT", "INT2STR", "STR2FLOAT", "FLOAT2STR", 
                      "STR2BOOL", "BOOL2STR", "ID_VARPAR", "ID_CONST", "ID_FUNC", 
                      "OCT", "DEC", "HEX", "BIN", "FLOAT", "BREAK", "CONTINUE", 
                      "IF", "ELSEIF", "ElSE", "WHILE", "FOREACH", "AS", 
                      "FUNCTION", "TRUE", "FALSE", "ARRAY_TYPE", "DEFINE", 
                      "RETURN", "ILLEGAL_ESCAPE", "STRING", "NOT_EQUAL", 
                      "GREATER", "GREATER_EQUAL", "LESS", "LESS_EQUAL", 
                      "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", "AND", "OR", 
                      "EQUAL", "ASSIGN", "STR_CMP", "STR_CAT", "ASSOCATE", 
                      "DOT", "COMMA", "SEMI", "COLON", "LP", "RP", "LSB", 
                      "RSB", "LB", "RB", "COMMENT", "WS", "ERROR_CHAR", 
                      "UNCLOSE_STRING", "UNTERMINATED_COMMENT" ]

    RULE_program = 0
    RULE_non_constdecl = 1
    RULE_list_stmt = 2
    RULE_stmt = 3
    RULE_funcdecl = 4
    RULE_decl_param = 5
    RULE_constdecl = 6
    RULE_stmt_assign = 7
    RULE_lhs = 8
    RULE_stmt_if = 9
    RULE_stmt_elseif = 10
    RULE_stmt_else = 11
    RULE_stmt_foreach = 12
    RULE_key_for = 13
    RULE_value_for = 14
    RULE_stmt_while = 15
    RULE_stmt_break = 16
    RULE_stmt_continue = 17
    RULE_stmt_call = 18
    RULE_stmt_return = 19
    RULE_expr = 20
    RULE_expr_1 = 21
    RULE_expr_2 = 22
    RULE_expr_3 = 23
    RULE_expr_4 = 24
    RULE_expr_5 = 25
    RULE_expr_6 = 26
    RULE_expr_7 = 27
    RULE_expr_8 = 28
    RULE_operand_index = 29
    RULE_index_operator = 30
    RULE_operand = 31
    RULE_func_call = 32
    RULE_list_param = 33
    RULE_param = 34
    RULE_type_coersion = 35
    RULE_op_string = 36
    RULE_op_relation = 37
    RULE_op_andor = 38
    RULE_op_adding = 39
    RULE_op_multiplyng = 40
    RULE_listARRAY = 41
    RULE_array = 42
    RULE_i_array = 43
    RULE_a_array = 44
    RULE_m_array = 45
    RULE_listKV = 46
    RULE_keyValue = 47
    RULE_key = 48
    RULE_listLIT = 49
    RULE_literal = 50
    RULE_integer = 51
    RULE_boolean = 52

    ruleNames =  [ "program", "non_constdecl", "list_stmt", "stmt", "funcdecl", 
                   "decl_param", "constdecl", "stmt_assign", "lhs", "stmt_if", 
                   "stmt_elseif", "stmt_else", "stmt_foreach", "key_for", 
                   "value_for", "stmt_while", "stmt_break", "stmt_continue", 
                   "stmt_call", "stmt_return", "expr", "expr_1", "expr_2", 
                   "expr_3", "expr_4", "expr_5", "expr_6", "expr_7", "expr_8", 
                   "operand_index", "index_operator", "operand", "func_call", 
                   "list_param", "param", "type_coersion", "op_string", 
                   "op_relation", "op_andor", "op_adding", "op_multiplyng", 
                   "listARRAY", "array", "i_array", "a_array", "m_array", 
                   "listKV", "keyValue", "key", "listLIT", "literal", "integer", 
                   "boolean" ]

    EOF = Token.EOF
    STR2INT=1
    INT2STR=2
    STR2FLOAT=3
    FLOAT2STR=4
    STR2BOOL=5
    BOOL2STR=6
    ID_VARPAR=7
    ID_CONST=8
    ID_FUNC=9
    OCT=10
    DEC=11
    HEX=12
    BIN=13
    FLOAT=14
    BREAK=15
    CONTINUE=16
    IF=17
    ELSEIF=18
    ElSE=19
    WHILE=20
    FOREACH=21
    AS=22
    FUNCTION=23
    TRUE=24
    FALSE=25
    ARRAY_TYPE=26
    DEFINE=27
    RETURN=28
    ILLEGAL_ESCAPE=29
    STRING=30
    NOT_EQUAL=31
    GREATER=32
    GREATER_EQUAL=33
    LESS=34
    LESS_EQUAL=35
    ADD=36
    SUB=37
    MUL=38
    DIV=39
    MOD=40
    NOT=41
    AND=42
    OR=43
    EQUAL=44
    ASSIGN=45
    STR_CMP=46
    STR_CAT=47
    ASSOCATE=48
    DOT=49
    COMMA=50
    SEMI=51
    COLON=52
    LP=53
    RP=54
    LSB=55
    RSB=56
    LB=57
    RB=58
    COMMENT=59
    WS=60
    ERROR_CHAR=61
    UNCLOSE_STRING=62
    UNTERMINATED_COMMENT=63

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(D95Parser.EOF, 0)

        def non_constdecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D95Parser.Non_constdeclContext)
            else:
                return self.getTypedRuleContext(D95Parser.Non_constdeclContext,i)


        def constdecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D95Parser.ConstdeclContext)
            else:
                return self.getTypedRuleContext(D95Parser.ConstdeclContext,i)


        def getRuleIndex(self):
            return D95Parser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = D95Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D95Parser.STR2INT) | (1 << D95Parser.INT2STR) | (1 << D95Parser.STR2FLOAT) | (1 << D95Parser.FLOAT2STR) | (1 << D95Parser.STR2BOOL) | (1 << D95Parser.BOOL2STR) | (1 << D95Parser.ID_VARPAR) | (1 << D95Parser.ID_CONST) | (1 << D95Parser.ID_FUNC) | (1 << D95Parser.OCT) | (1 << D95Parser.DEC) | (1 << D95Parser.HEX) | (1 << D95Parser.BIN) | (1 << D95Parser.FLOAT) | (1 << D95Parser.FUNCTION) | (1 << D95Parser.TRUE) | (1 << D95Parser.FALSE) | (1 << D95Parser.DEFINE) | (1 << D95Parser.STRING) | (1 << D95Parser.LP))) != 0):
                self.state = 108
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D95Parser.STR2INT, D95Parser.INT2STR, D95Parser.STR2FLOAT, D95Parser.FLOAT2STR, D95Parser.STR2BOOL, D95Parser.BOOL2STR, D95Parser.ID_VARPAR, D95Parser.ID_CONST, D95Parser.ID_FUNC, D95Parser.OCT, D95Parser.DEC, D95Parser.HEX, D95Parser.BIN, D95Parser.FLOAT, D95Parser.FUNCTION, D95Parser.TRUE, D95Parser.FALSE, D95Parser.STRING, D95Parser.LP]:
                    self.state = 106
                    self.non_constdecl()
                    pass
                elif token in [D95Parser.DEFINE]:
                    self.state = 107
                    self.constdecl()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 112
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 113
            self.match(D95Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Non_constdeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt_assign(self):
            return self.getTypedRuleContext(D95Parser.Stmt_assignContext,0)


        def funcdecl(self):
            return self.getTypedRuleContext(D95Parser.FuncdeclContext,0)


        def getRuleIndex(self):
            return D95Parser.RULE_non_constdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNon_constdecl" ):
                return visitor.visitNon_constdecl(self)
            else:
                return visitor.visitChildren(self)




    def non_constdecl(self):

        localctx = D95Parser.Non_constdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_non_constdecl)
        try:
            self.state = 117
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D95Parser.STR2INT, D95Parser.INT2STR, D95Parser.STR2FLOAT, D95Parser.FLOAT2STR, D95Parser.STR2BOOL, D95Parser.BOOL2STR, D95Parser.ID_VARPAR, D95Parser.ID_CONST, D95Parser.ID_FUNC, D95Parser.OCT, D95Parser.DEC, D95Parser.HEX, D95Parser.BIN, D95Parser.FLOAT, D95Parser.TRUE, D95Parser.FALSE, D95Parser.STRING, D95Parser.LP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 115
                self.stmt_assign()
                pass
            elif token in [D95Parser.FUNCTION]:
                self.enterOuterAlt(localctx, 2)
                self.state = 116
                self.funcdecl()
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


    class List_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(D95Parser.StmtContext,0)


        def list_stmt(self):
            return self.getTypedRuleContext(D95Parser.List_stmtContext,0)


        def getRuleIndex(self):
            return D95Parser.RULE_list_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_stmt" ):
                return visitor.visitList_stmt(self)
            else:
                return visitor.visitChildren(self)




    def list_stmt(self):

        localctx = D95Parser.List_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_list_stmt)
        try:
            self.state = 123
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D95Parser.STR2INT, D95Parser.INT2STR, D95Parser.STR2FLOAT, D95Parser.FLOAT2STR, D95Parser.STR2BOOL, D95Parser.BOOL2STR, D95Parser.ID_VARPAR, D95Parser.ID_CONST, D95Parser.ID_FUNC, D95Parser.OCT, D95Parser.DEC, D95Parser.HEX, D95Parser.BIN, D95Parser.FLOAT, D95Parser.BREAK, D95Parser.CONTINUE, D95Parser.IF, D95Parser.WHILE, D95Parser.FOREACH, D95Parser.TRUE, D95Parser.FALSE, D95Parser.RETURN, D95Parser.STRING, D95Parser.LP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 119
                self.stmt()
                self.state = 120
                self.list_stmt()
                pass
            elif token in [D95Parser.RB]:
                self.enterOuterAlt(localctx, 2)

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


    class StmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt_if(self):
            return self.getTypedRuleContext(D95Parser.Stmt_ifContext,0)


        def stmt_assign(self):
            return self.getTypedRuleContext(D95Parser.Stmt_assignContext,0)


        def stmt_foreach(self):
            return self.getTypedRuleContext(D95Parser.Stmt_foreachContext,0)


        def stmt_while(self):
            return self.getTypedRuleContext(D95Parser.Stmt_whileContext,0)


        def stmt_break(self):
            return self.getTypedRuleContext(D95Parser.Stmt_breakContext,0)


        def stmt_continue(self):
            return self.getTypedRuleContext(D95Parser.Stmt_continueContext,0)


        def stmt_call(self):
            return self.getTypedRuleContext(D95Parser.Stmt_callContext,0)


        def stmt_return(self):
            return self.getTypedRuleContext(D95Parser.Stmt_returnContext,0)


        def getRuleIndex(self):
            return D95Parser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = D95Parser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_stmt)
        try:
            self.state = 133
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 125
                self.stmt_if()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 126
                self.stmt_assign()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 127
                self.stmt_foreach()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 128
                self.stmt_while()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 129
                self.stmt_break()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 130
                self.stmt_continue()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 131
                self.stmt_call()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 132
                self.stmt_return()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(D95Parser.FUNCTION, 0)

        def ID_FUNC(self):
            return self.getToken(D95Parser.ID_FUNC, 0)

        def LP(self):
            return self.getToken(D95Parser.LP, 0)

        def decl_param(self):
            return self.getTypedRuleContext(D95Parser.Decl_paramContext,0)


        def RP(self):
            return self.getToken(D95Parser.RP, 0)

        def LB(self):
            return self.getToken(D95Parser.LB, 0)

        def list_stmt(self):
            return self.getTypedRuleContext(D95Parser.List_stmtContext,0)


        def RB(self):
            return self.getToken(D95Parser.RB, 0)

        def getRuleIndex(self):
            return D95Parser.RULE_funcdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncdecl" ):
                return visitor.visitFuncdecl(self)
            else:
                return visitor.visitChildren(self)




    def funcdecl(self):

        localctx = D95Parser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_funcdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(D95Parser.FUNCTION)
            self.state = 136
            self.match(D95Parser.ID_FUNC)
            self.state = 137
            self.match(D95Parser.LP)
            self.state = 138
            self.decl_param()
            self.state = 139
            self.match(D95Parser.RP)
            self.state = 140
            self.match(D95Parser.LB)
            self.state = 141
            self.list_stmt()
            self.state = 142
            self.match(D95Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decl_paramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID_VARPAR(self):
            return self.getToken(D95Parser.ID_VARPAR, 0)

        def COMMA(self):
            return self.getToken(D95Parser.COMMA, 0)

        def decl_param(self):
            return self.getTypedRuleContext(D95Parser.Decl_paramContext,0)


        def getRuleIndex(self):
            return D95Parser.RULE_decl_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl_param" ):
                return visitor.visitDecl_param(self)
            else:
                return visitor.visitChildren(self)




    def decl_param(self):

        localctx = D95Parser.Decl_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_decl_param)
        try:
            self.state = 149
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 144
                self.match(D95Parser.ID_VARPAR)
                self.state = 145
                self.match(D95Parser.COMMA)
                self.state = 146
                self.decl_param()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 147
                self.match(D95Parser.ID_VARPAR)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstdeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEFINE(self):
            return self.getToken(D95Parser.DEFINE, 0)

        def LP(self):
            return self.getToken(D95Parser.LP, 0)

        def ID_CONST(self):
            return self.getToken(D95Parser.ID_CONST, 0)

        def COMMA(self):
            return self.getToken(D95Parser.COMMA, 0)

        def expr(self):
            return self.getTypedRuleContext(D95Parser.ExprContext,0)


        def RP(self):
            return self.getToken(D95Parser.RP, 0)

        def SEMI(self):
            return self.getToken(D95Parser.SEMI, 0)

        def getRuleIndex(self):
            return D95Parser.RULE_constdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstdecl" ):
                return visitor.visitConstdecl(self)
            else:
                return visitor.visitChildren(self)




    def constdecl(self):

        localctx = D95Parser.ConstdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_constdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.match(D95Parser.DEFINE)
            self.state = 152
            self.match(D95Parser.LP)
            self.state = 153
            self.match(D95Parser.ID_CONST)
            self.state = 154
            self.match(D95Parser.COMMA)
            self.state = 155
            self.expr()
            self.state = 156
            self.match(D95Parser.RP)
            self.state = 157
            self.match(D95Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_assignContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(D95Parser.LhsContext,0)


        def ASSIGN(self):
            return self.getToken(D95Parser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(D95Parser.ExprContext,0)


        def SEMI(self):
            return self.getToken(D95Parser.SEMI, 0)

        def getRuleIndex(self):
            return D95Parser.RULE_stmt_assign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_assign" ):
                return visitor.visitStmt_assign(self)
            else:
                return visitor.visitChildren(self)




    def stmt_assign(self):

        localctx = D95Parser.Stmt_assignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_stmt_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.lhs()
            self.state = 160
            self.match(D95Parser.ASSIGN)
            self.state = 161
            self.expr()
            self.state = 162
            self.match(D95Parser.SEMI)
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

        def ID_VARPAR(self):
            return self.getToken(D95Parser.ID_VARPAR, 0)

        def expr_8(self):
            return self.getTypedRuleContext(D95Parser.Expr_8Context,0)


        def getRuleIndex(self):
            return D95Parser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = D95Parser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_lhs)
        try:
            self.state = 166
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 164
                self.match(D95Parser.ID_VARPAR)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 165
                self.expr_8()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_ifContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(D95Parser.IF, 0)

        def LP(self):
            return self.getToken(D95Parser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(D95Parser.ExprContext,0)


        def RP(self):
            return self.getToken(D95Parser.RP, 0)

        def LB(self):
            return self.getToken(D95Parser.LB, 0)

        def list_stmt(self):
            return self.getTypedRuleContext(D95Parser.List_stmtContext,0)


        def RB(self):
            return self.getToken(D95Parser.RB, 0)

        def stmt_elseif(self):
            return self.getTypedRuleContext(D95Parser.Stmt_elseifContext,0)


        def stmt_else(self):
            return self.getTypedRuleContext(D95Parser.Stmt_elseContext,0)


        def getRuleIndex(self):
            return D95Parser.RULE_stmt_if

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_if" ):
                return visitor.visitStmt_if(self)
            else:
                return visitor.visitChildren(self)




    def stmt_if(self):

        localctx = D95Parser.Stmt_ifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_stmt_if)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.match(D95Parser.IF)
            self.state = 169
            self.match(D95Parser.LP)
            self.state = 170
            self.expr()
            self.state = 171
            self.match(D95Parser.RP)
            self.state = 172
            self.match(D95Parser.LB)
            self.state = 173
            self.list_stmt()
            self.state = 174
            self.match(D95Parser.RB)
            self.state = 175
            self.stmt_elseif()
            self.state = 176
            self.stmt_else()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_elseifContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSEIF(self):
            return self.getToken(D95Parser.ELSEIF, 0)

        def LP(self):
            return self.getToken(D95Parser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(D95Parser.ExprContext,0)


        def RP(self):
            return self.getToken(D95Parser.RP, 0)

        def LB(self):
            return self.getToken(D95Parser.LB, 0)

        def list_stmt(self):
            return self.getTypedRuleContext(D95Parser.List_stmtContext,0)


        def RB(self):
            return self.getToken(D95Parser.RB, 0)

        def stmt_elseif(self):
            return self.getTypedRuleContext(D95Parser.Stmt_elseifContext,0)


        def getRuleIndex(self):
            return D95Parser.RULE_stmt_elseif

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_elseif" ):
                return visitor.visitStmt_elseif(self)
            else:
                return visitor.visitChildren(self)




    def stmt_elseif(self):

        localctx = D95Parser.Stmt_elseifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_stmt_elseif)
        try:
            self.state = 188
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D95Parser.ELSEIF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 178
                self.match(D95Parser.ELSEIF)
                self.state = 179
                self.match(D95Parser.LP)
                self.state = 180
                self.expr()
                self.state = 181
                self.match(D95Parser.RP)
                self.state = 182
                self.match(D95Parser.LB)
                self.state = 183
                self.list_stmt()
                self.state = 184
                self.match(D95Parser.RB)
                self.state = 185
                self.stmt_elseif()
                pass
            elif token in [D95Parser.STR2INT, D95Parser.INT2STR, D95Parser.STR2FLOAT, D95Parser.FLOAT2STR, D95Parser.STR2BOOL, D95Parser.BOOL2STR, D95Parser.ID_VARPAR, D95Parser.ID_CONST, D95Parser.ID_FUNC, D95Parser.OCT, D95Parser.DEC, D95Parser.HEX, D95Parser.BIN, D95Parser.FLOAT, D95Parser.BREAK, D95Parser.CONTINUE, D95Parser.IF, D95Parser.ElSE, D95Parser.WHILE, D95Parser.FOREACH, D95Parser.TRUE, D95Parser.FALSE, D95Parser.RETURN, D95Parser.STRING, D95Parser.LP, D95Parser.RB]:
                self.enterOuterAlt(localctx, 2)

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


    class Stmt_elseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ElSE(self):
            return self.getToken(D95Parser.ElSE, 0)

        def LB(self):
            return self.getToken(D95Parser.LB, 0)

        def list_stmt(self):
            return self.getTypedRuleContext(D95Parser.List_stmtContext,0)


        def RB(self):
            return self.getToken(D95Parser.RB, 0)

        def getRuleIndex(self):
            return D95Parser.RULE_stmt_else

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_else" ):
                return visitor.visitStmt_else(self)
            else:
                return visitor.visitChildren(self)




    def stmt_else(self):

        localctx = D95Parser.Stmt_elseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_stmt_else)
        try:
            self.state = 196
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D95Parser.ElSE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 190
                self.match(D95Parser.ElSE)
                self.state = 191
                self.match(D95Parser.LB)
                self.state = 192
                self.list_stmt()
                self.state = 193
                self.match(D95Parser.RB)
                pass
            elif token in [D95Parser.STR2INT, D95Parser.INT2STR, D95Parser.STR2FLOAT, D95Parser.FLOAT2STR, D95Parser.STR2BOOL, D95Parser.BOOL2STR, D95Parser.ID_VARPAR, D95Parser.ID_CONST, D95Parser.ID_FUNC, D95Parser.OCT, D95Parser.DEC, D95Parser.HEX, D95Parser.BIN, D95Parser.FLOAT, D95Parser.BREAK, D95Parser.CONTINUE, D95Parser.IF, D95Parser.WHILE, D95Parser.FOREACH, D95Parser.TRUE, D95Parser.FALSE, D95Parser.RETURN, D95Parser.STRING, D95Parser.LP, D95Parser.RB]:
                self.enterOuterAlt(localctx, 2)

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


    class Stmt_foreachContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOREACH(self):
            return self.getToken(D95Parser.FOREACH, 0)

        def LP(self):
            return self.getToken(D95Parser.LP, 0)

        def AS(self):
            return self.getToken(D95Parser.AS, 0)

        def key_for(self):
            return self.getTypedRuleContext(D95Parser.Key_forContext,0)


        def ASSOCATE(self):
            return self.getToken(D95Parser.ASSOCATE, 0)

        def value_for(self):
            return self.getTypedRuleContext(D95Parser.Value_forContext,0)


        def RP(self):
            return self.getToken(D95Parser.RP, 0)

        def LB(self):
            return self.getToken(D95Parser.LB, 0)

        def list_stmt(self):
            return self.getTypedRuleContext(D95Parser.List_stmtContext,0)


        def RB(self):
            return self.getToken(D95Parser.RB, 0)

        def ID_VARPAR(self):
            return self.getToken(D95Parser.ID_VARPAR, 0)

        def ID_CONST(self):
            return self.getToken(D95Parser.ID_CONST, 0)

        def array(self):
            return self.getTypedRuleContext(D95Parser.ArrayContext,0)


        def getRuleIndex(self):
            return D95Parser.RULE_stmt_foreach

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_foreach" ):
                return visitor.visitStmt_foreach(self)
            else:
                return visitor.visitChildren(self)




    def stmt_foreach(self):

        localctx = D95Parser.Stmt_foreachContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_stmt_foreach)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.match(D95Parser.FOREACH)
            self.state = 199
            self.match(D95Parser.LP)
            self.state = 203
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D95Parser.ID_VARPAR]:
                self.state = 200
                self.match(D95Parser.ID_VARPAR)
                pass
            elif token in [D95Parser.ID_CONST]:
                self.state = 201
                self.match(D95Parser.ID_CONST)
                pass
            elif token in [D95Parser.ARRAY_TYPE]:
                self.state = 202
                self.array()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 205
            self.match(D95Parser.AS)
            self.state = 206
            self.key_for()
            self.state = 207
            self.match(D95Parser.ASSOCATE)
            self.state = 208
            self.value_for()
            self.state = 209
            self.match(D95Parser.RP)
            self.state = 210
            self.match(D95Parser.LB)
            self.state = 211
            self.list_stmt()
            self.state = 212
            self.match(D95Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Key_forContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID_VARPAR(self):
            return self.getToken(D95Parser.ID_VARPAR, 0)

        def ID_CONST(self):
            return self.getToken(D95Parser.ID_CONST, 0)

        def getRuleIndex(self):
            return D95Parser.RULE_key_for

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKey_for" ):
                return visitor.visitKey_for(self)
            else:
                return visitor.visitChildren(self)




    def key_for(self):

        localctx = D95Parser.Key_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_key_for)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            _la = self._input.LA(1)
            if not(_la==D95Parser.ID_VARPAR or _la==D95Parser.ID_CONST):
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


    class Value_forContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID_VARPAR(self):
            return self.getToken(D95Parser.ID_VARPAR, 0)

        def ID_CONST(self):
            return self.getToken(D95Parser.ID_CONST, 0)

        def getRuleIndex(self):
            return D95Parser.RULE_value_for

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue_for" ):
                return visitor.visitValue_for(self)
            else:
                return visitor.visitChildren(self)




    def value_for(self):

        localctx = D95Parser.Value_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_value_for)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            _la = self._input.LA(1)
            if not(_la==D95Parser.ID_VARPAR or _la==D95Parser.ID_CONST):
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


    class Stmt_whileContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(D95Parser.WHILE, 0)

        def LP(self):
            return self.getToken(D95Parser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(D95Parser.ExprContext,0)


        def RP(self):
            return self.getToken(D95Parser.RP, 0)

        def LB(self):
            return self.getToken(D95Parser.LB, 0)

        def list_stmt(self):
            return self.getTypedRuleContext(D95Parser.List_stmtContext,0)


        def RB(self):
            return self.getToken(D95Parser.RB, 0)

        def getRuleIndex(self):
            return D95Parser.RULE_stmt_while

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_while" ):
                return visitor.visitStmt_while(self)
            else:
                return visitor.visitChildren(self)




    def stmt_while(self):

        localctx = D95Parser.Stmt_whileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_stmt_while)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self.match(D95Parser.WHILE)
            self.state = 219
            self.match(D95Parser.LP)
            self.state = 220
            self.expr()
            self.state = 221
            self.match(D95Parser.RP)
            self.state = 222
            self.match(D95Parser.LB)
            self.state = 223
            self.list_stmt()
            self.state = 224
            self.match(D95Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_breakContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(D95Parser.BREAK, 0)

        def SEMI(self):
            return self.getToken(D95Parser.SEMI, 0)

        def getRuleIndex(self):
            return D95Parser.RULE_stmt_break

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_break" ):
                return visitor.visitStmt_break(self)
            else:
                return visitor.visitChildren(self)




    def stmt_break(self):

        localctx = D95Parser.Stmt_breakContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_stmt_break)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self.match(D95Parser.BREAK)
            self.state = 227
            self.match(D95Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_continueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(D95Parser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(D95Parser.SEMI, 0)

        def getRuleIndex(self):
            return D95Parser.RULE_stmt_continue

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_continue" ):
                return visitor.visitStmt_continue(self)
            else:
                return visitor.visitChildren(self)




    def stmt_continue(self):

        localctx = D95Parser.Stmt_continueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_stmt_continue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.match(D95Parser.CONTINUE)
            self.state = 230
            self.match(D95Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_callContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func_call(self):
            return self.getTypedRuleContext(D95Parser.Func_callContext,0)


        def SEMI(self):
            return self.getToken(D95Parser.SEMI, 0)

        def getRuleIndex(self):
            return D95Parser.RULE_stmt_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_call" ):
                return visitor.visitStmt_call(self)
            else:
                return visitor.visitChildren(self)




    def stmt_call(self):

        localctx = D95Parser.Stmt_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_stmt_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.func_call()
            self.state = 233
            self.match(D95Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_returnContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(D95Parser.RETURN, 0)

        def SEMI(self):
            return self.getToken(D95Parser.SEMI, 0)

        def expr(self):
            return self.getTypedRuleContext(D95Parser.ExprContext,0)


        def getRuleIndex(self):
            return D95Parser.RULE_stmt_return

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_return" ):
                return visitor.visitStmt_return(self)
            else:
                return visitor.visitChildren(self)




    def stmt_return(self):

        localctx = D95Parser.Stmt_returnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_stmt_return)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            self.match(D95Parser.RETURN)
            self.state = 238
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D95Parser.STR2INT, D95Parser.INT2STR, D95Parser.STR2FLOAT, D95Parser.FLOAT2STR, D95Parser.STR2BOOL, D95Parser.BOOL2STR, D95Parser.ID_VARPAR, D95Parser.ID_CONST, D95Parser.ID_FUNC, D95Parser.OCT, D95Parser.DEC, D95Parser.HEX, D95Parser.BIN, D95Parser.FLOAT, D95Parser.TRUE, D95Parser.FALSE, D95Parser.ARRAY_TYPE, D95Parser.STRING, D95Parser.SUB, D95Parser.NOT, D95Parser.LP]:
                self.state = 236
                self.expr()
                pass
            elif token in [D95Parser.SEMI]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 240
            self.match(D95Parser.SEMI)
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

        def expr_1(self):
            return self.getTypedRuleContext(D95Parser.Expr_1Context,0)


        def array(self):
            return self.getTypedRuleContext(D95Parser.ArrayContext,0)


        def getRuleIndex(self):
            return D95Parser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = D95Parser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_expr)
        try:
            self.state = 244
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D95Parser.STR2INT, D95Parser.INT2STR, D95Parser.STR2FLOAT, D95Parser.FLOAT2STR, D95Parser.STR2BOOL, D95Parser.BOOL2STR, D95Parser.ID_VARPAR, D95Parser.ID_CONST, D95Parser.ID_FUNC, D95Parser.OCT, D95Parser.DEC, D95Parser.HEX, D95Parser.BIN, D95Parser.FLOAT, D95Parser.TRUE, D95Parser.FALSE, D95Parser.STRING, D95Parser.SUB, D95Parser.NOT, D95Parser.LP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 242
                self.expr_1()
                pass
            elif token in [D95Parser.ARRAY_TYPE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 243
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


    class Expr_1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D95Parser.Expr_2Context)
            else:
                return self.getTypedRuleContext(D95Parser.Expr_2Context,i)


        def op_string(self):
            return self.getTypedRuleContext(D95Parser.Op_stringContext,0)


        def getRuleIndex(self):
            return D95Parser.RULE_expr_1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_1" ):
                return visitor.visitExpr_1(self)
            else:
                return visitor.visitChildren(self)




    def expr_1(self):

        localctx = D95Parser.Expr_1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_expr_1)
        try:
            self.state = 251
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 246
                self.expr_2()
                self.state = 247
                self.op_string()
                self.state = 248
                self.expr_2()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 250
                self.expr_2()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_3(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D95Parser.Expr_3Context)
            else:
                return self.getTypedRuleContext(D95Parser.Expr_3Context,i)


        def op_relation(self):
            return self.getTypedRuleContext(D95Parser.Op_relationContext,0)


        def getRuleIndex(self):
            return D95Parser.RULE_expr_2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_2" ):
                return visitor.visitExpr_2(self)
            else:
                return visitor.visitChildren(self)




    def expr_2(self):

        localctx = D95Parser.Expr_2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_expr_2)
        try:
            self.state = 258
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 253
                self.expr_3(0)
                self.state = 254
                self.op_relation()
                self.state = 255
                self.expr_3(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 257
                self.expr_3(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_4(self):
            return self.getTypedRuleContext(D95Parser.Expr_4Context,0)


        def expr_3(self):
            return self.getTypedRuleContext(D95Parser.Expr_3Context,0)


        def op_andor(self):
            return self.getTypedRuleContext(D95Parser.Op_andorContext,0)


        def getRuleIndex(self):
            return D95Parser.RULE_expr_3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_3" ):
                return visitor.visitExpr_3(self)
            else:
                return visitor.visitChildren(self)



    def expr_3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D95Parser.Expr_3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_expr_3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self.expr_4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 269
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D95Parser.Expr_3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_3)
                    self.state = 263
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 264
                    self.op_andor()
                    self.state = 265
                    self.expr_4(0) 
                self.state = 271
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr_4Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_5(self):
            return self.getTypedRuleContext(D95Parser.Expr_5Context,0)


        def expr_4(self):
            return self.getTypedRuleContext(D95Parser.Expr_4Context,0)


        def op_adding(self):
            return self.getTypedRuleContext(D95Parser.Op_addingContext,0)


        def getRuleIndex(self):
            return D95Parser.RULE_expr_4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_4" ):
                return visitor.visitExpr_4(self)
            else:
                return visitor.visitChildren(self)



    def expr_4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D95Parser.Expr_4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 48
        self.enterRecursionRule(localctx, 48, self.RULE_expr_4, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            self.expr_5(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 281
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D95Parser.Expr_4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_4)
                    self.state = 275
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 276
                    self.op_adding()
                    self.state = 277
                    self.expr_5(0) 
                self.state = 283
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr_5Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_6(self):
            return self.getTypedRuleContext(D95Parser.Expr_6Context,0)


        def expr_5(self):
            return self.getTypedRuleContext(D95Parser.Expr_5Context,0)


        def op_multiplyng(self):
            return self.getTypedRuleContext(D95Parser.Op_multiplyngContext,0)


        def getRuleIndex(self):
            return D95Parser.RULE_expr_5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_5" ):
                return visitor.visitExpr_5(self)
            else:
                return visitor.visitChildren(self)



    def expr_5(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D95Parser.Expr_5Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 50
        self.enterRecursionRule(localctx, 50, self.RULE_expr_5, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            self.expr_6()
            self._ctx.stop = self._input.LT(-1)
            self.state = 293
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D95Parser.Expr_5Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_5)
                    self.state = 287
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 288
                    self.op_multiplyng()
                    self.state = 289
                    self.expr_6() 
                self.state = 295
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr_6Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(D95Parser.NOT, 0)

        def expr_6(self):
            return self.getTypedRuleContext(D95Parser.Expr_6Context,0)


        def expr_7(self):
            return self.getTypedRuleContext(D95Parser.Expr_7Context,0)


        def getRuleIndex(self):
            return D95Parser.RULE_expr_6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_6" ):
                return visitor.visitExpr_6(self)
            else:
                return visitor.visitChildren(self)




    def expr_6(self):

        localctx = D95Parser.Expr_6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_expr_6)
        try:
            self.state = 299
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D95Parser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 296
                self.match(D95Parser.NOT)
                self.state = 297
                self.expr_6()
                pass
            elif token in [D95Parser.STR2INT, D95Parser.INT2STR, D95Parser.STR2FLOAT, D95Parser.FLOAT2STR, D95Parser.STR2BOOL, D95Parser.BOOL2STR, D95Parser.ID_VARPAR, D95Parser.ID_CONST, D95Parser.ID_FUNC, D95Parser.OCT, D95Parser.DEC, D95Parser.HEX, D95Parser.BIN, D95Parser.FLOAT, D95Parser.TRUE, D95Parser.FALSE, D95Parser.STRING, D95Parser.SUB, D95Parser.LP]:
                self.enterOuterAlt(localctx, 2)
                self.state = 298
                self.expr_7()
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


    class Expr_7Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB(self):
            return self.getToken(D95Parser.SUB, 0)

        def expr_7(self):
            return self.getTypedRuleContext(D95Parser.Expr_7Context,0)


        def expr_8(self):
            return self.getTypedRuleContext(D95Parser.Expr_8Context,0)


        def getRuleIndex(self):
            return D95Parser.RULE_expr_7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_7" ):
                return visitor.visitExpr_7(self)
            else:
                return visitor.visitChildren(self)




    def expr_7(self):

        localctx = D95Parser.Expr_7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_expr_7)
        try:
            self.state = 304
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D95Parser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 301
                self.match(D95Parser.SUB)
                self.state = 302
                self.expr_7()
                pass
            elif token in [D95Parser.STR2INT, D95Parser.INT2STR, D95Parser.STR2FLOAT, D95Parser.FLOAT2STR, D95Parser.STR2BOOL, D95Parser.BOOL2STR, D95Parser.ID_VARPAR, D95Parser.ID_CONST, D95Parser.ID_FUNC, D95Parser.OCT, D95Parser.DEC, D95Parser.HEX, D95Parser.BIN, D95Parser.FLOAT, D95Parser.TRUE, D95Parser.FALSE, D95Parser.STRING, D95Parser.LP]:
                self.enterOuterAlt(localctx, 2)
                self.state = 303
                self.expr_8()
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


    class Expr_8Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operand_index(self):
            return self.getTypedRuleContext(D95Parser.Operand_indexContext,0)


        def index_operator(self):
            return self.getTypedRuleContext(D95Parser.Index_operatorContext,0)


        def operand(self):
            return self.getTypedRuleContext(D95Parser.OperandContext,0)


        def getRuleIndex(self):
            return D95Parser.RULE_expr_8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_8" ):
                return visitor.visitExpr_8(self)
            else:
                return visitor.visitChildren(self)




    def expr_8(self):

        localctx = D95Parser.Expr_8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_expr_8)
        try:
            self.state = 310
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 306
                self.operand_index()
                self.state = 307
                self.index_operator()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 309
                self.operand()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Operand_indexContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID_VARPAR(self):
            return self.getToken(D95Parser.ID_VARPAR, 0)

        def ID_CONST(self):
            return self.getToken(D95Parser.ID_CONST, 0)

        def getRuleIndex(self):
            return D95Parser.RULE_operand_index

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand_index" ):
                return visitor.visitOperand_index(self)
            else:
                return visitor.visitChildren(self)




    def operand_index(self):

        localctx = D95Parser.Operand_indexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_operand_index)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 312
            _la = self._input.LA(1)
            if not(_la==D95Parser.ID_VARPAR or _la==D95Parser.ID_CONST):
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


    class Index_operatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(D95Parser.LSB, 0)

        def expr_1(self):
            return self.getTypedRuleContext(D95Parser.Expr_1Context,0)


        def RSB(self):
            return self.getToken(D95Parser.RSB, 0)

        def index_operator(self):
            return self.getTypedRuleContext(D95Parser.Index_operatorContext,0)


        def getRuleIndex(self):
            return D95Parser.RULE_index_operator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_operator" ):
                return visitor.visitIndex_operator(self)
            else:
                return visitor.visitChildren(self)




    def index_operator(self):

        localctx = D95Parser.Index_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_index_operator)
        try:
            self.state = 323
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 314
                self.match(D95Parser.LSB)
                self.state = 315
                self.expr_1()
                self.state = 316
                self.match(D95Parser.RSB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 318
                self.match(D95Parser.LSB)
                self.state = 319
                self.expr_1()
                self.state = 320
                self.match(D95Parser.RSB)
                self.state = 321
                self.index_operator()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(D95Parser.LiteralContext,0)


        def ID_VARPAR(self):
            return self.getToken(D95Parser.ID_VARPAR, 0)

        def ID_CONST(self):
            return self.getToken(D95Parser.ID_CONST, 0)

        def func_call(self):
            return self.getTypedRuleContext(D95Parser.Func_callContext,0)


        def LP(self):
            return self.getToken(D95Parser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(D95Parser.ExprContext,0)


        def RP(self):
            return self.getToken(D95Parser.RP, 0)

        def getRuleIndex(self):
            return D95Parser.RULE_operand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = D95Parser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_operand)
        try:
            self.state = 333
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D95Parser.OCT, D95Parser.DEC, D95Parser.HEX, D95Parser.BIN, D95Parser.FLOAT, D95Parser.TRUE, D95Parser.FALSE, D95Parser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 325
                self.literal()
                pass
            elif token in [D95Parser.ID_VARPAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 326
                self.match(D95Parser.ID_VARPAR)
                pass
            elif token in [D95Parser.ID_CONST]:
                self.enterOuterAlt(localctx, 3)
                self.state = 327
                self.match(D95Parser.ID_CONST)
                pass
            elif token in [D95Parser.STR2INT, D95Parser.INT2STR, D95Parser.STR2FLOAT, D95Parser.FLOAT2STR, D95Parser.STR2BOOL, D95Parser.BOOL2STR, D95Parser.ID_FUNC]:
                self.enterOuterAlt(localctx, 4)
                self.state = 328
                self.func_call()
                pass
            elif token in [D95Parser.LP]:
                self.enterOuterAlt(localctx, 5)
                self.state = 329
                self.match(D95Parser.LP)
                self.state = 330
                self.expr()
                self.state = 331
                self.match(D95Parser.RP)
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


    class Func_callContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(D95Parser.LP, 0)

        def list_param(self):
            return self.getTypedRuleContext(D95Parser.List_paramContext,0)


        def RP(self):
            return self.getToken(D95Parser.RP, 0)

        def ID_FUNC(self):
            return self.getToken(D95Parser.ID_FUNC, 0)

        def type_coersion(self):
            return self.getTypedRuleContext(D95Parser.Type_coersionContext,0)


        def getRuleIndex(self):
            return D95Parser.RULE_func_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call" ):
                return visitor.visitFunc_call(self)
            else:
                return visitor.visitChildren(self)




    def func_call(self):

        localctx = D95Parser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_func_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 337
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D95Parser.ID_FUNC]:
                self.state = 335
                self.match(D95Parser.ID_FUNC)
                pass
            elif token in [D95Parser.STR2INT, D95Parser.INT2STR, D95Parser.STR2FLOAT, D95Parser.FLOAT2STR, D95Parser.STR2BOOL, D95Parser.BOOL2STR]:
                self.state = 336
                self.type_coersion()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 339
            self.match(D95Parser.LP)
            self.state = 340
            self.list_param()
            self.state = 341
            self.match(D95Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_paramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(D95Parser.ParamContext,0)


        def COMMA(self):
            return self.getToken(D95Parser.COMMA, 0)

        def list_param(self):
            return self.getTypedRuleContext(D95Parser.List_paramContext,0)


        def getRuleIndex(self):
            return D95Parser.RULE_list_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_param" ):
                return visitor.visitList_param(self)
            else:
                return visitor.visitChildren(self)




    def list_param(self):

        localctx = D95Parser.List_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_list_param)
        try:
            self.state = 349
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 343
                self.param()
                self.state = 344
                self.match(D95Parser.COMMA)
                self.state = 345
                self.list_param()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 347
                self.param()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(D95Parser.LiteralContext,0)


        def ID_VARPAR(self):
            return self.getToken(D95Parser.ID_VARPAR, 0)

        def expr(self):
            return self.getTypedRuleContext(D95Parser.ExprContext,0)


        def getRuleIndex(self):
            return D95Parser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = D95Parser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_param)
        try:
            self.state = 354
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 351
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 352
                self.match(D95Parser.ID_VARPAR)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 353
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_coersionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STR2INT(self):
            return self.getToken(D95Parser.STR2INT, 0)

        def INT2STR(self):
            return self.getToken(D95Parser.INT2STR, 0)

        def STR2BOOL(self):
            return self.getToken(D95Parser.STR2BOOL, 0)

        def BOOL2STR(self):
            return self.getToken(D95Parser.BOOL2STR, 0)

        def STR2FLOAT(self):
            return self.getToken(D95Parser.STR2FLOAT, 0)

        def FLOAT2STR(self):
            return self.getToken(D95Parser.FLOAT2STR, 0)

        def getRuleIndex(self):
            return D95Parser.RULE_type_coersion

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_coersion" ):
                return visitor.visitType_coersion(self)
            else:
                return visitor.visitChildren(self)




    def type_coersion(self):

        localctx = D95Parser.Type_coersionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_type_coersion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 356
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D95Parser.STR2INT) | (1 << D95Parser.INT2STR) | (1 << D95Parser.STR2FLOAT) | (1 << D95Parser.FLOAT2STR) | (1 << D95Parser.STR2BOOL) | (1 << D95Parser.BOOL2STR))) != 0)):
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


    class Op_stringContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STR_CAT(self):
            return self.getToken(D95Parser.STR_CAT, 0)

        def STR_CMP(self):
            return self.getToken(D95Parser.STR_CMP, 0)

        def getRuleIndex(self):
            return D95Parser.RULE_op_string

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp_string" ):
                return visitor.visitOp_string(self)
            else:
                return visitor.visitChildren(self)




    def op_string(self):

        localctx = D95Parser.Op_stringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_op_string)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 358
            _la = self._input.LA(1)
            if not(_la==D95Parser.STR_CMP or _la==D95Parser.STR_CAT):
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


    class Op_relationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUAL(self):
            return self.getToken(D95Parser.EQUAL, 0)

        def NOT_EQUAL(self):
            return self.getToken(D95Parser.NOT_EQUAL, 0)

        def LESS(self):
            return self.getToken(D95Parser.LESS, 0)

        def LESS_EQUAL(self):
            return self.getToken(D95Parser.LESS_EQUAL, 0)

        def GREATER(self):
            return self.getToken(D95Parser.GREATER, 0)

        def GREATER_EQUAL(self):
            return self.getToken(D95Parser.GREATER_EQUAL, 0)

        def getRuleIndex(self):
            return D95Parser.RULE_op_relation

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp_relation" ):
                return visitor.visitOp_relation(self)
            else:
                return visitor.visitChildren(self)




    def op_relation(self):

        localctx = D95Parser.Op_relationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_op_relation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 360
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D95Parser.NOT_EQUAL) | (1 << D95Parser.GREATER) | (1 << D95Parser.GREATER_EQUAL) | (1 << D95Parser.LESS) | (1 << D95Parser.LESS_EQUAL) | (1 << D95Parser.EQUAL))) != 0)):
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


    class Op_andorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AND(self):
            return self.getToken(D95Parser.AND, 0)

        def OR(self):
            return self.getToken(D95Parser.OR, 0)

        def getRuleIndex(self):
            return D95Parser.RULE_op_andor

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp_andor" ):
                return visitor.visitOp_andor(self)
            else:
                return visitor.visitChildren(self)




    def op_andor(self):

        localctx = D95Parser.Op_andorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_op_andor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 362
            _la = self._input.LA(1)
            if not(_la==D95Parser.AND or _la==D95Parser.OR):
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


    class Op_addingContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(D95Parser.ADD, 0)

        def SUB(self):
            return self.getToken(D95Parser.SUB, 0)

        def getRuleIndex(self):
            return D95Parser.RULE_op_adding

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp_adding" ):
                return visitor.visitOp_adding(self)
            else:
                return visitor.visitChildren(self)




    def op_adding(self):

        localctx = D95Parser.Op_addingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_op_adding)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 364
            _la = self._input.LA(1)
            if not(_la==D95Parser.ADD or _la==D95Parser.SUB):
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


    class Op_multiplyngContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MUL(self):
            return self.getToken(D95Parser.MUL, 0)

        def DIV(self):
            return self.getToken(D95Parser.DIV, 0)

        def MOD(self):
            return self.getToken(D95Parser.MOD, 0)

        def getRuleIndex(self):
            return D95Parser.RULE_op_multiplyng

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp_multiplyng" ):
                return visitor.visitOp_multiplyng(self)
            else:
                return visitor.visitChildren(self)




    def op_multiplyng(self):

        localctx = D95Parser.Op_multiplyngContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_op_multiplyng)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 366
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D95Parser.MUL) | (1 << D95Parser.DIV) | (1 << D95Parser.MOD))) != 0)):
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


    class ListARRAYContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array(self):
            return self.getTypedRuleContext(D95Parser.ArrayContext,0)


        def COMMA(self):
            return self.getToken(D95Parser.COMMA, 0)

        def listARRAY(self):
            return self.getTypedRuleContext(D95Parser.ListARRAYContext,0)


        def getRuleIndex(self):
            return D95Parser.RULE_listARRAY

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListARRAY" ):
                return visitor.visitListARRAY(self)
            else:
                return visitor.visitChildren(self)




    def listARRAY(self):

        localctx = D95Parser.ListARRAYContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_listARRAY)
        try:
            self.state = 373
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 368
                self.array()
                self.state = 369
                self.match(D95Parser.COMMA)
                self.state = 370
                self.listARRAY()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 372
                self.array()
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

        def i_array(self):
            return self.getTypedRuleContext(D95Parser.I_arrayContext,0)


        def a_array(self):
            return self.getTypedRuleContext(D95Parser.A_arrayContext,0)


        def m_array(self):
            return self.getTypedRuleContext(D95Parser.M_arrayContext,0)


        def getRuleIndex(self):
            return D95Parser.RULE_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray" ):
                return visitor.visitArray(self)
            else:
                return visitor.visitChildren(self)




    def array(self):

        localctx = D95Parser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_array)
        try:
            self.state = 378
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 375
                self.i_array()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 376
                self.a_array()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 377
                self.m_array()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class I_arrayContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY_TYPE(self):
            return self.getToken(D95Parser.ARRAY_TYPE, 0)

        def LP(self):
            return self.getToken(D95Parser.LP, 0)

        def listLIT(self):
            return self.getTypedRuleContext(D95Parser.ListLITContext,0)


        def RP(self):
            return self.getToken(D95Parser.RP, 0)

        def getRuleIndex(self):
            return D95Parser.RULE_i_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitI_array" ):
                return visitor.visitI_array(self)
            else:
                return visitor.visitChildren(self)




    def i_array(self):

        localctx = D95Parser.I_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_i_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 380
            self.match(D95Parser.ARRAY_TYPE)
            self.state = 381
            self.match(D95Parser.LP)
            self.state = 382
            self.listLIT()
            self.state = 383
            self.match(D95Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class A_arrayContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY_TYPE(self):
            return self.getToken(D95Parser.ARRAY_TYPE, 0)

        def LP(self):
            return self.getToken(D95Parser.LP, 0)

        def listKV(self):
            return self.getTypedRuleContext(D95Parser.ListKVContext,0)


        def RP(self):
            return self.getToken(D95Parser.RP, 0)

        def getRuleIndex(self):
            return D95Parser.RULE_a_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitA_array" ):
                return visitor.visitA_array(self)
            else:
                return visitor.visitChildren(self)




    def a_array(self):

        localctx = D95Parser.A_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_a_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 385
            self.match(D95Parser.ARRAY_TYPE)
            self.state = 386
            self.match(D95Parser.LP)
            self.state = 387
            self.listKV()
            self.state = 388
            self.match(D95Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class M_arrayContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY_TYPE(self):
            return self.getToken(D95Parser.ARRAY_TYPE, 0)

        def LP(self):
            return self.getToken(D95Parser.LP, 0)

        def listARRAY(self):
            return self.getTypedRuleContext(D95Parser.ListARRAYContext,0)


        def RP(self):
            return self.getToken(D95Parser.RP, 0)

        def getRuleIndex(self):
            return D95Parser.RULE_m_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitM_array" ):
                return visitor.visitM_array(self)
            else:
                return visitor.visitChildren(self)




    def m_array(self):

        localctx = D95Parser.M_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_m_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 390
            self.match(D95Parser.ARRAY_TYPE)
            self.state = 391
            self.match(D95Parser.LP)
            self.state = 392
            self.listARRAY()
            self.state = 393
            self.match(D95Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListKVContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def keyValue(self):
            return self.getTypedRuleContext(D95Parser.KeyValueContext,0)


        def COMMA(self):
            return self.getToken(D95Parser.COMMA, 0)

        def listKV(self):
            return self.getTypedRuleContext(D95Parser.ListKVContext,0)


        def getRuleIndex(self):
            return D95Parser.RULE_listKV

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListKV" ):
                return visitor.visitListKV(self)
            else:
                return visitor.visitChildren(self)




    def listKV(self):

        localctx = D95Parser.ListKVContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_listKV)
        try:
            self.state = 400
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 395
                self.keyValue()
                self.state = 396
                self.match(D95Parser.COMMA)
                self.state = 397
                self.listKV()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 399
                self.keyValue()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KeyValueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def key(self):
            return self.getTypedRuleContext(D95Parser.KeyContext,0)


        def ASSOCATE(self):
            return self.getToken(D95Parser.ASSOCATE, 0)

        def expr(self):
            return self.getTypedRuleContext(D95Parser.ExprContext,0)


        def getRuleIndex(self):
            return D95Parser.RULE_keyValue

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKeyValue" ):
                return visitor.visitKeyValue(self)
            else:
                return visitor.visitChildren(self)




    def keyValue(self):

        localctx = D95Parser.KeyValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_keyValue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 402
            self.key()
            self.state = 403
            self.match(D95Parser.ASSOCATE)
            self.state = 404
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KeyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def integer(self):
            return self.getTypedRuleContext(D95Parser.IntegerContext,0)


        def STRING(self):
            return self.getToken(D95Parser.STRING, 0)

        def ID_VARPAR(self):
            return self.getToken(D95Parser.ID_VARPAR, 0)

        def getRuleIndex(self):
            return D95Parser.RULE_key

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKey" ):
                return visitor.visitKey(self)
            else:
                return visitor.visitChildren(self)




    def key(self):

        localctx = D95Parser.KeyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_key)
        try:
            self.state = 409
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D95Parser.OCT, D95Parser.DEC, D95Parser.HEX, D95Parser.BIN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 406
                self.integer()
                pass
            elif token in [D95Parser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 407
                self.match(D95Parser.STRING)
                pass
            elif token in [D95Parser.ID_VARPAR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 408
                self.match(D95Parser.ID_VARPAR)
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


    class ListLITContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(D95Parser.LiteralContext,0)


        def COMMA(self):
            return self.getToken(D95Parser.COMMA, 0)

        def listLIT(self):
            return self.getTypedRuleContext(D95Parser.ListLITContext,0)


        def getRuleIndex(self):
            return D95Parser.RULE_listLIT

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListLIT" ):
                return visitor.visitListLIT(self)
            else:
                return visitor.visitChildren(self)




    def listLIT(self):

        localctx = D95Parser.ListLITContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_listLIT)
        try:
            self.state = 417
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 411
                self.literal()
                self.state = 412
                self.match(D95Parser.COMMA)
                self.state = 413
                self.listLIT()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 415
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


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

        def integer(self):
            return self.getTypedRuleContext(D95Parser.IntegerContext,0)


        def FLOAT(self):
            return self.getToken(D95Parser.FLOAT, 0)

        def boolean(self):
            return self.getTypedRuleContext(D95Parser.BooleanContext,0)


        def STRING(self):
            return self.getToken(D95Parser.STRING, 0)

        def getRuleIndex(self):
            return D95Parser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = D95Parser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_literal)
        try:
            self.state = 423
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D95Parser.OCT, D95Parser.DEC, D95Parser.HEX, D95Parser.BIN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 419
                self.integer()
                pass
            elif token in [D95Parser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 420
                self.match(D95Parser.FLOAT)
                pass
            elif token in [D95Parser.TRUE, D95Parser.FALSE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 421
                self.boolean()
                pass
            elif token in [D95Parser.STRING]:
                self.enterOuterAlt(localctx, 4)
                self.state = 422
                self.match(D95Parser.STRING)
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


    class IntegerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OCT(self):
            return self.getToken(D95Parser.OCT, 0)

        def DEC(self):
            return self.getToken(D95Parser.DEC, 0)

        def HEX(self):
            return self.getToken(D95Parser.HEX, 0)

        def BIN(self):
            return self.getToken(D95Parser.BIN, 0)

        def getRuleIndex(self):
            return D95Parser.RULE_integer

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInteger" ):
                return visitor.visitInteger(self)
            else:
                return visitor.visitChildren(self)




    def integer(self):

        localctx = D95Parser.IntegerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_integer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 425
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D95Parser.OCT) | (1 << D95Parser.DEC) | (1 << D95Parser.HEX) | (1 << D95Parser.BIN))) != 0)):
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


    class BooleanContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(D95Parser.TRUE, 0)

        def FALSE(self):
            return self.getToken(D95Parser.FALSE, 0)

        def getRuleIndex(self):
            return D95Parser.RULE_boolean

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolean" ):
                return visitor.visitBoolean(self)
            else:
                return visitor.visitChildren(self)




    def boolean(self):

        localctx = D95Parser.BooleanContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_boolean)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 427
            _la = self._input.LA(1)
            if not(_la==D95Parser.TRUE or _la==D95Parser.FALSE):
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
        self._predicates[23] = self.expr_3_sempred
        self._predicates[24] = self.expr_4_sempred
        self._predicates[25] = self.expr_5_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_3_sempred(self, localctx:Expr_3Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr_4_sempred(self, localctx:Expr_4Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr_5_sempred(self, localctx:Expr_5Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




