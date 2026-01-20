
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.maxIncreasingGroups(*[[1, 2, 5]]) == 3
assert my_solution.maxIncreasingGroups(*[[2, 1, 2]]) == 2
assert my_solution.maxIncreasingGroups(*[[1, 1]]) == 1
assert my_solution.maxIncreasingGroups(*[[1, 4]]) == 2
assert my_solution.maxIncreasingGroups(*[[1, 5]]) == 2
assert my_solution.maxIncreasingGroups(*[[1, 7]]) == 2
assert my_solution.maxIncreasingGroups(*[[1, 8]]) == 2
assert my_solution.maxIncreasingGroups(*[[2, 1]]) == 2
assert my_solution.maxIncreasingGroups(*[[2, 2]]) == 2
assert my_solution.maxIncreasingGroups(*[[2, 3]]) == 2
assert my_solution.maxIncreasingGroups(*[[2, 4]]) == 2
assert my_solution.maxIncreasingGroups(*[[2, 5]]) == 2
assert my_solution.maxIncreasingGroups(*[[2, 7]]) == 2
assert my_solution.maxIncreasingGroups(*[[2, 8]]) == 2
assert my_solution.maxIncreasingGroups(*[[2, 9]]) == 2
assert my_solution.maxIncreasingGroups(*[[3, 1]]) == 2
assert my_solution.maxIncreasingGroups(*[[3, 4]]) == 2
assert my_solution.maxIncreasingGroups(*[[3, 7]]) == 2
assert my_solution.maxIncreasingGroups(*[[3, 10]]) == 2
assert my_solution.maxIncreasingGroups(*[[4, 1]]) == 2
