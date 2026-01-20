
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.findKOr(*[[7, 12, 9, 8, 9, 15], 4]) == 9
assert my_solution.findKOr(*[[2, 12, 1, 11, 4, 5], 6]) == 0
assert my_solution.findKOr(*[[10, 8, 5, 9, 11, 6, 8], 1]) == 15
assert my_solution.findKOr(*[[14, 7, 12, 9, 8, 9, 1, 15], 4]) == 13
assert my_solution.findKOr(*[[2, 12, 1, 11, 4, 5], 3]) == 5
assert my_solution.findKOr(*[[10, 8, 5, 10, 11, 11, 6, 8], 1]) == 15
assert my_solution.findKOr(*[[0], 1]) == 0
assert my_solution.findKOr(*[[1], 1]) == 1
assert my_solution.findKOr(*[[2], 1]) == 2
assert my_solution.findKOr(*[[3], 1]) == 3
assert my_solution.findKOr(*[[4], 1]) == 4
assert my_solution.findKOr(*[[5], 1]) == 5
assert my_solution.findKOr(*[[6], 1]) == 6
assert my_solution.findKOr(*[[7], 1]) == 7
assert my_solution.findKOr(*[[8], 1]) == 8
assert my_solution.findKOr(*[[9], 1]) == 9
assert my_solution.findKOr(*[[10], 1]) == 10
assert my_solution.findKOr(*[[11], 1]) == 11
assert my_solution.findKOr(*[[12], 1]) == 12
assert my_solution.findKOr(*[[13], 1]) == 13
