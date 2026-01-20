
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.maximumSumOfHeights(*[[5, 3, 4, 1, 1]]) == 13
assert my_solution.maximumSumOfHeights(*[[6, 5, 3, 9, 2, 7]]) == 22
assert my_solution.maximumSumOfHeights(*[[3, 2, 5, 5, 2, 3]]) == 18
assert my_solution.maximumSumOfHeights(*[[1000000000]]) == 1000000000
assert my_solution.maximumSumOfHeights(*[[1]]) == 1
assert my_solution.maximumSumOfHeights(*[[933754743]]) == 933754743
assert my_solution.maximumSumOfHeights(*[[1, 1000000000]]) == 1000000001
assert my_solution.maximumSumOfHeights(*[[1000000000, 1000000000]]) == 2000000000
assert my_solution.maximumSumOfHeights(*[[999999999, 1000000000]]) == 1999999999
assert my_solution.maximumSumOfHeights(*[[1000000000, 999999999]]) == 1999999999
assert my_solution.maximumSumOfHeights(*[[30, 1]]) == 31
assert my_solution.maximumSumOfHeights(*[[1, 12, 19]]) == 32
assert my_solution.maximumSumOfHeights(*[[1000000000, 1000000000, 1000000000]]) == 3000000000
assert my_solution.maximumSumOfHeights(*[[999999999, 1000000000, 999999999]]) == 2999999998
assert my_solution.maximumSumOfHeights(*[[1000000000, 999999999, 999999998]]) == 2999999997
assert my_solution.maximumSumOfHeights(*[[999999998, 999999999, 1000000000]]) == 2999999997
assert my_solution.maximumSumOfHeights(*[[1, 1, 1]]) == 3
assert my_solution.maximumSumOfHeights(*[[1, 1, 4, 3, 3, 3, 6]]) == 20
assert my_solution.maximumSumOfHeights(*[[2, 4, 1, 3, 5]]) == 11
assert my_solution.maximumSumOfHeights(*[[1, 5, 2, 5, 6, 4, 6, 3, 4, 5]]) == 33
