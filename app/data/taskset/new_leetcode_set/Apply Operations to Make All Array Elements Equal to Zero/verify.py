
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.checkArray(*[[2, 2, 3, 1, 1, 0], 3]) == True
assert my_solution.checkArray(*[[1, 3, 1, 1], 2]) == False
assert my_solution.checkArray(*[[60, 72, 87, 89, 63, 52, 64, 62, 31, 37, 57, 83, 98, 94, 92, 77, 94, 91, 87, 100, 91, 91, 50, 26], 4]) == True
assert my_solution.checkArray(*[[63, 40, 30, 0, 72, 53], 1]) == True
assert my_solution.checkArray(*[[59, 60, 99, 99, 99, 99, 99, 99, 99, 40, 39, 0], 9]) == True
assert my_solution.checkArray(*[[24, 24, 14, 37, 31, 88, 94, 38, 94, 0, 100, 100, 4, 46, 5, 50, 0, 33, 22, 25, 0], 10]) == False
assert my_solution.checkArray(*[[0, 0, 51, 67, 80, 98, 88, 75, 89, 83, 100, 70, 77, 82, 57, 100, 80, 69, 19, 17], 3]) == True
assert my_solution.checkArray(*[[22], 1]) == True
assert my_solution.checkArray(*[[22, 4, 1, 25, 68, 30, 97, 99, 100, 22, 20, 39, 85, 68, 3, 1, 1, 74], 4]) == False
assert my_solution.checkArray(*[[8, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 43, 0], 25]) == True
assert my_solution.checkArray(*[[27, 99, 7, 1, 94, 63, 84, 46, 76, 35, 97, 77, 19, 72, 3], 2]) == False
assert my_solution.checkArray(*[[0, 0, 39, 84, 86, 94, 55, 10, 8, 0], 4]) == True
assert my_solution.checkArray(*[[60, 78, 96, 97, 97, 97, 49, 7, 97, 97, 97, 99, 97, 97, 97, 97, 85, 97, 97, 97, 37, 5, 1], 20]) == False
assert my_solution.checkArray(*[[12, 79, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 83, 16, 0], 24]) == True
assert my_solution.checkArray(*[[0, 0, 33, 72, 86, 53, 14], 3]) == True
assert my_solution.checkArray(*[[0, 0, 8, 64, 89, 89, 89, 89, 89, 89, 89, 89, 89, 89, 89, 89, 89, 89, 89, 89, 89, 89, 89, 89, 89, 89, 89, 81, 25], 25]) == True
assert my_solution.checkArray(*[[84, 0, 68, 95, 95, 0, 25, 0, 7, 71, 4, 68, 23, 97, 80, 0], 1]) == True
assert my_solution.checkArray(*[[48, 48, 48, 48, 48], 5]) == True
assert my_solution.checkArray(*[[34, 34, 99, 93, 93, 26, 99, 100, 94, 94, 82, 86, 100, 100, 87, 100, 100, 100, 100, 100, 63, 100, 100, 66, 17, 10, 8, 7, 3, 1], 23]) == False
assert my_solution.checkArray(*[[67, 98, 97, 99, 98, 97, 97, 96, 99, 99, 99, 42, 68, 18, 99, 44, 95, 79, 1, 16, 49, 1, 2, 2, 0], 16]) == False
