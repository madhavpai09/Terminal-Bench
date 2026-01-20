
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.countFairPairs(*[[0, 1, 7, 4, 4, 5], 3, 6]) == 6
assert my_solution.countFairPairs(*[[1, 7, 9, 2, 5], 11, 11]) == 1
assert my_solution.countFairPairs(*[[-1, 0], 1, 1]) == 0
assert my_solution.countFairPairs(*[[-1, -1, 0, 0], 1, 1]) == 0
assert my_solution.countFairPairs(*[[0, 0, 0, 0, 0, 0], 0, 0]) == 15
assert my_solution.countFairPairs(*[[0, 0, 0, 0, 0, 0], -1000000000, 1000000000]) == 15
assert my_solution.countFairPairs(*[[6, 5, 10, 2, 4, 9, 0, 7], 20, 20]) == 0
assert my_solution.countFairPairs(*[[6, 9, 4, 2, 7, 5, 10, 3], 13, 13]) == 3
assert my_solution.countFairPairs(*[[5, 7, 5, 7, 5], 12, 12]) == 6
assert my_solution.countFairPairs(*[[-5, -7, -5, -7, -5], -12, -12]) == 6
assert my_solution.countFairPairs(*[[7, 9, 8, 6, -1000000000, -1000000000, -1000000000, -1000000000], -14, 11]) == 0
assert my_solution.countFairPairs(*[[-2, -6, 4, 0, -1000000000, -1000000000, -1000000000, -1000000000], -15, 15]) == 6
assert my_solution.countFairPairs(*[[7, -2, 2, 8, -1000000000, -1000000000, -1000000000, -1000000000], -15, 11]) == 5
assert my_solution.countFairPairs(*[[-3, 0, 6, -9, 10, 9, -7, -1000000000, -1000000000, -1000000000, -1000000000, -1000000000, -1000000000, -1000000000], -15, 14]) == 17
assert my_solution.countFairPairs(*[[10, -9, -5, 8, -2, -1000000000, -1000000000, -1000000000, -1000000000, -1000000000], -12, 11]) == 8
assert my_solution.countFairPairs(*[[9, -2, 4, -1000000000, -1000000000, -1000000000], -14, 11]) == 2
assert my_solution.countFairPairs(*[[3, -8, -5, -4, -1000000000, -1000000000, -1000000000, -1000000000], -10, 15]) == 4
assert my_solution.countFairPairs(*[[-9, -6, -3, -7, 0, 1, -1000000000, -1000000000, -1000000000, -1000000000, -1000000000, -1000000000], -11, 15]) == 11
assert my_solution.countFairPairs(*[[-3, -10, -9, -5, 4, -1000000000, -1000000000, -1000000000, -1000000000, -1000000000], -10, 11]) == 5
assert my_solution.countFairPairs(*[[10, -3, 3, 8, 2, -1000000000, -1000000000, -1000000000, -1000000000, -1000000000], -14, 14]) == 9
