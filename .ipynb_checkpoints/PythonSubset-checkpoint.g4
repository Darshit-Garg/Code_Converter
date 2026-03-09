
grammar PythonSubset;

program : statement+ ;

statement : assignment ;

assignment : ID '=' NUMBER;

ID : [a-zA-Z_][a-zA-Z_0-9]* ;
NUMBER : [0-9]+ ;
WS : [\s\t\r\n]+ -> skip ;
