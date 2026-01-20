
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.minChanges(*['1001']) == 2
assert my_solution.minChanges(*['10']) == 1
assert my_solution.minChanges(*['0000']) == 0
assert my_solution.minChanges(*['11000111']) == 1
assert my_solution.minChanges(*['01010001']) == 3
assert my_solution.minChanges(*['010010']) == 2
assert my_solution.minChanges(*['111111111110010001']) == 3
assert my_solution.minChanges(*['01010000011001001101']) == 6
assert my_solution.minChanges(*['011011100001110111']) == 5
assert my_solution.minChanges(*['1001000010111010']) == 5
assert my_solution.minChanges(*['0011']) == 0
assert my_solution.minChanges(*['11100100010010']) == 4
assert my_solution.minChanges(*['110100']) == 1
assert my_solution.minChanges(*['01']) == 1
assert my_solution.minChanges(*['10110010']) == 2
assert my_solution.minChanges(*['0010']) == 1
assert my_solution.minChanges(*['01000011000111']) == 2
assert my_solution.minChanges(*['0001110001']) == 2
assert my_solution.minChanges(*['000000001010100011']) == 3
assert my_solution.minChanges(*['100001']) == 2
