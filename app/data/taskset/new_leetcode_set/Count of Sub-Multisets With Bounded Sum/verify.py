
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.countSubMultisets(*[[1, 2, 2, 3], 6, 6]) == 1
assert my_solution.countSubMultisets(*[[2, 1, 4, 2, 7], 1, 5]) == 7
assert my_solution.countSubMultisets(*[[1, 2, 1, 3, 5, 2], 3, 5]) == 9
assert my_solution.countSubMultisets(*[[0, 0, 1, 2, 3], 2, 3]) == 9
assert my_solution.countSubMultisets(*[[0, 0, 0, 0, 0], 0, 0]) == 6
assert my_solution.countSubMultisets(*[[0, 0, 0, 1, 2, 5, 2, 3], 0, 3]) == 20
assert my_solution.countSubMultisets(*[[1, 1], 2, 2]) == 1
assert my_solution.countSubMultisets(*[[1, 1, 1], 2, 2]) == 1
assert my_solution.countSubMultisets(*[[1, 1, 2], 2, 4]) == 4
assert my_solution.countSubMultisets(*[[1, 2, 1], 2, 2]) == 2
assert my_solution.countSubMultisets(*[[1, 2, 2], 3, 5]) == 3
assert my_solution.countSubMultisets(*[[2, 1, 1], 1, 2]) == 3
assert my_solution.countSubMultisets(*[[2, 1, 2], 2, 2]) == 1
assert my_solution.countSubMultisets(*[[2, 2, 1], 4, 5]) == 2
assert my_solution.countSubMultisets(*[[2, 2, 2], 3, 6]) == 2
assert my_solution.countSubMultisets(*[[1, 1, 1, 1], 3, 3]) == 1
assert my_solution.countSubMultisets(*[[1, 1, 1, 2], 1, 1]) == 1
assert my_solution.countSubMultisets(*[[1, 1, 1, 3], 4, 4]) == 1
assert my_solution.countSubMultisets(*[[1, 1, 2, 1], 3, 4]) == 3
assert my_solution.countSubMultisets(*[[1, 1, 2, 2], 2, 3]) == 3
