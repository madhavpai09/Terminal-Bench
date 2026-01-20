
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.maximumLength(*['aaaa']) == 2
assert my_solution.maximumLength(*['abcdef']) == -1
assert my_solution.maximumLength(*['abcaba']) == 1
assert my_solution.maximumLength(*['abcccccdddd']) == 3
assert my_solution.maximumLength(*['acd']) == -1
assert my_solution.maximumLength(*['bad']) == -1
assert my_solution.maximumLength(*['bbc']) == -1
assert my_solution.maximumLength(*['ccc']) == 1
assert my_solution.maximumLength(*['cda']) == -1
assert my_solution.maximumLength(*['dab']) == -1
assert my_solution.maximumLength(*['ddd']) == 1
assert my_solution.maximumLength(*['eee']) == 1
assert my_solution.maximumLength(*['fff']) == 1
assert my_solution.maximumLength(*['hhh']) == 1
assert my_solution.maximumLength(*['jjj']) == 1
assert my_solution.maximumLength(*['kkk']) == 1
assert my_solution.maximumLength(*['lll']) == 1
assert my_solution.maximumLength(*['mmm']) == 1
assert my_solution.maximumLength(*['nnn']) == 1
assert my_solution.maximumLength(*['ooo']) == 1
