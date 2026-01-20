
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.minOperations(*[[1, 2, 8], 7]) == 1
assert my_solution.minOperations(*[[1, 32, 1, 2], 12]) == 2
assert my_solution.minOperations(*[[1, 32, 1], 35]) == -1
assert my_solution.minOperations(*[[1], 1]) == 0
assert my_solution.minOperations(*[[16, 128, 32], 1]) == 4
assert my_solution.minOperations(*[[1, 1], 2]) == 0
assert my_solution.minOperations(*[[64, 128, 128], 2]) == 5
assert my_solution.minOperations(*[[2], 2]) == 0
assert my_solution.minOperations(*[[32, 256, 4], 2]) == 1
assert my_solution.minOperations(*[[1, 1, 1], 3]) == 0
assert my_solution.minOperations(*[[1, 256, 16, 128], 3]) == 3
assert my_solution.minOperations(*[[1, 2], 3]) == 0
assert my_solution.minOperations(*[[16, 16, 4], 3]) == 2
assert my_solution.minOperations(*[[1, 1, 1, 1], 4]) == 0
assert my_solution.minOperations(*[[128, 1, 128, 1, 64], 4]) == 4
assert my_solution.minOperations(*[[2, 1, 1], 4]) == 0
assert my_solution.minOperations(*[[8, 2, 64, 32], 4]) == 1
assert my_solution.minOperations(*[[16, 128, 8, 1, 1], 4]) == 1
assert my_solution.minOperations(*[[1, 2, 1], 4]) == 0
assert my_solution.minOperations(*[[128, 8, 8, 2], 4]) == 1
