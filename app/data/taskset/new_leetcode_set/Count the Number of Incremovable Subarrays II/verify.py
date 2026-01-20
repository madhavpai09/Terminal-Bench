
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.incremovableSubarrayCount(*[[1, 2, 3, 4]]) == 10
assert my_solution.incremovableSubarrayCount(*[[6, 5, 7, 8]]) == 7
assert my_solution.incremovableSubarrayCount(*[[8, 7, 6, 6]]) == 3
assert my_solution.incremovableSubarrayCount(*[[1]]) == 1
assert my_solution.incremovableSubarrayCount(*[[2]]) == 1
assert my_solution.incremovableSubarrayCount(*[[3]]) == 1
assert my_solution.incremovableSubarrayCount(*[[4]]) == 1
assert my_solution.incremovableSubarrayCount(*[[5]]) == 1
assert my_solution.incremovableSubarrayCount(*[[6]]) == 1
assert my_solution.incremovableSubarrayCount(*[[7]]) == 1
assert my_solution.incremovableSubarrayCount(*[[8]]) == 1
assert my_solution.incremovableSubarrayCount(*[[9]]) == 1
assert my_solution.incremovableSubarrayCount(*[[10]]) == 1
assert my_solution.incremovableSubarrayCount(*[[4, 10]]) == 3
assert my_solution.incremovableSubarrayCount(*[[7, 3]]) == 3
assert my_solution.incremovableSubarrayCount(*[[8, 5]]) == 3
assert my_solution.incremovableSubarrayCount(*[[8, 10]]) == 3
assert my_solution.incremovableSubarrayCount(*[[9, 9]]) == 3
assert my_solution.incremovableSubarrayCount(*[[5, 5, 6]]) == 5
assert my_solution.incremovableSubarrayCount(*[[6, 7, 5]]) == 4
