
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.minGroupsForValidAssignment(*[[3, 2, 3, 2, 3]]) == 2
assert my_solution.minGroupsForValidAssignment(*[[10, 10, 10, 3, 1, 1]]) == 4
assert my_solution.minGroupsForValidAssignment(*[[1, 1]]) == 1
assert my_solution.minGroupsForValidAssignment(*[[1, 2]]) == 2
assert my_solution.minGroupsForValidAssignment(*[[1, 3]]) == 2
assert my_solution.minGroupsForValidAssignment(*[[2, 1]]) == 2
assert my_solution.minGroupsForValidAssignment(*[[2, 2]]) == 1
assert my_solution.minGroupsForValidAssignment(*[[3, 1]]) == 2
assert my_solution.minGroupsForValidAssignment(*[[3, 2]]) == 2
assert my_solution.minGroupsForValidAssignment(*[[3, 3]]) == 1
assert my_solution.minGroupsForValidAssignment(*[[3, 4]]) == 2
assert my_solution.minGroupsForValidAssignment(*[[10, 4]]) == 2
assert my_solution.minGroupsForValidAssignment(*[[10, 10]]) == 1
assert my_solution.minGroupsForValidAssignment(*[[14, 15]]) == 2
assert my_solution.minGroupsForValidAssignment(*[[1, 1, 1]]) == 1
assert my_solution.minGroupsForValidAssignment(*[[1, 2, 1]]) == 2
assert my_solution.minGroupsForValidAssignment(*[[1, 7, 10]]) == 3
assert my_solution.minGroupsForValidAssignment(*[[2, 1, 1]]) == 2
assert my_solution.minGroupsForValidAssignment(*[[2, 1, 2]]) == 2
assert my_solution.minGroupsForValidAssignment(*[[2, 2, 1]]) == 2
