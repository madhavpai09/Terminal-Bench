
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.minimumString(*['abc', 'bca', 'aaa']) == aaabca
assert my_solution.minimumString(*['ab', 'ba', 'aba']) == aba
assert my_solution.minimumString(*['xyyyz', 'xzyz', 'zzz']) == xyyyzxzyzzz
assert my_solution.minimumString(*['a', 'a', 'a']) == a
assert my_solution.minimumString(*['a', 'a', 'b']) == ab
assert my_solution.minimumString(*['a', 'c', 'a']) == ac
assert my_solution.minimumString(*['a', 'b', 'b']) == ab
assert my_solution.minimumString(*['a', 'a', 'c']) == ac
assert my_solution.minimumString(*['a', 'c', 'b']) == abc
assert my_solution.minimumString(*['c', 'c', 'a']) == ac
assert my_solution.minimumString(*['k', 'e', 'a']) == aek
assert my_solution.minimumString(*['a', 'b', 'a']) == ab
assert my_solution.minimumString(*['b', 'b', 'a']) == ab
assert my_solution.minimumString(*['b', 'b', 'b']) == b
assert my_solution.minimumString(*['b', 'b', 'c']) == bc
assert my_solution.minimumString(*['c', 'b', 'b']) == bc
assert my_solution.minimumString(*['b', 'c', 'c']) == bc
assert my_solution.minimumString(*['b', 'c', 'a']) == abc
assert my_solution.minimumString(*['c', 'a', 'c']) == ac
assert my_solution.minimumString(*['c', 'b', 'c']) == bc
