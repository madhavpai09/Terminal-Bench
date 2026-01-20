
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.findIndices(*[[5, 1, 4, 1], 2, 4]) == [0, 3]
assert my_solution.findIndices(*[[2, 1], 0, 0]) == [0, 0]
assert my_solution.findIndices(*[[1, 2, 3], 2, 4]) == [-1, -1]
assert my_solution.findIndices(*[[1], 0, 1]) == [-1, -1]
assert my_solution.findIndices(*[[1], 1, 0]) == [-1, -1]
assert my_solution.findIndices(*[[2], 0, 2]) == [-1, -1]
assert my_solution.findIndices(*[[6], 1, 4]) == [-1, -1]
assert my_solution.findIndices(*[[7], 0, 0]) == [0, 0]
assert my_solution.findIndices(*[[8], 1, 6]) == [-1, -1]
assert my_solution.findIndices(*[[9], 0, 1]) == [-1, -1]
assert my_solution.findIndices(*[[9], 1, 9]) == [-1, -1]
assert my_solution.findIndices(*[[12], 0, 5]) == [-1, -1]
assert my_solution.findIndices(*[[16], 0, 16]) == [-1, -1]
assert my_solution.findIndices(*[[16], 1, 6]) == [-1, -1]
assert my_solution.findIndices(*[[46], 0, 36]) == [-1, -1]
assert my_solution.findIndices(*[[0, 10], 2, 4]) == [-1, -1]
assert my_solution.findIndices(*[[2, 7], 2, 7]) == [-1, -1]
assert my_solution.findIndices(*[[5, 1], 2, 5]) == [-1, -1]
assert my_solution.findIndices(*[[5, 12], 0, 10]) == [-1, -1]
assert my_solution.findIndices(*[[8, 0], 1, 7]) == [0, 1]
