
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.minCapability(*[[2, 3, 5, 9], 2]) == 5
assert my_solution.minCapability(*[[2, 7, 9, 3, 1], 2]) == 2
assert my_solution.minCapability(*[[2, 2], 1]) == 2
assert my_solution.minCapability(*[[7, 3, 9, 5], 2]) == 5
assert my_solution.minCapability(*[[1, 4, 5], 1]) == 1
assert my_solution.minCapability(*[[1], 1]) == 1
assert my_solution.minCapability(*[[7, 1, 8, 11], 1]) == 1
assert my_solution.minCapability(*[[4, 22, 11, 14, 25], 3]) == 25
assert my_solution.minCapability(*[[10, 15, 6, 2], 1]) == 2
assert my_solution.minCapability(*[[9, 25, 16, 6, 18], 1]) == 6
assert my_solution.minCapability(*[[3, 6, 6, 9], 2]) == 6
assert my_solution.minCapability(*[[7, 14, 3, 6], 1]) == 3
assert my_solution.minCapability(*[[4, 4], 1]) == 4
assert my_solution.minCapability(*[[2, 1], 1]) == 1
assert my_solution.minCapability(*[[9, 6, 2], 1]) == 2
assert my_solution.minCapability(*[[3, 4, 1], 1]) == 1
assert my_solution.minCapability(*[[4, 2], 1]) == 2
assert my_solution.minCapability(*[[9, 6, 20, 21, 8], 3]) == 20
assert my_solution.minCapability(*[[13, 1, 13, 7], 2]) == 7
assert my_solution.minCapability(*[[2, 12, 11, 13], 2]) == 11
