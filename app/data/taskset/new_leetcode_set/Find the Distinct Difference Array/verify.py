
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.distinctDifferenceArray(*[[1, 2, 3, 4, 5]]) == [-3, -1, 1, 3, 5]
assert my_solution.distinctDifferenceArray(*[[3, 2, 3, 4, 2]]) == [-2, -1, 0, 2, 3]
assert my_solution.distinctDifferenceArray(*[[16]]) == [1]
assert my_solution.distinctDifferenceArray(*[[16, 16]]) == [0, 1]
assert my_solution.distinctDifferenceArray(*[[13, 13, 13]]) == [0, 0, 1]
assert my_solution.distinctDifferenceArray(*[[36, 36, 36, 36]]) == [0, 0, 0, 1]
assert my_solution.distinctDifferenceArray(*[[40, 40, 40, 40, 40]]) == [0, 0, 0, 0, 1]
assert my_solution.distinctDifferenceArray(*[[37, 37, 37, 37, 33]]) == [-1, -1, -1, 0, 2]
assert my_solution.distinctDifferenceArray(*[[42, 42, 42, 42, 47]]) == [-1, -1, -1, 0, 2]
assert my_solution.distinctDifferenceArray(*[[9, 9, 9, 9, 31]]) == [-1, -1, -1, 0, 2]
assert my_solution.distinctDifferenceArray(*[[14, 14, 14, 14, 5]]) == [-1, -1, -1, 0, 2]
assert my_solution.distinctDifferenceArray(*[[41, 41, 41, 17]]) == [-1, -1, 0, 2]
assert my_solution.distinctDifferenceArray(*[[9, 9, 9, 30, 9]]) == [-1, -1, -1, 1, 2]
assert my_solution.distinctDifferenceArray(*[[21, 21, 21, 4, 4]]) == [-1, -1, 0, 1, 2]
assert my_solution.distinctDifferenceArray(*[[38, 38, 38, 14, 19]]) == [-2, -2, -1, 1, 3]
assert my_solution.distinctDifferenceArray(*[[11, 11, 11, 7, 13]]) == [-2, -2, -1, 1, 3]
assert my_solution.distinctDifferenceArray(*[[36, 36, 36, 18, 27]]) == [-2, -2, -1, 1, 3]
assert my_solution.distinctDifferenceArray(*[[37, 37, 37, 47]]) == [-1, -1, 0, 2]
assert my_solution.distinctDifferenceArray(*[[13, 13, 13, 34, 13]]) == [-1, -1, -1, 1, 2]
assert my_solution.distinctDifferenceArray(*[[39, 39, 39, 38, 1]]) == [-2, -2, -1, 1, 3]
