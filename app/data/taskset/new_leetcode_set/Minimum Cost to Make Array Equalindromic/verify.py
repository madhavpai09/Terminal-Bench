
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.minimumCost(*[[1, 2, 3, 4, 5]]) == 6
assert my_solution.minimumCost(*[[10, 12, 13, 14, 15]]) == 11
assert my_solution.minimumCost(*[[22, 33, 22, 33, 22]]) == 22
assert my_solution.minimumCost(*[[1]]) == 0
assert my_solution.minimumCost(*[[2]]) == 0
assert my_solution.minimumCost(*[[3]]) == 0
assert my_solution.minimumCost(*[[4]]) == 0
assert my_solution.minimumCost(*[[5]]) == 0
assert my_solution.minimumCost(*[[2, 1]]) == 1
assert my_solution.minimumCost(*[[3, 1]]) == 2
assert my_solution.minimumCost(*[[3, 2]]) == 1
assert my_solution.minimumCost(*[[4, 1]]) == 3
assert my_solution.minimumCost(*[[4, 2]]) == 2
assert my_solution.minimumCost(*[[4, 3]]) == 1
assert my_solution.minimumCost(*[[5, 1]]) == 4
assert my_solution.minimumCost(*[[5, 2]]) == 3
assert my_solution.minimumCost(*[[5, 3]]) == 2
assert my_solution.minimumCost(*[[5, 4]]) == 1
assert my_solution.minimumCost(*[[3, 2, 1]]) == 2
assert my_solution.minimumCost(*[[4, 2, 1]]) == 3
