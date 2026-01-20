
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.paintWalls(*[[1, 2, 3, 2], [1, 2, 3, 2]]) == 3
assert my_solution.paintWalls(*[[2, 3, 4, 2], [1, 1, 1, 1]]) == 4
assert my_solution.paintWalls(*[[8, 7, 5, 15], [1, 1, 2, 1]]) == 12
assert my_solution.paintWalls(*[[42, 8, 28, 35, 21, 13, 21, 35], [2, 1, 1, 1, 2, 1, 1, 2]]) == 63
assert my_solution.paintWalls(*[[49, 35, 32, 20, 30, 12, 42], [1, 1, 2, 2, 1, 1, 2]]) == 62
assert my_solution.paintWalls(*[[2, 2], [1, 1]]) == 2
assert my_solution.paintWalls(*[[26, 53, 10, 24, 25, 20, 63, 51], [1, 1, 1, 1, 2, 2, 2, 1]]) == 55
assert my_solution.paintWalls(*[[76, 25, 96, 46, 85, 19, 29, 88, 2, 5], [1, 2, 1, 3, 1, 3, 3, 3, 2, 1]]) == 46
assert my_solution.paintWalls(*[[82, 30, 94, 55, 76, 94, 51, 82, 3, 89], [2, 3, 3, 1, 2, 2, 1, 2, 3, 2]]) == 84
assert my_solution.paintWalls(*[[23, 2, 9, 1, 48, 3, 31], [1, 2, 1, 1, 2, 2, 1]]) == 6
assert my_solution.paintWalls(*[[21, 52, 42, 21, 2, 55, 63, 50], [2, 2, 1, 2, 1, 1, 2, 2]]) == 44
assert my_solution.paintWalls(*[[7, 15, 38, 35, 61, 90, 34, 29, 68, 35], [1, 1, 3, 3, 2, 1, 3, 1, 2, 3]]) == 76
assert my_solution.paintWalls(*[[1, 4], [1, 1]]) == 1
assert my_solution.paintWalls(*[[23, 33, 19, 12, 27, 20], [2, 2, 2, 2, 2, 1]]) == 31
assert my_solution.paintWalls(*[[74, 34, 54, 65, 65, 9, 62, 85, 95, 36], [2, 1, 2, 1, 1, 3, 2, 3, 2, 1]]) == 125
assert my_solution.paintWalls(*[[9, 9, 5], [1, 1, 1]]) == 14
assert my_solution.paintWalls(*[[4, 7, 9], [1, 1, 1]]) == 11
assert my_solution.paintWalls(*[[1, 27, 29, 35, 36, 7], [1, 1, 1, 1, 1, 2]]) == 35
assert my_solution.paintWalls(*[[1], [1]]) == 1
assert my_solution.paintWalls(*[[41, 15, 27, 36, 28, 47, 36], [2, 1, 2, 2, 2, 1, 2]]) == 70
