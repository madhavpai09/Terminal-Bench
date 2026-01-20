
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.numberOfSequence(*[5, [0, 4]]) == 4
assert my_solution.numberOfSequence(*[4, [1]]) == 3
assert my_solution.numberOfSequence(*[2, [0]]) == 1
assert my_solution.numberOfSequence(*[5, [0]]) == 1
assert my_solution.numberOfSequence(*[100, [0]]) == 1
assert my_solution.numberOfSequence(*[2, [1]]) == 1
assert my_solution.numberOfSequence(*[5, [1]]) == 4
assert my_solution.numberOfSequence(*[5, [2]]) == 6
assert my_solution.numberOfSequence(*[5, [3]]) == 4
assert my_solution.numberOfSequence(*[5, [4]]) == 1
assert my_solution.numberOfSequence(*[5, [0, 1]]) == 1
assert my_solution.numberOfSequence(*[3, [0, 2]]) == 1
assert my_solution.numberOfSequence(*[5, [0, 2]]) == 3
assert my_solution.numberOfSequence(*[5, [0, 3]]) == 6
assert my_solution.numberOfSequence(*[5, [1, 2]]) == 3
assert my_solution.numberOfSequence(*[5, [1, 3]]) == 6
assert my_solution.numberOfSequence(*[5, [1, 4]]) == 6
assert my_solution.numberOfSequence(*[5, [2, 3]]) == 3
assert my_solution.numberOfSequence(*[5, [2, 4]]) == 3
assert my_solution.numberOfSequence(*[5, [3, 4]]) == 1
