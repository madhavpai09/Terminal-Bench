
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.constructProductMatrix(*[[[1, 2], [3, 4]]]) == [[24, 12], [8, 6]]
assert my_solution.constructProductMatrix(*[[[12345], [2], [1]]]) == [[2], [0], [0]]
assert my_solution.constructProductMatrix(*[[[1], [2]]]) == [[2], [1]]
assert my_solution.constructProductMatrix(*[[[1, 2]]]) == [[2, 1]]
assert my_solution.constructProductMatrix(*[[[12345, 12345]]]) == [[0, 0]]
assert my_solution.constructProductMatrix(*[[[1], [4]]]) == [[4], [1]]
assert my_solution.constructProductMatrix(*[[[3], [4]]]) == [[4], [3]]
assert my_solution.constructProductMatrix(*[[[4], [3]]]) == [[3], [4]]
assert my_solution.constructProductMatrix(*[[[1, 1, 1]]]) == [[1, 1, 1]]
assert my_solution.constructProductMatrix(*[[[2, 1, 1]]]) == [[1, 2, 2]]
assert my_solution.constructProductMatrix(*[[[3], [5], [2]]]) == [[10], [6], [15]]
assert my_solution.constructProductMatrix(*[[[1, 2], [1, 1], [6, 4]]]) == [[48, 24], [48, 48], [8, 12]]
assert my_solution.constructProductMatrix(*[[[1, 2, 2], [1, 4, 3]]]) == [[48, 24, 24], [48, 12, 16]]
assert my_solution.constructProductMatrix(*[[[2], [7], [2], [6]]]) == [[84], [24], [84], [28]]
assert my_solution.constructProductMatrix(*[[[3], [4], [7], [7]]]) == [[196], [147], [84], [84]]
assert my_solution.constructProductMatrix(*[[[3, 1, 1], [1, 3, 4]]]) == [[12, 36, 36], [36, 12, 9]]
assert my_solution.constructProductMatrix(*[[[4], [8], [3], [7]]]) == [[168], [84], [224], [96]]
assert my_solution.constructProductMatrix(*[[[5], [8], [8], [3]]]) == [[192], [120], [120], [320]]
assert my_solution.constructProductMatrix(*[[[6], [5], [8], [5]]]) == [[200], [240], [150], [240]]
assert my_solution.constructProductMatrix(*[[[8], [1], [3], [8]]]) == [[24], [192], [64], [24]]
