
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.minimumTime(*[[1, 2, 3], [1, 2, 3], 4]) == 3
assert my_solution.minimumTime(*[[1, 2, 3], [3, 3, 3], 4]) == -1
assert my_solution.minimumTime(*[[4, 4, 9, 10], [4, 4, 1, 3], 16]) == 4
assert my_solution.minimumTime(*[[5, 3], [3, 2], 4]) == 2
assert my_solution.minimumTime(*[[4, 5, 3, 2, 3, 9, 5, 7, 10, 4], [4, 4, 0, 4, 1, 2, 4, 0, 4, 0], 47]) == -1
assert my_solution.minimumTime(*[[7, 9, 8, 5, 8, 3], [0, 1, 4, 2, 3, 1], 37]) == 2
assert my_solution.minimumTime(*[[8, 2, 3], [1, 4, 2], 13]) == 0
assert my_solution.minimumTime(*[[4, 7, 2, 3, 4, 3, 10, 8], [3, 4, 0, 1, 1, 0, 2, 2], 36]) == 4
assert my_solution.minimumTime(*[[2, 10, 10, 4, 6, 3], [1, 0, 0, 1, 3, 1], 35]) == 0
assert my_solution.minimumTime(*[[9, 5, 3], [4, 1, 3], 17]) == 0
assert my_solution.minimumTime(*[[1, 7, 9, 4, 8, 8, 1], [2, 2, 3, 2, 0, 1, 0], 20]) == 6
assert my_solution.minimumTime(*[[9, 2, 8, 3, 1, 9, 7, 6], [0, 3, 4, 1, 3, 4, 2, 1], 40]) == 8
assert my_solution.minimumTime(*[[10], [3], 10]) == 0
assert my_solution.minimumTime(*[[7, 6, 8, 2, 8, 9, 3, 3], [2, 2, 4, 0, 0, 2, 2, 3], 45]) == 5
assert my_solution.minimumTime(*[[4, 9, 5, 2, 3], [4, 2, 0, 4, 0], 18]) == 3
assert my_solution.minimumTime(*[[2, 10, 2, 7, 8, 9, 7, 6, 6], [4, 2, 1, 4, 3, 2, 4, 4, 4], 55]) == -1
assert my_solution.minimumTime(*[[6, 8, 10, 7, 10, 9], [4, 2, 0, 4, 4, 2], 38]) == 5
assert my_solution.minimumTime(*[[9, 2, 8, 5, 8, 3, 5, 2, 2], [4, 3, 4, 2, 0, 1, 4, 4, 2], 41]) == -1
assert my_solution.minimumTime(*[[5, 3, 2, 3, 10, 4, 7, 9, 1, 10], [2, 0, 2, 0, 3, 3, 4, 4, 0, 1], 30]) == -1
assert my_solution.minimumTime(*[[2, 3, 5], [0, 0, 1], 8]) == 1
