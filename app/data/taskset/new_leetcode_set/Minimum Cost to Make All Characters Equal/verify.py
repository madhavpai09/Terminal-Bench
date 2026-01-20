
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.minimumCost(*['0011']) == 2
assert my_solution.minimumCost(*['010101']) == 9
assert my_solution.minimumCost(*['0']) == 0
assert my_solution.minimumCost(*['00']) == 0
assert my_solution.minimumCost(*['000']) == 0
assert my_solution.minimumCost(*['0000']) == 0
assert my_solution.minimumCost(*['00000']) == 0
assert my_solution.minimumCost(*['000000']) == 0
assert my_solution.minimumCost(*['0000000']) == 0
assert my_solution.minimumCost(*['00000000']) == 0
assert my_solution.minimumCost(*['000000000']) == 0
assert my_solution.minimumCost(*['000000001']) == 1
assert my_solution.minimumCost(*['00000001']) == 1
assert my_solution.minimumCost(*['000000010']) == 3
assert my_solution.minimumCost(*['000000011']) == 2
assert my_solution.minimumCost(*['0000001']) == 1
assert my_solution.minimumCost(*['00000010']) == 3
assert my_solution.minimumCost(*['000000100']) == 5
assert my_solution.minimumCost(*['000000101']) == 6
assert my_solution.minimumCost(*['00000011']) == 2
