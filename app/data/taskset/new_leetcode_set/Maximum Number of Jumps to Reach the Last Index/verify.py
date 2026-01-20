
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.maximumJumps(*[[1, 3, 6, 4, 1, 2], 2]) == 3
assert my_solution.maximumJumps(*[[1, 3, 6, 4, 1, 2], 3]) == 5
assert my_solution.maximumJumps(*[[1, 3, 6, 4, 1, 2], 0]) == -1
assert my_solution.maximumJumps(*[[0, 1], 0]) == -1
assert my_solution.maximumJumps(*[[0, 1], 1]) == 1
assert my_solution.maximumJumps(*[[0, 1], 2]) == 1
assert my_solution.maximumJumps(*[[1, 0], 0]) == -1
assert my_solution.maximumJumps(*[[1, 0], 1]) == 1
assert my_solution.maximumJumps(*[[1, 0], 2]) == 1
assert my_solution.maximumJumps(*[[0, 1, 2], 0]) == -1
assert my_solution.maximumJumps(*[[0, 1, 2], 1]) == 2
assert my_solution.maximumJumps(*[[0, 1, 2], 2]) == 2
assert my_solution.maximumJumps(*[[0, 1, 2], 3]) == 2
assert my_solution.maximumJumps(*[[0, 2, 1], 0]) == -1
assert my_solution.maximumJumps(*[[0, 2, 1], 1]) == 1
assert my_solution.maximumJumps(*[[0, 2, 1], 2]) == 2
assert my_solution.maximumJumps(*[[0, 2, 1], 3]) == 2
assert my_solution.maximumJumps(*[[1, 0, 2], 0]) == -1
assert my_solution.maximumJumps(*[[1, 0, 2], 1]) == 1
assert my_solution.maximumJumps(*[[1, 0, 2], 2]) == 2
