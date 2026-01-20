
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.countWays(*[[1, 1]]) == 2
assert my_solution.countWays(*[[6, 0, 3, 3, 6, 7, 2, 7]]) == 3
assert my_solution.countWays(*[[1, 1, 0, 1]]) == 1
assert my_solution.countWays(*[[5, 0, 3, 4, 2, 1, 2, 4]]) == 1
assert my_solution.countWays(*[[0, 4, 4, 4, 4, 4, 2]]) == 2
assert my_solution.countWays(*[[0, 1, 5, 6, 8, 7, 4, 7, 2]]) == 2
assert my_solution.countWays(*[[0]]) == 1
assert my_solution.countWays(*[[2, 2, 7, 1, 2, 2, 4, 7]]) == 3
assert my_solution.countWays(*[[0, 2, 2, 2, 3, 3, 3, 3]]) == 2
assert my_solution.countWays(*[[7, 7, 7, 7, 7, 7, 7, 7, 2]]) == 2
assert my_solution.countWays(*[[4, 2, 3, 6, 6, 0, 6, 8, 3]]) == 3
assert my_solution.countWays(*[[0, 0, 1, 7, 2, 0, 6, 5]]) == 1
assert my_solution.countWays(*[[6, 6, 6, 6, 6, 6, 6, 7, 1, 7]]) == 2
assert my_solution.countWays(*[[2, 2, 4, 5, 0, 1, 4, 4, 7]]) == 1
assert my_solution.countWays(*[[4, 4, 4, 4, 4]]) == 2
assert my_solution.countWays(*[[0, 4, 0, 3, 4]]) == 2
assert my_solution.countWays(*[[6, 5, 5, 8, 4, 2, 6, 4, 8]]) == 3
assert my_solution.countWays(*[[0, 9, 4, 6, 8, 8, 1, 7, 4, 7]]) == 2
assert my_solution.countWays(*[[1, 0, 0]]) == 1
assert my_solution.countWays(*[[1, 1, 2, 2, 2, 3, 3, 3, 3]]) == 2
