
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.maxSpending(*[[[8, 5, 2], [6, 4, 1], [9, 7, 3]]]) == 285
assert my_solution.maxSpending(*[[[10, 8, 6, 4, 2], [9, 7, 5, 3, 2]]]) == 386
assert my_solution.maxSpending(*[[[1000000]]]) == 1000000
assert my_solution.maxSpending(*[[[1]]]) == 1
assert my_solution.maxSpending(*[[[1], [2]]]) == 5
assert my_solution.maxSpending(*[[[2], [1]]]) == 5
assert my_solution.maxSpending(*[[[1], [1]]]) == 3
assert my_solution.maxSpending(*[[[5, 2]]]) == 12
assert my_solution.maxSpending(*[[[5, 5]]]) == 15
assert my_solution.maxSpending(*[[[7, 5]]]) == 19
assert my_solution.maxSpending(*[[[3, 2, 1]]]) == 14
assert my_solution.maxSpending(*[[[2, 2, 1]]]) == 11
assert my_solution.maxSpending(*[[[3, 3, 2]]]) == 17
assert my_solution.maxSpending(*[[[3], [2], [1]]]) == 14
assert my_solution.maxSpending(*[[[2], [10], [1]]]) == 35
assert my_solution.maxSpending(*[[[1000000, 1000000, 1000000]]]) == 6000000
assert my_solution.maxSpending(*[[[1000000, 1000000, 1000000, 1000000]]]) == 10000000
assert my_solution.maxSpending(*[[[1000000], [1000000], [1000000], [1000000]]]) == 10000000
assert my_solution.maxSpending(*[[[1000000, 1000000], [1000000, 1000000]]]) == 10000000
assert my_solution.maxSpending(*[[[2, 1], [4, 3]]]) == 30
