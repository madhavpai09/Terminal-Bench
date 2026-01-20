
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.minimumChanges(*['abcac', 2]) == 1
assert my_solution.minimumChanges(*['abcdef', 2]) == 2
assert my_solution.minimumChanges(*['aabbaa', 3]) == 0
assert my_solution.minimumChanges(*['aq', 1]) == 1
assert my_solution.minimumChanges(*['bb', 1]) == 0
assert my_solution.minimumChanges(*['aac', 1]) == 1
assert my_solution.minimumChanges(*['abcc', 1]) == 2
assert my_solution.minimumChanges(*['acba', 2]) == 2
assert my_solution.minimumChanges(*['edaswf', 1]) == 2
assert my_solution.minimumChanges(*['aabcbaa', 1]) == 0
assert my_solution.minimumChanges(*['dqpldq', 3]) == 3
assert my_solution.minimumChanges(*['eksddulf', 1]) == 3
assert my_solution.minimumChanges(*['aaaaacabbb', 1]) == 3
assert my_solution.minimumChanges(*['aaabacacbb', 1]) == 3
assert my_solution.minimumChanges(*['abbbbacaaa', 1]) == 3
assert my_solution.minimumChanges(*['abcccbaccb', 1]) == 2
assert my_solution.minimumChanges(*['baacbbbaba', 1]) == 2
assert my_solution.minimumChanges(*['babcbaccba', 1]) == 1
assert my_solution.minimumChanges(*['cabbcabcbc', 1]) == 3
assert my_solution.minimumChanges(*['ccbccaaabb', 1]) == 4
