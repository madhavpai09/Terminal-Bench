
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.numberOfGoodPartitions(*[[1, 2, 3, 4]]) == 8
assert my_solution.numberOfGoodPartitions(*[[1, 1, 1, 1]]) == 1
assert my_solution.numberOfGoodPartitions(*[[1, 2, 1, 3]]) == 2
assert my_solution.numberOfGoodPartitions(*[[1]]) == 1
assert my_solution.numberOfGoodPartitions(*[[100000]]) == 1
assert my_solution.numberOfGoodPartitions(*[[1000000000]]) == 1
assert my_solution.numberOfGoodPartitions(*[[1, 1, 1, 3, 2]]) == 4
assert my_solution.numberOfGoodPartitions(*[[1, 1, 1, 9, 7]]) == 4
assert my_solution.numberOfGoodPartitions(*[[1, 1, 5, 9, 2]]) == 8
assert my_solution.numberOfGoodPartitions(*[[1, 4, 1, 7, 5]]) == 4
assert my_solution.numberOfGoodPartitions(*[[1, 5, 1, 5, 6]]) == 2
assert my_solution.numberOfGoodPartitions(*[[1, 5, 1, 10, 8]]) == 4
assert my_solution.numberOfGoodPartitions(*[[1, 6, 8, 1, 5]]) == 2
assert my_solution.numberOfGoodPartitions(*[[1, 6, 9, 4, 10]]) == 16
assert my_solution.numberOfGoodPartitions(*[[1, 7, 1, 6, 8]]) == 4
assert my_solution.numberOfGoodPartitions(*[[1, 9, 1, 1, 7]]) == 2
assert my_solution.numberOfGoodPartitions(*[[2, 1, 6, 7, 5]]) == 16
assert my_solution.numberOfGoodPartitions(*[[2, 3, 2, 6, 9]]) == 4
assert my_solution.numberOfGoodPartitions(*[[2, 3, 2, 8, 8]]) == 2
assert my_solution.numberOfGoodPartitions(*[[2, 3, 9, 2, 6]]) == 2
