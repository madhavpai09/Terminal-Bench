
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.largestPerimeter(*[[5, 5, 5]]) == 15
assert my_solution.largestPerimeter(*[[1, 12, 1, 2, 5, 50, 3]]) == 12
assert my_solution.largestPerimeter(*[[5, 5, 50]]) == -1
assert my_solution.largestPerimeter(*[[1, 1, 1]]) == 3
assert my_solution.largestPerimeter(*[[1, 1, 2]]) == -1
assert my_solution.largestPerimeter(*[[1, 1, 3]]) == -1
assert my_solution.largestPerimeter(*[[1, 1, 4]]) == -1
assert my_solution.largestPerimeter(*[[1, 1, 5]]) == -1
assert my_solution.largestPerimeter(*[[1, 2, 1]]) == -1
assert my_solution.largestPerimeter(*[[1, 2, 2]]) == 5
assert my_solution.largestPerimeter(*[[1, 2, 3]]) == -1
assert my_solution.largestPerimeter(*[[1, 2, 4]]) == -1
assert my_solution.largestPerimeter(*[[1, 2, 5]]) == -1
assert my_solution.largestPerimeter(*[[1, 3, 1]]) == -1
assert my_solution.largestPerimeter(*[[1, 3, 2]]) == -1
assert my_solution.largestPerimeter(*[[1, 3, 3]]) == 7
assert my_solution.largestPerimeter(*[[1, 3, 4]]) == -1
assert my_solution.largestPerimeter(*[[1, 3, 5]]) == -1
assert my_solution.largestPerimeter(*[[1, 4, 1]]) == -1
assert my_solution.largestPerimeter(*[[1, 4, 2]]) == -1
