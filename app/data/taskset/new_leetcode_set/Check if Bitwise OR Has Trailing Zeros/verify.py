
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.hasTrailingZeros(*[[1, 2, 3, 4, 5]]) == True
assert my_solution.hasTrailingZeros(*[[2, 4, 8, 16]]) == True
assert my_solution.hasTrailingZeros(*[[1, 3, 5, 7, 9]]) == False
assert my_solution.hasTrailingZeros(*[[1, 2]]) == False
assert my_solution.hasTrailingZeros(*[[1, 3]]) == False
assert my_solution.hasTrailingZeros(*[[1, 7]]) == False
assert my_solution.hasTrailingZeros(*[[2, 2]]) == True
assert my_solution.hasTrailingZeros(*[[3, 3]]) == False
assert my_solution.hasTrailingZeros(*[[3, 4]]) == False
assert my_solution.hasTrailingZeros(*[[3, 9]]) == False
assert my_solution.hasTrailingZeros(*[[4, 3]]) == False
assert my_solution.hasTrailingZeros(*[[4, 8]]) == True
assert my_solution.hasTrailingZeros(*[[4, 32]]) == True
assert my_solution.hasTrailingZeros(*[[5, 6]]) == False
assert my_solution.hasTrailingZeros(*[[6, 2]]) == True
assert my_solution.hasTrailingZeros(*[[6, 8]]) == True
assert my_solution.hasTrailingZeros(*[[7, 9]]) == False
assert my_solution.hasTrailingZeros(*[[7, 10]]) == False
assert my_solution.hasTrailingZeros(*[[8, 2]]) == True
assert my_solution.hasTrailingZeros(*[[8, 4]]) == True
