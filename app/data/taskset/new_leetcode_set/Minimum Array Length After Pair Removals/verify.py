
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.minLengthAfterRemovals(*[[1, 3, 4, 9]]) == 0
assert my_solution.minLengthAfterRemovals(*[[2, 3, 6, 9]]) == 0
assert my_solution.minLengthAfterRemovals(*[[1, 1, 2]]) == 1
assert my_solution.minLengthAfterRemovals(*[[1]]) == 1
assert my_solution.minLengthAfterRemovals(*[[2]]) == 1
assert my_solution.minLengthAfterRemovals(*[[3]]) == 1
assert my_solution.minLengthAfterRemovals(*[[5]]) == 1
assert my_solution.minLengthAfterRemovals(*[[1, 1]]) == 2
assert my_solution.minLengthAfterRemovals(*[[1, 2]]) == 0
assert my_solution.minLengthAfterRemovals(*[[1, 4]]) == 0
assert my_solution.minLengthAfterRemovals(*[[2, 3]]) == 0
assert my_solution.minLengthAfterRemovals(*[[3, 3]]) == 2
assert my_solution.minLengthAfterRemovals(*[[4, 5]]) == 0
assert my_solution.minLengthAfterRemovals(*[[1, 1, 1]]) == 3
assert my_solution.minLengthAfterRemovals(*[[1, 2, 2]]) == 1
assert my_solution.minLengthAfterRemovals(*[[1, 3, 3]]) == 1
assert my_solution.minLengthAfterRemovals(*[[2, 2, 2]]) == 3
assert my_solution.minLengthAfterRemovals(*[[2, 3, 3]]) == 1
assert my_solution.minLengthAfterRemovals(*[[2, 3, 4]]) == 1
assert my_solution.minLengthAfterRemovals(*[[3, 4, 5]]) == 1
