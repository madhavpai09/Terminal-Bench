
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.numberOfWays(*[10, 2]) == 1
assert my_solution.numberOfWays(*[4, 1]) == 2
assert my_solution.numberOfWays(*[1, 1]) == 1
assert my_solution.numberOfWays(*[1, 2]) == 1
assert my_solution.numberOfWays(*[1, 3]) == 1
assert my_solution.numberOfWays(*[1, 4]) == 1
assert my_solution.numberOfWays(*[1, 5]) == 1
assert my_solution.numberOfWays(*[2, 1]) == 1
assert my_solution.numberOfWays(*[2, 2]) == 0
assert my_solution.numberOfWays(*[2, 3]) == 0
assert my_solution.numberOfWays(*[2, 4]) == 0
assert my_solution.numberOfWays(*[2, 5]) == 0
assert my_solution.numberOfWays(*[3, 1]) == 2
assert my_solution.numberOfWays(*[3, 2]) == 0
assert my_solution.numberOfWays(*[3, 3]) == 0
assert my_solution.numberOfWays(*[3, 4]) == 0
assert my_solution.numberOfWays(*[3, 5]) == 0
assert my_solution.numberOfWays(*[4, 2]) == 1
assert my_solution.numberOfWays(*[4, 3]) == 0
assert my_solution.numberOfWays(*[4, 4]) == 0
