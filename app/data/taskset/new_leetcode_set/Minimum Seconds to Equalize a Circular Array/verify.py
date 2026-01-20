
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.minimumSeconds(*[[1, 2, 1, 2]]) == 1
assert my_solution.minimumSeconds(*[[2, 1, 3, 3, 2]]) == 2
assert my_solution.minimumSeconds(*[[5, 5, 5, 5]]) == 0
assert my_solution.minimumSeconds(*[[4, 18]]) == 1
assert my_solution.minimumSeconds(*[[11, 7]]) == 1
assert my_solution.minimumSeconds(*[[14, 2]]) == 1
assert my_solution.minimumSeconds(*[[14, 9]]) == 1
assert my_solution.minimumSeconds(*[[20, 1]]) == 1
assert my_solution.minimumSeconds(*[[17, 15]]) == 1
assert my_solution.minimumSeconds(*[[11, 13]]) == 1
assert my_solution.minimumSeconds(*[[7, 13]]) == 1
assert my_solution.minimumSeconds(*[[18, 17]]) == 1
assert my_solution.minimumSeconds(*[[15, 17]]) == 1
assert my_solution.minimumSeconds(*[[13, 8]]) == 1
assert my_solution.minimumSeconds(*[[12, 16]]) == 1
assert my_solution.minimumSeconds(*[[12, 8]]) == 1
assert my_solution.minimumSeconds(*[[18, 16]]) == 1
assert my_solution.minimumSeconds(*[[16, 16]]) == 0
assert my_solution.minimumSeconds(*[[6, 12]]) == 1
assert my_solution.minimumSeconds(*[[9, 6]]) == 1
