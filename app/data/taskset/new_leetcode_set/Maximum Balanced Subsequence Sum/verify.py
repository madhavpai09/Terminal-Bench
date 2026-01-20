
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.maxBalancedSubsequenceSum(*[[3, 3, 5, 6]]) == 14
assert my_solution.maxBalancedSubsequenceSum(*[[5, -1, -3, 8]]) == 13
assert my_solution.maxBalancedSubsequenceSum(*[[-2, -1]]) == -1
assert my_solution.maxBalancedSubsequenceSum(*[[0]]) == 0
assert my_solution.maxBalancedSubsequenceSum(*[[-47]]) == -47
assert my_solution.maxBalancedSubsequenceSum(*[[-8]]) == -8
assert my_solution.maxBalancedSubsequenceSum(*[[-7]]) == -7
assert my_solution.maxBalancedSubsequenceSum(*[[-6]]) == -6
assert my_solution.maxBalancedSubsequenceSum(*[[-5]]) == -5
assert my_solution.maxBalancedSubsequenceSum(*[[-3]]) == -3
assert my_solution.maxBalancedSubsequenceSum(*[[-2]]) == -2
assert my_solution.maxBalancedSubsequenceSum(*[[-1]]) == -1
assert my_solution.maxBalancedSubsequenceSum(*[[1]]) == 1
assert my_solution.maxBalancedSubsequenceSum(*[[3]]) == 3
assert my_solution.maxBalancedSubsequenceSum(*[[4]]) == 4
assert my_solution.maxBalancedSubsequenceSum(*[[5]]) == 5
assert my_solution.maxBalancedSubsequenceSum(*[[7]]) == 7
assert my_solution.maxBalancedSubsequenceSum(*[[8]]) == 8
assert my_solution.maxBalancedSubsequenceSum(*[[9]]) == 9
assert my_solution.maxBalancedSubsequenceSum(*[[45]]) == 45
