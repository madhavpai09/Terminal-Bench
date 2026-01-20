
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.longestEqualSubarray(*[[1, 3, 2, 3, 1, 3], 3]) == 3
assert my_solution.longestEqualSubarray(*[[1, 1, 2, 2, 1, 1], 2]) == 4
assert my_solution.longestEqualSubarray(*[[1], 0]) == 1
assert my_solution.longestEqualSubarray(*[[1], 1]) == 1
assert my_solution.longestEqualSubarray(*[[2, 1], 1]) == 1
assert my_solution.longestEqualSubarray(*[[2, 2], 1]) == 2
assert my_solution.longestEqualSubarray(*[[1, 1], 0]) == 2
assert my_solution.longestEqualSubarray(*[[2, 1], 0]) == 1
assert my_solution.longestEqualSubarray(*[[1, 2], 1]) == 1
assert my_solution.longestEqualSubarray(*[[2, 2], 2]) == 2
assert my_solution.longestEqualSubarray(*[[2, 3, 2], 1]) == 2
assert my_solution.longestEqualSubarray(*[[3, 2, 2], 1]) == 2
assert my_solution.longestEqualSubarray(*[[3, 1, 1], 2]) == 2
assert my_solution.longestEqualSubarray(*[[1, 2, 3], 2]) == 1
assert my_solution.longestEqualSubarray(*[[1, 2, 3], 3]) == 1
assert my_solution.longestEqualSubarray(*[[2, 3, 1], 2]) == 1
assert my_solution.longestEqualSubarray(*[[2, 2, 1], 1]) == 2
assert my_solution.longestEqualSubarray(*[[1, 3, 2], 3]) == 1
assert my_solution.longestEqualSubarray(*[[2, 3, 3], 3]) == 2
assert my_solution.longestEqualSubarray(*[[3, 2, 3], 3]) == 2
