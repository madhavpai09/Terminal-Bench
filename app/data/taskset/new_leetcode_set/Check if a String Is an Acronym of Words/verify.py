
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.isAcronym(*[['alice', 'bob', 'charlie'], 'abc']) == True
assert my_solution.isAcronym(*[['an', 'apple'], 'a']) == False
assert my_solution.isAcronym(*[['never', 'gonna', 'give', 'up', 'on', 'you'], 'ngguoy']) == True
assert my_solution.isAcronym(*[['ad', 'uadhrwxki'], 'au']) == True
assert my_solution.isAcronym(*[['afkc', 'icxufam'], 'ai']) == True
assert my_solution.isAcronym(*[['afqcpzsx', 'icenu'], 'yi']) == False
assert my_solution.isAcronym(*[['ahbibag', 'aoximesw'], 'aa']) == True
assert my_solution.isAcronym(*[['auqoc', 'koioxa'], 'ak']) == True
assert my_solution.isAcronym(*[['b', 'x'], 'bx']) == True
assert my_solution.isAcronym(*[['bpctc', 'kaqquqbpmw'], 'bk']) == True
assert my_solution.isAcronym(*[['c', 'df'], 'bd']) == False
assert my_solution.isAcronym(*[['c', 'evlvvhrsqa'], 'ce']) == True
assert my_solution.isAcronym(*[['cfsrsyt', 'md'], 'cm']) == True
assert my_solution.isAcronym(*[['ddnlfpvy', 'exs'], 'de']) == True
assert my_solution.isAcronym(*[['deacf', 'hldiauk'], 'dh']) == True
assert my_solution.isAcronym(*[['dllcn', 'tnzrnzypg'], 'dt']) == True
assert my_solution.isAcronym(*[['dmekslxlpo', 'wqdgxqwdk'], 'dw']) == True
assert my_solution.isAcronym(*[['dv', 'g'], 'sg']) == False
assert my_solution.isAcronym(*[['dvn', 'acafe'], 'dp']) == False
assert my_solution.isAcronym(*[['dwrvgkxdtm', 'wy'], 'hw']) == False
