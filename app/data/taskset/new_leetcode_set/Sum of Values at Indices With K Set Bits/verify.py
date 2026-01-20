
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.sumIndicesWithKSetBits(*[[5, 10, 1, 5, 2], 1]) == 13
assert my_solution.sumIndicesWithKSetBits(*[[4, 3, 2, 1], 2]) == 1
assert my_solution.sumIndicesWithKSetBits(*[[1], 0]) == 1
assert my_solution.sumIndicesWithKSetBits(*[[100000], 0]) == 100000
assert my_solution.sumIndicesWithKSetBits(*[[2, 2], 1]) == 2
assert my_solution.sumIndicesWithKSetBits(*[[2, 4], 1]) == 4
assert my_solution.sumIndicesWithKSetBits(*[[2, 7], 1]) == 7
assert my_solution.sumIndicesWithKSetBits(*[[3, 3], 1]) == 3
assert my_solution.sumIndicesWithKSetBits(*[[3, 9], 1]) == 9
assert my_solution.sumIndicesWithKSetBits(*[[4, 7], 1]) == 7
assert my_solution.sumIndicesWithKSetBits(*[[4, 8], 1]) == 8
assert my_solution.sumIndicesWithKSetBits(*[[6, 6], 1]) == 6
assert my_solution.sumIndicesWithKSetBits(*[[7, 2], 1]) == 2
assert my_solution.sumIndicesWithKSetBits(*[[7, 4], 1]) == 4
assert my_solution.sumIndicesWithKSetBits(*[[8, 4], 1]) == 4
assert my_solution.sumIndicesWithKSetBits(*[[8, 9], 1]) == 9
assert my_solution.sumIndicesWithKSetBits(*[[9, 9], 1]) == 9
assert my_solution.sumIndicesWithKSetBits(*[[15, 43], 1]) == 43
assert my_solution.sumIndicesWithKSetBits(*[[35, 86], 1]) == 86
assert my_solution.sumIndicesWithKSetBits(*[[36, 14], 1]) == 14
