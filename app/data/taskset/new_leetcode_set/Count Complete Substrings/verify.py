
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.countCompleteSubstrings(*['igigee', 2]) == 3
assert my_solution.countCompleteSubstrings(*['aaabbbccc', 3]) == 6
assert my_solution.countCompleteSubstrings(*['a', 1]) == 1
assert my_solution.countCompleteSubstrings(*['b', 1]) == 1
assert my_solution.countCompleteSubstrings(*['c', 1]) == 1
assert my_solution.countCompleteSubstrings(*['aa', 2]) == 1
assert my_solution.countCompleteSubstrings(*['ab', 2]) == 0
assert my_solution.countCompleteSubstrings(*['ac', 2]) == 0
assert my_solution.countCompleteSubstrings(*['ba', 1]) == 3
assert my_solution.countCompleteSubstrings(*['bb', 2]) == 1
assert my_solution.countCompleteSubstrings(*['bc', 1]) == 3
assert my_solution.countCompleteSubstrings(*['ca', 1]) == 3
assert my_solution.countCompleteSubstrings(*['cb', 1]) == 3
assert my_solution.countCompleteSubstrings(*['cc', 2]) == 1
assert my_solution.countCompleteSubstrings(*['aaa', 1]) == 3
assert my_solution.countCompleteSubstrings(*['aab', 3]) == 0
assert my_solution.countCompleteSubstrings(*['aac', 2]) == 1
assert my_solution.countCompleteSubstrings(*['aba', 3]) == 0
assert my_solution.countCompleteSubstrings(*['abb', 1]) == 4
assert my_solution.countCompleteSubstrings(*['abc', 3]) == 0
