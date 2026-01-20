
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.maximumLength(*['aaaa']) == 2
assert my_solution.maximumLength(*['abcdef']) == -1
assert my_solution.maximumLength(*['abcaba']) == 1
assert my_solution.maximumLength(*['abcccccdddd']) == 3
assert my_solution.maximumLength(*['aaa']) == 1
assert my_solution.maximumLength(*['acc']) == -1
assert my_solution.maximumLength(*['cab']) == -1
assert my_solution.maximumLength(*['cad']) == -1
assert my_solution.maximumLength(*['cbc']) == -1
assert my_solution.maximumLength(*['ccc']) == 1
assert my_solution.maximumLength(*['dca']) == -1
assert my_solution.maximumLength(*['ddd']) == 1
assert my_solution.maximumLength(*['fff']) == 1
assert my_solution.maximumLength(*['ggg']) == 1
assert my_solution.maximumLength(*['hhh']) == 1
assert my_solution.maximumLength(*['kkk']) == 1
assert my_solution.maximumLength(*['lll']) == 1
assert my_solution.maximumLength(*['ooo']) == 1
assert my_solution.maximumLength(*['ppp']) == 1
assert my_solution.maximumLength(*['qqq']) == 1
