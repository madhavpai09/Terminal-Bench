
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.removeAlmostEqualCharacters(*['aaaaa']) == 2
assert my_solution.removeAlmostEqualCharacters(*['abddez']) == 2
assert my_solution.removeAlmostEqualCharacters(*['zyxyxyz']) == 3
assert my_solution.removeAlmostEqualCharacters(*['a']) == 0
assert my_solution.removeAlmostEqualCharacters(*['b']) == 0
assert my_solution.removeAlmostEqualCharacters(*['c']) == 0
assert my_solution.removeAlmostEqualCharacters(*['aa']) == 1
assert my_solution.removeAlmostEqualCharacters(*['ab']) == 1
assert my_solution.removeAlmostEqualCharacters(*['ac']) == 0
assert my_solution.removeAlmostEqualCharacters(*['ba']) == 1
assert my_solution.removeAlmostEqualCharacters(*['bb']) == 1
assert my_solution.removeAlmostEqualCharacters(*['bc']) == 1
assert my_solution.removeAlmostEqualCharacters(*['ca']) == 0
assert my_solution.removeAlmostEqualCharacters(*['cb']) == 1
assert my_solution.removeAlmostEqualCharacters(*['cc']) == 1
assert my_solution.removeAlmostEqualCharacters(*['aaa']) == 1
assert my_solution.removeAlmostEqualCharacters(*['aab']) == 1
assert my_solution.removeAlmostEqualCharacters(*['aac']) == 1
assert my_solution.removeAlmostEqualCharacters(*['aba']) == 1
assert my_solution.removeAlmostEqualCharacters(*['abb']) == 1
