
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.findIntersectionValues(*[[4, 3, 2, 3, 1], [2, 2, 5, 2, 3, 6]]) == [3, 4]
assert my_solution.findIntersectionValues(*[[3, 4, 2, 3], [1, 5]]) == [0, 0]
assert my_solution.findIntersectionValues(*[[24, 28, 7, 27, 7, 27, 9, 24, 9, 10], [12, 29, 9, 7, 5]]) == [4, 2]
assert my_solution.findIntersectionValues(*[[10, 30, 16, 18], [23, 30, 30, 6, 10, 26, 9, 27, 6, 16, 18, 10, 27, 2, 20, 7, 16]]) == [4, 7]
assert my_solution.findIntersectionValues(*[[7, 23, 27, 20, 21, 29, 7, 27, 27, 18, 7, 6, 20, 10], [27, 27, 28, 24, 20, 4, 6, 17, 9, 29, 20, 14, 20]]) == [7, 7]
assert my_solution.findIntersectionValues(*[[15, 30, 6, 6], [15, 4, 16, 10, 7, 23, 24, 3, 4, 6, 14, 8, 18, 1, 29, 27, 2, 17]]) == [3, 2]
assert my_solution.findIntersectionValues(*[[24, 7, 8, 6, 22, 28, 22, 28, 7, 19], [3, 7, 28, 7, 3, 3]]) == [4, 3]
assert my_solution.findIntersectionValues(*[[23, 4, 26, 17, 23, 13], [24, 17, 20, 16, 1, 13, 17, 28, 17]]) == [2, 4]
assert my_solution.findIntersectionValues(*[[5, 8, 18, 27, 16, 29, 27, 12, 1, 29, 16, 27, 22, 19, 14, 12, 11, 25], [24, 8, 16]]) == [3, 2]
assert my_solution.findIntersectionValues(*[[29, 17, 30, 17, 15, 30, 11, 2, 24, 28, 28, 30, 30, 27, 30, 2, 30, 9, 1, 7], [12, 12, 11, 21, 2, 28, 5, 24, 12, 17, 24, 29, 22, 19, 11, 17, 1, 23]]) == [10, 10]
assert my_solution.findIntersectionValues(*[[4, 27, 12, 16, 16, 21, 26, 7, 19, 21, 24, 26, 12, 24, 22, 12, 16], [1, 25, 8, 27, 23, 27, 27, 24]]) == [3, 4]
assert my_solution.findIntersectionValues(*[[27, 19, 20, 16, 24, 27, 27, 24], [30, 21, 21, 6, 17, 16]]) == [1, 1]
assert my_solution.findIntersectionValues(*[[3, 19, 21, 5, 24, 26, 22, 22, 5], [23, 26, 20, 14, 30, 9, 10, 24, 19, 22, 19, 6, 3, 20, 22, 22, 5, 24, 24]]) == [8, 11]
assert my_solution.findIntersectionValues(*[[13, 13, 29, 12], [29, 29, 13, 7, 30, 22]]) == [3, 3]
assert my_solution.findIntersectionValues(*[[30, 4, 16, 14, 14, 14, 20, 15, 20, 30, 6, 10, 14], [30, 16, 20, 2, 18, 10, 5, 6, 30, 20, 22, 18, 14, 23, 15]]) == [12, 9]
assert my_solution.findIntersectionValues(*[[22, 1, 22, 4, 11, 22, 4, 20, 11, 29, 11, 11, 4, 26, 20, 12, 20, 8, 26, 17], [4, 17, 7, 15]]) == [4, 2]
assert my_solution.findIntersectionValues(*[[30, 15, 16, 15, 11, 16, 26, 15, 21], [22, 25, 27, 2, 26, 20, 18, 15, 26, 20, 16]]) == [6, 4]
assert my_solution.findIntersectionValues(*[[5, 6], [13, 12, 8, 5, 19, 13, 27]]) == [1, 1]
assert my_solution.findIntersectionValues(*[[27, 28, 15, 20, 5, 13, 28, 29, 24, 29, 20, 15, 5, 20, 20, 25, 9, 20, 24, 20], [16, 20, 13, 24, 11]]) == [9, 3]
assert my_solution.findIntersectionValues(*[[25, 7, 18], [28, 1, 14, 22, 24, 8, 25, 17]]) == [1, 1]
