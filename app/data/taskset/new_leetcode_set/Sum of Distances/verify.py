
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.distance(*[[1, 3, 1, 1, 2]]) == [5, 0, 3, 4, 0]
assert my_solution.distance(*[[0, 5, 3]]) == [0, 0, 0]
assert my_solution.distance(*[[2, 0, 2, 2, 6, 5, 2]]) == [11, 0, 7, 7, 0, 0, 13]
assert my_solution.distance(*[[0, 5, 3, 1, 2, 8, 6, 6, 6]]) == [0, 0, 0, 0, 0, 0, 3, 2, 3]
assert my_solution.distance(*[[1]]) == [0]
assert my_solution.distance(*[[6, 1, 3, 3, 4, 3, 4]]) == [0, 0, 4, 3, 2, 5, 2]
assert my_solution.distance(*[[3, 2, 0, 2]]) == [0, 2, 0, 2]
assert my_solution.distance(*[[2, 7, 2, 5, 2, 5, 4]]) == [6, 0, 4, 2, 6, 2, 0]
assert my_solution.distance(*[[3, 3, 0, 2]]) == [1, 1, 0, 0]
assert my_solution.distance(*[[1, 2, 4, 2]]) == [0, 2, 0, 2]
assert my_solution.distance(*[[1, 5, 2, 2]]) == [0, 0, 1, 1]
assert my_solution.distance(*[[0, 6, 3, 1, 0, 1, 2]]) == [4, 0, 0, 2, 4, 2, 0]
assert my_solution.distance(*[[0, 1]]) == [0, 0]
assert my_solution.distance(*[[0]]) == [0]
assert my_solution.distance(*[[1, 2, 2, 3, 3, 0]]) == [0, 1, 1, 1, 1, 0]
assert my_solution.distance(*[[7, 9, 4, 0, 2, 2, 0, 8, 5]]) == [0, 0, 0, 3, 1, 1, 3, 0, 0]
assert my_solution.distance(*[[5, 5, 3, 2, 5, 5]]) == [10, 8, 0, 0, 8, 10]
assert my_solution.distance(*[[4, 2, 3, 3, 8, 3]]) == [0, 0, 4, 3, 0, 5]
assert my_solution.distance(*[[3, 0, 3, 5, 0, 0, 7, 7]]) == [2, 7, 2, 0, 4, 5, 1, 1]
assert my_solution.distance(*[[7, 4, 9, 1, 8, 5, 5, 7, 2, 6, 5]]) == [7, 0, 0, 0, 0, 6, 5, 7, 0, 0, 9]
