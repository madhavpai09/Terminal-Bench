
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.sumImbalanceNumbers(*[[2, 3, 1, 4]]) == 3
assert my_solution.sumImbalanceNumbers(*[[1, 3, 3, 3, 5]]) == 8
assert my_solution.sumImbalanceNumbers(*[[1]]) == 0
assert my_solution.sumImbalanceNumbers(*[[1, 1]]) == 0
assert my_solution.sumImbalanceNumbers(*[[1, 2]]) == 0
assert my_solution.sumImbalanceNumbers(*[[2, 1]]) == 0
assert my_solution.sumImbalanceNumbers(*[[2, 2]]) == 0
assert my_solution.sumImbalanceNumbers(*[[1, 1, 1]]) == 0
assert my_solution.sumImbalanceNumbers(*[[1, 1, 2]]) == 0
assert my_solution.sumImbalanceNumbers(*[[1, 1, 3]]) == 2
assert my_solution.sumImbalanceNumbers(*[[1, 2, 1]]) == 0
assert my_solution.sumImbalanceNumbers(*[[1, 2, 2]]) == 0
assert my_solution.sumImbalanceNumbers(*[[1, 2, 3]]) == 0
assert my_solution.sumImbalanceNumbers(*[[1, 3, 1]]) == 3
assert my_solution.sumImbalanceNumbers(*[[1, 3, 2]]) == 1
assert my_solution.sumImbalanceNumbers(*[[1, 3, 3]]) == 2
assert my_solution.sumImbalanceNumbers(*[[2, 1, 1]]) == 0
assert my_solution.sumImbalanceNumbers(*[[2, 1, 2]]) == 0
assert my_solution.sumImbalanceNumbers(*[[2, 1, 3]]) == 1
assert my_solution.sumImbalanceNumbers(*[[2, 2, 1]]) == 0
