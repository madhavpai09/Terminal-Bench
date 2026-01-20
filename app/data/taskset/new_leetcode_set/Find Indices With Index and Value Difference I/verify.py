
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.findIndices(*[[5, 1, 4, 1], 2, 4]) == [0, 3]
assert my_solution.findIndices(*[[2, 1], 0, 0]) == [0, 0]
assert my_solution.findIndices(*[[1, 2, 3], 2, 4]) == [-1, -1]
assert my_solution.findIndices(*[[0], 0, 0]) == [0, 0]
assert my_solution.findIndices(*[[3], 0, 0]) == [0, 0]
assert my_solution.findIndices(*[[3], 1, 1]) == [-1, -1]
assert my_solution.findIndices(*[[4], 1, 0]) == [-1, -1]
assert my_solution.findIndices(*[[5], 1, 3]) == [-1, -1]
assert my_solution.findIndices(*[[7], 1, 7]) == [-1, -1]
assert my_solution.findIndices(*[[8], 0, 2]) == [-1, -1]
assert my_solution.findIndices(*[[8], 1, 7]) == [-1, -1]
assert my_solution.findIndices(*[[10], 0, 9]) == [-1, -1]
assert my_solution.findIndices(*[[11], 1, 0]) == [-1, -1]
assert my_solution.findIndices(*[[18], 1, 4]) == [-1, -1]
assert my_solution.findIndices(*[[38], 1, 34]) == [-1, -1]
assert my_solution.findIndices(*[[40], 1, 2]) == [-1, -1]
assert my_solution.findIndices(*[[5, 10], 1, 2]) == [0, 1]
assert my_solution.findIndices(*[[5, 48], 0, 29]) == [0, 1]
assert my_solution.findIndices(*[[6, 3], 1, 2]) == [0, 1]
assert my_solution.findIndices(*[[7, 6], 1, 0]) == [0, 1]
