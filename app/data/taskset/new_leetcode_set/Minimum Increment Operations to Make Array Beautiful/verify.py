
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.minIncrementOperations(*[[2, 3, 0, 0, 2], 4]) == 3
assert my_solution.minIncrementOperations(*[[0, 1, 3, 3], 5]) == 2
assert my_solution.minIncrementOperations(*[[1, 1, 2], 1]) == 0
assert my_solution.minIncrementOperations(*[[0, 5, 5], 8]) == 3
assert my_solution.minIncrementOperations(*[[0, 18, 28], 93]) == 65
assert my_solution.minIncrementOperations(*[[0, 24, 14], 7]) == 0
assert my_solution.minIncrementOperations(*[[2, 3, 4], 3]) == 0
assert my_solution.minIncrementOperations(*[[3, 5, 9], 6]) == 0
assert my_solution.minIncrementOperations(*[[4, 3, 0], 2]) == 0
assert my_solution.minIncrementOperations(*[[5, 6, 5], 9]) == 3
assert my_solution.minIncrementOperations(*[[6, 9, 6], 3]) == 0
assert my_solution.minIncrementOperations(*[[7, 9, 0], 6]) == 0
assert my_solution.minIncrementOperations(*[[7, 47, 16], 39]) == 0
assert my_solution.minIncrementOperations(*[[9, 6, 1], 6]) == 0
assert my_solution.minIncrementOperations(*[[41, 44, 37], 55]) == 11
assert my_solution.minIncrementOperations(*[[48, 3, 13], 1]) == 0
assert my_solution.minIncrementOperations(*[[1, 2, 6, 9], 8]) == 2
assert my_solution.minIncrementOperations(*[[1, 3, 1, 6], 6]) == 3
assert my_solution.minIncrementOperations(*[[2, 35, 41, 20], 4]) == 0
assert my_solution.minIncrementOperations(*[[3, 9, 9, 7], 6]) == 0
