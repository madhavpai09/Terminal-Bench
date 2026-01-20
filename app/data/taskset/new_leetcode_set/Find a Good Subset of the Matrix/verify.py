
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.goodSubsetofBinaryMatrix(*[[[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 1, 1]]]) == [0, 1]
assert my_solution.goodSubsetofBinaryMatrix(*[[[0]]]) == [0]
assert my_solution.goodSubsetofBinaryMatrix(*[[[1, 1, 1], [1, 1, 1]]]) == []
assert my_solution.goodSubsetofBinaryMatrix(*[[[0, 0], [1, 1], [1, 0], [1, 0]]]) == [0]
assert my_solution.goodSubsetofBinaryMatrix(*[[[1, 0, 0, 1, 0], [1, 0, 1, 0, 1], [0, 0, 0, 0, 1], [1, 0, 1, 1, 1]]]) == [0, 2]
assert my_solution.goodSubsetofBinaryMatrix(*[[[1, 1, 0, 0, 1], [0, 1, 1, 1, 0], [1, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [1, 0, 1, 1, 0], [1, 0, 0, 0, 1], [1, 1, 0, 1, 0], [1, 0, 1, 0, 1], [1, 1, 1, 1, 1]]]) == [0, 3]
assert my_solution.goodSubsetofBinaryMatrix(*[[[1, 1], [0, 1], [1, 0], [0, 0], [1, 0], [0, 1], [1, 1], [0, 1], [1, 1]]]) == [3]
assert my_solution.goodSubsetofBinaryMatrix(*[[[0, 1], [0, 1], [0, 1], [1, 1], [1, 1], [0, 0], [1, 1], [1, 1]]]) == [5]
assert my_solution.goodSubsetofBinaryMatrix(*[[[0, 0, 0], [0, 0, 1]]]) == [0]
assert my_solution.goodSubsetofBinaryMatrix(*[[[0, 1, 1, 0], [1, 1, 1, 0], [1, 1, 1, 0]]]) == []
assert my_solution.goodSubsetofBinaryMatrix(*[[[1], [0], [1], [0], [0], [0]]]) == [1]
assert my_solution.goodSubsetofBinaryMatrix(*[[[0, 0], [1, 0], [0, 0], [1, 0], [0, 1], [1, 1], [0, 0], [0, 1], [1, 1], [0, 1]]]) == [0]
assert my_solution.goodSubsetofBinaryMatrix(*[[[0, 0], [1, 1], [0, 0], [1, 1], [1, 1]]]) == [0]
assert my_solution.goodSubsetofBinaryMatrix(*[[[1, 1], [0, 1]]]) == []
assert my_solution.goodSubsetofBinaryMatrix(*[[[1, 0, 0], [1, 0, 1], [1, 1, 0], [0, 0, 1], [0, 0, 0], [0, 1, 1], [0, 1, 1], [1, 0, 0], [0, 1, 1]]]) == [4]
assert my_solution.goodSubsetofBinaryMatrix(*[[[1, 1, 1, 0, 0], [0, 1, 0, 1, 0], [1, 0, 0, 1, 0], [0, 1, 1, 1, 0], [1, 0, 1, 0, 0], [1, 0, 0, 1, 0], [0, 1, 1, 1, 1]]]) == [1, 4]
assert my_solution.goodSubsetofBinaryMatrix(*[[[0, 0, 0, 1, 0], [1, 1, 1, 0, 0], [1, 1, 1, 0, 0], [0, 0, 1, 0, 1]]]) == [0, 1]
assert my_solution.goodSubsetofBinaryMatrix(*[[[0], [1], [1], [1], [1], [1], [0], [1], [1], [0]]]) == [0]
assert my_solution.goodSubsetofBinaryMatrix(*[[[1, 1], [1, 0], [1, 1], [0, 1], [1, 1], [1, 0], [1, 0], [1, 0], [0, 1], [1, 1]]]) == [1, 3]
assert my_solution.goodSubsetofBinaryMatrix(*[[[0, 1, 0, 1, 0], [0, 1, 1, 1, 0], [1, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 0, 1, 1], [1, 1, 1, 0, 0]]]) == [4, 5]
