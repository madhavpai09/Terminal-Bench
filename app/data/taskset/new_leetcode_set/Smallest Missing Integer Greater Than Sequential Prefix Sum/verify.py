
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.missingInteger(*[[1, 2, 3, 2, 5]]) == 6
assert my_solution.missingInteger(*[[3, 4, 5, 1, 12, 14, 13]]) == 15
assert my_solution.missingInteger(*[[29, 30, 31, 32, 33, 34, 35, 36, 37]]) == 297
assert my_solution.missingInteger(*[[19, 20, 21, 22]]) == 82
assert my_solution.missingInteger(*[[18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 9]]) == 253
assert my_solution.missingInteger(*[[4, 5, 6, 7, 8, 8, 9, 4, 3, 2, 7]]) == 30
assert my_solution.missingInteger(*[[38]]) == 39
assert my_solution.missingInteger(*[[1]]) == 2
assert my_solution.missingInteger(*[[11, 12, 13]]) == 36
assert my_solution.missingInteger(*[[47, 48, 49, 5, 3]]) == 144
assert my_solution.missingInteger(*[[23, 24, 25, 4, 5, 1]]) == 72
assert my_solution.missingInteger(*[[8, 9, 10, 10, 7, 8]]) == 27
assert my_solution.missingInteger(*[[31, 32, 33, 34, 10, 8, 7, 9, 7, 9, 9, 5, 10, 1]]) == 130
assert my_solution.missingInteger(*[[17, 18, 19, 20, 21, 22, 3, 7, 10, 10]]) == 117
assert my_solution.missingInteger(*[[6, 7, 8, 9, 10, 8, 6, 7, 4, 1]]) == 40
assert my_solution.missingInteger(*[[46, 8, 2, 4, 1, 4, 10, 2, 4, 10, 2, 5, 7, 3, 1]]) == 47
assert my_solution.missingInteger(*[[37, 1, 2, 9, 5, 8, 5, 2, 9, 4]]) == 38
assert my_solution.missingInteger(*[[31, 32, 33, 34, 1]]) == 130
assert my_solution.missingInteger(*[[45, 46, 47, 48, 49, 10, 8, 1, 7, 4, 10, 10, 6, 6, 2]]) == 235
assert my_solution.missingInteger(*[[13, 10, 7, 5, 7, 10, 6, 10, 2]]) == 14
