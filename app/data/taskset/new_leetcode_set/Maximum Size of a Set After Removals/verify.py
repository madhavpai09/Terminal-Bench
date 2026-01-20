
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.maximumSetSize(*[[1, 2, 1, 2], [1, 1, 1, 1]]) == 2
assert my_solution.maximumSetSize(*[[1, 2, 3, 4, 5, 6], [2, 3, 2, 3, 2, 3]]) == 5
assert my_solution.maximumSetSize(*[[1, 1, 2, 2, 3, 3], [4, 4, 5, 5, 6, 6]]) == 6
assert my_solution.maximumSetSize(*[[1, 2, 1, 1], [1, 2, 3, 4]]) == 4
assert my_solution.maximumSetSize(*[[1, 1, 1, 1], [12, 23, 41, 9]]) == 3
assert my_solution.maximumSetSize(*[[12, 23, 41, 9], [1, 1, 1, 1]]) == 3
assert my_solution.maximumSetSize(*[[9, 8, 4, 7], [5, 5, 9, 5]]) == 4
assert my_solution.maximumSetSize(*[[8, 9], [4, 3]]) == 2
assert my_solution.maximumSetSize(*[[7, 1], [6, 10]]) == 2
assert my_solution.maximumSetSize(*[[10, 3], [5, 6]]) == 2
assert my_solution.maximumSetSize(*[[3, 6], [6, 6]]) == 2
assert my_solution.maximumSetSize(*[[5, 1], [6, 6]]) == 2
assert my_solution.maximumSetSize(*[[10, 7], [8, 4]]) == 2
assert my_solution.maximumSetSize(*[[10, 8, 7, 9], [7, 9, 9, 5]]) == 4
assert my_solution.maximumSetSize(*[[1, 10, 6, 5], [3, 7, 10, 10]]) == 4
assert my_solution.maximumSetSize(*[[5, 2, 8, 6], [7, 4, 1, 1]]) == 4
assert my_solution.maximumSetSize(*[[2, 4, 1, 4], [10, 2, 4, 10]]) == 4
assert my_solution.maximumSetSize(*[[5, 7], [3, 1]]) == 2
assert my_solution.maximumSetSize(*[[1, 10, 1, 2], [9, 5, 8, 5]]) == 4
assert my_solution.maximumSetSize(*[[9, 4], [5, 7]]) == 2
