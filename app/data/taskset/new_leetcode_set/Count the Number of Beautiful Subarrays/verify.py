
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.beautifulSubarrays(*[[4, 3, 1, 2, 4]]) == 2
assert my_solution.beautifulSubarrays(*[[1, 10, 4]]) == 0
assert my_solution.beautifulSubarrays(*[[0]]) == 1
assert my_solution.beautifulSubarrays(*[[1]]) == 0
assert my_solution.beautifulSubarrays(*[[0, 0]]) == 3
assert my_solution.beautifulSubarrays(*[[0, 1]]) == 1
assert my_solution.beautifulSubarrays(*[[1, 0]]) == 1
assert my_solution.beautifulSubarrays(*[[1, 1]]) == 1
assert my_solution.beautifulSubarrays(*[[0, 0, 0]]) == 6
assert my_solution.beautifulSubarrays(*[[1, 0, 0]]) == 3
assert my_solution.beautifulSubarrays(*[[0, 1, 0]]) == 2
assert my_solution.beautifulSubarrays(*[[1, 1, 0]]) == 3
assert my_solution.beautifulSubarrays(*[[0, 0, 1]]) == 3
assert my_solution.beautifulSubarrays(*[[1, 0, 1]]) == 2
assert my_solution.beautifulSubarrays(*[[0, 1, 1]]) == 3
assert my_solution.beautifulSubarrays(*[[1, 1, 1]]) == 2
assert my_solution.beautifulSubarrays(*[[0, 0, 0, 0]]) == 10
assert my_solution.beautifulSubarrays(*[[1, 0, 0, 0]]) == 6
assert my_solution.beautifulSubarrays(*[[0, 1, 0, 0]]) == 4
assert my_solution.beautifulSubarrays(*[[1, 1, 0, 0]]) == 6
