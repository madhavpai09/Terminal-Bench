
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.maxSum(*[[2, 6, 7, 3, 1, 7], 3, 4]) == 18
assert my_solution.maxSum(*[[5, 9, 9, 2, 4, 5, 4], 1, 3]) == 23
assert my_solution.maxSum(*[[1, 2, 1, 2, 1, 2, 1], 3, 3]) == 0
assert my_solution.maxSum(*[[1], 1, 1]) == 1
assert my_solution.maxSum(*[[1, 1], 2, 2]) == 0
assert my_solution.maxSum(*[[1, 1, 1], 1, 1]) == 1
assert my_solution.maxSum(*[[1, 1, 1, 1], 1, 1]) == 1
assert my_solution.maxSum(*[[1, 1, 1, 2], 2, 4]) == 5
assert my_solution.maxSum(*[[1, 1, 1, 3], 2, 2]) == 4
assert my_solution.maxSum(*[[1, 1, 1, 4], 2, 4]) == 7
assert my_solution.maxSum(*[[1, 1, 2], 1, 1]) == 2
assert my_solution.maxSum(*[[1, 1, 2, 1], 2, 2]) == 3
assert my_solution.maxSum(*[[1, 1, 2, 2], 1, 3]) == 5
assert my_solution.maxSum(*[[1, 1, 2, 3], 1, 1]) == 3
assert my_solution.maxSum(*[[1, 1, 2, 4], 1, 1]) == 4
assert my_solution.maxSum(*[[1, 1, 3], 1, 2]) == 4
assert my_solution.maxSum(*[[1, 1, 3, 1], 2, 4]) == 6
assert my_solution.maxSum(*[[1, 1, 3, 2], 1, 2]) == 5
assert my_solution.maxSum(*[[1, 1, 3, 3], 1, 1]) == 3
assert my_solution.maxSum(*[[1, 1, 3, 4], 1, 1]) == 4
