
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.getSubarrayBeauty(*[[1, -1, -3, -2, 3], 3, 2]) == [-1, -2, -2]
assert my_solution.getSubarrayBeauty(*[[-1, -2, -3, -4, -5], 2, 2]) == [-1, -2, -3, -4]
assert my_solution.getSubarrayBeauty(*[[-3, 1, 2, -3, 0, -3], 2, 1]) == [-3, 0, -3, -3, -3]
assert my_solution.getSubarrayBeauty(*[[-43], 1, 1]) == [-43]
assert my_solution.getSubarrayBeauty(*[[-26], 1, 1]) == [-26]
assert my_solution.getSubarrayBeauty(*[[-22], 1, 1]) == [-22]
assert my_solution.getSubarrayBeauty(*[[-20], 1, 1]) == [-20]
assert my_solution.getSubarrayBeauty(*[[-19], 1, 1]) == [-19]
assert my_solution.getSubarrayBeauty(*[[-18], 1, 1]) == [-18]
assert my_solution.getSubarrayBeauty(*[[-17], 1, 1]) == [-17]
assert my_solution.getSubarrayBeauty(*[[-15], 1, 1]) == [-15]
assert my_solution.getSubarrayBeauty(*[[-2], 1, 1]) == [-2]
assert my_solution.getSubarrayBeauty(*[[5], 1, 1]) == [0]
assert my_solution.getSubarrayBeauty(*[[7], 1, 1]) == [0]
assert my_solution.getSubarrayBeauty(*[[14], 1, 1]) == [0]
assert my_solution.getSubarrayBeauty(*[[16], 1, 1]) == [0]
assert my_solution.getSubarrayBeauty(*[[19], 1, 1]) == [0]
assert my_solution.getSubarrayBeauty(*[[20], 1, 1]) == [0]
assert my_solution.getSubarrayBeauty(*[[23], 1, 1]) == [0]
assert my_solution.getSubarrayBeauty(*[[27], 1, 1]) == [0]
