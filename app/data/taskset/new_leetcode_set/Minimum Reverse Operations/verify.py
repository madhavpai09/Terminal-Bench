
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.minReverseOperations(*[4, 0, [1, 2], 4]) == [0, -1, -1, 1]
assert my_solution.minReverseOperations(*[5, 0, [2, 4], 3]) == [0, -1, -1, -1, -1]
assert my_solution.minReverseOperations(*[4, 2, [0, 1, 3], 1]) == [-1, -1, 0, -1]
assert my_solution.minReverseOperations(*[5, 0, [], 2]) == [0, 1, 2, 3, 4]
assert my_solution.minReverseOperations(*[1, 0, [], 1]) == [0]
assert my_solution.minReverseOperations(*[2, 0, [], 1]) == [0, -1]
assert my_solution.minReverseOperations(*[2, 0, [], 2]) == [0, 1]
assert my_solution.minReverseOperations(*[2, 1, [], 1]) == [-1, 0]
assert my_solution.minReverseOperations(*[2, 1, [], 2]) == [1, 0]
assert my_solution.minReverseOperations(*[2, 0, [1], 1]) == [0, -1]
assert my_solution.minReverseOperations(*[2, 0, [1], 2]) == [0, -1]
assert my_solution.minReverseOperations(*[2, 1, [0], 1]) == [-1, 0]
assert my_solution.minReverseOperations(*[2, 1, [0], 2]) == [-1, 0]
assert my_solution.minReverseOperations(*[3, 0, [], 1]) == [0, -1, -1]
assert my_solution.minReverseOperations(*[3, 0, [], 2]) == [0, 1, 2]
assert my_solution.minReverseOperations(*[3, 0, [], 3]) == [0, -1, 1]
assert my_solution.minReverseOperations(*[3, 1, [], 1]) == [-1, 0, -1]
assert my_solution.minReverseOperations(*[3, 1, [], 2]) == [1, 0, 1]
assert my_solution.minReverseOperations(*[3, 1, [], 3]) == [-1, 0, -1]
assert my_solution.minReverseOperations(*[3, 2, [], 1]) == [-1, -1, 0]
