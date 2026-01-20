
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.findMissingAndRepeatedValues(*[[[1, 3], [2, 2]]]) == [2, 4]
assert my_solution.findMissingAndRepeatedValues(*[[[9, 1, 7], [8, 9, 2], [3, 4, 6]]]) == [9, 5]
assert my_solution.findMissingAndRepeatedValues(*[[[1, 1], [3, 2]]]) == [1, 4]
assert my_solution.findMissingAndRepeatedValues(*[[[1, 1], [3, 4]]]) == [1, 2]
assert my_solution.findMissingAndRepeatedValues(*[[[1, 2], [1, 3]]]) == [1, 4]
assert my_solution.findMissingAndRepeatedValues(*[[[1, 2], [1, 4]]]) == [1, 3]
assert my_solution.findMissingAndRepeatedValues(*[[[1, 2], [3, 3]]]) == [3, 4]
assert my_solution.findMissingAndRepeatedValues(*[[[1, 2], [4, 1]]]) == [1, 3]
assert my_solution.findMissingAndRepeatedValues(*[[[1, 2], [4, 2]]]) == [2, 3]
assert my_solution.findMissingAndRepeatedValues(*[[[1, 2], [4, 4]]]) == [4, 3]
assert my_solution.findMissingAndRepeatedValues(*[[[1, 4], [1, 3]]]) == [1, 2]
assert my_solution.findMissingAndRepeatedValues(*[[[1, 4], [2, 1]]]) == [1, 3]
assert my_solution.findMissingAndRepeatedValues(*[[[1, 4], [3, 1]]]) == [1, 2]
assert my_solution.findMissingAndRepeatedValues(*[[[1, 4], [3, 4]]]) == [4, 2]
assert my_solution.findMissingAndRepeatedValues(*[[[1, 4], [4, 2]]]) == [4, 3]
assert my_solution.findMissingAndRepeatedValues(*[[[2, 1], [4, 2]]]) == [2, 3]
assert my_solution.findMissingAndRepeatedValues(*[[[2, 1], [4, 4]]]) == [4, 3]
assert my_solution.findMissingAndRepeatedValues(*[[[2, 2], [3, 4]]]) == [2, 1]
assert my_solution.findMissingAndRepeatedValues(*[[[2, 2], [4, 1]]]) == [2, 3]
assert my_solution.findMissingAndRepeatedValues(*[[[2, 3], [2, 1]]]) == [2, 4]
