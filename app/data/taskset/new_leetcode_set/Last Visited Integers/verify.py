
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.lastVisitedIntegers(*[['1', '2', 'prev', 'prev', 'prev']]) == [2, 1, -1]
assert my_solution.lastVisitedIntegers(*[['1', 'prev', '2', 'prev', 'prev']]) == [1, 2, 1]
assert my_solution.lastVisitedIntegers(*[['prev', 'prev', 'prev', '27']]) == [-1, -1, -1]
assert my_solution.lastVisitedIntegers(*[['17', '42']]) == []
assert my_solution.lastVisitedIntegers(*[['prev']]) == [-1]
assert my_solution.lastVisitedIntegers(*[['prev', 'prev', 'prev', '52', 'prev']]) == [-1, -1, -1, 52]
assert my_solution.lastVisitedIntegers(*[['prev', 'prev', '68', 'prev', 'prev', '53', '40', '23', 'prev']]) == [-1, -1, 68, -1, 23]
assert my_solution.lastVisitedIntegers(*[['99', '23', 'prev']]) == [23]
assert my_solution.lastVisitedIntegers(*[['prev', 'prev', 'prev', '58', '99', 'prev', '10', 'prev']]) == [-1, -1, -1, 99, 10]
assert my_solution.lastVisitedIntegers(*[['prev', '51', 'prev', 'prev']]) == [-1, 51, -1]
assert my_solution.lastVisitedIntegers(*[['prev', '46', '9', 'prev']]) == [-1, 9]
assert my_solution.lastVisitedIntegers(*[['prev', 'prev', 'prev', 'prev', 'prev', '26']]) == [-1, -1, -1, -1, -1]
assert my_solution.lastVisitedIntegers(*[['prev', '21', 'prev', '76', '82', 'prev', '96', 'prev', '57', 'prev']]) == [-1, 21, 82, 96, 57]
assert my_solution.lastVisitedIntegers(*[['52', '4', 'prev', 'prev', 'prev', '69']]) == [4, 52, -1]
assert my_solution.lastVisitedIntegers(*[['24', 'prev']]) == [24]
assert my_solution.lastVisitedIntegers(*[['46', 'prev', '78', 'prev', '83', '21', 'prev', '94', '50']]) == [46, 78, 21]
assert my_solution.lastVisitedIntegers(*[['14', '66', 'prev', 'prev', '46', 'prev']]) == [66, 14, 46]
assert my_solution.lastVisitedIntegers(*[['35', '90']]) == []
assert my_solution.lastVisitedIntegers(*[['prev', '9', 'prev', '8', 'prev']]) == [-1, 9, 8]
assert my_solution.lastVisitedIntegers(*[['prev', 'prev', '88', '71', '47', '65', '24', '39']]) == [-1, -1]
