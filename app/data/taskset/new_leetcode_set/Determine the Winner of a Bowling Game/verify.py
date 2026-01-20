
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.isWinner(*[[4, 10, 7, 9], [6, 5, 2, 3]]) == 1
assert my_solution.isWinner(*[[3, 5, 7, 6], [8, 10, 10, 2]]) == 2
assert my_solution.isWinner(*[[2, 3], [4, 1]]) == 0
assert my_solution.isWinner(*[[0, 4, 7, 2, 0], [2, 3, 3, 0, 1]]) == 1
assert my_solution.isWinner(*[[5, 6, 1, 10], [5, 1, 10, 5]]) == 2
assert my_solution.isWinner(*[[0, 9, 2, 0], [4, 6, 9, 1]]) == 2
assert my_solution.isWinner(*[[7, 3, 6, 7], [4, 2, 6, 7]]) == 1
assert my_solution.isWinner(*[[6, 10, 4], [5, 9, 2]]) == 1
assert my_solution.isWinner(*[[9, 8, 5, 3, 7], [8, 7, 4, 9, 0]]) == 1
assert my_solution.isWinner(*[[2, 8, 10, 6], [8, 0, 4, 2]]) == 1
assert my_solution.isWinner(*[[3, 2, 6, 6, 2], [1, 4, 5, 2, 5]]) == 1
assert my_solution.isWinner(*[[0, 1, 8], [3, 9, 1]]) == 2
assert my_solution.isWinner(*[[5, 2, 4, 2, 0], [6, 1, 5, 2, 6]]) == 2
assert my_solution.isWinner(*[[3, 6, 9], [0, 7, 4]]) == 1
assert my_solution.isWinner(*[[1, 2, 7, 6], [6, 7, 0, 0]]) == 1
assert my_solution.isWinner(*[[7, 5, 10, 5], [2, 5, 7, 10]]) == 1
assert my_solution.isWinner(*[[9, 6, 10, 0], [4, 4, 0, 5]]) == 1
assert my_solution.isWinner(*[[7, 1, 3, 10], [10, 9, 0, 9]]) == 2
assert my_solution.isWinner(*[[7], [8]]) == 2
assert my_solution.isWinner(*[[1, 3, 0], [2, 0, 0]]) == 1
