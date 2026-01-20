
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.alternatingSubarray(*[[2, 3, 4, 3, 4]]) == 4
assert my_solution.alternatingSubarray(*[[4, 5, 6]]) == 2
assert my_solution.alternatingSubarray(*[[31, 32, 31, 32, 33]]) == 4
assert my_solution.alternatingSubarray(*[[21, 9, 5]]) == -1
assert my_solution.alternatingSubarray(*[[42, 43, 44, 43, 44, 43, 44, 45, 46]]) == 6
assert my_solution.alternatingSubarray(*[[13, 14, 15, 14]]) == 3
assert my_solution.alternatingSubarray(*[[74, 75, 74, 75, 74, 75, 74, 75]]) == 8
assert my_solution.alternatingSubarray(*[[77, 78, 79, 78, 79, 78, 79, 78, 79, 80]]) == 8
assert my_solution.alternatingSubarray(*[[88, 42, 53]]) == -1
assert my_solution.alternatingSubarray(*[[64, 65, 64, 65, 64, 65, 66, 65, 66, 65]]) == 6
assert my_solution.alternatingSubarray(*[[99, 100, 99, 100]]) == 4
assert my_solution.alternatingSubarray(*[[21, 22]]) == 2
assert my_solution.alternatingSubarray(*[[23, 24, 23, 24, 25, 24, 25, 24, 25]]) == 6
assert my_solution.alternatingSubarray(*[[20, 9, 15, 15]]) == -1
assert my_solution.alternatingSubarray(*[[92, 93, 92, 93, 92]]) == 5
assert my_solution.alternatingSubarray(*[[24, 25, 26]]) == 2
assert my_solution.alternatingSubarray(*[[51, 52, 53, 52, 53, 52, 53, 54, 53]]) == 6
assert my_solution.alternatingSubarray(*[[65, 66, 65, 66, 67, 68, 69]]) == 4
assert my_solution.alternatingSubarray(*[[29, 2, 5, 24]]) == -1
assert my_solution.alternatingSubarray(*[[26, 27, 26, 27, 28, 27, 28, 27, 28]]) == 6
