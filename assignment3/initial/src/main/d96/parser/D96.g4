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
	CLASS IDEN LP mem_decl* RP
	| CLASS IDEN COL IDEN LP mem_decl* RP;
mem_decl: attr_decls | method_decl;

/*** Attribute Declare ***/
attr_decls: attr_decl SEMI;
attr_decl: (VAL | VAR) id_list_type (OP_AS expr_list)?;

id_list_type: id_list COL data_type;
id_list: iden_dol (COM iden_dol)*;
iden_dol: IDEN | DOL_IDEN;
expr_list: expr (COM expr)*;
data_type: INT | FLOAT | STRING | BOOLEAN | array_type | IDEN;
/*** Method Declare ***/
method_decl:
	constr_decl
	| destr_decl
	| iden_dol LB params_list? RB block_stmt;

constr_decl: CONSTRUCTOR LB params_list? RB block_stmt;
destr_decl: DESTRUCTOR LB RB block_stmt;

params_list: param_decl (SEMI param_decl)*;
param_decl: id_list_type;

block_stmt: LP block_item* RP;
block_item:
	assign_stmt
	| attr_stmt
	| if_stmt
	| break_stmt
	| continue_stmt
	| forin_stmt
	| return_stmt
	| method_invocation_stmt
	| block_stmt;

assign_stmt: assign_lhs SEMI;
assign_lhs: lhs OP_AS expr;
lhs: (IDEN | DOL_IDEN) | array_operator | field_access;
attr_stmt: attr_decl SEMI;
array_operator: expr8 (LSB expr RSB)+;

field_access: expr DOT IDEN | expr DCOL DOL_IDEN;

if_stmt: IF LB expr RB block_stmt (else_stmt)?;

else_stmt:
	ELSEIF LB expr RB block_stmt (else_stmt)?
	| ELSE block_stmt;

break_stmt: BREAK SEMI;

continue_stmt: CONTINUE SEMI;

//Declare Foreach/In
forin_stmt:
	FOREACH LB IDEN IN expr DDOT expr (
		BY expr
	)? RB block_stmt;

return_stmt: RETURN expr? SEMI;

method_invocation_stmt: method_invocation SEMI;
method_invocation:
	expr (DOT IDEN | DCOL DOL_IDEN) LB expr_list? RB;

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
expr7: expr8 (LSB expr RSB)+ | expr8;
expr8: expr8 DOT IDEN (LB expr_list? RB)? | expr9;
expr9: expr9 DCOL DOL_IDEN (LB expr_list? RB)? | expr10;
expr10: NEW IDEN LB expr_list? RB | expr11;
expr11: LB expr RB | operands;
operands: (IDEN | DOL_IDEN) | literal | SELF | NULL;
list_literal: literal (COM literal)*;
literal:
	INTEGER_LITERAL
	| FLOAT_LITERAL
	| BOOLEAN_LITERAL
	| STRING_LITERAL
	| array;

array: muldi_arr | indx_arr;
muldi_arr: ARRAY LB array_list RB;
// array_list: indx_arr COM array_list | indx_arr;
array_list: indx_arr (COM indx_arr)*;
indx_arr: ARRAY LB expr_list RB;

array_type: ARRAY LSB data_type COM INTEGER_LITERAL RSB;

//Declare Literals

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
SELF: 'Self';

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
