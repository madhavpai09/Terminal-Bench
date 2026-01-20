
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.numberOfPoints(*[[[3, 6], [1, 5], [4, 7]]]) == 7
assert my_solution.numberOfPoints(*[[[1, 3], [5, 8]]]) == 7
assert my_solution.numberOfPoints(*[[[4, 4], [9, 10], [9, 10], [3, 8]]]) == 8
assert my_solution.numberOfPoints(*[[[2, 5], [3, 8], [1, 6], [4, 10]]]) == 10
assert my_solution.numberOfPoints(*[[[2, 3], [3, 9], [5, 7], [4, 10], [9, 10]]]) == 9
assert my_solution.numberOfPoints(*[[[4, 10]]]) == 7
assert my_solution.numberOfPoints(*[[[1, 9], [2, 10], [6, 7], [8, 9], [5, 8], [1, 3]]]) == 10
assert my_solution.numberOfPoints(*[[[5, 10], [3, 8], [3, 9]]]) == 8
assert my_solution.numberOfPoints(*[[[2, 3], [3, 10], [5, 8], [4, 8], [2, 7], [3, 4], [3, 10], [7, 8]]]) == 9
assert my_solution.numberOfPoints(*[[[1, 3], [2, 4], [6, 6], [6, 9], [2, 10], [4, 10], [3, 6], [1, 4], [1, 3]]]) == 10
assert my_solution.numberOfPoints(*[[[4, 10], [3, 9], [3, 5], [4, 10], [7, 10], [1, 7], [7, 9], [4, 8]]]) == 10
assert my_solution.numberOfPoints(*[[[1, 6], [6, 7], [1, 6], [1, 3], [1, 8], [2, 9], [3, 8], [1, 9]]]) == 9
assert my_solution.numberOfPoints(*[[[1, 6], [8, 10], [3, 7], [6, 10], [3, 10], [1, 10], [7, 8]]]) == 10
assert my_solution.numberOfPoints(*[[[6, 8], [2, 8], [3, 9], [3, 5], [6, 10], [1, 2], [5, 5]]]) == 10
assert my_solution.numberOfPoints(*[[[4, 5], [5, 9], [2, 3], [5, 10], [1, 9], [1, 8], [2, 9], [2, 10]]]) == 10
assert my_solution.numberOfPoints(*[[[8, 9], [6, 7], [6, 9], [3, 5], [7, 10], [5, 9], [10, 10]]]) == 8
assert my_solution.numberOfPoints(*[[[6, 8], [7, 10], [9, 10], [6, 10], [1, 10], [5, 10]]]) == 10
assert my_solution.numberOfPoints(*[[[9, 9], [2, 8], [5, 8], [3, 5], [2, 2], [7, 9], [5, 10]]]) == 9
assert my_solution.numberOfPoints(*[[[3, 9], [5, 9]]]) == 7
assert my_solution.numberOfPoints(*[[[5, 10], [2, 3], [3, 10], [4, 7], [1, 9], [5, 10], [2, 6], [1, 7], [8, 9], [2, 9]]]) == 10
