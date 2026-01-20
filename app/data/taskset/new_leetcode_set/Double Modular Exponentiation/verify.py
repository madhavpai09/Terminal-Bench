
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.getGoodIndices(*[[[2, 3, 3, 10], [3, 3, 3, 1], [6, 1, 1, 4]], 2]) == [0, 2]
assert my_solution.getGoodIndices(*[[[39, 3, 1000, 1000]], 17]) == []
assert my_solution.getGoodIndices(*[[[3, 2, 4, 2], [3, 3, 1, 3], [2, 2, 2, 4], [4, 4, 2, 3], [2, 4, 1, 3]], 4]) == []
assert my_solution.getGoodIndices(*[[[9, 2, 8, 5], [7, 8, 8, 8], [8, 9, 6, 1], [8, 6, 2, 2], [3, 6, 3, 1]], 9]) == []
assert my_solution.getGoodIndices(*[[[2, 2, 3, 2], [1, 3, 3, 2], [3, 2, 2, 3], [3, 1, 2, 3], [1, 2, 3, 1], [2, 2, 2, 2], [2, 1, 3, 1], [3, 2, 2, 2], [2, 1, 3, 1], [3, 3, 1, 3]], 0]) == [0, 2, 3, 4, 5, 6, 8]
assert my_solution.getGoodIndices(*[[[1, 3, 2, 3], [4, 2, 3, 3], [4, 1, 4, 4], [4, 2, 3, 1], [4, 2, 1, 1], [1, 2, 4, 1], [1, 1, 4, 2], [1, 4, 4, 3], [1, 2, 2, 3]], 2]) == []
assert my_solution.getGoodIndices(*[[[5, 4, 1, 3], [2, 5, 5, 1], [5, 3, 4, 1]], 5]) == []
assert my_solution.getGoodIndices(*[[[4, 7, 6, 7], [7, 6, 6, 4], [6, 8, 2, 3], [8, 3, 5, 8]], 4]) == []
assert my_solution.getGoodIndices(*[[[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]], 0]) == [0, 1, 2, 3, 4, 5, 6]
assert my_solution.getGoodIndices(*[[[3, 5, 1, 2], [3, 2, 5, 2], [4, 4, 3, 2], [3, 2, 5, 3], [1, 5, 1, 4]], 1]) == [0, 1, 4]
assert my_solution.getGoodIndices(*[[[1, 2, 1, 1], [2, 2, 2, 2], [1, 1, 1, 2], [1, 2, 2, 2]], 2]) == []
assert my_solution.getGoodIndices(*[[[3, 3, 5, 6], [8, 2, 9, 2], [1, 4, 6, 1], [6, 4, 7, 7]], 8]) == []
assert my_solution.getGoodIndices(*[[[3, 5, 4, 3], [1, 3, 3, 1], [3, 3, 5, 5], [4, 5, 5, 5], [5, 1, 4, 3], [2, 5, 3, 4]], 7]) == []
assert my_solution.getGoodIndices(*[[[9, 7, 2, 7], [9, 1, 8, 1], [9, 3, 5, 6], [6, 1, 8, 4], [9, 6, 2, 3]], 8]) == []
assert my_solution.getGoodIndices(*[[[10, 6, 8, 7], [3, 6, 1, 8]], 5]) == []
assert my_solution.getGoodIndices(*[[[4, 6, 5, 2], [2, 6, 4, 6], [4, 6, 3, 6], [2, 2, 6, 5], [6, 5, 5, 2]], 2]) == []
assert my_solution.getGoodIndices(*[[[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]], 1]) == []
assert my_solution.getGoodIndices(*[[[5, 6, 5, 1], [4, 3, 1, 6], [5, 4, 4, 2]], 4]) == [1]
assert my_solution.getGoodIndices(*[[[5, 1, 2, 4], [4, 5, 5, 5], [5, 9, 7, 4], [7, 9, 6, 3], [1, 8, 6, 1], [1, 1, 9, 9], [3, 7, 6, 5], [2, 6, 2, 6]], 1]) == [0, 2, 3, 5]
assert my_solution.getGoodIndices(*[[[1, 3, 2, 5], [5, 4, 1, 2], [2, 2, 3, 2], [4, 2, 5, 4], [1, 5, 4, 1], [2, 2, 5, 2], [3, 3, 2, 1], [2, 5, 4, 3], [2, 1, 5, 1]], 4]) == []
