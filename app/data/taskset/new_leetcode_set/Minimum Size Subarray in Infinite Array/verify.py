
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.minSizeSubarray(*[[1, 2, 3], 5]) == 2
assert my_solution.minSizeSubarray(*[[1, 1, 1, 2, 3], 4]) == 2
assert my_solution.minSizeSubarray(*[[2, 4, 6, 8], 3]) == -1
assert my_solution.minSizeSubarray(*[[2, 1, 5, 7, 7, 1, 6, 3], 39]) == 9
assert my_solution.minSizeSubarray(*[[17, 4, 3, 14, 17, 6, 15], 85]) == -1
assert my_solution.minSizeSubarray(*[[18, 3, 11, 19, 7, 16, 6, 7, 3, 6, 18, 9, 9, 1, 14, 17, 15, 14, 12, 10], 7]) == 1
assert my_solution.minSizeSubarray(*[[2, 3, 5, 2, 3, 4, 4, 1, 3, 5, 2, 2, 5, 1, 1, 2, 5], 19]) == 6
assert my_solution.minSizeSubarray(*[[4, 1, 5, 7, 1, 6, 1, 7, 2, 2, 5, 5, 5, 6, 3], 20]) == 5
assert my_solution.minSizeSubarray(*[[7, 3, 5], 36]) == -1
assert my_solution.minSizeSubarray(*[[1, 11, 6, 4, 13], 22]) == 4
assert my_solution.minSizeSubarray(*[[1, 2, 2, 2, 1, 2, 1, 2, 1, 2, 1], 83]) == 53
assert my_solution.minSizeSubarray(*[[4, 3, 5, 4, 5, 4, 4, 4, 5, 7, 4, 5, 6, 3, 1, 4, 6, 3, 7], 15]) == 3
assert my_solution.minSizeSubarray(*[[1, 2, 3, 2, 1, 5, 3, 4, 5], 53]) == 19
assert my_solution.minSizeSubarray(*[[2, 5, 6, 4], 95]) == 22
assert my_solution.minSizeSubarray(*[[6, 6, 4, 5, 2, 8, 1, 8, 7, 6, 6, 7, 4, 1, 9, 6, 8, 8], 55]) == 9
assert my_solution.minSizeSubarray(*[[1, 2, 8, 19, 17, 2, 3, 11, 8, 12, 16, 18, 7], 36]) == 2
assert my_solution.minSizeSubarray(*[[12, 14, 4, 14, 13, 16, 5], 36]) == -1
assert my_solution.minSizeSubarray(*[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 37]) == 37
assert my_solution.minSizeSubarray(*[[5, 7, 2, 6, 4, 1, 6, 7, 1, 4, 7, 6, 7, 7, 6, 6, 4, 6, 8], 90]) == 17
assert my_solution.minSizeSubarray(*[[3, 5, 15, 17, 6, 17, 10, 15, 10, 4, 6], 25]) == 2
