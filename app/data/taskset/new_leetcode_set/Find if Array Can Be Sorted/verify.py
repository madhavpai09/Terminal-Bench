
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.canSortArray(*[[8, 4, 2, 30, 15]]) == True
assert my_solution.canSortArray(*[[1, 2, 3, 4, 5]]) == True
assert my_solution.canSortArray(*[[3, 16, 8, 4, 2]]) == False
assert my_solution.canSortArray(*[[1]]) == True
assert my_solution.canSortArray(*[[4]]) == True
assert my_solution.canSortArray(*[[7]]) == True
assert my_solution.canSortArray(*[[10]]) == True
assert my_solution.canSortArray(*[[18]]) == True
assert my_solution.canSortArray(*[[30]]) == True
assert my_solution.canSortArray(*[[1, 2]]) == True
assert my_solution.canSortArray(*[[2, 17]]) == True
assert my_solution.canSortArray(*[[20, 16]]) == False
assert my_solution.canSortArray(*[[21, 17]]) == False
assert my_solution.canSortArray(*[[24, 12]]) == True
assert my_solution.canSortArray(*[[26, 10]]) == False
assert my_solution.canSortArray(*[[128, 128]]) == True
assert my_solution.canSortArray(*[[1, 2, 3]]) == True
assert my_solution.canSortArray(*[[1, 256, 64]]) == True
assert my_solution.canSortArray(*[[2, 28, 9]]) == False
assert my_solution.canSortArray(*[[6, 6, 192]]) == True
