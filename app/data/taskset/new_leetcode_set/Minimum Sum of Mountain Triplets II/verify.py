
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.minimumSum(*[[8, 6, 1, 5, 3]]) == 9
assert my_solution.minimumSum(*[[5, 4, 8, 7, 10, 2]]) == 13
assert my_solution.minimumSum(*[[6, 5, 4, 3, 4, 5]]) == -1
assert my_solution.minimumSum(*[[50, 50, 50]]) == -1
assert my_solution.minimumSum(*[[49, 50, 48]]) == 147
assert my_solution.minimumSum(*[[48, 50, 49]]) == 147
assert my_solution.minimumSum(*[[99999999, 100000000, 99999999]]) == 299999998
assert my_solution.minimumSum(*[[1, 1, 1]]) == -1
assert my_solution.minimumSum(*[[1, 1, 2]]) == -1
assert my_solution.minimumSum(*[[1, 1, 3]]) == -1
assert my_solution.minimumSum(*[[1, 2, 1]]) == 4
assert my_solution.minimumSum(*[[1, 2, 2]]) == -1
assert my_solution.minimumSum(*[[1, 2, 3]]) == -1
assert my_solution.minimumSum(*[[1, 3, 1]]) == 5
assert my_solution.minimumSum(*[[1, 3, 2]]) == 6
assert my_solution.minimumSum(*[[1, 3, 3]]) == -1
assert my_solution.minimumSum(*[[2, 1, 1]]) == -1
assert my_solution.minimumSum(*[[2, 1, 2]]) == -1
assert my_solution.minimumSum(*[[2, 1, 3]]) == -1
assert my_solution.minimumSum(*[[2, 2, 1]]) == -1
