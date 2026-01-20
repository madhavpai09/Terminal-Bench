
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.numberOfGoodSubarraySplits(*[[0, 1, 0, 0, 1]]) == 3
assert my_solution.numberOfGoodSubarraySplits(*[[0, 1, 0]]) == 1
assert my_solution.numberOfGoodSubarraySplits(*[[0, 1, 0, 0]]) == 1
assert my_solution.numberOfGoodSubarraySplits(*[[0, 0, 1, 1]]) == 1
assert my_solution.numberOfGoodSubarraySplits(*[[1, 0, 0, 0, 0, 0, 1, 0, 1]]) == 12
assert my_solution.numberOfGoodSubarraySplits(*[[0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1]]) == 8
assert my_solution.numberOfGoodSubarraySplits(*[[0, 1, 1, 1, 0, 1, 1, 0, 0, 0]]) == 2
assert my_solution.numberOfGoodSubarraySplits(*[[0, 1, 0, 0, 1, 0, 1, 0, 1, 1]]) == 12
assert my_solution.numberOfGoodSubarraySplits(*[[1, 0, 1, 1, 0, 1, 0, 0, 1]]) == 12
assert my_solution.numberOfGoodSubarraySplits(*[[0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1]]) == 6
assert my_solution.numberOfGoodSubarraySplits(*[[0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1]]) == 18
assert my_solution.numberOfGoodSubarraySplits(*[[0, 0, 1]]) == 1
assert my_solution.numberOfGoodSubarraySplits(*[[1, 1, 0, 1, 1, 1, 1, 1]]) == 2
assert my_solution.numberOfGoodSubarraySplits(*[[0, 1]]) == 1
assert my_solution.numberOfGoodSubarraySplits(*[[1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0]]) == 18
assert my_solution.numberOfGoodSubarraySplits(*[[1, 0, 1, 0, 0]]) == 2
assert my_solution.numberOfGoodSubarraySplits(*[[1, 1, 0]]) == 1
assert my_solution.numberOfGoodSubarraySplits(*[[1, 0, 0, 1, 0, 0, 1, 1]]) == 9
assert my_solution.numberOfGoodSubarraySplits(*[[1, 0, 1, 1, 0, 0]]) == 2
assert my_solution.numberOfGoodSubarraySplits(*[[1]]) == 1
