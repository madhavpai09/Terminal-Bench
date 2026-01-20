
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.relocateMarbles(*[[1, 6, 7, 8], [1, 7, 2], [2, 9, 5]]) == [5, 6, 8, 9]
assert my_solution.relocateMarbles(*[[1, 1, 3, 3], [1, 3], [2, 2]]) == [2]
assert my_solution.relocateMarbles(*[[5, 7, 8, 15], [5, 7, 8, 9], [9, 15, 2, 7]]) == [2, 7, 15]
assert my_solution.relocateMarbles(*[[4, 6, 6, 9, 18], [18, 6, 17, 4, 9, 19, 2], [23, 17, 20, 19, 11, 2, 20]]) == [11, 20, 23]
assert my_solution.relocateMarbles(*[[3, 4], [4, 3, 1, 2, 2, 3, 2, 4, 1], [3, 1, 2, 2, 3, 2, 4, 1, 1]]) == [1]
assert my_solution.relocateMarbles(*[[5, 13, 22, 23, 23, 33], [13, 5, 12], [1, 12, 13]]) == [1, 13, 22, 23, 33]
assert my_solution.relocateMarbles(*[[21, 24, 35, 72, 77, 82, 82, 96, 97, 97], [82, 76, 3, 97], [76, 3, 52, 27]]) == [21, 24, 27, 35, 52, 72, 77, 96]
assert my_solution.relocateMarbles(*[[4, 6, 17, 41, 46, 46, 52, 57], [4], [62]]) == [6, 17, 41, 46, 52, 57, 62]
assert my_solution.relocateMarbles(*[[1, 4, 10, 24, 46, 55, 61, 63, 71], [10, 52, 1, 80, 63, 55, 4, 46, 71, 24], [52, 42, 80, 55, 50, 62, 60, 17, 46, 38]]) == [17, 38, 42, 46, 50, 60, 61, 62]
assert my_solution.relocateMarbles(*[[8, 9, 16, 17, 23], [8, 5, 16, 2, 9], [5, 20, 2, 18, 22]]) == [17, 18, 20, 22, 23]
assert my_solution.relocateMarbles(*[[12, 37, 46, 47, 49, 55, 59, 65, 71, 88], [88, 59, 71], [81, 39, 73]]) == [12, 37, 39, 46, 47, 49, 55, 65, 73, 81]
assert my_solution.relocateMarbles(*[[2, 45, 45, 48, 51, 57, 67, 73, 78, 78], [78, 67, 45, 34, 51, 62, 48, 95, 2, 67], [34, 65, 62, 95, 62, 12, 85, 67, 79, 71]]) == [12, 57, 65, 71, 73, 79, 85]
assert my_solution.relocateMarbles(*[[1, 2], [1, 2, 3], [2, 3, 2]]) == [2]
assert my_solution.relocateMarbles(*[[7, 19, 28, 34, 36, 36, 47], [36, 33, 34, 28, 41, 19, 14, 47, 28, 40], [33, 41, 27, 47, 14, 40, 46, 28, 42, 16]]) == [7, 16, 27, 42, 46]
assert my_solution.relocateMarbles(*[[1, 1, 1], [1], [7]]) == [7]
assert my_solution.relocateMarbles(*[[1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]) == [1]
assert my_solution.relocateMarbles(*[[5, 9, 17, 20, 29, 29], [20, 5, 1, 29, 22, 21, 9, 36, 33, 1], [1, 22, 21, 36, 36, 15, 33, 1, 3, 15]]) == [3, 15, 17]
assert my_solution.relocateMarbles(*[[1], [1, 1, 1, 1], [1, 1, 1, 1]]) == [1]
assert my_solution.relocateMarbles(*[[27, 41, 50, 52, 57, 60, 65, 67, 70], [52, 67, 70, 50, 57, 27, 47], [45, 45, 61, 47, 21, 65, 60]]) == [21, 41, 45, 60, 61, 65]
assert my_solution.relocateMarbles(*[[2, 3, 7], [2, 7, 8, 8, 3, 5, 1, 4], [8, 5, 8, 1, 4, 4, 4, 5]]) == [5]
