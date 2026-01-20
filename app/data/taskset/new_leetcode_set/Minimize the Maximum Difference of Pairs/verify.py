
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.minimizeMax(*[[10, 1, 2, 7, 1, 3], 2]) == 1
assert my_solution.minimizeMax(*[[4, 2, 1, 2], 1]) == 0
assert my_solution.minimizeMax(*[[4, 0, 2, 1, 2, 5, 5, 3], 3]) == 1
assert my_solution.minimizeMax(*[[0, 5, 3, 4], 0]) == 0
assert my_solution.minimizeMax(*[[4, 1, 3, 3, 0, 4, 3], 1]) == 0
assert my_solution.minimizeMax(*[[3, 4, 1, 2, 1], 2]) == 1
assert my_solution.minimizeMax(*[[3, 6, 8, 7, 5, 4, 9, 5], 0]) == 0
assert my_solution.minimizeMax(*[[5, 6, 0, 5, 4, 0, 0], 1]) == 0
assert my_solution.minimizeMax(*[[8, 9, 1, 5, 4, 3, 6, 4, 3, 7], 4]) == 1
assert my_solution.minimizeMax(*[[3, 3, 5, 1, 0, 5, 6, 6], 4]) == 1
assert my_solution.minimizeMax(*[[5, 10, 6, 9, 12, 3, 8, 1, 3, 0, 7], 3]) == 1
assert my_solution.minimizeMax(*[[3, 1, 5, 0, 3], 0]) == 0
assert my_solution.minimizeMax(*[[2, 2, 0, 2, 0], 2]) == 0
assert my_solution.minimizeMax(*[[3, 4, 2, 3, 2, 1, 2], 3]) == 1
assert my_solution.minimizeMax(*[[4, 2, 8, 0, 0, 0, 3, 5, 4], 0]) == 0
assert my_solution.minimizeMax(*[[3, 11, 4, 3, 5, 7, 4, 4, 5, 5], 3]) == 0
assert my_solution.minimizeMax(*[[1, 2], 1]) == 1
assert my_solution.minimizeMax(*[[2, 6, 2, 4, 2, 2, 0, 2], 4]) == 2
assert my_solution.minimizeMax(*[[2, 6, 2, 2, 4, 2, 1, 1], 0]) == 0
assert my_solution.minimizeMax(*[[0, 4, 4, 6, 5, 5, 0, 3], 0]) == 0
