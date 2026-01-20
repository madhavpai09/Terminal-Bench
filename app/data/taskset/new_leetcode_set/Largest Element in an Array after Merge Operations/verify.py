
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.maxArrayValue(*[[2, 3, 7, 9, 3]]) == 21
assert my_solution.maxArrayValue(*[[5, 3, 3]]) == 11
assert my_solution.maxArrayValue(*[[77]]) == 77
assert my_solution.maxArrayValue(*[[34, 95, 50, 12, 25, 100, 21, 3, 25, 16, 76, 73, 93, 46, 18]]) == 623
assert my_solution.maxArrayValue(*[[40, 15, 35, 98, 77, 79, 24, 62, 53, 84, 97, 16, 30, 22, 49]]) == 781
assert my_solution.maxArrayValue(*[[64, 35, 42, 19, 95, 8, 83, 89, 33, 21, 97, 11, 51, 93, 36, 34, 67, 53]]) == 878
assert my_solution.maxArrayValue(*[[65, 68, 55, 6, 79, 30, 81, 25, 61, 2, 28, 59, 63, 15, 35, 8, 10, 83]]) == 773
assert my_solution.maxArrayValue(*[[56]]) == 56
assert my_solution.maxArrayValue(*[[100]]) == 100
assert my_solution.maxArrayValue(*[[35, 23, 71, 38]]) == 129
assert my_solution.maxArrayValue(*[[56, 67, 18, 81, 95, 41, 39, 56, 63, 70, 56, 31, 84, 46, 28, 38, 27, 56, 13, 10, 58, 16, 85, 21, 63, 8]]) == 1134
assert my_solution.maxArrayValue(*[[72, 72]]) == 144
assert my_solution.maxArrayValue(*[[16, 31, 55]]) == 102
assert my_solution.maxArrayValue(*[[6, 65, 68, 7, 35, 19, 28]]) == 228
assert my_solution.maxArrayValue(*[[38, 37, 88, 60, 93, 4, 5, 65, 74, 25, 59, 28, 86, 33, 28, 33, 93]]) == 849
assert my_solution.maxArrayValue(*[[29, 9, 3, 55, 25, 38, 88, 39, 38, 73, 47, 57, 40, 56, 4, 52, 1, 44, 88, 20, 18, 8]]) == 786
assert my_solution.maxArrayValue(*[[34, 92, 42, 24, 98, 87, 40, 82, 51, 67, 70, 75, 45, 57, 67]]) == 931
assert my_solution.maxArrayValue(*[[31, 75, 44, 92, 13, 10, 3, 41, 47, 89, 5, 92, 17, 62, 65, 40, 43, 68, 30, 45, 85, 24, 40, 77, 80, 65]]) == 1218
assert my_solution.maxArrayValue(*[[63, 58, 61, 58, 82, 48, 83, 24, 24, 61, 31, 16, 26, 50]]) == 685
assert my_solution.maxArrayValue(*[[10, 82, 74, 54, 20, 43, 74, 95, 17, 28, 44, 74, 25, 19, 75, 2, 84, 99]]) == 919
