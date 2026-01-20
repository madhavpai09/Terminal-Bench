
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.maxNonDecreasingLength(*[[2, 3, 1], [1, 2, 1]]) == 2
assert my_solution.maxNonDecreasingLength(*[[1, 3, 2, 1], [2, 2, 3, 4]]) == 4
assert my_solution.maxNonDecreasingLength(*[[1, 1], [2, 2]]) == 2
assert my_solution.maxNonDecreasingLength(*[[1], [1]]) == 1
assert my_solution.maxNonDecreasingLength(*[[1], [2]]) == 1
assert my_solution.maxNonDecreasingLength(*[[1, 4], [4, 19]]) == 2
assert my_solution.maxNonDecreasingLength(*[[1, 8], [10, 1]]) == 2
assert my_solution.maxNonDecreasingLength(*[[1, 11], [9, 1]]) == 2
assert my_solution.maxNonDecreasingLength(*[[1, 13], [18, 1]]) == 2
assert my_solution.maxNonDecreasingLength(*[[1, 19], [12, 20]]) == 2
assert my_solution.maxNonDecreasingLength(*[[1, 19], [18, 9]]) == 2
assert my_solution.maxNonDecreasingLength(*[[2, 20], [1, 18]]) == 2
assert my_solution.maxNonDecreasingLength(*[[3, 5], [13, 3]]) == 2
assert my_solution.maxNonDecreasingLength(*[[3, 6], [10, 12]]) == 2
assert my_solution.maxNonDecreasingLength(*[[3, 7], [8, 3]]) == 2
assert my_solution.maxNonDecreasingLength(*[[3, 8], [15, 2]]) == 2
assert my_solution.maxNonDecreasingLength(*[[3, 9], [11, 3]]) == 2
assert my_solution.maxNonDecreasingLength(*[[3, 12], [7, 3]]) == 2
assert my_solution.maxNonDecreasingLength(*[[3, 12], [20, 3]]) == 2
assert my_solution.maxNonDecreasingLength(*[[3, 20], [5, 17]]) == 2
