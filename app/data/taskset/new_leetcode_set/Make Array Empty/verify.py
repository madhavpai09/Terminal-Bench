
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.countOperationsToEmptyArray(*[[3, 4, -1]]) == 5
assert my_solution.countOperationsToEmptyArray(*[[1, 2, 4, 3]]) == 5
assert my_solution.countOperationsToEmptyArray(*[[1, 2, 3]]) == 3
assert my_solution.countOperationsToEmptyArray(*[[-18]]) == 1
assert my_solution.countOperationsToEmptyArray(*[[-17]]) == 1
assert my_solution.countOperationsToEmptyArray(*[[-13]]) == 1
assert my_solution.countOperationsToEmptyArray(*[[-8]]) == 1
assert my_solution.countOperationsToEmptyArray(*[[-6]]) == 1
assert my_solution.countOperationsToEmptyArray(*[[3]]) == 1
assert my_solution.countOperationsToEmptyArray(*[[14]]) == 1
assert my_solution.countOperationsToEmptyArray(*[[-20, -6]]) == 2
assert my_solution.countOperationsToEmptyArray(*[[-19, -11]]) == 2
assert my_solution.countOperationsToEmptyArray(*[[-17, -18]]) == 3
assert my_solution.countOperationsToEmptyArray(*[[-10, -1]]) == 2
assert my_solution.countOperationsToEmptyArray(*[[-10, 10]]) == 2
assert my_solution.countOperationsToEmptyArray(*[[-9, -10]]) == 3
assert my_solution.countOperationsToEmptyArray(*[[-3, -4]]) == 3
assert my_solution.countOperationsToEmptyArray(*[[1, -4]]) == 3
assert my_solution.countOperationsToEmptyArray(*[[1, 0]]) == 3
assert my_solution.countOperationsToEmptyArray(*[[5, 18]]) == 2
