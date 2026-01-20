
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.maximumOddBinaryNumber(*['010']) == 001
assert my_solution.maximumOddBinaryNumber(*['0101']) == 1001
assert my_solution.maximumOddBinaryNumber(*['1']) == 1
assert my_solution.maximumOddBinaryNumber(*['01']) == 01
assert my_solution.maximumOddBinaryNumber(*['10']) == 01
assert my_solution.maximumOddBinaryNumber(*['11']) == 11
assert my_solution.maximumOddBinaryNumber(*['001']) == 001
assert my_solution.maximumOddBinaryNumber(*['011']) == 101
assert my_solution.maximumOddBinaryNumber(*['100']) == 001
assert my_solution.maximumOddBinaryNumber(*['101']) == 101
assert my_solution.maximumOddBinaryNumber(*['110']) == 101
assert my_solution.maximumOddBinaryNumber(*['111']) == 111
assert my_solution.maximumOddBinaryNumber(*['0010']) == 0001
assert my_solution.maximumOddBinaryNumber(*['0011']) == 1001
assert my_solution.maximumOddBinaryNumber(*['0100']) == 0001
assert my_solution.maximumOddBinaryNumber(*['0111']) == 1101
assert my_solution.maximumOddBinaryNumber(*['1000']) == 0001
assert my_solution.maximumOddBinaryNumber(*['1001']) == 1001
assert my_solution.maximumOddBinaryNumber(*['1011']) == 1101
assert my_solution.maximumOddBinaryNumber(*['1100']) == 1001
