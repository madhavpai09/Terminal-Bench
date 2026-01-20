
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.semiOrderedPermutation(*[[2, 1, 4, 3]]) == 2
assert my_solution.semiOrderedPermutation(*[[2, 4, 1, 3]]) == 3
assert my_solution.semiOrderedPermutation(*[[1, 3, 4, 2, 5]]) == 0
assert my_solution.semiOrderedPermutation(*[[1, 2]]) == 0
assert my_solution.semiOrderedPermutation(*[[2, 1]]) == 1
assert my_solution.semiOrderedPermutation(*[[1, 2, 3]]) == 0
assert my_solution.semiOrderedPermutation(*[[2, 1, 3]]) == 1
assert my_solution.semiOrderedPermutation(*[[2, 3, 1]]) == 2
assert my_solution.semiOrderedPermutation(*[[1, 3, 2]]) == 1
assert my_solution.semiOrderedPermutation(*[[3, 1, 2]]) == 2
assert my_solution.semiOrderedPermutation(*[[3, 2, 1]]) == 3
assert my_solution.semiOrderedPermutation(*[[1, 2, 3, 4]]) == 0
assert my_solution.semiOrderedPermutation(*[[2, 1, 3, 4]]) == 1
assert my_solution.semiOrderedPermutation(*[[2, 3, 1, 4]]) == 2
assert my_solution.semiOrderedPermutation(*[[2, 3, 4, 1]]) == 3
assert my_solution.semiOrderedPermutation(*[[1, 3, 2, 4]]) == 0
assert my_solution.semiOrderedPermutation(*[[3, 1, 2, 4]]) == 1
assert my_solution.semiOrderedPermutation(*[[3, 2, 1, 4]]) == 2
assert my_solution.semiOrderedPermutation(*[[3, 2, 4, 1]]) == 3
assert my_solution.semiOrderedPermutation(*[[1, 3, 4, 2]]) == 1
