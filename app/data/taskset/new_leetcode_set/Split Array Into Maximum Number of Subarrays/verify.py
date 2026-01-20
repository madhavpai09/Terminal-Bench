
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.maxSubarrays(*[[1, 0, 2, 0, 1, 2]]) == 3
assert my_solution.maxSubarrays(*[[5, 7, 1, 3]]) == 1
assert my_solution.maxSubarrays(*[[1, 0, 2, 1]]) == 2
assert my_solution.maxSubarrays(*[[0]]) == 1
assert my_solution.maxSubarrays(*[[0, 0]]) == 2
assert my_solution.maxSubarrays(*[[100000]]) == 1
assert my_solution.maxSubarrays(*[[1, 2, 2, 1]]) == 2
assert my_solution.maxSubarrays(*[[30, 18, 19, 20, 11, 21, 12, 22, 26]]) == 2
assert my_solution.maxSubarrays(*[[0, 8, 0, 0, 0, 23]]) == 4
assert my_solution.maxSubarrays(*[[8, 10, 23, 26, 21, 28, 21, 14, 21, 14, 9, 16, 24, 29, 7, 26]]) == 4
assert my_solution.maxSubarrays(*[[18, 12, 16, 28, 7, 15, 24, 7, 8, 26, 22, 6, 23, 7, 17, 1, 16]]) == 6
assert my_solution.maxSubarrays(*[[22]]) == 1
assert my_solution.maxSubarrays(*[[15, 24, 20, 28, 11, 16, 0, 0, 0, 22, 7, 18]]) == 5
assert my_solution.maxSubarrays(*[[0, 0, 27]]) == 2
assert my_solution.maxSubarrays(*[[18, 7, 20, 10, 0, 14, 0, 28, 7, 0, 0, 9, 12, 0]]) == 6
assert my_solution.maxSubarrays(*[[0, 29, 16, 0, 6, 17]]) == 3
assert my_solution.maxSubarrays(*[[4, 7, 13, 0, 23, 6, 4]]) == 1
assert my_solution.maxSubarrays(*[[4, 27]]) == 1
assert my_solution.maxSubarrays(*[[29, 5, 0, 25, 0, 15, 19, 24, 20, 0, 23]]) == 4
assert my_solution.maxSubarrays(*[[24, 6]]) == 1
