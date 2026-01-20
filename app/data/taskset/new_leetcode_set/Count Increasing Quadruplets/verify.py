
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.countQuadruplets(*[[1, 3, 2, 4, 5]]) == 2
assert my_solution.countQuadruplets(*[[1, 2, 3, 4]]) == 0
assert my_solution.countQuadruplets(*[[2, 5, 3, 1, 4]]) == 0
assert my_solution.countQuadruplets(*[[1, 3, 5, 2, 4]]) == 1
assert my_solution.countQuadruplets(*[[2, 4, 1, 3]]) == 0
assert my_solution.countQuadruplets(*[[3, 9, 5, 4, 8, 2, 1, 10, 7, 6]]) == 7
assert my_solution.countQuadruplets(*[[1, 7, 6, 5, 8, 3, 2, 4]]) == 4
assert my_solution.countQuadruplets(*[[9, 8, 5, 4, 2, 1, 6, 3, 7, 10]]) == 4
assert my_solution.countQuadruplets(*[[5, 2, 4, 1, 3]]) == 0
assert my_solution.countQuadruplets(*[[5, 3, 2, 4, 1]]) == 0
assert my_solution.countQuadruplets(*[[7, 2, 8, 9, 6, 4, 5, 1, 3]]) == 0
assert my_solution.countQuadruplets(*[[4, 2, 6, 3, 5, 7, 1, 8, 10, 9]]) == 12
assert my_solution.countQuadruplets(*[[3, 4, 6, 1, 7, 2, 8, 5, 9]]) == 11
assert my_solution.countQuadruplets(*[[9, 5, 3, 10, 6, 2, 4, 8, 7, 1]]) == 2
assert my_solution.countQuadruplets(*[[7, 4, 8, 9, 1, 3, 6, 2, 5]]) == 1
assert my_solution.countQuadruplets(*[[6, 1, 3, 9, 10, 7, 4, 8, 5, 2]]) == 2
assert my_solution.countQuadruplets(*[[1, 4, 2, 5, 3]]) == 1
assert my_solution.countQuadruplets(*[[3, 6, 4, 5, 8, 1, 7, 2]]) == 4
assert my_solution.countQuadruplets(*[[8, 7, 3, 4, 1, 6, 9, 5, 2]]) == 0
assert my_solution.countQuadruplets(*[[3, 5, 1, 4, 2, 6]]) == 2
