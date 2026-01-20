
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.minOperations(*[[2, 1, 3, 4], 1]) == 2
assert my_solution.minOperations(*[[2, 0, 2, 0], 0]) == 0
assert my_solution.minOperations(*[[4], 7]) == 2
assert my_solution.minOperations(*[[3, 13, 9, 8, 5, 18, 11, 10], 13]) == 2
assert my_solution.minOperations(*[[9, 7, 9, 14, 8, 6], 12]) == 3
assert my_solution.minOperations(*[[13, 9, 10, 16, 11, 8, 1], 17]) == 3
assert my_solution.minOperations(*[[12, 14], 1]) == 2
assert my_solution.minOperations(*[[18, 18], 20]) == 2
assert my_solution.minOperations(*[[3, 5, 1, 1], 19]) == 3
assert my_solution.minOperations(*[[7, 0, 0, 0], 8]) == 4
assert my_solution.minOperations(*[[13, 15, 19, 18, 2, 9, 18, 11, 0, 7], 6]) == 1
assert my_solution.minOperations(*[[9, 15, 19, 15, 10, 15, 14, 0, 2, 5], 20]) == 1
assert my_solution.minOperations(*[[19, 4, 19, 6, 3, 19, 14, 4, 16, 12], 4]) == 0
assert my_solution.minOperations(*[[2, 10, 5, 5, 12, 3, 14, 6, 11, 14], 3]) == 2
assert my_solution.minOperations(*[[11, 20], 10]) == 3
assert my_solution.minOperations(*[[10, 12, 5, 3, 16, 0], 1]) == 2
assert my_solution.minOperations(*[[0, 4, 4, 7, 14, 13], 1]) == 2
assert my_solution.minOperations(*[[16, 2, 20, 13, 15, 20, 13], 16]) == 3
assert my_solution.minOperations(*[[19, 11, 11, 0, 16, 2, 2, 0, 9], 4]) == 3
assert my_solution.minOperations(*[[10, 17, 19, 8, 15], 19]) == 3
