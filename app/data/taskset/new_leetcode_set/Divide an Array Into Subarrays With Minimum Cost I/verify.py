
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.minimumCost(*[[1, 2, 3, 12]]) == 6
assert my_solution.minimumCost(*[[5, 4, 3]]) == 12
assert my_solution.minimumCost(*[[10, 3, 1, 1]]) == 12
assert my_solution.minimumCost(*[[1, 1, 1]]) == 3
assert my_solution.minimumCost(*[[1, 1, 2]]) == 4
assert my_solution.minimumCost(*[[1, 1, 3]]) == 5
assert my_solution.minimumCost(*[[1, 1, 4]]) == 6
assert my_solution.minimumCost(*[[1, 1, 5]]) == 7
assert my_solution.minimumCost(*[[1, 2, 1]]) == 4
assert my_solution.minimumCost(*[[1, 2, 2]]) == 5
assert my_solution.minimumCost(*[[1, 2, 3]]) == 6
assert my_solution.minimumCost(*[[1, 2, 4]]) == 7
assert my_solution.minimumCost(*[[1, 2, 5]]) == 8
assert my_solution.minimumCost(*[[1, 3, 1]]) == 5
assert my_solution.minimumCost(*[[1, 3, 2]]) == 6
assert my_solution.minimumCost(*[[1, 3, 3]]) == 7
assert my_solution.minimumCost(*[[1, 3, 4]]) == 8
assert my_solution.minimumCost(*[[1, 3, 5]]) == 9
assert my_solution.minimumCost(*[[1, 4, 1]]) == 6
assert my_solution.minimumCost(*[[1, 4, 2]]) == 7
