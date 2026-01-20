
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.canSplitArray(*[[2, 2, 1], 4]) == True
assert my_solution.canSplitArray(*[[2, 1, 3], 5]) == False
assert my_solution.canSplitArray(*[[2, 3, 3, 2, 3], 6]) == True
assert my_solution.canSplitArray(*[[1], 1]) == True
assert my_solution.canSplitArray(*[[2], 1]) == True
assert my_solution.canSplitArray(*[[3], 1]) == True
assert my_solution.canSplitArray(*[[1], 2]) == True
assert my_solution.canSplitArray(*[[2], 2]) == True
assert my_solution.canSplitArray(*[[3], 2]) == True
assert my_solution.canSplitArray(*[[3], 3]) == True
assert my_solution.canSplitArray(*[[7], 5]) == True
assert my_solution.canSplitArray(*[[4], 7]) == True
assert my_solution.canSplitArray(*[[9], 7]) == True
assert my_solution.canSplitArray(*[[2], 8]) == True
assert my_solution.canSplitArray(*[[4], 8]) == True
assert my_solution.canSplitArray(*[[10], 11]) == True
assert my_solution.canSplitArray(*[[6], 12]) == True
assert my_solution.canSplitArray(*[[2], 14]) == True
assert my_solution.canSplitArray(*[[3], 18]) == True
assert my_solution.canSplitArray(*[[9, 7], 1]) == True
