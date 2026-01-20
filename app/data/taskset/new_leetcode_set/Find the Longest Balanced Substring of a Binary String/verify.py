
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.findTheLongestBalancedSubstring(*['01000111']) == 6
assert my_solution.findTheLongestBalancedSubstring(*['0011']) == 4
assert my_solution.findTheLongestBalancedSubstring(*['111']) == 0
assert my_solution.findTheLongestBalancedSubstring(*['0']) == 0
assert my_solution.findTheLongestBalancedSubstring(*['1']) == 0
assert my_solution.findTheLongestBalancedSubstring(*['00']) == 0
assert my_solution.findTheLongestBalancedSubstring(*['01']) == 2
assert my_solution.findTheLongestBalancedSubstring(*['10']) == 0
assert my_solution.findTheLongestBalancedSubstring(*['11']) == 0
assert my_solution.findTheLongestBalancedSubstring(*['000']) == 0
assert my_solution.findTheLongestBalancedSubstring(*['001']) == 2
assert my_solution.findTheLongestBalancedSubstring(*['010']) == 2
assert my_solution.findTheLongestBalancedSubstring(*['011']) == 2
assert my_solution.findTheLongestBalancedSubstring(*['100']) == 0
assert my_solution.findTheLongestBalancedSubstring(*['101']) == 2
assert my_solution.findTheLongestBalancedSubstring(*['110']) == 0
assert my_solution.findTheLongestBalancedSubstring(*['0000']) == 0
assert my_solution.findTheLongestBalancedSubstring(*['0001']) == 2
assert my_solution.findTheLongestBalancedSubstring(*['0010']) == 2
assert my_solution.findTheLongestBalancedSubstring(*['0100']) == 2
