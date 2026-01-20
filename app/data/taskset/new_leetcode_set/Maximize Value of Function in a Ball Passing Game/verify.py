
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.getMaxFunctionValue(*[[2, 0, 1], 4]) == 6
assert my_solution.getMaxFunctionValue(*[[1, 1, 1, 2, 3], 3]) == 10
assert my_solution.getMaxFunctionValue(*[[0], 1]) == 0
assert my_solution.getMaxFunctionValue(*[[0], 2]) == 0
assert my_solution.getMaxFunctionValue(*[[0], 3]) == 0
assert my_solution.getMaxFunctionValue(*[[0], 100]) == 0
assert my_solution.getMaxFunctionValue(*[[0, 0], 1]) == 1
assert my_solution.getMaxFunctionValue(*[[0, 0], 7]) == 1
assert my_solution.getMaxFunctionValue(*[[0, 0], 10]) == 1
assert my_solution.getMaxFunctionValue(*[[0, 0], 13]) == 1
assert my_solution.getMaxFunctionValue(*[[0, 0], 16]) == 1
assert my_solution.getMaxFunctionValue(*[[0, 1], 1]) == 2
assert my_solution.getMaxFunctionValue(*[[0, 1], 3]) == 4
assert my_solution.getMaxFunctionValue(*[[0, 1], 5]) == 6
assert my_solution.getMaxFunctionValue(*[[0, 1], 8]) == 9
assert my_solution.getMaxFunctionValue(*[[0, 1], 13]) == 14
assert my_solution.getMaxFunctionValue(*[[0, 1], 14]) == 15
assert my_solution.getMaxFunctionValue(*[[0, 1], 15]) == 16
assert my_solution.getMaxFunctionValue(*[[1, 0], 5]) == 3
assert my_solution.getMaxFunctionValue(*[[1, 0], 6]) == 4
