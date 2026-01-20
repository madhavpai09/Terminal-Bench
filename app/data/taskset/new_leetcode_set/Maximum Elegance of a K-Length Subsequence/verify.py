
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.findMaximumElegance(*[[[3, 2], [5, 1], [10, 1]], 2]) == 17
assert my_solution.findMaximumElegance(*[[[3, 1], [3, 1], [2, 2], [5, 3]], 3]) == 19
assert my_solution.findMaximumElegance(*[[[1, 1], [2, 1], [3, 1]], 3]) == 7
assert my_solution.findMaximumElegance(*[[[1, 1], [1, 2]], 2]) == 6
assert my_solution.findMaximumElegance(*[[[1, 1], [4, 1]], 1]) == 5
assert my_solution.findMaximumElegance(*[[[1, 1], [4, 1]], 2]) == 6
assert my_solution.findMaximumElegance(*[[[1, 1], [6, 1]], 1]) == 7
assert my_solution.findMaximumElegance(*[[[1, 1], [6, 1]], 2]) == 8
assert my_solution.findMaximumElegance(*[[[1, 1], [8, 2]], 2]) == 13
assert my_solution.findMaximumElegance(*[[[1, 2], [6, 2]], 1]) == 7
assert my_solution.findMaximumElegance(*[[[1, 2], [10, 1]], 1]) == 11
assert my_solution.findMaximumElegance(*[[[2, 1], [6, 1]], 2]) == 9
assert my_solution.findMaximumElegance(*[[[2, 1], [7, 1]], 2]) == 10
assert my_solution.findMaximumElegance(*[[[2, 1], [9, 2]], 1]) == 10
assert my_solution.findMaximumElegance(*[[[2, 2], [2, 2]], 1]) == 3
assert my_solution.findMaximumElegance(*[[[2, 2], [2, 2]], 2]) == 5
assert my_solution.findMaximumElegance(*[[[2, 2], [3, 1]], 2]) == 9
assert my_solution.findMaximumElegance(*[[[2, 2], [6, 1]], 2]) == 12
assert my_solution.findMaximumElegance(*[[[3, 1], [1, 2]], 2]) == 8
assert my_solution.findMaximumElegance(*[[[3, 1], [9, 1]], 2]) == 13
