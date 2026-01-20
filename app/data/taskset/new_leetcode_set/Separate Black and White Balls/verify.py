
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.minimumSteps(*['101']) == 1
assert my_solution.minimumSteps(*['100']) == 2
assert my_solution.minimumSteps(*['0111']) == 0
assert my_solution.minimumSteps(*['11000111']) == 6
assert my_solution.minimumSteps(*['01010001']) == 7
assert my_solution.minimumSteps(*['0100101']) == 4
assert my_solution.minimumSteps(*['111111111100100010']) == 65
assert my_solution.minimumSteps(*['10100000110010011010']) == 44
assert my_solution.minimumSteps(*['1101110000111011110']) == 42
assert my_solution.minimumSteps(*['01000010111010001']) == 29
assert my_solution.minimumSteps(*['11110']) == 4
assert my_solution.minimumSteps(*['010001001011010']) == 21
assert my_solution.minimumSteps(*['0011011']) == 2
assert my_solution.minimumSteps(*['001']) == 0
assert my_solution.minimumSteps(*['000100100']) == 6
assert my_solution.minimumSteps(*['00110']) == 2
assert my_solution.minimumSteps(*['001110001110001']) == 27
assert my_solution.minimumSteps(*['10000000001']) == 9
assert my_solution.minimumSteps(*['01']) == 0
assert my_solution.minimumSteps(*['0100011100001100100']) == 45
