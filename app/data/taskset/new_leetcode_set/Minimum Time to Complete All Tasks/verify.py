
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.findMinimumTime(*[[[2, 3, 1], [4, 5, 1], [1, 5, 2]]]) == 2
assert my_solution.findMinimumTime(*[[[1, 3, 2], [2, 5, 3], [5, 6, 2]]]) == 4
assert my_solution.findMinimumTime(*[[[1, 1, 1]]]) == 1
assert my_solution.findMinimumTime(*[[[2000, 2000, 1]]]) == 1
assert my_solution.findMinimumTime(*[[[1, 2000, 1]]]) == 1
assert my_solution.findMinimumTime(*[[[1, 2000, 2000]]]) == 2000
assert my_solution.findMinimumTime(*[[[3, 16, 2]]]) == 2
assert my_solution.findMinimumTime(*[[[1, 18, 5], [3, 15, 1]]]) == 5
assert my_solution.findMinimumTime(*[[[2, 13, 2], [6, 18, 5], [2, 13, 3]]]) == 5
assert my_solution.findMinimumTime(*[[[14, 20, 5], [2, 18, 7], [6, 14, 1], [3, 16, 3]]]) == 7
assert my_solution.findMinimumTime(*[[[8, 19, 6]]]) == 6
assert my_solution.findMinimumTime(*[[[7, 18, 1], [4, 19, 5]]]) == 5
assert my_solution.findMinimumTime(*[[[6, 15, 4], [3, 7, 1], [4, 20, 4]]]) == 4
assert my_solution.findMinimumTime(*[[[8, 19, 1], [3, 20, 1], [1, 20, 2], [6, 13, 3]]]) == 3
assert my_solution.findMinimumTime(*[[[4, 20, 10]]]) == 10
assert my_solution.findMinimumTime(*[[[1, 14, 7], [6, 17, 2]]]) == 7
assert my_solution.findMinimumTime(*[[[10, 18, 2], [1, 8, 1], [10, 20, 8]]]) == 9
assert my_solution.findMinimumTime(*[[[3, 15, 9], [1, 18, 9], [4, 16, 4], [2, 20, 10]]]) == 10
assert my_solution.findMinimumTime(*[[[13, 18, 5]]]) == 5
assert my_solution.findMinimumTime(*[[[3, 17, 2], [3, 20, 1]]]) == 2
