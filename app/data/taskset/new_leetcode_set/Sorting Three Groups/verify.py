
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.minimumOperations(*[[2, 1, 3, 2, 1]]) == 3
assert my_solution.minimumOperations(*[[1, 3, 2, 1, 3, 3]]) == 2
assert my_solution.minimumOperations(*[[2, 2, 2, 2, 3, 3]]) == 0
assert my_solution.minimumOperations(*[[1]]) == 0
assert my_solution.minimumOperations(*[[2]]) == 0
assert my_solution.minimumOperations(*[[3]]) == 0
assert my_solution.minimumOperations(*[[1, 2]]) == 0
assert my_solution.minimumOperations(*[[2, 2]]) == 0
assert my_solution.minimumOperations(*[[3, 2]]) == 1
assert my_solution.minimumOperations(*[[1, 3]]) == 0
assert my_solution.minimumOperations(*[[2, 3]]) == 0
assert my_solution.minimumOperations(*[[3, 3]]) == 0
assert my_solution.minimumOperations(*[[1, 1, 2]]) == 0
assert my_solution.minimumOperations(*[[2, 1, 2]]) == 1
assert my_solution.minimumOperations(*[[3, 1, 2]]) == 1
assert my_solution.minimumOperations(*[[1, 2, 2]]) == 0
assert my_solution.minimumOperations(*[[2, 2, 2]]) == 0
assert my_solution.minimumOperations(*[[3, 2, 2]]) == 1
assert my_solution.minimumOperations(*[[1, 3, 2]]) == 1
assert my_solution.minimumOperations(*[[2, 3, 2]]) == 1
