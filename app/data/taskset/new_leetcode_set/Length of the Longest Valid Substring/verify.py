
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.longestValidSubstring(*['cbaaaabc', ['aaa', 'cb']]) == 4
assert my_solution.longestValidSubstring(*['leetcode', ['de', 'le', 'e']]) == 4
assert my_solution.longestValidSubstring(*['a', ['n']]) == 1
assert my_solution.longestValidSubstring(*['a', ['s']]) == 1
assert my_solution.longestValidSubstring(*['a', ['a']]) == 0
assert my_solution.longestValidSubstring(*['b', ['g']]) == 1
assert my_solution.longestValidSubstring(*['b', ['t']]) == 1
assert my_solution.longestValidSubstring(*['b', ['b']]) == 0
assert my_solution.longestValidSubstring(*['c', ['k']]) == 1
assert my_solution.longestValidSubstring(*['c', ['s']]) == 1
assert my_solution.longestValidSubstring(*['c', ['c']]) == 0
assert my_solution.longestValidSubstring(*['d', ['h']]) == 1
assert my_solution.longestValidSubstring(*['d', ['n']]) == 1
assert my_solution.longestValidSubstring(*['d', ['d']]) == 0
assert my_solution.longestValidSubstring(*['e', ['s']]) == 1
assert my_solution.longestValidSubstring(*['e', ['e']]) == 0
assert my_solution.longestValidSubstring(*['f', ['b']]) == 1
assert my_solution.longestValidSubstring(*['f', ['s']]) == 1
assert my_solution.longestValidSubstring(*['f', ['f']]) == 0
assert my_solution.longestValidSubstring(*['g', ['r']]) == 1
