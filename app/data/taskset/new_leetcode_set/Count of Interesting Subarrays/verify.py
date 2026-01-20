
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.countInterestingSubarrays(*[[3, 2, 4], 2, 1]) == 3
assert my_solution.countInterestingSubarrays(*[[3, 1, 9, 6], 3, 0]) == 2
assert my_solution.countInterestingSubarrays(*[[11, 12, 21, 31], 10, 1]) == 5
assert my_solution.countInterestingSubarrays(*[[2, 4], 7, 2]) == 0
assert my_solution.countInterestingSubarrays(*[[2, 7], 7, 0]) == 1
assert my_solution.countInterestingSubarrays(*[[2, 45], 13, 2]) == 0
assert my_solution.countInterestingSubarrays(*[[3, 3], 5, 3]) == 0
assert my_solution.countInterestingSubarrays(*[[3, 4], 8, 3]) == 0
assert my_solution.countInterestingSubarrays(*[[4, 5], 1, 0]) == 3
assert my_solution.countInterestingSubarrays(*[[5, 1], 6, 1]) == 2
assert my_solution.countInterestingSubarrays(*[[7, 2], 7, 0]) == 1
assert my_solution.countInterestingSubarrays(*[[7, 4], 7, 0]) == 1
assert my_solution.countInterestingSubarrays(*[[8, 8], 4, 0]) == 0
assert my_solution.countInterestingSubarrays(*[[9, 2], 2, 0]) == 1
assert my_solution.countInterestingSubarrays(*[[18, 43], 3, 0]) == 1
assert my_solution.countInterestingSubarrays(*[[19, 67], 47, 19]) == 0
assert my_solution.countInterestingSubarrays(*[[20, 8], 41, 8]) == 0
assert my_solution.countInterestingSubarrays(*[[26, 5], 21, 5]) == 0
assert my_solution.countInterestingSubarrays(*[[81, 36], 4, 0]) == 1
assert my_solution.countInterestingSubarrays(*[[2, 1, 5], 9, 1]) == 4
