
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.maximumStrongPairXor(*[[1, 2, 3, 4, 5]]) == 7
assert my_solution.maximumStrongPairXor(*[[10, 100]]) == 0
assert my_solution.maximumStrongPairXor(*[[5, 6, 25, 30]]) == 7
assert my_solution.maximumStrongPairXor(*[[1]]) == 0
assert my_solution.maximumStrongPairXor(*[[100]]) == 0
assert my_solution.maximumStrongPairXor(*[[1, 1, 2, 3, 5]]) == 6
assert my_solution.maximumStrongPairXor(*[[1, 1, 3, 8, 7]]) == 15
assert my_solution.maximumStrongPairXor(*[[1, 1, 4, 4, 3]]) == 7
assert my_solution.maximumStrongPairXor(*[[1, 1, 6, 6, 9]]) == 15
assert my_solution.maximumStrongPairXor(*[[1, 1, 10, 3, 9]]) == 3
assert my_solution.maximumStrongPairXor(*[[1, 2, 1, 5, 3]]) == 6
assert my_solution.maximumStrongPairXor(*[[1, 2, 2, 1, 2]]) == 3
assert my_solution.maximumStrongPairXor(*[[1, 2, 3, 8, 1]]) == 3
assert my_solution.maximumStrongPairXor(*[[1, 2, 5, 5, 10]]) == 15
assert my_solution.maximumStrongPairXor(*[[1, 2, 8, 3, 2]]) == 3
assert my_solution.maximumStrongPairXor(*[[1, 2, 9, 2, 8]]) == 3
assert my_solution.maximumStrongPairXor(*[[1, 3, 3, 2, 1]]) == 3
assert my_solution.maximumStrongPairXor(*[[1, 3, 8, 5, 3]]) == 13
assert my_solution.maximumStrongPairXor(*[[1, 3, 9, 6, 5]]) == 15
assert my_solution.maximumStrongPairXor(*[[1, 4, 1, 2, 5]]) == 6
