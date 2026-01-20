
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.maxFrequencyScore(*[[1, 2, 6, 4], 3]) == 3
assert my_solution.maxFrequencyScore(*[[1, 4, 4, 2, 4], 0]) == 3
assert my_solution.maxFrequencyScore(*[[3, 20, 13, 2, 3, 15, 24, 19, 8, 13, 19, 20, 21], 45]) == 10
assert my_solution.maxFrequencyScore(*[[13, 22, 29, 21, 13, 17, 5, 2, 27, 6, 10, 4, 23, 29, 27], 117]) == 14
assert my_solution.maxFrequencyScore(*[[27, 8, 30, 3, 13, 28, 7, 14, 21, 19, 24, 28, 29, 1, 14, 22, 6], 23]) == 8
assert my_solution.maxFrequencyScore(*[[10, 11, 3], 1]) == 2
assert my_solution.maxFrequencyScore(*[[10, 19, 26, 18, 27, 18], 9]) == 4
assert my_solution.maxFrequencyScore(*[[17, 24, 10, 23, 22, 15, 25, 2, 13, 24, 22, 25, 25, 21], 52]) == 13
assert my_solution.maxFrequencyScore(*[[28, 6, 22, 10], 12]) == 2
assert my_solution.maxFrequencyScore(*[[17, 17, 25, 14, 29, 28, 20, 14, 16, 22, 4, 28, 2, 5, 3, 11, 6, 20, 17], 76]) == 14
assert my_solution.maxFrequencyScore(*[[23, 10, 18, 21, 16, 23, 14], 2]) == 3
assert my_solution.maxFrequencyScore(*[[5, 13, 7], 8]) == 3
assert my_solution.maxFrequencyScore(*[[6, 29, 3, 19, 10, 6, 20, 26, 1, 30, 11, 25, 29, 12, 29, 14, 15, 16, 5], 64]) == 12
assert my_solution.maxFrequencyScore(*[[10, 26, 21, 18, 30, 25, 1], 8]) == 3
assert my_solution.maxFrequencyScore(*[[29, 10, 26, 1, 2, 2, 17, 7, 5, 16, 24, 27, 7, 7, 26, 26, 24], 3]) == 5
assert my_solution.maxFrequencyScore(*[[11, 16, 6, 12, 3, 8, 5, 29, 9, 15, 7, 9, 14, 6, 11, 14, 12, 23, 22, 14], 79]) == 19
assert my_solution.maxFrequencyScore(*[[5, 17, 15, 14, 27, 11, 22, 6, 4], 26]) == 6
assert my_solution.maxFrequencyScore(*[[13, 22, 17], 4]) == 2
assert my_solution.maxFrequencyScore(*[[24, 6, 14, 6, 30, 9, 6, 11, 21, 10, 12, 27, 1], 90]) == 13
assert my_solution.maxFrequencyScore(*[[19, 5, 2, 23, 16, 22, 3, 2, 5, 20, 17, 3, 22, 1], 15]) == 7
