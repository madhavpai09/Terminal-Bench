
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.rowAndMaximumOnes(*[[[0, 1], [1, 0]]]) == [0, 1]
assert my_solution.rowAndMaximumOnes(*[[[0, 0, 0], [0, 1, 1]]]) == [1, 2]
assert my_solution.rowAndMaximumOnes(*[[[0, 0], [1, 1], [0, 0]]]) == [1, 2]
assert my_solution.rowAndMaximumOnes(*[[[1]]]) == [0, 1]
assert my_solution.rowAndMaximumOnes(*[[[0], [0]]]) == [0, 0]
assert my_solution.rowAndMaximumOnes(*[[[0, 1]]]) == [0, 1]
assert my_solution.rowAndMaximumOnes(*[[[0], [1], [1]]]) == [1, 1]
assert my_solution.rowAndMaximumOnes(*[[[1, 0, 0]]]) == [0, 1]
assert my_solution.rowAndMaximumOnes(*[[[0], [1], [0], [0]]]) == [1, 1]
assert my_solution.rowAndMaximumOnes(*[[[0], [1], [1], [0]]]) == [1, 1]
assert my_solution.rowAndMaximumOnes(*[[[0, 0], [0, 1]]]) == [1, 1]
assert my_solution.rowAndMaximumOnes(*[[[0, 0], [1, 1]]]) == [1, 2]
assert my_solution.rowAndMaximumOnes(*[[[0, 0, 0, 0]]]) == [0, 0]
assert my_solution.rowAndMaximumOnes(*[[[0, 1], [1, 1]]]) == [1, 2]
assert my_solution.rowAndMaximumOnes(*[[[1, 0, 1, 1]]]) == [0, 3]
assert my_solution.rowAndMaximumOnes(*[[[1, 1], [0, 1]]]) == [0, 2]
assert my_solution.rowAndMaximumOnes(*[[[1, 1, 0, 0]]]) == [0, 2]
assert my_solution.rowAndMaximumOnes(*[[[0], [1], [0], [0], [0]]]) == [1, 1]
assert my_solution.rowAndMaximumOnes(*[[[0], [1], [1], [1], [0]]]) == [1, 1]
assert my_solution.rowAndMaximumOnes(*[[[1], [0], [0], [0], [0]]]) == [0, 1]
