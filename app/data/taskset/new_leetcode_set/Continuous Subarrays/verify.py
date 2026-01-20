
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.continuousSubarrays(*[[5, 4, 2, 4]]) == 8
assert my_solution.continuousSubarrays(*[[1, 2, 3]]) == 6
assert my_solution.continuousSubarrays(*[[31, 30, 31, 32]]) == 10
assert my_solution.continuousSubarrays(*[[65, 66, 67, 66, 66, 65, 64, 65, 65, 64]]) == 43
assert my_solution.continuousSubarrays(*[[42, 41, 42, 41, 41, 40, 39, 38]]) == 28
assert my_solution.continuousSubarrays(*[[35, 35, 36, 37, 36, 37, 38, 37, 38]]) == 39
assert my_solution.continuousSubarrays(*[[43, 44, 43, 44]]) == 10
assert my_solution.continuousSubarrays(*[[14, 15, 15, 15, 16, 16, 16, 16, 15, 16]]) == 55
assert my_solution.continuousSubarrays(*[[21]]) == 1
assert my_solution.continuousSubarrays(*[[34, 34, 33, 34, 33, 33, 32, 31, 30, 31]]) == 39
assert my_solution.continuousSubarrays(*[[58, 59, 59, 58, 59]]) == 15
assert my_solution.continuousSubarrays(*[[10, 9, 8, 7, 8, 9, 9]]) == 24
assert my_solution.continuousSubarrays(*[[65, 66, 65, 64, 63, 62, 62]]) == 20
assert my_solution.continuousSubarrays(*[[65, 65, 64, 65, 66, 65]]) == 21
assert my_solution.continuousSubarrays(*[[85, 84, 83, 84, 83, 82]]) == 20
assert my_solution.continuousSubarrays(*[[60, 59, 60]]) == 6
assert my_solution.continuousSubarrays(*[[96, 97, 98]]) == 6
assert my_solution.continuousSubarrays(*[[21, 22, 23, 22, 23]]) == 15
assert my_solution.continuousSubarrays(*[[76, 77, 77, 78, 77, 78, 78]]) == 28
assert my_solution.continuousSubarrays(*[[27, 27, 27, 26, 26, 27, 27, 27, 27]]) == 45
