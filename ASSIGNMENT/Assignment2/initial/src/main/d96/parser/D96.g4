grammar D96;
//My ID: 1914659
@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: class_decl+ EOF;

class_decl:  CLASS IDEN LP mem_decl* RP
	| CLASS IDEN COL IDEN LP mem_decl* RP;
mem_decl: attr_decl | method_decl;

/*** Attribute Declare ***/
// att_decl: ATTR (para_list_eq | para_list_nor) SEMI; //val $a, b, c : Int = 4,5,6;
attr_decl: immutable_attr SEMI | mutable_attr SEMI;

immutable_attr:
	VAL id_list_type OP_AS expr_list
	| VAL id_list_type;
mutable_attr:
	VAR id_list_type OP_AS expr_list
	| VAR id_list_type;

id_list_type: id_list COL data_type;
id_list: iden_dol (COM iden_dol)*;
iden_dol: IDEN | DOL_IDEN;
expr_list: expr (COM expr)*;
data_type: INT | FLOAT | STRING | BOOLEAN | array_type | IDEN;
/*** Method Declare ***/
method_decl 
			: constr_decl | destr_decl
			| iden_dol LB params_list? RB block_stmt;

constr_decl:
	CONSTRUCTOR LB params_list? RB block_stmt;
destr_decl: DESTRUCTOR LB RB block_stmt;

params_list: param_decl (SEMI param_decl)*;
param_decl: id_list_type;


block_stmt : LP block_item* RP;
block_item
			: assign_stmt
			| attr_decl
			| if_stmt
			| break_stmt
			| continue_stmt
			| forin_stmt
			| return_stmt
			| method_invocation_stmt
			| block_stmt;

assign_stmt: assign_lhs SEMI;
assign_lhs: lhs OP_AS expr;
lhs: IDEN | array_operator | field_access;
array_operator: expr8 (LSB expr RSB)+;

field_access: expr DOT IDEN | expr DCOL DOL_IDEN;


if_stmt	: IF LB expr RB block_stmt  (else_stmt)?;

// if_element: IF LB expr RB block_stmt;
else_stmt : ELSEIF LB expr RB block_stmt (else_stmt)? | ELSE block_stmt;
// elif_element: ELSEIF LB expr RB block_stmt;
// else_element: ELSE block_stmt;

break_stmt: BREAK SEMI;

continue_stmt: CONTINUE SEMI;

//Declare Foreach/In
forin_stmt:
	FOREACH LB IDEN IN INTEGER_LITERAL DDOT INTEGER_LITERAL (
		BY INTEGER_LITERAL
	)? RB block_stmt;

return_stmt: RETURN expr? SEMI;

method_invocation_stmt: method_invocation SEMI;
method_invocation
					: expr (DOT IDEN | DCOL DOL_IDEN)  LB expr_list? RB;


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
expr7: expr8 (LSB expr RSB)+| expr8;
expr8 
	: expr8 DOT IDEN (LB expr_list? RB)?
	| expr9;
expr9
	 : expr9 DCOL DOL_IDEN (LB expr_list? RB)?
	 | expr10;
expr10: NEW IDEN LB expr_list? RB | expr11;
expr11: LB expr RB | operands;
operands: IDEN | literal | SELF | NULL;
list_literal: literal (COM literal)*;
literal
	: INTEGER_LITERAL
	| FLOAT_LITERAL
	| BOOLEAN_LITERAL
	| STRING_LITERAL
	| array;



array: muldi_arr | indx_arr;
muldi_arr: ARRAY LB array_list RB;
// array_list: indx_arr COM array_list | indx_arr;
array_list: indx_arr (COM  indx_arr)*;
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
















// grammar D96;
// //My ID: 1914659
// @lexer::header {
// from lexererr import *
// }

// options {
// 	language = Python3;
// }

// program: (class_decl LP (body_class)* RP)* (CLASS 'Program' LP body_class_main* main_func body_class_main*  RP)? EOF;


// class_decl: CLASS (IDEN | 'main') (COL (IDEN | 'main'))?;


// body_class
// 		  : att_decl
// 		  | func_decl
// 		  | constr_decl
// 		  | destr_decl;
// body_class_main: att_decl | func_decl;
// main_func: 'main' LB RB  block_stmt ;

// stmt
// 	: block_items 
// 	| return_stmt 
// 	| block_stmt
// 	| assign_stmt
// 	| att_decl;

// att_decl:
// 	ATTR (para_list_eq | para_list_nor)  SEMI; //val $a, b, c : Int = 4,5,6;

// para_list_nor:  ids_list COL (data_types | arr_type);
// para_list_eq
// 		: para ',' (para_list_eq) ',' (expr | array)
// 		| (para COL rest_para );
// rest_para: (data_types | arr_type) OP_AS (expr | array) | (data_types | arr_type) ;

// para: IDEN | DOL_IDEN;

// func_decl: (IDEN | DOL_IDEN) LB params_list_can? RB LP (stmt)* RP;

// destr_decl: DESTRUCTOR LB RB block_stmt;

// constr_decl: CONSTRUCTOR LB params_list_can? RB block_stmt;

// block_stmt: LP (block_items | block_stmt)* RP;

// block_items
// 			: assign_stmt
// 			| if_stmt
// 			| att_decl
// 			| break_stmt
// 			| continue_stmt
// 			| forin_stmt
// 			| return_stmt
// 			| member_acc SEMI;

// assign_stmt: assign_lhs SEMI;
// assign_lhs: expr OP_AS expr;



// method_invo_stmt: IDEN DCOL (DOL_IDEN) LB list_expr_method? RB;

// params_list_can: params_list (SEMI params_list)* ;

// params_list:
// 	ids_list_with_type (OP_AS expr (COM expr)*)? // a, b, c : Int = 4,5,6
// 	| ids_list_with_arr (OP_AS (array COM)* array )?; 

// ids_list_with_type: ids_list COL data_types; // a, b, c : Int
// ids_list_with_arr: ids_list COL arr_type;

// ids_list: (IDEN | DOL_IDEN) ( COM (IDEN | DOL_IDEN) )*; //a, b, c

// data_types: element_types;

// element_types: INT | FLOAT | STRING | BOOLEAN;

// if_stmt : IF LB expr RB block_stmt (ELSEIF LB expr RB block_stmt)* (ELSE block_stmt)? ;

// return_stmt: RETURN expr? SEMI;

// break_stmt: BREAK SEMI;

// continue_stmt: CONTINUE SEMI;

// //Declare Foreach/In
// forin_stmt:
// 	FOREACH LB IDEN IN INTEGER_LITERAL DDOT INTEGER_LITERAL (BY INTEGER_LITERAL)? RB 
// 	block_stmt ;

// // Expressions
// expr_stmt: expr SEMI;

// expr
// 	: atom 
// 	| <assoc = right> NEW expr
// 	| expr DCOL '$' expr
// 	| expr (DOT) expr
// 	| expr LSB expr RSB
// 	| <assoc = right> (OP_NOT | OP_SUB) expr
// 	| expr (OP_MUL | OP_DIV | OP_MOD) expr
// 	| expr (OP_ADD | OP_SUB) expr
// 	| expr (OP_AND | OP_OR) expr
// 	| expr (OP_LTE | OP_GTE | OP_NEQ | OP_LT | OP_GT | OP_EQ) expr
// 	| expr ( OP_EQ_STR | OP_ADD_STR) expr;




// atom:
// 	IDEN? LB expr RB
// 	| literal
// 	| IDEN
// 	| self_type
// 	| array_declare
// 	| method_invo_stmt
// 	| member_acc
// 	| class_type
// 	| ATTR ids_list_with_type;


// array_declare
// 			 : muldi_arr
// 			 | indx_arr
// 			 | arr_type;

// array
// 		: muldi_arr
// 		| indx_arr;

// muldi_arr:
// 	ARRAY LB (indx_arr COM)* indx_arr?  RB;

// indx_arr:
// 	ARRAY LB list_literal RB;

// arr_type: ARRAY LSB element_types COM literal RSB ;


// self_type: SELF DOT IDEN;


// class_type: 
// 			NEW IDEN LB list_literal?  RB ;

// // Member access
// member_acc
// 		  : inst_attr_acc
// 		  | stat_attr_acc
// 		  | inst_meth_invo
// 		  | stat_meth_invo;

// inst_attr_acc: IDEN DOT (IDEN );
// stat_attr_acc: IDEN DCOL (DOL_IDEN);
// inst_meth_invo:
// 	IDEN DOT (IDEN) LB list_expr_method? RB;
// stat_meth_invo: IDEN DCOL (DOL_IDEN) LB list_expr_method? RB;

// list_expr_method: (elem_expr_method COM)* elem_expr_method;
// elem_expr_method: expr | literal| stat_attr_acc | inst_meth_invo | stat_meth_invo | inst_attr_acc;
// //Declare Literals
// list_literal: (literal COM)* literal;

// literal
// 		: number_literal
// 		| STRING_LITERAL
// 		| IDEN;

// number_literal
// 			  : 
// 			   INTEGER_LITERAL
// 			   | FLOAT_LITERAL
// 			  | BOOLEAN_LITERAL;

// FLOAT_LITERAL	:
// 				(DEC_FORM DOT DIGIT* EXPONENT
// 				| DEC_FORM DOT DIGIT*
// 				| DEC_FORM EXPONENT
// 				| DOT DIGIT* EXPONENT)
// 				 {
// 				y = str(self.text);
// 				self.text = y.replace('_', '');
// 			};

// fragment DEC_FORM: ([1-9] [_0-9]* [0-9]+ | [0-9]);

//  INTEGER_LITERAL
// 				:
// 				([0] [bB] ( [0] | [1][0-1]*([_]? [0-1]+)*)
// 				| ( [1-9] [0-9]* ([_]? [0-9]+)* [0-9]*  | [0-9])
// 				| [0] [xX]( ([A-F0-9]+ [_]? [A-F0-9]+)+ | [A-F0-9])
// 				| [0] (([0-7]+ [_]? [0-7]+)+ | [0-7]))
// 			{
// 				y = str(self.text);
// 				self.text = y.replace('_', '');
// 			};

//  BOOLEAN_LITERAL: 'True' | 'False';

//  STRING_LITERAL: 
// 			    '"'( STR_CHAR | [']["])*  '"'
// 				{
// 					y = str(self.text)
// 					self.text = y[1:len(y)-1]
// 				};
// fragment STR_CHAR: ESC_SEQ | ~["\\];

// fragment ESC_SEQ: '\\' [btnfr'\\] ;
				
// fragment ESC_ILLEGAL: '\\' ~[btnfr'\\] | ~'\\';

// fragment EXPONENT: [eE] SIGN? DIGIT+;

// fragment SIGN: [_+-];

// fragment DIGIT: [0-9];

// //Seperators
// LB: '(';

// RB: ')';

// LP: '{';

// RP: '}';

// LSB: '[';

// RSB: ']';

// SEMI: ';';

// COL: ':';

// DCOL: '::';

// COM: ',';


// CLASS: 'Class';

// //2.2 Attribute declaration
// ATTR: 'Val' | 'Var';

// //3 Lexical structure 3.2 Program comment
// BLOCK_COMMENT: ('##' .*? '##') -> skip;


// //3.4 Keywords
// ARRAY: 'Array';
// INT: 'Int';
// FLOAT: 'Float';
// BOOLEAN: 'Boolean';
// STRING: 'String';
// NULL: 'Null';
// BREAK: 'Break';
// CONTINUE: 'Continue';
// IF: 'If';
// ELSEIF: 'Elseif';
// ELSE: 'Else';
// FOREACH: 'Foreach';
// RETURN: 'Return';
// SELF: 'self';

// NEW: 'New';
// CONSTRUCTOR: 'Constructor';
// DESTRUCTOR: 'Destructor';
// IN: 'In';
// BY: 'By';
// DOT: '.';
// DDOT: '..';
// // 3.5 Operators
// OP_ADD: '+';
// OP_SUB: '-';
// OP_MUL: '*';
// OP_DIV: '/';
// OP_MOD: '%';
// OP_NOT: '!';
// OP_AND: '&&';
// OP_OR: '||';
// OP_LTE: '<=';
// OP_GTE: '>=';
// OP_NEQ: '!=';
// OP_AS: '=';
// OP_EQ: '==';
// OP_LT: '<';
// OP_GT: '>';
// OP_EQ_STR: '==.';
// OP_ADD_STR: '+.';

// //Declare Identifier

// IDEN: [_a-zA-Z][_a-zA-Z0-9]*;
// DOL_IDEN: [$] [_a-zA-Z0-9]*;
// // WS: [ \t\r\n\f]+ -> skip;
// WS: ('\t' | ' ' | '\r' | '\n')+ -> skip;


// /***
// 	Throw error away if there has any mistakes happened
//  */
// UNCLOSE_STRING: '"' STR_CHAR* {
// 		y = str(self.text)
// 		raise UncloseString(y[1:])
// 	};

// ILLEGAL_ESCAPE:
// 	'"' STR_CHAR* ESC_ILLEGAL 
// 	{
// 		y = str(self.text)
// 		raise IllegalEscape(y[1:])
// 	};

// ERROR_CHAR: . 
// 	{
// 		raise ErrorToken(self.text);
// 	};















// grammar D96;
// //My ID: 1914659
// @lexer::header {
// from lexererr import *
// }

// options {
// 	language = Python3;
// }

// program: class_decl+ EOF;

// class_decl:
// 	CLASS IDEN LP RP
// 	| CLASS IDEN LP mem_decl+ RP
// 	| CLASS IDEN COL IDEN LP RP
// 	| CLASS IDEN COL IDEN LP mem_decl+ RP;
// mem_decl: attr_decl | method_decl;

// /*** Attribute Declare ***/
// // att_decl: ATTR (para_list_eq | para_list_nor) SEMI; //val $a, b, c : Int = 4,5,6;
// attr_decl: immutable_attr SEMI | mutable_attr SEMI;

// immutable_attr:
// 	VAL id_list_type OP_AS expr_list
// 	| VAL id_list_type;
// mutable_attr:
// 	VAR id_list_type OP_AS expr_list
// 	| VAR id_list_type;

// id_list_type: id_list COL data_type;
// id_list: iden_dol (COM iden_dol)*;
// iden_dol: IDEN | DOL_IDEN;
// expr_list: expr  COM expr_list | expr;
// data_type: INT | FLOAT | STRING | BOOLEAN | array_type;
// /*** Method Declare ***/
// method_decl 
// 			: constr_decl | destr_decl
// 			| iden_dol LB RB block_stmt
// 			| iden_dol LB params_list RB block_stmt;

// constr_decl:
// 	CONSTRUCTOR LB RB block_stmt
// 	| CONSTRUCTOR LB params_list RB block_stmt;
// destr_decl: DESTRUCTOR LB RB block_stmt;

// params_list: param_decl SEMI params_list
// 			| param_decl;
// param_decl: id_list_type;


// block_stmt : LP block_item+ RP | LP RP;
// block_item
// 			: assign_stmt
// 			| attr_decl
// 			| if_stmt
// 			| break_stmt
// 			| continue_stmt
// 			| forin_stmt
// 			| return_stmt
// 			| method_invocation_stmt
// 			| block_stmt;

// assign_stmt: assign_lhs SEMI;
// assign_lhs: lhs OP_AS expr;
// lhs: IDEN | array_operator | field_access;
// array_operator: expr8 index_operators;

// field_access: expr DOT IDEN | expr DCOL DOL_IDEN;


// if_stmt	: if_element else_stmt
// 		| if_element;
// if_element: IF LB expr RB block_stmt;
// else_stmt : elif_element else_stmt
// 		  | elif_element
// 		  | else_element;
// elif_element: ELSEIF LB expr RB block_stmt;
// else_element: ELSE block_stmt;

// break_stmt: BREAK SEMI;

// continue_stmt: CONTINUE SEMI;

// //Declare Foreach/In
// forin_stmt:
// 	FOREACH LB IDEN IN INTEGER_LITERAL DDOT INTEGER_LITERAL (
// 		BY INTEGER_LITERAL
// 	)? RB block_stmt;

// return_stmt: RETURN expr? SEMI;

// method_invocation_stmt: method_invocation SEMI;
// method_invocation
// 					: expr DOT IDEN LB RB
// 					| expr DOT IDEN LB expr_list RB
// 					| expr DCOL DOL_IDEN LB RB
// 					| expr DCOL DOL_IDEN LB expr_list RB;


// // Expressions expr_stmt: expr SEMI;

// expr: expr1 ( OP_EQ_STR | OP_ADD_STR) expr1 | expr1;
// expr1:
// 	expr2 (OP_LTE | OP_GTE | OP_NEQ | OP_LT | OP_GT | OP_EQ) expr2
// 	| expr2;
// expr2: expr2 (OP_AND | OP_OR) expr3 | expr3;
// expr3: expr3 (OP_ADD | OP_SUB) expr4 | expr4;
// expr4: expr4 (OP_MUL | OP_DIV | OP_MOD) expr5 | expr5;
// expr5: OP_NOT expr5 | expr6;
// expr6: OP_SUB expr6 | expr7;
// expr7: expr8 index_operators| expr8;
// index_operators: LSB expr RSB index_operators | LSB expr RSB;
// expr8 
// 	: expr8 DOT IDEN
// 	| expr8 DOT IDEN LB RB
// 	| expr8 DOT IDEN LB expr_list RB
// 	| expr9;
// expr9
// 	 : expr10 DCOL DOL_IDEN
// 	 | expr10 DCOL DOL_IDEN LB RB
// 	 | expr10 DCOL DOL_IDEN LB expr_list RB
// 	 | expr10;
// expr10: NEW IDEN LB RB | NEW IDEN LB expr_list RB | expr11;
// expr11: LB expr RB | operands;
// operands: IDEN | literal | SELF | NULL;
// list_literal: literal COM list_literal | literal;
// literal
// 	: INTEGER_LITERAL
// 	| FLOAT_LITERAL
// 	| BOOLEAN_LITERAL
// 	| STRING_LITERAL
// 	| array;



// array: muldi_arr | indx_arr;
// muldi_arr: ARRAY LB array_list RB;
// array_list: indx_arr COM array_list | indx_arr;
// indx_arr: ARRAY LB expr_list RB;

// array_type: ARRAY LSB data_type COM INTEGER_LITERAL RSB;

// //Declare Literals


// FLOAT_LITERAL:
// 	(
// 		DEC_FORM DOT DIGIT* EXPONENT
// 		| DEC_FORM DOT DIGIT*
// 		| DEC_FORM EXPONENT
// 		| DOT DIGIT* EXPONENT
// 	) {
// 				y = str(self.text);
// 				self.text = y.replace('_', '');
// 			};

// fragment DEC_FORM: ([1-9] [_0-9]* [0-9]+ | [0-9]);

// INTEGER_LITERAL:
// 	(
// 		[0] [bB] ( [0] | [1][0-1]* ([_]? [0-1]+)*)
// 		| ( [1-9] [0-9]* ([_]? [0-9]+)* [0-9]* | [0-9])
// 		| [0] [xX]( ([A-F0-9]+ [_]? [A-F0-9]+)+ | [A-F0-9])
// 		| [0] (([0-7]+ [_]? [0-7]+)+ | [0-7])
// 	) {
// 				y = str(self.text);
// 				self.text = y.replace('_', '');
// 			};

// BOOLEAN_LITERAL: 'True' | 'False';

// STRING_LITERAL:
// 	'"' (STR_CHAR | [']["])* '"' {
// 					y = str(self.text)
// 					self.text = y[1:len(y)-1]
// 				};

// fragment STR_CHAR: ESC_SEQ | ~["\\];

// fragment ESC_SEQ: '\\' [btnfr'\\];

// fragment ESC_ILLEGAL: '\\' ~[btnfr'\\] | ~'\\';

// fragment EXPONENT: [eE] SIGN? DIGIT+;

// fragment SIGN: [_+-];

// fragment DIGIT: [0-9];

// //Seperators
// LB: '(';

// RB: ')';

// LP: '{';

// RP: '}';

// LSB: '[';

// RSB: ']';

// SEMI: ';';

// COL: ':';

// DCOL: '::';

// COM: ',';

// CLASS: 'Class';

// //2.2 Attribute declaration
// VAL: 'Val';
// VAR: 'Var';

// //3 Lexical structure 3.2 Program comment
// BLOCK_COMMENT: ('##' .*? '##') -> skip;

// //3.4 Keywords
// ARRAY: 'Array';
// INT: 'Int';
// FLOAT: 'Float';
// BOOLEAN: 'Boolean';
// STRING: 'String';
// NULL: 'Null';
// BREAK: 'Break';
// CONTINUE: 'Continue';
// IF: 'If';
// ELSEIF: 'Elseif';
// ELSE: 'Else';
// FOREACH: 'Foreach';
// RETURN: 'Return';
// SELF: 'self';

// NEW: 'New';
// CONSTRUCTOR: 'Constructor';
// DESTRUCTOR: 'Destructor';
// IN: 'In';
// BY: 'By';
// DOT: '.';
// DDOT: '..';
// // 3.5 Operators
// OP_ADD: '+';
// OP_SUB: '-';
// OP_MUL: '*';
// OP_DIV: '/';
// OP_MOD: '%';
// OP_NOT: '!';
// OP_AND: '&&';
// OP_OR: '||';
// OP_LTE: '<=';
// OP_GTE: '>=';
// OP_NEQ: '!=';
// OP_AS: '=';
// OP_EQ: '==';
// OP_LT: '<';
// OP_GT: '>';
// OP_EQ_STR: '==.';
// OP_ADD_STR: '+.';

// //Declare Identifier

// IDEN: [_a-zA-Z][_a-zA-Z0-9]*;
// DOL_IDEN: [$] [_a-zA-Z0-9]*;
// // WS: [ \t\r\n\f]+ -> skip;
// WS: ('\t' | ' ' | '\r' | '\n')+ -> skip;

// /***
//  Throw error away if there has any mistakes happened
//  */
// UNCLOSE_STRING:
// 	'"' STR_CHAR* {
// 		y = str(self.text)
// 		raise UncloseString(y[1:])
// 	};

// ILLEGAL_ESCAPE:
// 	'"' STR_CHAR* ESC_ILLEGAL {
// 		y = str(self.text)
// 		raise IllegalEscape(y[1:])
// 	};

// ERROR_CHAR:
// 	. {
// 		raise ErrorToken(self.text);
// 	};

