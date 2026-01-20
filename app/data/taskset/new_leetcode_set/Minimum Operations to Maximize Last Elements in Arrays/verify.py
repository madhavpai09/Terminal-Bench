
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.minOperations(*[[1, 2, 7], [4, 5, 3]]) == 1
assert my_solution.minOperations(*[[2, 3, 4, 5, 9], [8, 8, 4, 4, 4]]) == 2
assert my_solution.minOperations(*[[1, 5, 4], [2, 5, 3]]) == -1
assert my_solution.minOperations(*[[1], [1]]) == 0
assert my_solution.minOperations(*[[1, 2], [2, 1]]) == 1
assert my_solution.minOperations(*[[1, 1, 10], [1, 5, 1]]) == 1
assert my_solution.minOperations(*[[1, 4, 16], [16, 16, 16]]) == 0
assert my_solution.minOperations(*[[1, 5, 15], [1, 1, 1]]) == 0
assert my_solution.minOperations(*[[2, 5, 7], [2, 2, 2]]) == 0
assert my_solution.minOperations(*[[8, 9, 10], [10, 9, 9]]) == 1
assert my_solution.minOperations(*[[9, 14, 14], [14, 11, 14]]) == 0
assert my_solution.minOperations(*[[16, 16, 16], [6, 7, 16]]) == 0
assert my_solution.minOperations(*[[19, 7, 19], [5, 19, 19]]) == 0
assert my_solution.minOperations(*[[1, 1, 8, 9], [1, 7, 1, 1]]) == 1
assert my_solution.minOperations(*[[1, 5, 9, 9], [9, 9, 8, 9]]) == 0
assert my_solution.minOperations(*[[1, 7, 7, 7], [7, 3, 3, 7]]) == 0
assert my_solution.minOperations(*[[10, 18, 12, 12], [19, 6, 5, 12]]) == -1
assert my_solution.minOperations(*[[12, 9, 11, 12], [3, 9, 9, 9]]) == 0
assert my_solution.minOperations(*[[15, 54, 22, 54], [54, 19, 54, 54]]) == 0
assert my_solution.minOperations(*[[20, 20, 20, 20], [5, 8, 19, 20]]) == 0
