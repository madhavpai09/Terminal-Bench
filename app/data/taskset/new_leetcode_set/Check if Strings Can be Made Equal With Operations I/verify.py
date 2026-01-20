
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.canBeEqual(*['abcd', 'cdab']) == True
assert my_solution.canBeEqual(*['abcd', 'dacb']) == False
assert my_solution.canBeEqual(*['bnxw', 'bwxn']) == True
assert my_solution.canBeEqual(*['gudo', 'ogdu']) == False
assert my_solution.canBeEqual(*['xsvc', 'vcxs']) == True
assert my_solution.canBeEqual(*['hvsz', 'hzsv']) == True
assert my_solution.canBeEqual(*['zzon', 'zozn']) == False
assert my_solution.canBeEqual(*['zrmq', 'mrzq']) == True
assert my_solution.canBeEqual(*['cmpr', 'rmcp']) == False
assert my_solution.canBeEqual(*['qnde', 'flsi']) == False
assert my_solution.canBeEqual(*['kina', 'kina']) == True
assert my_solution.canBeEqual(*['vofo', 'oofv']) == False
assert my_solution.canBeEqual(*['riti', 'riti']) == True
assert my_solution.canBeEqual(*['ifjz', 'jzfi']) == False
assert my_solution.canBeEqual(*['hazw', 'pfmp']) == False
assert my_solution.canBeEqual(*['goze', 'gezo']) == True
assert my_solution.canBeEqual(*['gcdm', 'dmgc']) == True
assert my_solution.canBeEqual(*['fymg', 'famj']) == False
assert my_solution.canBeEqual(*['seeo', 'vfvm']) == False
assert my_solution.canBeEqual(*['kvne', 'nekv']) == True
