grammar BKOOL;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program  : mptype 'main' LB RB LP body? RP EOF ;

mptype: INTTYPE | VOIDTYPE ;

body: funcall SEMI;

exp: funcall | INTLIT | FLOATLIT;

funcall: ID LB exp? RB ;

INTTYPE: 'int' ;

VOIDTYPE: 'void'  ;

ID: [a-zA-Z]+ ;

INTLIT: [0-9]+;

fragment INT_PART: [1-9][0-9]* | '0';
fragment DEC_PART: '.' [0-9]+;
fragment E_PART: [eE] '-'? [0-9]+;
FLOATLIT: INT_PART DEC_PART? E_PART | INT_PART DEC_PART;

LB: '(' ;

RB: ')' ;

LP: '{';

RP: '}';

SEMI: ';' ;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;