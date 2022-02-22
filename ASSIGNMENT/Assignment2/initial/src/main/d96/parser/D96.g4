grammar D96;
//My ID: 1914659
@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: class_decl+ EOF;

class_decl:
	CLASS IDEN LP RP
	| CLASS IDEN LP mem_decl+ RP
	| CLASS IDEN COL IDEN LP RP
	| CLASS IDEN COL IDEN LP mem_decl+ RP;
mem_decl: attr_decl | method_decl;

// att_decl: ATTR (para_list_eq | para_list_nor) SEMI; //val $a, b, c : Int = 4,5,6;
attr_decl: immutable_attr SEMI | mutable_attr SEMI;
method_decl 
			: constr_decl | destr_decl
			| iden_dol LB RB block_stmt
			| iden_dol LB params_list RB block_stmt;
constr_decl:
	CONSTRUCTOR LB RB block_stmt
	| CONSTRUCTOR LB params_list RB block_stmt;
destr_decl: DESTRUCTOR LB RB block_stmt;

immutable_attr:
	VAL id_list_type OP_AS expr_list
	| VAL id_list_type;
mutable_attr:
	VAR id_list_type OP_AS expr_list
	| VAR id_list_type;

params_list: id_list_type (SEMI id_list_type)*;

id_list_type: id_list COL data_type;
id_list: iden_dol (COM iden_dol)*;

expr_list: expr (COM expr)*;
iden_dol: IDEN | DOL_IDEN;

block_stmt: LP (block_items | block_stmt)* RP;

block_items:
	assign_stmt
	| if_stmt
	| attr_decl
	| break_stmt
	| continue_stmt
	| forin_stmt
	| return_stmt
	| method_invocation_stmt;

assign_stmt: assign_lhs SEMI;
assign_lhs: lhs OP_AS expr;
lhs: IDEN | array_operator | field_access;

data_type: INT | FLOAT | STRING | BOOLEAN | array_type;

if_stmt:
	IF LB expr RB block_stmt (ELSEIF LB expr RB block_stmt)* (
		ELSE block_stmt
	)?;

return_stmt: RETURN expr? SEMI;

break_stmt: BREAK SEMI;

continue_stmt: CONTINUE SEMI;

//Declare Foreach/In
forin_stmt:
	FOREACH LB IDEN IN INTEGER_LITERAL DDOT INTEGER_LITERAL (
		BY INTEGER_LITERAL
	)? RB block_stmt;

// Expressions expr_stmt: expr SEMI;

expr: expr1 ( OP_EQ_STR | OP_ADD_STR) expr1 | expr1;
expr1:
	expr2 (OP_LTE | OP_GTE | OP_NEQ | OP_LT | OP_GT | OP_EQ) expr2
	| expr2;
expr2: expr2 (OP_AND | OP_OR) expr3 | expr3;
expr3: expr3 (OP_ADD | OP_SUB) expr4 | expr4;
expr4: expr4 (OP_MUL | OP_DIV | OP_MOD) expr5 | expr5;
expr5: OP_NOT expr5 | expr6;
expr6: OP_SUB expr6 | expr7;
expr7: expr8 index_operators| expr8;
index_operators: LSB expr RSB index_operators | LSB expr RSB;
expr8 
	: expr8 DOT IDEN
	| expr8 DOT IDEN LB RB
	| expr8 DOT IDEN LB expr_list RB
	| expr9;
expr9
	 : expr10 DCOL DOL_IDEN
	 | expr10 DCOL DOL_IDEN LB RB
	 | expr10 DCOL DOL_IDEN LB expr_list RB
	 | expr10;
expr10: NEW IDEN LB RB | NEW IDEN LB expr_list RB | expr11;
expr11: LB expr RB | operands;
operands: IDEN | literal | SELF DOT IDEN | SELF DCOL IDEN;
array_operator: expr8 LSB expr RSB;
field_access: expr DOT IDEN | expr DCOL IDEN;

method_invocation_stmt: method_invocation SEMI;
method_invocation
					: expr DOT IDEN LB RB
					| expr DOT IDEN LB expr_list RB
					| expr DCOL DOL_IDEN LB RB
					| expr DCOL DOL_IDEN LB expr_list RB;

array: muldi_arr | indx_arr;
muldi_arr: ARRAY LB array_list RB;
array_list: indx_arr COM array_list | indx_arr;
indx_arr: ARRAY LB expr_list RB;

array_type: ARRAY LSB data_type COM literal RSB;

//Declare Literals
list_literal: (literal COM)* literal;

literal:
	INTEGER_LITERAL
	| FLOAT_LITERAL
	| BOOLEAN_LITERAL
	| STRING_LITERAL
	| array;

FLOAT_LITERAL:
	(
		DEC_FORM DOT DIGIT* EXPONENT
		| DEC_FORM DOT DIGIT*
		| DEC_FORM EXPONENT
		| DOT DIGIT* EXPONENT
	) {
				y = str(self.text);
				self.text = y.replace('_', '');
			};

fragment DEC_FORM: ([1-9] [_0-9]* [0-9]+ | [0-9]);

INTEGER_LITERAL:
	(
		[0] [bB] ( [0] | [1][0-1]* ([_]? [0-1]+)*)
		| ( [1-9] [0-9]* ([_]? [0-9]+)* [0-9]* | [0-9])
		| [0] [xX]( ([A-F0-9]+ [_]? [A-F0-9]+)+ | [A-F0-9])
		| [0] (([0-7]+ [_]? [0-7]+)+ | [0-7])
	) {
				y = str(self.text);
				self.text = y.replace('_', '');
			};

BOOLEAN_LITERAL: 'True' | 'False';

STRING_LITERAL:
	'"' (STR_CHAR | [']["])* '"' {
					y = str(self.text)
					self.text = y[1:len(y)-1]
				};

fragment STR_CHAR: ESC_SEQ | ~["\\];

fragment ESC_SEQ: '\\' [btnfr'\\];

fragment ESC_ILLEGAL: '\\' ~[btnfr'\\] | ~'\\';

fragment EXPONENT: [eE] SIGN? DIGIT+;

fragment SIGN: [_+-];

fragment DIGIT: [0-9];

//Seperators
LB: '(';

RB: ')';

LP: '{';

RP: '}';

LSB: '[';

RSB: ']';

SEMI: ';';

COL: ':';

DCOL: '::';

COM: ',';

CLASS: 'Class';

//2.2 Attribute declaration
VAL: 'Val';
VAR: 'Var';

//3 Lexical structure 3.2 Program comment
BLOCK_COMMENT: ('##' .*? '##') -> skip;

//3.4 Keywords
ARRAY: 'Array';
INT: 'Int';
FLOAT: 'Float';
BOOLEAN: 'Boolean';
STRING: 'String';
NULL: 'Null';
BREAK: 'Break';
CONTINUE: 'Continue';
IF: 'If';
ELSEIF: 'Elseif';
ELSE: 'Else';
FOREACH: 'Foreach';
RETURN: 'Return';
SELF: 'self';

NEW: 'New';
CONSTRUCTOR: 'Constructor';
DESTRUCTOR: 'Destructor';
IN: 'In';
BY: 'By';
DOT: '.';
DDOT: '..';
// 3.5 Operators
OP_ADD: '+';
OP_SUB: '-';
OP_MUL: '*';
OP_DIV: '/';
OP_MOD: '%';
OP_NOT: '!';
OP_AND: '&&';
OP_OR: '||';
OP_LTE: '<=';
OP_GTE: '>=';
OP_NEQ: '!=';
OP_AS: '=';
OP_EQ: '==';
OP_LT: '<';
OP_GT: '>';
OP_EQ_STR: '==.';
OP_ADD_STR: '+.';

//Declare Identifier

IDEN: [_a-zA-Z][_a-zA-Z0-9]*;
DOL_IDEN: [$] [_a-zA-Z0-9]*;
// WS: [ \t\r\n\f]+ -> skip;
WS: ('\t' | ' ' | '\r' | '\n')+ -> skip;

/***
 Throw error away if there has any mistakes happened
 */
UNCLOSE_STRING:
	'"' STR_CHAR* {
		y = str(self.text)
		raise UncloseString(y[1:])
	};

ILLEGAL_ESCAPE:
	'"' STR_CHAR* ESC_ILLEGAL {
		y = str(self.text)
		raise IllegalEscape(y[1:])
	};

ERROR_CHAR:
	. {
		raise ErrorToken(self.text);
	};

