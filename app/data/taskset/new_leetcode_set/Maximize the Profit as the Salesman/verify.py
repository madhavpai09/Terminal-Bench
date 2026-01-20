
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.maximizeTheProfit(*[5, [[0, 0, 1], [0, 2, 2], [1, 3, 2]]]) == 3
assert my_solution.maximizeTheProfit(*[5, [[0, 0, 1], [0, 2, 10], [1, 3, 2]]]) == 10
assert my_solution.maximizeTheProfit(*[4, [[1, 3, 10], [1, 3, 3], [0, 0, 1], [0, 0, 7]]]) == 17
assert my_solution.maximizeTheProfit(*[4, [[0, 0, 6], [1, 2, 8], [0, 3, 7], [2, 2, 5], [0, 1, 5], [2, 3, 2], [0, 2, 8], [2, 3, 10], [0, 3, 2]]]) == 16
assert my_solution.maximizeTheProfit(*[15, [[5, 5, 10], [2, 6, 6], [8, 11, 5], [7, 11, 9], [2, 4, 1], [3, 8, 5], [0, 6, 9], [0, 10, 5], [5, 10, 8], [4, 5, 1]]]) == 20
assert my_solution.maximizeTheProfit(*[10, [[1, 6, 1], [0, 1, 10], [3, 6, 2], [0, 5, 10], [0, 0, 3], [0, 0, 4], [1, 1, 4], [0, 6, 7], [4, 4, 1]]]) == 12
assert my_solution.maximizeTheProfit(*[11, [[7, 8, 6], [6, 6, 4], [4, 6, 9], [6, 7, 4], [5, 5, 8], [1, 5, 9], [7, 7, 8], [1, 2, 5], [0, 2, 9], [1, 3, 8], [0, 2, 7], [2, 2, 8]]]) == 29
assert my_solution.maximizeTheProfit(*[3, [[0, 0, 6], [0, 1, 8], [1, 2, 1], [0, 1, 4], [0, 1, 2], [0, 0, 7], [0, 0, 6], [0, 0, 5]]]) == 8
assert my_solution.maximizeTheProfit(*[4, [[0, 1, 9], [1, 1, 4]]]) == 9
assert my_solution.maximizeTheProfit(*[11, [[1, 10, 6], [1, 10, 5], [0, 2, 7], [0, 0, 8], [8, 10, 7]]]) == 15
assert my_solution.maximizeTheProfit(*[3, [[0, 1, 8], [1, 1, 6], [2, 2, 7], [0, 2, 6], [0, 2, 2], [0, 0, 6], [0, 0, 9], [0, 1, 4]]]) == 22
assert my_solution.maximizeTheProfit(*[6, [[0, 2, 4]]]) == 4
assert my_solution.maximizeTheProfit(*[10, [[5, 9, 3], [1, 5, 8], [0, 0, 6], [5, 8, 10]]]) == 16
assert my_solution.maximizeTheProfit(*[5, [[1, 1, 3], [1, 1, 3], [0, 0, 8], [1, 3, 8], [0, 2, 1], [3, 3, 9], [0, 0, 7], [0, 2, 3], [0, 0, 5], [0, 3, 10], [1, 3, 10], [4, 4, 6], [0, 1, 1], [2, 4, 10]]]) == 26
assert my_solution.maximizeTheProfit(*[13, [[2, 2, 5], [1, 8, 10], [2, 3, 3]]]) == 10
assert my_solution.maximizeTheProfit(*[2, [[1, 1, 8], [1, 1, 8], [1, 1, 10], [1, 1, 7], [0, 0, 7], [0, 0, 3], [0, 1, 8], [0, 0, 4], [0, 0, 4], [0, 0, 7], [0, 0, 10], [0, 1, 4], [1, 1, 1], [0, 1, 5]]]) == 20
assert my_solution.maximizeTheProfit(*[3, [[0, 1, 7], [1, 1, 3], [0, 0, 2], [1, 1, 6], [0, 0, 10], [1, 1, 7], [0, 2, 3], [0, 1, 2], [0, 0, 7]]]) == 17
assert my_solution.maximizeTheProfit(*[5, [[0, 0, 5], [1, 3, 9], [0, 2, 2], [1, 1, 6], [1, 2, 10], [0, 2, 10], [1, 1, 3]]]) == 15
assert my_solution.maximizeTheProfit(*[10, [[0, 1, 9], [5, 6, 10], [1, 3, 8], [1, 9, 7], [7, 8, 1], [2, 7, 1], [0, 8, 7], [1, 6, 6], [1, 4, 4], [0, 5, 4], [0, 0, 3], [0, 8, 6]]]) == 22
assert my_solution.maximizeTheProfit(*[4, [[0, 0, 1], [0, 0, 10], [0, 2, 1], [0, 0, 6], [0, 3, 10], [0, 1, 5], [1, 2, 10], [0, 0, 2], [3, 3, 1], [0, 0, 9], [0, 1, 2], [0, 0, 4], [1, 3, 5], [1, 1, 1]]]) == 21
