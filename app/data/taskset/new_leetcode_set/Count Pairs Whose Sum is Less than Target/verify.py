
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.countPairs(*[[-1, 1, 2, 3, 1], 2]) == 3
assert my_solution.countPairs(*[[-6, 2, 5, -2, -7, -1, 3], -2]) == 10
assert my_solution.countPairs(*[[9, -5, -5, 5, -5, -4, -6, 6, -6], 3]) == 27
assert my_solution.countPairs(*[[-8, -5, 5, -4, 10], 2]) == 6
assert my_solution.countPairs(*[[-5, 0, -7, -1, 9, 8, -9, 9], -14]) == 1
assert my_solution.countPairs(*[[6, -1, 7, 4, 2, 3], 8]) == 8
assert my_solution.countPairs(*[[2, 8, 2, 8, 7], 10]) == 3
assert my_solution.countPairs(*[[-6, 1, 1, -1, -10, -7, 1, -5, -4, 0], -15]) == 2
assert my_solution.countPairs(*[[10, -2, -1, 7, 8, 5, 3, -4, -9], -10]) == 2
assert my_solution.countPairs(*[[3, 8, -3, 4, 10, -6], 1]) == 4
assert my_solution.countPairs(*[[-4, -6, -7, 8], -13]) == 0
assert my_solution.countPairs(*[[-4, 0, 10, 8, -2], 0]) == 3
assert my_solution.countPairs(*[[-8, -5, -3, 1, -7], -6]) == 7
assert my_solution.countPairs(*[[4, -8, -2, 5, 2, -9, 6, 5, -4], -4]) == 9
assert my_solution.countPairs(*[[-1, -5, 4, 4, -10], -6]) == 2
assert my_solution.countPairs(*[[-5, 4, -6, -5, -10, -1, 10, 3], 6]) == 24
assert my_solution.countPairs(*[[-9, 6, -4, 10, 1, 8], 11]) == 11
assert my_solution.countPairs(*[[-10, -6, -8, -9, 6, 6, -6, -6, -3], -2]) == 25
assert my_solution.countPairs(*[[-7, 7, 6, -9, -4, 10, 8, -8, 2, 2], -1]) == 17
assert my_solution.countPairs(*[[0, -1, 0, -6, -9], -9]) == 2
