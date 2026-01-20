
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.findMatrix(*[[1, 3, 4, 1, 2, 3, 1]]) == [[1, 3, 4, 2], [1, 3], [1]]
assert my_solution.findMatrix(*[[2, 1, 1]]) == [[1, 2], [1]]
assert my_solution.findMatrix(*[[4, 5, 3, 3, 3]]) == [[3, 5, 4], [3], [3]]
assert my_solution.findMatrix(*[[9, 8, 8, 4, 9, 8, 8, 3, 9]]) == [[8, 9, 4, 3], [8, 9], [8, 9], [8]]
assert my_solution.findMatrix(*[[8, 8, 8, 8, 2, 4, 4, 2, 4]]) == [[8, 4, 2], [8, 4, 2], [8, 4], [8]]
assert my_solution.findMatrix(*[[2, 2]]) == [[2], [2]]
assert my_solution.findMatrix(*[[3, 5, 3, 3, 8, 3, 2, 5]]) == [[3, 5, 8, 2], [3, 5], [3], [3]]
assert my_solution.findMatrix(*[[4, 4, 4, 4, 2]]) == [[4, 2], [4], [4], [4]]
assert my_solution.findMatrix(*[[3, 1, 2, 1, 3]]) == [[3, 1, 2], [3, 1]]
assert my_solution.findMatrix(*[[9, 9, 9, 9, 3, 9, 2, 9, 1]]) == [[9, 3, 2, 1], [9], [9], [9], [9], [9]]
assert my_solution.findMatrix(*[[3, 3, 4, 3]]) == [[3, 4], [3], [3]]
assert my_solution.findMatrix(*[[3, 3, 2, 1]]) == [[3, 2, 1], [3]]
assert my_solution.findMatrix(*[[1, 1]]) == [[1], [1]]
assert my_solution.findMatrix(*[[3, 3, 3]]) == [[3], [3], [3]]
assert my_solution.findMatrix(*[[6, 4, 6, 4, 3, 3, 6, 2]]) == [[6, 4, 3, 2], [6, 4, 3], [6]]
assert my_solution.findMatrix(*[[2, 3, 1, 2]]) == [[2, 3, 1], [2]]
assert my_solution.findMatrix(*[[8, 7, 8, 8, 1, 8, 8, 7, 9]]) == [[8, 7, 9, 1], [8, 7], [8], [8], [8]]
assert my_solution.findMatrix(*[[7, 7, 7, 7, 7, 7, 7, 7]]) == [[7], [7], [7], [7], [7], [7], [7], [7]]
assert my_solution.findMatrix(*[[2, 6, 3, 3, 2, 3, 2, 2, 3]]) == [[3, 2, 6], [3, 2], [3, 2], [3, 2]]
assert my_solution.findMatrix(*[[1, 2, 2, 1]]) == [[2, 1], [2, 1]]
