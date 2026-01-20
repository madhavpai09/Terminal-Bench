
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.minimizeConcatenatedLength(*[['aa', 'ab', 'bc']]) == 4
assert my_solution.minimizeConcatenatedLength(*[['ab', 'b']]) == 2
assert my_solution.minimizeConcatenatedLength(*[['aaa', 'c', 'aba']]) == 6
assert my_solution.minimizeConcatenatedLength(*[['a', 'a']]) == 1
assert my_solution.minimizeConcatenatedLength(*[['a', 'ab']]) == 2
assert my_solution.minimizeConcatenatedLength(*[['a', 'b']]) == 2
assert my_solution.minimizeConcatenatedLength(*[['a', 'ca']]) == 2
assert my_solution.minimizeConcatenatedLength(*[['a', 'cb']]) == 3
assert my_solution.minimizeConcatenatedLength(*[['aa', 'a']]) == 2
assert my_solution.minimizeConcatenatedLength(*[['aa', 'b']]) == 3
assert my_solution.minimizeConcatenatedLength(*[['aa', 'ca']]) == 3
assert my_solution.minimizeConcatenatedLength(*[['aa', 'ccc']]) == 5
assert my_solution.minimizeConcatenatedLength(*[['aab', 'b']]) == 3
assert my_solution.minimizeConcatenatedLength(*[['aab', 'ba']]) == 4
assert my_solution.minimizeConcatenatedLength(*[['aab', 'bb']]) == 4
assert my_solution.minimizeConcatenatedLength(*[['aab', 'bba']]) == 5
assert my_solution.minimizeConcatenatedLength(*[['aab', 'c']]) == 4
assert my_solution.minimizeConcatenatedLength(*[['aac', 'b']]) == 4
assert my_solution.minimizeConcatenatedLength(*[['ab', 'acb']]) == 5
assert my_solution.minimizeConcatenatedLength(*[['ab', 'bc']]) == 3
