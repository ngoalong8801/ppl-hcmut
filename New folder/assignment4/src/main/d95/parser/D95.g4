grammar D95;
// 1913695
@lexer::header {
from lexererr import *
}

@lexer::members {
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
}

options{
	language=Python3;
}

program: (non_constdecl | constdecl)* EOF;

// PARSER
// Decl
non_constdecl: stmt_assign | funcdecl;

// Statement
list_stmt: stmt list_stmt
         |;
stmt: stmt_if | stmt_assign
    | stmt_foreach | stmt_while | stmt_break
    | stmt_continue | stmt_call | stmt_return;

//Function declaration
funcdecl: FUNCTION ID_FUNC LP decl_param RP LB list_stmt RB;
decl_param: ID_VARPAR COMMA decl_param
            | ID_VARPAR
            | ;

// Constant declaration
constdecl: DEFINE LP ID_CONST COMMA expr RP SEMI;

// Assign statement
stmt_assign: lhs ASSIGN expr SEMI;
lhs: ID_VARPAR | expr_8;

// If statement
stmt_if: IF LP expr RP LB list_stmt RB stmt_elseif stmt_else;

stmt_elseif: ELSEIF LP expr RP LB list_stmt RB stmt_elseif
            | ;
stmt_else: ElSE LB list_stmt RB
            |;

// Foreach statement: foreach($array as key => value){statememnt-list}
stmt_foreach: FOREACH LP (ID_VARPAR | ID_CONST | array) AS key_for ASSOCATE value_for RP LB list_stmt RB ;
key_for: ID_VARPAR | ID_CONST;
value_for: ID_VARPAR | ID_CONST;

// While statement
stmt_while: WHILE LP expr RP LB list_stmt RB;

// Break statement
stmt_break: BREAK SEMI;

// Continue statement
stmt_continue: CONTINUE SEMI;

// Call statement
stmt_call: func_call SEMI;

// Return statement
stmt_return: RETURN (expr|) SEMI;

//--------------------------------------
// Expression
expr: expr_1 | array;
// String expression
expr_1: expr_2 op_string expr_2
      | expr_2;
// Relational expression: return Boolean
expr_2: expr_3 op_relation expr_3
      | expr_3;
// And or expression
expr_3: expr_3 op_andor expr_4
      | expr_4;
// Adding expression
expr_4: expr_4 op_adding expr_5
      | expr_5;
// Multiplyng expression
expr_5: expr_5 op_multiplyng expr_6
      | expr_6;
// Not expression
expr_6: NOT expr_6
      | expr_7;
// Sign expression
expr_7: SUB expr_7
      | expr_8;
// Index operator expression
expr_8: operand_index index_operator
      | operand;
operand_index: ID_VARPAR
             | ID_CONST;
index_operator: LSB expr_1 RSB
              | LSB expr_1 RSB index_operator;

// Operand
operand: literal
       | ID_VARPAR
       | ID_CONST
       | func_call
       | LP expr RP;

// Function call expression
func_call: (ID_FUNC | type_coersion) LP list_param RP;

list_param: param COMMA list_param
          | param
          | ;
param: literal | ID_VARPAR | expr;

// Type coercion
type_coersion: STR2INT | INT2STR
             | STR2BOOL | BOOL2STR
             | STR2FLOAT | FLOAT2STR;

// Operator
op_string: STR_CAT | STR_CMP;
op_relation: EQUAL | NOT_EQUAL | LESS| LESS_EQUAL | GREATER | GREATER_EQUAL;
op_andor: AND | OR;
op_adding: ADD | SUB;
op_multiplyng: MUL | DIV | MOD;

// Array
listARRAY: array COMMA listARRAY
        | array;
array: i_array | a_array | m_array;
// Indexed Array
i_array: ARRAY_TYPE LP listLIT RP;
// Associative Arrays
a_array: ARRAY_TYPE LP listKV RP;
// Multi-dimensional arrays
m_array: ARRAY_TYPE LP listARRAY RP;

listKV: keyValue COMMA listKV
      | keyValue;
keyValue: key ASSOCATE expr;
key: integer | STRING | ID_VARPAR;

listLIT: literal COMMA listLIT
       | literal
       | ;
literal: integer | FLOAT | boolean | STRING;

//---------------------------------------------------
// LEXER
// Type coercion function
STR2INT: 'str2int';
INT2STR: 'int2str' ;
STR2FLOAT: 'str2float';
FLOAT2STR: 'float2str';
STR2BOOL: 'str2bool';
BOOL2STR: 'bool2str';

// Identifiers
//identifier: ID_VARPAR | ID_FUNC | ID_CONST;
ID_VARPAR: '$'([A-Za-z0-9] | '_')*;
ID_CONST: [A-Z]([A-Za-z0-9] | '_')*;
ID_FUNC: '_'([A-Za-z0-9] | '_')*;

// Integer
integer: OCT | DEC | HEX | BIN;
OCT: '0'[0-7_]+;
DEC: [1-9] ([0-9_])* | '0';
HEX: '0'('x'|'X')[0-9A-Fa-f_]+;
BIN: '0'('b'|'B')('0' | '1' | '_')+;

// Float
fragment Num: ('-'| '+')?[0-9]+;
fragment FLOAT1: DEC ('e'Num | 'E'Num)?;
fragment FLOAT2: DEC ('e'Num | 'E'Num)? '.' DEC?;
fragment FLOAT3: DEC '.' DEC ('e'Num | 'E'Num)?;
FLOAT: FLOAT1 | FLOAT2 | FLOAT3;

// Boolean
boolean: TRUE | FALSE;

// Keywords
BREAK: 'break'; CONTINUE: 'continue'; IF :'if'; ELSEIF : 'elseif'; ElSE : 'else';
WHILE : 'while'; FOREACH : 'foreach'; AS : 'as'; FUNCTION : 'function';
TRUE : 'true'; FALSE : 'false'; ARRAY_TYPE : 'array'; DEFINE : 'define';

RETURN: 'return';

// String
fragment I_ESCAPE: '\\'~('b'|'t'|'n'|'f'|'r'|'\\'|'\'');
fragment ESCAPE: '\\' ('b'|'t'|'n'|'f'|'r'|'\\'|'\'');
fragment TMP: (~'"' | '""' | '\'"' );
ILLEGAL_ESCAPE: '"' (TMP* I_ESCAPE TMP*)+ '"';
STRING: '"' (ESCAPE|~'"' | '""' | '\'"' )* '"';

// Operators
NOT_EQUAL: '!='; GREATER: '>'; GREATER_EQUAL: '>='; LESS: '<'; LESS_EQUAL: '<=';
ADD: '+'; SUB: '-'; MUL: '*'; DIV: '/'; MOD: '%';
NOT: '!'; AND: '&&'; OR: '||'; EQUAL: '=='; ASSIGN: '=';
STR_CMP: '==.'; STR_CAT: '+.';

// a_array assign
ASSOCATE: '=>';

// seperators
DOT: '.'; COMMA: ','; SEMI: ';' ; COLON: ':';
LP: '('; RP: ')';
LSB: '['; RSB: ']';
LB: '{'; RB: '}';

// Comments
COMMENT:   '/*' .*? '*/' -> skip;
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

ERROR_CHAR: .;
UNCLOSE_STRING: '"' ( '\\' [btnfr"\\] | ~[\b\t\f\r\n\\"] )*;
UNTERMINATED_COMMENT: '/*' ~('/')*;