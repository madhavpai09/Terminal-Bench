
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.longestAlternatingSubarray(*[[3, 2, 5, 4], 5]) == 3
assert my_solution.longestAlternatingSubarray(*[[1, 2], 2]) == 1
assert my_solution.longestAlternatingSubarray(*[[2, 3, 4, 5], 4]) == 3
assert my_solution.longestAlternatingSubarray(*[[1], 1]) == 0
assert my_solution.longestAlternatingSubarray(*[[2], 2]) == 1
assert my_solution.longestAlternatingSubarray(*[[3], 3]) == 0
assert my_solution.longestAlternatingSubarray(*[[4], 1]) == 0
assert my_solution.longestAlternatingSubarray(*[[5], 3]) == 0
assert my_solution.longestAlternatingSubarray(*[[6], 5]) == 0
assert my_solution.longestAlternatingSubarray(*[[7], 2]) == 0
assert my_solution.longestAlternatingSubarray(*[[8], 1]) == 0
assert my_solution.longestAlternatingSubarray(*[[9], 7]) == 0
assert my_solution.longestAlternatingSubarray(*[[10], 7]) == 0
assert my_solution.longestAlternatingSubarray(*[[1, 3], 16]) == 0
assert my_solution.longestAlternatingSubarray(*[[1, 6], 2]) == 0
assert my_solution.longestAlternatingSubarray(*[[1, 10], 6]) == 0
assert my_solution.longestAlternatingSubarray(*[[1, 10], 7]) == 0
assert my_solution.longestAlternatingSubarray(*[[2, 2], 18]) == 1
assert my_solution.longestAlternatingSubarray(*[[2, 4], 7]) == 1
assert my_solution.longestAlternatingSubarray(*[[2, 5], 2]) == 1
