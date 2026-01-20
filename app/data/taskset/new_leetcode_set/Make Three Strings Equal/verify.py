
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.findMinimumOperations(*['abc', 'abb', 'ab']) == 2
assert my_solution.findMinimumOperations(*['dac', 'bac', 'cac']) == -1
assert my_solution.findMinimumOperations(*['a', 'a', 'a']) == 0
assert my_solution.findMinimumOperations(*['kui', 'm', 'v']) == -1
assert my_solution.findMinimumOperations(*['a', 'aabc', 'a']) == 3
assert my_solution.findMinimumOperations(*['cc', 'cccb', 'c']) == 4
assert my_solution.findMinimumOperations(*['luso', 'lu', 'lu']) == 2
assert my_solution.findMinimumOperations(*['xx', 'phe', 'xie']) == -1
assert my_solution.findMinimumOperations(*['gzd', 'bcju', 'db']) == -1
assert my_solution.findMinimumOperations(*['cbba', 'cbaa', 'c']) == 6
assert my_solution.findMinimumOperations(*['k', 'kfb', 'krcnf']) == 6
assert my_solution.findMinimumOperations(*['oby', 'obz', 'obf']) == 3
assert my_solution.findMinimumOperations(*['b', 'aba', 'aaccaa']) == -1
assert my_solution.findMinimumOperations(*['a', 'accabb', 'aaa']) == 7
assert my_solution.findMinimumOperations(*['b', 'bccaaba', 'ba']) == 7
assert my_solution.findMinimumOperations(*['b', 'bacccab', 'cc']) == -1
assert my_solution.findMinimumOperations(*['ca', 'cccabb', 'cb']) == 7
assert my_solution.findMinimumOperations(*['ccb', 'ccba', 'ccb']) == 1
assert my_solution.findMinimumOperations(*['mbooi', 'pdq', 'br']) == -1
assert my_solution.findMinimumOperations(*['xxfzj', 'faho', 'c']) == -1
