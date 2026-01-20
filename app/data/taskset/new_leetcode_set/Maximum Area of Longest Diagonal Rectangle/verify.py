
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.areaOfMaxDiagonal(*[[[9, 3], [8, 6]]]) == 48
assert my_solution.areaOfMaxDiagonal(*[[[3, 4], [4, 3]]]) == 12
assert my_solution.areaOfMaxDiagonal(*[[[4, 10], [4, 9], [9, 3], [10, 8]]]) == 80
assert my_solution.areaOfMaxDiagonal(*[[[2, 6], [5, 1], [3, 10], [8, 4]]]) == 30
assert my_solution.areaOfMaxDiagonal(*[[[3, 7], [2, 10], [3, 4], [9, 9], [5, 10]]]) == 81
assert my_solution.areaOfMaxDiagonal(*[[[10, 4]]]) == 40
assert my_solution.areaOfMaxDiagonal(*[[[9, 9], [1, 8], [10, 5], [2, 8], [6, 3], [7, 1]]]) == 81
assert my_solution.areaOfMaxDiagonal(*[[[10, 3], [5, 9], [8, 3]]]) == 30
assert my_solution.areaOfMaxDiagonal(*[[[2, 7], [3, 2], [3, 3], [10, 4], [5, 3], [8, 10], [8, 8], [4, 7]]]) == 80
assert my_solution.areaOfMaxDiagonal(*[[[1, 10], [3, 10], [4, 4], [2, 6], [6, 3], [6, 4], [9, 1], [6, 1], [2, 3]]]) == 30
assert my_solution.areaOfMaxDiagonal(*[[[4, 7], [10, 10], [3, 7], [9, 1], [5, 7], [3, 9], [10, 4], [4, 8]]]) == 100
assert my_solution.areaOfMaxDiagonal(*[[[1, 1], [6, 8], [6, 9], [7, 2], [6, 8], [1, 3], [3, 1], [1, 9]]]) == 54
assert my_solution.areaOfMaxDiagonal(*[[[6, 6], [1, 3], [8, 10], [10, 1], [3, 10], [7, 7], [10, 8]]]) == 80
assert my_solution.areaOfMaxDiagonal(*[[[6, 5], [8, 6], [2, 10], [8, 1], [9, 2], [3, 5], [3, 5]]]) == 20
assert my_solution.areaOfMaxDiagonal(*[[[5, 1], [4, 9], [9, 1], [5, 8], [2, 9], [3, 2], [10, 10], [5, 2]]]) == 100
assert my_solution.areaOfMaxDiagonal(*[[[8, 3], [9, 10], [7, 7], [6, 5], [6, 9], [9, 10], [5, 10]]]) == 90
assert my_solution.areaOfMaxDiagonal(*[[[6, 10], [8, 6], [10, 1], [7, 10], [10, 10], [9, 5]]]) == 100
assert my_solution.areaOfMaxDiagonal(*[[[9, 5], [9, 2], [2, 2], [8, 9], [5, 7], [8, 10], [3, 5]]]) == 80
assert my_solution.areaOfMaxDiagonal(*[[[3, 9], [9, 5]]]) == 45
assert my_solution.areaOfMaxDiagonal(*[[[10, 10], [5, 5], [3, 2], [2, 6], [3, 1], [10, 7], [4, 8], [7, 9], [9, 9], [1, 2]]]) == 100
