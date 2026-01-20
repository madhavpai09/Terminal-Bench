
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.numberGame(*[[5, 4, 2, 3]]) == [3, 2, 5, 4]
assert my_solution.numberGame(*[[2, 5]]) == [5, 2]
assert my_solution.numberGame(*[[4, 4, 3, 8]]) == [4, 3, 8, 4]
assert my_solution.numberGame(*[[2, 5, 3, 8]]) == [3, 2, 8, 5]
assert my_solution.numberGame(*[[2, 7, 9, 6, 4, 6]]) == [4, 2, 6, 6, 9, 7]
assert my_solution.numberGame(*[[18, 26, 37, 46, 13, 33, 39, 1, 37, 16]]) == [13, 1, 18, 16, 33, 26, 37, 37, 46, 39]
assert my_solution.numberGame(*[[17, 2, 4, 11, 14, 18]]) == [4, 2, 14, 11, 18, 17]
assert my_solution.numberGame(*[[20, 30, 12, 3, 11, 17, 32, 12]]) == [11, 3, 12, 12, 20, 17, 32, 30]
assert my_solution.numberGame(*[[9, 32, 6, 11, 11, 39, 18, 29, 44, 29]]) == [9, 6, 11, 11, 29, 18, 32, 29, 44, 39]
assert my_solution.numberGame(*[[7, 2, 3, 4]]) == [3, 2, 7, 4]
assert my_solution.numberGame(*[[8, 7, 1, 3]]) == [3, 1, 8, 7]
assert my_solution.numberGame(*[[2, 6, 6, 6]]) == [6, 2, 6, 6]
assert my_solution.numberGame(*[[1, 2]]) == [2, 1]
assert my_solution.numberGame(*[[4, 1, 1, 3]]) == [1, 1, 4, 3]
assert my_solution.numberGame(*[[13, 12, 18, 11, 15, 28, 26, 2]]) == [11, 2, 13, 12, 18, 15, 28, 26]
assert my_solution.numberGame(*[[14, 30, 29, 3, 23, 21, 26, 23]]) == [14, 3, 23, 21, 26, 23, 30, 29]
assert my_solution.numberGame(*[[1, 1]]) == [1, 1]
assert my_solution.numberGame(*[[2, 1]]) == [2, 1]
assert my_solution.numberGame(*[[12, 1, 28, 23, 2, 31, 11, 26]]) == [2, 1, 12, 11, 26, 23, 31, 28]
assert my_solution.numberGame(*[[21, 11, 37, 1, 40, 50, 49, 45, 28, 47]]) == [11, 1, 28, 21, 40, 37, 47, 45, 50, 49]
