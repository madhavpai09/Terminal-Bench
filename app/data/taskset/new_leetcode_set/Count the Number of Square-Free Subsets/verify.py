
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.squareFreeSubsets(*[[3, 4, 4, 5]]) == 3
assert my_solution.squareFreeSubsets(*[[1]]) == 1
assert my_solution.squareFreeSubsets(*[[11, 2, 19, 7, 9, 27]]) == 15
assert my_solution.squareFreeSubsets(*[[26, 6, 4, 27, 6, 18]]) == 3
assert my_solution.squareFreeSubsets(*[[9, 13, 19, 23, 7, 27]]) == 15
assert my_solution.squareFreeSubsets(*[[17, 27, 20, 1, 19]]) == 7
assert my_solution.squareFreeSubsets(*[[8, 11, 17, 2, 25, 29, 21, 20, 4, 22]]) == 39
assert my_solution.squareFreeSubsets(*[[11, 14, 25, 18, 29, 16]]) == 7
assert my_solution.squareFreeSubsets(*[[10, 15, 6, 25]]) == 3
assert my_solution.squareFreeSubsets(*[[26, 21, 2, 6, 19, 9, 29]]) == 27
assert my_solution.squareFreeSubsets(*[[25, 16, 6, 18, 5]]) == 3
assert my_solution.squareFreeSubsets(*[[16, 3, 6, 6, 20, 9, 15, 30, 22, 15]]) == 10
assert my_solution.squareFreeSubsets(*[[22, 2, 5, 26, 28, 8, 4, 11, 12, 17, 11, 3, 19, 29, 19, 7, 24, 12, 22, 5, 8, 22]]) == 1727
assert my_solution.squareFreeSubsets(*[[1, 2, 6, 15, 7, 19, 6, 29, 28, 24, 21, 25, 25, 18, 9, 6, 20, 21, 8, 24, 14, 19, 24, 28, 30, 27, 13, 21, 1, 23, 13, 29, 24, 29, 18, 7]]) == 9215
assert my_solution.squareFreeSubsets(*[[15, 15, 25, 2, 12, 22, 28, 11, 28, 13, 26, 12, 1, 5]]) == 95
assert my_solution.squareFreeSubsets(*[[1, 24, 2, 16, 18, 3, 26, 29, 16, 6, 1, 28, 18, 14, 12, 1, 16, 20, 27, 6, 22]]) == 191
assert my_solution.squareFreeSubsets(*[[13, 21, 20, 11, 6, 19, 1, 20, 27, 25, 25, 23, 14, 24, 16, 13, 11, 27, 16, 4, 21, 30]]) == 431
assert my_solution.squareFreeSubsets(*[[23, 15, 17, 5, 5, 9, 12, 20, 2, 4, 10, 9, 27, 16, 23, 9, 8, 17, 9]]) == 80
assert my_solution.squareFreeSubsets(*[[3, 5, 21, 20, 10, 2, 29, 18, 28, 1, 29, 15, 18, 3, 22, 19, 3, 14, 22, 15, 18, 13, 12, 26, 12, 26, 17, 10, 6, 19, 21, 14, 10, 26, 18, 19, 20, 28, 12, 12, 15, 28, 19, 13, 20, 17]]) == 31589
assert my_solution.squareFreeSubsets(*[[20, 12, 1, 21, 20, 19, 9, 14, 17, 17, 27, 28, 3, 16, 29, 22, 24, 9, 16, 6, 10, 4, 30, 3, 17, 13, 20, 9, 3, 22, 5, 30, 17, 24, 17, 21, 10, 20, 19, 23, 21]]) == 19583
