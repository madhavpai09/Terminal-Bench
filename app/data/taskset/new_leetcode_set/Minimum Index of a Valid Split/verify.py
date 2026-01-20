
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.minimumIndex(*[[1, 2, 2, 2]]) == 2
assert my_solution.minimumIndex(*[[2, 1, 3, 1, 1, 1, 7, 1, 2, 1]]) == 4
assert my_solution.minimumIndex(*[[3, 3, 3, 3, 7, 2, 2]]) == -1
assert my_solution.minimumIndex(*[[1]]) == -1
assert my_solution.minimumIndex(*[[1, 1]]) == 0
assert my_solution.minimumIndex(*[[1, 1, 1]]) == 0
assert my_solution.minimumIndex(*[[1, 1, 1, 1]]) == 0
assert my_solution.minimumIndex(*[[1, 1, 1, 2]]) == 0
assert my_solution.minimumIndex(*[[1, 1, 1, 3]]) == 0
assert my_solution.minimumIndex(*[[1, 1, 1, 4]]) == 0
assert my_solution.minimumIndex(*[[1, 1, 2]]) == -1
assert my_solution.minimumIndex(*[[1, 1, 2, 1]]) == 0
assert my_solution.minimumIndex(*[[1, 1, 3]]) == -1
assert my_solution.minimumIndex(*[[1, 1, 3, 1]]) == 0
assert my_solution.minimumIndex(*[[1, 1, 4]]) == -1
assert my_solution.minimumIndex(*[[1, 1, 4, 1]]) == 0
assert my_solution.minimumIndex(*[[1, 2, 1]]) == -1
assert my_solution.minimumIndex(*[[1, 2, 1, 1]]) == 0
assert my_solution.minimumIndex(*[[1, 2, 2]]) == -1
assert my_solution.minimumIndex(*[[1, 3, 1]]) == -1
