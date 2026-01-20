
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.minimumCost(*[[1, 3, 2, 6, 4, 2], 3, 3]) == 5
assert my_solution.minimumCost(*[[10, 1, 2, 2, 2, 1], 4, 3]) == 15
assert my_solution.minimumCost(*[[10, 8, 18, 9], 3, 1]) == 36
assert my_solution.minimumCost(*[[1, 1, 1], 3, 1]) == 3
assert my_solution.minimumCost(*[[1, 1, 3], 3, 1]) == 5
assert my_solution.minimumCost(*[[1, 2, 2], 3, 1]) == 5
assert my_solution.minimumCost(*[[1, 2, 5], 3, 1]) == 8
assert my_solution.minimumCost(*[[1, 4, 4], 3, 1]) == 9
assert my_solution.minimumCost(*[[2, 2, 1], 3, 1]) == 5
assert my_solution.minimumCost(*[[2, 3, 2], 3, 1]) == 7
assert my_solution.minimumCost(*[[2, 5, 4], 3, 1]) == 11
assert my_solution.minimumCost(*[[3, 1, 2], 3, 1]) == 6
assert my_solution.minimumCost(*[[3, 1, 3], 3, 1]) == 7
assert my_solution.minimumCost(*[[3, 2, 2], 3, 1]) == 7
assert my_solution.minimumCost(*[[3, 3, 2], 3, 1]) == 8
assert my_solution.minimumCost(*[[3, 4, 1], 3, 1]) == 8
assert my_solution.minimumCost(*[[3, 5, 3], 3, 1]) == 11
assert my_solution.minimumCost(*[[4, 1, 4], 3, 1]) == 9
assert my_solution.minimumCost(*[[4, 1, 5], 3, 1]) == 10
assert my_solution.minimumCost(*[[4, 2, 1], 3, 1]) == 7
