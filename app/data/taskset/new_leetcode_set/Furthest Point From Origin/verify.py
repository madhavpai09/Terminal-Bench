
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.furthestDistanceFromOrigin(*['L_RL__R']) == 3
assert my_solution.furthestDistanceFromOrigin(*['_R__LL_']) == 5
assert my_solution.furthestDistanceFromOrigin(*['_______']) == 7
assert my_solution.furthestDistanceFromOrigin(*['L']) == 1
assert my_solution.furthestDistanceFromOrigin(*['R']) == 1
assert my_solution.furthestDistanceFromOrigin(*['_']) == 1
assert my_solution.furthestDistanceFromOrigin(*['LL']) == 2
assert my_solution.furthestDistanceFromOrigin(*['LR']) == 0
assert my_solution.furthestDistanceFromOrigin(*['L_']) == 2
assert my_solution.furthestDistanceFromOrigin(*['RL']) == 0
assert my_solution.furthestDistanceFromOrigin(*['RR']) == 2
assert my_solution.furthestDistanceFromOrigin(*['R_']) == 2
assert my_solution.furthestDistanceFromOrigin(*['_L']) == 2
assert my_solution.furthestDistanceFromOrigin(*['_R']) == 2
assert my_solution.furthestDistanceFromOrigin(*['__']) == 2
assert my_solution.furthestDistanceFromOrigin(*['LLL']) == 3
assert my_solution.furthestDistanceFromOrigin(*['LLR']) == 1
assert my_solution.furthestDistanceFromOrigin(*['LL_']) == 3
assert my_solution.furthestDistanceFromOrigin(*['LRL']) == 1
assert my_solution.furthestDistanceFromOrigin(*['LRR']) == 1
