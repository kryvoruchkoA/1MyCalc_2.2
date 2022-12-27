         HOW TO ORGANIZE CALCULATION

1) set oriority for all operations
2) parentheses increase level of all internal operations on 10 (next internal 20 and so on)
3) all function must have ( ) , to define their argument

4) calculation of the "sentence" performed in a loop:
    4.1 find the operation with highest priority
    4.2 calculate it and perform replaycment with the result
    4.3 next loop cycle



Storage likes a 2D array. So it is represented as a table with a strings.
Each string is a item record which consist of 3 values:

priority == {from 0 for numbers to 10 for hight priority calculations}
val type == {num, operand}
the item (itself) == {'12', 'SUM', 'MULT', etc.}
e.g.:
12 + 4 * 3
[[0, 'num', 12],[1, 'opr', 'sum'],[0, 'num', 4],[2, 'opr', 'mult'],[0, 'num', 3]]


Priority range:

Numbers, Variables => 0
# Variable => 1 ( ? ) - a variant
ADD (+), SUB (-) => 1
MUL (MULT * ), DIV ( / ) => 2

SIN, COS, ..., Ln, Lg