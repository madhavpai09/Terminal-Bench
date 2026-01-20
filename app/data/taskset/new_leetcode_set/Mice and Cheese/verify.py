
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.miceAndCheese(*[[1, 1, 3, 4], [4, 4, 1, 1], 2]) == 15
assert my_solution.miceAndCheese(*[[1, 1], [1, 1], 2]) == 2
assert my_solution.miceAndCheese(*[[2, 1], [1, 2], 1]) == 4
assert my_solution.miceAndCheese(*[[3, 3], [3, 5], 1]) == 8
assert my_solution.miceAndCheese(*[[4, 1, 5, 3, 3], [3, 4, 4, 5, 2], 3]) == 21
assert my_solution.miceAndCheese(*[[1, 4, 4, 6, 4], [6, 5, 3, 6, 1], 1]) == 24
assert my_solution.miceAndCheese(*[[1, 2, 1, 2, 1, 2], [2, 1, 1, 2, 2, 1], 0]) == 9
assert my_solution.miceAndCheese(*[[2, 2, 1, 2], [1, 2, 1, 2], 2]) == 7
assert my_solution.miceAndCheese(*[[1], [4], 1]) == 1
assert my_solution.miceAndCheese(*[[1, 2, 2], [2, 1, 2], 2]) == 6
assert my_solution.miceAndCheese(*[[3, 1, 1, 3], [3, 2, 3, 1], 3]) == 10
assert my_solution.miceAndCheese(*[[4], [5], 0]) == 5
assert my_solution.miceAndCheese(*[[2, 3], [3, 3], 2]) == 5
assert my_solution.miceAndCheese(*[[1, 1], [1, 1], 1]) == 2
assert my_solution.miceAndCheese(*[[1, 3], [5, 4], 1]) == 8
assert my_solution.miceAndCheese(*[[2, 1, 4], [1, 4, 2], 0]) == 7
assert my_solution.miceAndCheese(*[[3, 4, 2, 1, 5], [2, 3, 5, 2, 4], 0]) == 16
assert my_solution.miceAndCheese(*[[5, 2], [3, 1], 2]) == 7
assert my_solution.miceAndCheese(*[[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], 5]) == 5
assert my_solution.miceAndCheese(*[[2, 2, 1, 2, 1], [1, 1, 2, 1, 1], 0]) == 6
