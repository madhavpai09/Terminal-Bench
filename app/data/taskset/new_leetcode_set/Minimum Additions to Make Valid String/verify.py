
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.addMinimum(*['b']) == 2
assert my_solution.addMinimum(*['aaa']) == 6
assert my_solution.addMinimum(*['abc']) == 0
assert my_solution.addMinimum(*['a']) == 2
assert my_solution.addMinimum(*['aa']) == 4
assert my_solution.addMinimum(*['aaaa']) == 8
assert my_solution.addMinimum(*['aaaaa']) == 10
assert my_solution.addMinimum(*['aaaaaa']) == 12
assert my_solution.addMinimum(*['aaaaab']) == 9
assert my_solution.addMinimum(*['aaaaac']) == 9
assert my_solution.addMinimum(*['aaaab']) == 7
assert my_solution.addMinimum(*['aaaaba']) == 9
assert my_solution.addMinimum(*['aaaabb']) == 9
assert my_solution.addMinimum(*['aaaabc']) == 6
assert my_solution.addMinimum(*['aaaac']) == 7
assert my_solution.addMinimum(*['aaaaca']) == 9
assert my_solution.addMinimum(*['aaaacb']) == 9
assert my_solution.addMinimum(*['aaaacc']) == 9
assert my_solution.addMinimum(*['aaab']) == 5
assert my_solution.addMinimum(*['aaaba']) == 7
