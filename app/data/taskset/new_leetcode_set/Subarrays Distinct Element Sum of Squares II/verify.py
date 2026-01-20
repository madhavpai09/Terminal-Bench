
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.sumCounts(*[[1, 2, 1]]) == 15
assert my_solution.sumCounts(*[[2, 2]]) == 3
assert my_solution.sumCounts(*[[2, 2, 5, 5]]) == 22
assert my_solution.sumCounts(*[[5, 2, 4, 2, 1, 3, 2, 4, 3, 1]]) == 578
assert my_solution.sumCounts(*[[2, 3, 2, 1, 2, 5, 3, 4, 5, 2]]) == 629
assert my_solution.sumCounts(*[[5, 1, 5, 2, 3, 5, 1, 5, 1]]) == 385
assert my_solution.sumCounts(*[[4, 5, 4, 3, 4, 2]]) == 120
assert my_solution.sumCounts(*[[2]]) == 1
assert my_solution.sumCounts(*[[3, 4, 2, 5, 2, 4, 1, 2, 2, 5]]) == 535
assert my_solution.sumCounts(*[[4, 4, 2, 4, 1]]) == 57
assert my_solution.sumCounts(*[[2, 2, 5]]) == 12
assert my_solution.sumCounts(*[[4, 5, 1, 2, 2, 1, 3, 3]]) == 266
assert my_solution.sumCounts(*[[3, 1, 5, 5, 2, 3, 2, 2, 1]]) == 334
assert my_solution.sumCounts(*[[2, 5, 2, 5, 3, 2, 5, 2]]) == 205
assert my_solution.sumCounts(*[[5, 4, 1, 4, 5, 2, 4]]) == 203
assert my_solution.sumCounts(*[[1, 3, 3, 4, 3, 1, 2, 1]]) == 253
assert my_solution.sumCounts(*[[4]]) == 1
assert my_solution.sumCounts(*[[1, 4, 2, 1, 5, 4, 3, 1, 4]]) == 507
assert my_solution.sumCounts(*[[2, 4, 5, 3, 2, 5, 1, 5, 4, 4]]) == 626
assert my_solution.sumCounts(*[[3, 4, 1, 4, 5, 2, 2]]) == 220
