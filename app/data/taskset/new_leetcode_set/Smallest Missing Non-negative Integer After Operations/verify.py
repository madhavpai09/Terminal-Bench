
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.findSmallestInteger(*[[1, -10, 7, 13, 6, 8], 5]) == 4
assert my_solution.findSmallestInteger(*[[1, -10, 7, 13, 6, 8], 7]) == 2
assert my_solution.findSmallestInteger(*[[1, 3, 5, 7], 2]) == 0
assert my_solution.findSmallestInteger(*[[3, 0, 3, 2, 4, 2, 1, 1, 0, 4], 5]) == 10
assert my_solution.findSmallestInteger(*[[3, 2, 3, 1, 0, 1, 4, 2, 3, 1, 4, 1, 3], 5]) == 5
assert my_solution.findSmallestInteger(*[[0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1], 2]) == 15
assert my_solution.findSmallestInteger(*[[0, 3, 1, 1, 2, 2, 0, 0, 2, 2, 3, 2], 4]) == 9
assert my_solution.findSmallestInteger(*[[2, 2, 2, 3, 3, 2, 0, 2, 3, 0, 3, 2, 3, 1, 2, 0], 4]) == 5
assert my_solution.findSmallestInteger(*[[0, 0, 1, 0, 0, 0, 1, 0], 2]) == 5
assert my_solution.findSmallestInteger(*[[1, 0, 4, 2, 4, 3, 3, 1, 4], 5]) == 5
assert my_solution.findSmallestInteger(*[[2, 1, 0, 0, 1, 1, 1, 0, 2, 1, 0, 1, 1], 3]) == 8
assert my_solution.findSmallestInteger(*[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 1]) == 19
assert my_solution.findSmallestInteger(*[[0, 3, 2, 2, 0, 3, 3, 0, 2, 1, 1, 2, 1, 0, 1, 0, 3], 4]) == 17
assert my_solution.findSmallestInteger(*[[2, 2, 1, 2, 0, 1, 2, 0, 0, 0, 1, 2, 2, 1, 0, 1, 2], 3]) == 15
assert my_solution.findSmallestInteger(*[[0, 3, 3, 2, 0, 1, 0, 3, 2, 3, 0, 4, 3, 1, 4, 4, 4, 2, 1, 1, 0, 4, 2, 4, 1, 2, 4, 0, 4, 1, 2, 1, 2, 3, 3, 4], 5]) == 30
assert my_solution.findSmallestInteger(*[[0, 2, 2, 3, 1, 2, 1, 0, 1, 3, 2, 2, 3, 2, 1, 1, 2, 1, 0, 1, 3, 1], 4]) == 12
assert my_solution.findSmallestInteger(*[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 1]) == 34
assert my_solution.findSmallestInteger(*[[4, 1, 0, 1, 1, 1, 1, 3, 2, 3, 1, 2, 4], 5]) == 5
assert my_solution.findSmallestInteger(*[[1, 1, 2, 1, 2, 1, 0, 2, 2, 2, 1, 1, 1, 2, 1, 1, 2, 2, 0, 1, 0, 1, 1, 2, 1, 2, 2, 1, 2], 3]) == 9
assert my_solution.findSmallestInteger(*[[0, -3], 4]) == 2
