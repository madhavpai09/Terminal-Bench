
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.circularGameLosers(*[5, 2]) == [4, 5]
assert my_solution.circularGameLosers(*[4, 4]) == [2, 3, 4]
assert my_solution.circularGameLosers(*[1, 1]) == []
assert my_solution.circularGameLosers(*[2, 1]) == []
assert my_solution.circularGameLosers(*[2, 2]) == [2]
assert my_solution.circularGameLosers(*[3, 1]) == [3]
assert my_solution.circularGameLosers(*[3, 2]) == [2]
assert my_solution.circularGameLosers(*[3, 3]) == [2, 3]
assert my_solution.circularGameLosers(*[4, 1]) == []
assert my_solution.circularGameLosers(*[4, 2]) == [2, 4]
assert my_solution.circularGameLosers(*[4, 3]) == []
assert my_solution.circularGameLosers(*[5, 1]) == [3, 5]
assert my_solution.circularGameLosers(*[5, 3]) == [2, 3]
assert my_solution.circularGameLosers(*[5, 4]) == [2, 4]
assert my_solution.circularGameLosers(*[5, 5]) == [2, 3, 4, 5]
assert my_solution.circularGameLosers(*[6, 1]) == [3, 5, 6]
assert my_solution.circularGameLosers(*[6, 2]) == [2, 4, 5, 6]
assert my_solution.circularGameLosers(*[6, 3]) == [2, 3, 5, 6]
assert my_solution.circularGameLosers(*[6, 4]) == [2, 3, 4, 6]
assert my_solution.circularGameLosers(*[6, 5]) == [2, 3, 5]
