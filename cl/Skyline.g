grammar Skyline;

root : expr EOF ;

expr : sky
     | IDENT ASSIGN sky
     ;

sky : msky (SUM msky | RES NUM | SUM NUM)* ;

msky : rsky (MUL rsky | MUL NUM)* ;

rsky : (RES)* basicsky ;

basicsky : '(' sky ')'
         | EDIF
         | EDIFS
         | RAND
         | IDENT
         ;

IDENT : [a-zA-Z] [a-zA-Z0-9]* ;
NUM : [0-9]+ ;
INT : NUM
    | '-' NUM
    ;
RES : '-' ;
SUM : '+' ;
MUL : '*' ;
ASSIGN : ':=' ;
EDIF : '(' INT ',' NUM ',' INT ')' ;
RAND : '{' NUM ',' NUM ',' NUM ',' INT ',' INT '}' ;
EDIFS : '[' (EDIF ',')* EDIF ']' ;
WS : [ \n\t\r]+ -> skip ;
