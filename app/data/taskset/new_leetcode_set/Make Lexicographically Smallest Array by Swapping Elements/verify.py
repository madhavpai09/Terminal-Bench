
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.lexicographicallySmallestArray(*[[1, 5, 3, 9, 8], 2]) == [1, 3, 5, 8, 9]
assert my_solution.lexicographicallySmallestArray(*[[1, 7, 6, 18, 2, 1], 3]) == [1, 6, 7, 18, 1, 2]
assert my_solution.lexicographicallySmallestArray(*[[1, 7, 28, 19, 10], 3]) == [1, 7, 28, 19, 10]
assert my_solution.lexicographicallySmallestArray(*[[1000000000], 1]) == [1000000000]
assert my_solution.lexicographicallySmallestArray(*[[1, 60, 34, 84, 62, 56, 39, 76, 49, 38], 4]) == [1, 56, 34, 84, 60, 62, 38, 76, 49, 39]
assert my_solution.lexicographicallySmallestArray(*[[1, 81, 10, 79, 36, 2, 87, 12, 20, 77], 7]) == [1, 77, 10, 79, 36, 2, 81, 12, 20, 87]
assert my_solution.lexicographicallySmallestArray(*[[2, 71, 5, 87, 11, 15, 70, 70, 14, 38], 14]) == [2, 70, 5, 87, 11, 14, 70, 71, 15, 38]
assert my_solution.lexicographicallySmallestArray(*[[4, 3, 23, 84, 34, 88, 44, 44, 18, 15], 3]) == [3, 4, 23, 84, 34, 88, 44, 44, 15, 18]
assert my_solution.lexicographicallySmallestArray(*[[4, 34, 29, 73, 51, 11, 8, 53, 98, 47], 10]) == [4, 29, 34, 73, 47, 8, 11, 51, 98, 53]
assert my_solution.lexicographicallySmallestArray(*[[4, 52, 38, 59, 71, 27, 31, 83, 88, 10], 14]) == [4, 27, 31, 38, 52, 59, 71, 83, 88, 10]
assert my_solution.lexicographicallySmallestArray(*[[4, 68, 8, 10, 70, 62, 27, 5, 42, 61], 11]) == [4, 61, 5, 8, 62, 68, 27, 10, 42, 70]
assert my_solution.lexicographicallySmallestArray(*[[5, 9, 35, 60, 73, 91, 61, 57, 87, 76], 11]) == [5, 9, 35, 57, 73, 76, 60, 61, 87, 91]
assert my_solution.lexicographicallySmallestArray(*[[5, 15, 68, 47, 49, 67, 9, 6, 35, 14], 4]) == [5, 14, 67, 47, 49, 68, 6, 9, 35, 15]
assert my_solution.lexicographicallySmallestArray(*[[5, 16, 43, 15, 66, 21, 58, 74, 55, 66], 9]) == [5, 15, 43, 16, 55, 21, 58, 66, 66, 74]
assert my_solution.lexicographicallySmallestArray(*[[5, 30, 92, 4, 31, 2, 17, 39, 15, 7], 3]) == [2, 30, 92, 4, 31, 5, 15, 39, 17, 7]
assert my_solution.lexicographicallySmallestArray(*[[5, 38, 68, 80, 64, 79, 50, 5, 8, 95], 7]) == [5, 38, 64, 79, 68, 80, 50, 5, 8, 95]
assert my_solution.lexicographicallySmallestArray(*[[5, 100, 44, 45, 16, 30, 14, 65, 83, 64], 15]) == [5, 100, 14, 16, 30, 44, 45, 64, 83, 65]
assert my_solution.lexicographicallySmallestArray(*[[6, 57, 100, 67, 4, 63, 47, 59, 21, 66], 8]) == [4, 57, 100, 59, 6, 63, 47, 66, 21, 67]
assert my_solution.lexicographicallySmallestArray(*[[6, 70, 90, 1, 33, 81, 60, 80, 68, 44], 7]) == [1, 68, 90, 6, 33, 80, 60, 81, 70, 44]
assert my_solution.lexicographicallySmallestArray(*[[6, 74, 74, 74, 30, 70, 91, 74, 76, 41], 1]) == [6, 74, 74, 74, 30, 70, 91, 74, 76, 41]
