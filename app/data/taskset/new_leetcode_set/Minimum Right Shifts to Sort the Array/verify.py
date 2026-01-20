
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.minimumRightShifts(*[[3, 4, 5, 1, 2]]) == 2
assert my_solution.minimumRightShifts(*[[1, 3, 5]]) == 0
assert my_solution.minimumRightShifts(*[[2, 1, 4]]) == -1
assert my_solution.minimumRightShifts(*[[31, 72, 79, 25]]) == 1
assert my_solution.minimumRightShifts(*[[27, 33, 42, 58, 81, 8, 9, 17]]) == 3
assert my_solution.minimumRightShifts(*[[72, 13, 21, 35, 52]]) == 4
assert my_solution.minimumRightShifts(*[[65, 73, 77, 1]]) == 1
assert my_solution.minimumRightShifts(*[[100, 8, 14, 68, 80, 84]]) == 5
assert my_solution.minimumRightShifts(*[[53, 60, 64, 69, 98, 40]]) == 1
assert my_solution.minimumRightShifts(*[[21]]) == 0
assert my_solution.minimumRightShifts(*[[78, 12, 18, 21, 23, 36, 64, 70]]) == 7
assert my_solution.minimumRightShifts(*[[25, 26, 53, 91, 92, 99, 10, 24]]) == 2
assert my_solution.minimumRightShifts(*[[63, 51, 65, 87, 6, 17, 32, 14, 42, 46]]) == -1
assert my_solution.minimumRightShifts(*[[43, 46, 75, 76, 85, 96, 9, 19, 25]]) == 3
assert my_solution.minimumRightShifts(*[[5]]) == 0
assert my_solution.minimumRightShifts(*[[35, 72, 76, 82, 96, 97, 24, 26]]) == 2
assert my_solution.minimumRightShifts(*[[82, 30, 94, 55, 76, 51, 3, 89, 52, 96]]) == -1
assert my_solution.minimumRightShifts(*[[57, 59, 88, 97, 6, 27, 41, 46, 52]]) == 5
assert my_solution.minimumRightShifts(*[[17]]) == 0
assert my_solution.minimumRightShifts(*[[62]]) == 0
