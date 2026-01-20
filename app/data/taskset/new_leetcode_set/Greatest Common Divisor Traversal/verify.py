
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.canTraverseAllPairs(*[[2, 3, 6]]) == True
assert my_solution.canTraverseAllPairs(*[[3, 9, 5]]) == False
assert my_solution.canTraverseAllPairs(*[[4, 3, 12, 8]]) == True
assert my_solution.canTraverseAllPairs(*[[10]]) == True
assert my_solution.canTraverseAllPairs(*[[11]]) == True
assert my_solution.canTraverseAllPairs(*[[14]]) == True
assert my_solution.canTraverseAllPairs(*[[20]]) == True
assert my_solution.canTraverseAllPairs(*[[28]]) == True
assert my_solution.canTraverseAllPairs(*[[30]]) == True
assert my_solution.canTraverseAllPairs(*[[35]]) == True
assert my_solution.canTraverseAllPairs(*[[42]]) == True
assert my_solution.canTraverseAllPairs(*[[44]]) == True
assert my_solution.canTraverseAllPairs(*[[98]]) == True
assert my_solution.canTraverseAllPairs(*[[20, 6]]) == True
assert my_solution.canTraverseAllPairs(*[[28, 39]]) == False
assert my_solution.canTraverseAllPairs(*[[30, 14]]) == True
assert my_solution.canTraverseAllPairs(*[[30, 30]]) == True
assert my_solution.canTraverseAllPairs(*[[33, 60]]) == True
assert my_solution.canTraverseAllPairs(*[[35, 26]]) == False
assert my_solution.canTraverseAllPairs(*[[42, 42]]) == True
