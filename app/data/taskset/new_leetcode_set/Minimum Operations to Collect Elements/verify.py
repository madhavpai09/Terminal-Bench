
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.minOperations(*[[3, 1, 5, 4, 2], 2]) == 4
assert my_solution.minOperations(*[[3, 1, 5, 4, 2], 5]) == 5
assert my_solution.minOperations(*[[3, 2, 5, 3, 1], 3]) == 4
assert my_solution.minOperations(*[[1], 1]) == 1
assert my_solution.minOperations(*[[1, 1], 1]) == 1
assert my_solution.minOperations(*[[1, 2], 1]) == 2
assert my_solution.minOperations(*[[1, 2], 2]) == 2
assert my_solution.minOperations(*[[2, 1], 1]) == 1
assert my_solution.minOperations(*[[2, 1], 2]) == 2
assert my_solution.minOperations(*[[1, 1, 1], 1]) == 1
assert my_solution.minOperations(*[[1, 1, 2], 1]) == 2
assert my_solution.minOperations(*[[1, 1, 2], 2]) == 2
assert my_solution.minOperations(*[[1, 1, 3], 1]) == 2
assert my_solution.minOperations(*[[1, 2, 1], 1]) == 1
assert my_solution.minOperations(*[[1, 2, 1], 2]) == 2
assert my_solution.minOperations(*[[1, 2, 2], 1]) == 3
assert my_solution.minOperations(*[[1, 2, 2], 2]) == 3
assert my_solution.minOperations(*[[1, 2, 3], 1]) == 3
assert my_solution.minOperations(*[[1, 2, 3], 2]) == 3
assert my_solution.minOperations(*[[1, 2, 3], 3]) == 3
