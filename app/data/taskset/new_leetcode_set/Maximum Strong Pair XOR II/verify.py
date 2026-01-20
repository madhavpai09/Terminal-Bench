
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.maximumStrongPairXor(*[[1, 2, 3, 4, 5]]) == 7
assert my_solution.maximumStrongPairXor(*[[10, 100]]) == 0
assert my_solution.maximumStrongPairXor(*[[500, 520, 2500, 3000]]) == 1020
assert my_solution.maximumStrongPairXor(*[[1]]) == 0
assert my_solution.maximumStrongPairXor(*[[2, 3]]) == 1
assert my_solution.maximumStrongPairXor(*[[3, 4]]) == 7
assert my_solution.maximumStrongPairXor(*[[4, 5]]) == 1
assert my_solution.maximumStrongPairXor(*[[5, 6]]) == 3
assert my_solution.maximumStrongPairXor(*[[1, 1, 1]]) == 0
assert my_solution.maximumStrongPairXor(*[[1, 1, 2]]) == 3
assert my_solution.maximumStrongPairXor(*[[1, 1, 3]]) == 0
assert my_solution.maximumStrongPairXor(*[[1, 1, 4]]) == 0
assert my_solution.maximumStrongPairXor(*[[1, 1, 5]]) == 0
assert my_solution.maximumStrongPairXor(*[[1, 2, 1]]) == 3
assert my_solution.maximumStrongPairXor(*[[1, 2, 2]]) == 3
assert my_solution.maximumStrongPairXor(*[[1, 2, 3]]) == 3
assert my_solution.maximumStrongPairXor(*[[1, 2, 4]]) == 6
assert my_solution.maximumStrongPairXor(*[[1, 2, 5]]) == 3
assert my_solution.maximumStrongPairXor(*[[1, 3, 1]]) == 0
assert my_solution.maximumStrongPairXor(*[[1, 3, 2]]) == 3
