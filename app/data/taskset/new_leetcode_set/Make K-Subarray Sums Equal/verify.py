
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.makeSubKSumEqual(*[[1, 4, 1, 3], 2]) == 1
assert my_solution.makeSubKSumEqual(*[[2, 5, 5, 7], 3]) == 5
assert my_solution.makeSubKSumEqual(*[[9], 1]) == 0
assert my_solution.makeSubKSumEqual(*[[1, 10], 1]) == 9
assert my_solution.makeSubKSumEqual(*[[4, 6], 2]) == 0
assert my_solution.makeSubKSumEqual(*[[2, 10, 9], 1]) == 8
assert my_solution.makeSubKSumEqual(*[[10, 3, 8], 2]) == 7
assert my_solution.makeSubKSumEqual(*[[3, 3, 9], 3]) == 0
assert my_solution.makeSubKSumEqual(*[[1, 7, 9, 6], 1]) == 9
assert my_solution.makeSubKSumEqual(*[[7, 3, 10, 6], 2]) == 6
assert my_solution.makeSubKSumEqual(*[[1, 5, 8, 10], 3]) == 12
assert my_solution.makeSubKSumEqual(*[[2, 6, 7, 2], 4]) == 0
assert my_solution.makeSubKSumEqual(*[[2, 4, 2, 10, 3], 1]) == 10
assert my_solution.makeSubKSumEqual(*[[9, 1, 5, 10, 6], 2]) == 13
assert my_solution.makeSubKSumEqual(*[[10, 9, 1, 10, 5], 3]) == 14
assert my_solution.makeSubKSumEqual(*[[9, 7, 2, 6, 4], 4]) == 10
assert my_solution.makeSubKSumEqual(*[[10, 5, 10, 2, 9], 5]) == 0
assert my_solution.makeSubKSumEqual(*[[5, 8, 2, 6, 9, 1], 1]) == 15
assert my_solution.makeSubKSumEqual(*[[8, 2, 5, 9, 8, 10], 2]) == 11
assert my_solution.makeSubKSumEqual(*[[9, 4, 8, 8, 5, 8], 3]) == 2
