
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.kItemsWithMaximumSum(*[3, 2, 0, 2]) == 2
assert my_solution.kItemsWithMaximumSum(*[3, 2, 0, 4]) == 3
assert my_solution.kItemsWithMaximumSum(*[4, 0, 1, 2]) == 2
assert my_solution.kItemsWithMaximumSum(*[1, 4, 1, 3]) == 1
assert my_solution.kItemsWithMaximumSum(*[6, 6, 6, 13]) == 5
assert my_solution.kItemsWithMaximumSum(*[2, 1, 2, 1]) == 1
assert my_solution.kItemsWithMaximumSum(*[8, 4, 0, 8]) == 8
assert my_solution.kItemsWithMaximumSum(*[0, 3, 1, 1]) == 0
assert my_solution.kItemsWithMaximumSum(*[2, 4, 4, 0]) == 0
assert my_solution.kItemsWithMaximumSum(*[3, 7, 4, 8]) == 3
assert my_solution.kItemsWithMaximumSum(*[3, 3, 5, 11]) == -2
assert my_solution.kItemsWithMaximumSum(*[1, 2, 0, 2]) == 1
assert my_solution.kItemsWithMaximumSum(*[1, 6, 4, 4]) == 1
assert my_solution.kItemsWithMaximumSum(*[1, 1, 2, 2]) == 1
assert my_solution.kItemsWithMaximumSum(*[3, 0, 5, 8]) == -2
assert my_solution.kItemsWithMaximumSum(*[1, 0, 3, 4]) == -2
assert my_solution.kItemsWithMaximumSum(*[2, 0, 4, 2]) == 2
assert my_solution.kItemsWithMaximumSum(*[1, 3, 3, 5]) == 0
assert my_solution.kItemsWithMaximumSum(*[4, 3, 2, 1]) == 1
assert my_solution.kItemsWithMaximumSum(*[4, 4, 0, 5]) == 4
