
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.minimumArrayLength(*[[1, 4, 3, 1]]) == 1
assert my_solution.minimumArrayLength(*[[5, 5, 5, 10, 5]]) == 2
assert my_solution.minimumArrayLength(*[[2, 3, 4]]) == 1
assert my_solution.minimumArrayLength(*[[1]]) == 1
assert my_solution.minimumArrayLength(*[[3]]) == 1
assert my_solution.minimumArrayLength(*[[6]]) == 1
assert my_solution.minimumArrayLength(*[[1, 4]]) == 1
assert my_solution.minimumArrayLength(*[[1, 5]]) == 1
assert my_solution.minimumArrayLength(*[[2, 4]]) == 1
assert my_solution.minimumArrayLength(*[[3, 4]]) == 1
assert my_solution.minimumArrayLength(*[[5, 3]]) == 1
assert my_solution.minimumArrayLength(*[[6, 9]]) == 1
assert my_solution.minimumArrayLength(*[[8, 2]]) == 1
assert my_solution.minimumArrayLength(*[[9, 9]]) == 1
assert my_solution.minimumArrayLength(*[[9, 10]]) == 1
assert my_solution.minimumArrayLength(*[[1, 2, 5]]) == 1
assert my_solution.minimumArrayLength(*[[2, 1, 1]]) == 1
assert my_solution.minimumArrayLength(*[[2, 7, 10]]) == 1
assert my_solution.minimumArrayLength(*[[2, 9, 5]]) == 1
assert my_solution.minimumArrayLength(*[[3, 2, 1]]) == 1
