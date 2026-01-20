
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.maxSubarrayLength(*[[1, 2, 3, 1, 2, 3, 1, 2], 2]) == 6
assert my_solution.maxSubarrayLength(*[[1, 2, 1, 2, 1, 2, 1, 2], 1]) == 2
assert my_solution.maxSubarrayLength(*[[5, 5, 5, 5, 5, 5, 5], 4]) == 4
assert my_solution.maxSubarrayLength(*[[1], 1]) == 1
assert my_solution.maxSubarrayLength(*[[2], 1]) == 1
assert my_solution.maxSubarrayLength(*[[3], 1]) == 1
assert my_solution.maxSubarrayLength(*[[4], 1]) == 1
assert my_solution.maxSubarrayLength(*[[5], 1]) == 1
assert my_solution.maxSubarrayLength(*[[6], 1]) == 1
assert my_solution.maxSubarrayLength(*[[7], 1]) == 1
assert my_solution.maxSubarrayLength(*[[8], 1]) == 1
assert my_solution.maxSubarrayLength(*[[9], 1]) == 1
assert my_solution.maxSubarrayLength(*[[10], 1]) == 1
assert my_solution.maxSubarrayLength(*[[1, 11], 2]) == 2
assert my_solution.maxSubarrayLength(*[[2, 11], 1]) == 2
assert my_solution.maxSubarrayLength(*[[3, 5], 2]) == 2
assert my_solution.maxSubarrayLength(*[[4, 6], 2]) == 2
assert my_solution.maxSubarrayLength(*[[5, 8], 2]) == 2
assert my_solution.maxSubarrayLength(*[[6, 7], 1]) == 2
assert my_solution.maxSubarrayLength(*[[7, 9], 2]) == 2
