
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.findPrimePairs(*[10]) == [[3, 7], [5, 5]]
assert my_solution.findPrimePairs(*[2]) == []
assert my_solution.findPrimePairs(*[1]) == []
assert my_solution.findPrimePairs(*[3]) == []
assert my_solution.findPrimePairs(*[4]) == [[2, 2]]
assert my_solution.findPrimePairs(*[5]) == [[2, 3]]
assert my_solution.findPrimePairs(*[6]) == [[3, 3]]
assert my_solution.findPrimePairs(*[7]) == [[2, 5]]
assert my_solution.findPrimePairs(*[8]) == [[3, 5]]
assert my_solution.findPrimePairs(*[9]) == [[2, 7]]
assert my_solution.findPrimePairs(*[11]) == []
assert my_solution.findPrimePairs(*[12]) == [[5, 7]]
assert my_solution.findPrimePairs(*[13]) == [[2, 11]]
assert my_solution.findPrimePairs(*[14]) == [[3, 11], [7, 7]]
assert my_solution.findPrimePairs(*[15]) == [[2, 13]]
assert my_solution.findPrimePairs(*[16]) == [[3, 13], [5, 11]]
assert my_solution.findPrimePairs(*[17]) == []
assert my_solution.findPrimePairs(*[18]) == [[5, 13], [7, 11]]
assert my_solution.findPrimePairs(*[19]) == [[2, 17]]
assert my_solution.findPrimePairs(*[20]) == [[3, 17], [7, 13]]
