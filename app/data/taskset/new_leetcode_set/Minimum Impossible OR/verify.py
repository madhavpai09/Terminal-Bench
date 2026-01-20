
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.minImpossibleOR(*[[2, 1]]) == 4
assert my_solution.minImpossibleOR(*[[5, 3, 2]]) == 1
assert my_solution.minImpossibleOR(*[[1, 25, 2, 72]]) == 4
assert my_solution.minImpossibleOR(*[[4, 32, 16, 8, 8, 75, 1, 2]]) == 64
assert my_solution.minImpossibleOR(*[[25, 2, 1, 92, 8, 4, 16]]) == 32
assert my_solution.minImpossibleOR(*[[4, 1, 2, 8, 8, 16]]) == 32
assert my_solution.minImpossibleOR(*[[2, 64, 1, 32, 4, 8, 16]]) == 128
assert my_solution.minImpossibleOR(*[[1, 4, 2]]) == 8
assert my_solution.minImpossibleOR(*[[4, 2, 1]]) == 8
assert my_solution.minImpossibleOR(*[[21, 1]]) == 2
assert my_solution.minImpossibleOR(*[[2, 4, 16, 1, 128, 64, 32, 8]]) == 256
assert my_solution.minImpossibleOR(*[[1, 2, 4]]) == 8
assert my_solution.minImpossibleOR(*[[4, 2, 8, 1, 87, 16, 6]]) == 32
assert my_solution.minImpossibleOR(*[[96, 1]]) == 2
assert my_solution.minImpossibleOR(*[[2, 1, 88]]) == 4
assert my_solution.minImpossibleOR(*[[76, 2, 96, 82, 4, 8, 24, 1]]) == 16
assert my_solution.minImpossibleOR(*[[1]]) == 2
assert my_solution.minImpossibleOR(*[[6, 8, 46, 57, 59, 97, 4, 2, 1]]) == 16
assert my_solution.minImpossibleOR(*[[2, 46, 1, 1, 24, 55, 71, 63]]) == 4
assert my_solution.minImpossibleOR(*[[2, 8, 32, 1, 4, 16, 43, 64]]) == 128
