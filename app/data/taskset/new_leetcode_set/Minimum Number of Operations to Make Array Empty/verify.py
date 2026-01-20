
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.minOperations(*[[2, 3, 3, 2, 2, 4, 2, 3, 4]]) == 4
assert my_solution.minOperations(*[[2, 1, 2, 2, 3, 3]]) == -1
assert my_solution.minOperations(*[[3, 3]]) == 1
assert my_solution.minOperations(*[[14, 12, 14, 14, 12, 14, 14, 12, 12, 12, 12, 14, 14, 12, 14, 14, 14, 12, 12]]) == 7
assert my_solution.minOperations(*[[2, 2, 2, 2, 2, 2, 2, 2, 2]]) == 3
assert my_solution.minOperations(*[[15, 3, 3, 15, 15, 13, 8, 15, 6, 15, 3, 1, 8, 8, 15]]) == -1
assert my_solution.minOperations(*[[19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19]]) == 5
assert my_solution.minOperations(*[[13, 7, 13, 7, 13, 7, 13, 13, 7]]) == 4
assert my_solution.minOperations(*[[5, 5]]) == 1
assert my_solution.minOperations(*[[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]]) == 5
assert my_solution.minOperations(*[[3, 14, 3, 14, 3, 14, 14, 3, 3, 14, 14, 14, 3, 14, 14, 3, 14, 14, 14, 3]]) == 7
assert my_solution.minOperations(*[[16, 16, 16, 19, 16, 3, 16, 8, 16, 16, 16, 19, 3, 16, 16]]) == -1
assert my_solution.minOperations(*[[11, 11, 11, 11, 19, 11, 11, 11, 11, 11, 19, 11, 11, 11, 11, 11, 19]]) == 6
assert my_solution.minOperations(*[[1, 1, 1, 5, 1, 5, 1, 1, 1, 1, 1, 1, 1]]) == 5
assert my_solution.minOperations(*[[16, 16, 16, 3, 16, 16, 3]]) == 3
assert my_solution.minOperations(*[[14, 4, 4, 19, 19]]) == -1
assert my_solution.minOperations(*[[1, 14, 1, 1, 1]]) == -1
assert my_solution.minOperations(*[[3, 10, 11, 3, 3, 11, 3, 3, 3, 3, 3, 3, 3, 3, 10, 3, 3, 3]]) == 7
assert my_solution.minOperations(*[[3, 8, 8, 8, 8, 3, 8, 8, 8, 8, 8, 8, 8, 8]]) == 5
assert my_solution.minOperations(*[[9, 9, 9]]) == 1
