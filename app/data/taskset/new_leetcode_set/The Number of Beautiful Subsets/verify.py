
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.beautifulSubsets(*[[2, 4, 6], 2]) == 4
assert my_solution.beautifulSubsets(*[[1], 1]) == 1
assert my_solution.beautifulSubsets(*[[4, 2, 5, 9, 10, 3], 1]) == 23
assert my_solution.beautifulSubsets(*[[10, 4, 5, 7, 2, 1], 3]) == 23
assert my_solution.beautifulSubsets(*[[9, 5, 7, 10, 6, 2], 9]) == 63
assert my_solution.beautifulSubsets(*[[10, 1, 4, 3, 5], 1]) == 19
assert my_solution.beautifulSubsets(*[[10, 2, 6, 4, 5, 7, 3, 9, 1, 8], 3]) == 199
assert my_solution.beautifulSubsets(*[[30, 22, 15, 25, 7, 23, 27], 14]) == 127
assert my_solution.beautifulSubsets(*[[3, 6, 7, 5, 23, 19, 16, 13, 17, 2], 5]) == 767
assert my_solution.beautifulSubsets(*[[26, 28, 8, 4, 11], 12]) == 31
assert my_solution.beautifulSubsets(*[[17, 11, 3, 19, 29], 19]) == 31
assert my_solution.beautifulSubsets(*[[7, 24, 12, 22, 5, 8, 27, 1, 2, 6], 15]) == 575
assert my_solution.beautifulSubsets(*[[7, 19, 6, 29], 28]) == 15
assert my_solution.beautifulSubsets(*[[24, 21, 25, 18, 9], 6]) == 23
assert my_solution.beautifulSubsets(*[[20, 21, 8, 24, 14], 19]) == 31
assert my_solution.beautifulSubsets(*[[24, 28, 27, 13, 21, 1, 23], 13]) == 127
assert my_solution.beautifulSubsets(*[[29, 24, 18, 7, 15, 26, 2, 12, 22, 11], 28]) == 1023
assert my_solution.beautifulSubsets(*[[16, 6, 1, 14, 12, 18, 8, 10, 3, 11, 7, 19, 20], 19]) == 6143
assert my_solution.beautifulSubsets(*[[1, 14, 16, 13, 11, 19, 8, 2, 18, 15, 9, 3], 5]) == 959
assert my_solution.beautifulSubsets(*[[9, 12, 2, 4, 10, 5, 14, 8, 19, 15], 8]) == 575
