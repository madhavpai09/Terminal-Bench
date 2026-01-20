
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.numberOfEmployeesWhoMetTarget(*[[0, 1, 2, 3, 4], 2]) == 3
assert my_solution.numberOfEmployeesWhoMetTarget(*[[5, 1, 4, 2, 2], 6]) == 0
assert my_solution.numberOfEmployeesWhoMetTarget(*[[98], 5]) == 1
assert my_solution.numberOfEmployeesWhoMetTarget(*[[19], 13]) == 1
assert my_solution.numberOfEmployeesWhoMetTarget(*[[70], 13]) == 1
assert my_solution.numberOfEmployeesWhoMetTarget(*[[26], 14]) == 1
assert my_solution.numberOfEmployeesWhoMetTarget(*[[2], 16]) == 0
assert my_solution.numberOfEmployeesWhoMetTarget(*[[77], 19]) == 1
assert my_solution.numberOfEmployeesWhoMetTarget(*[[6], 21]) == 0
assert my_solution.numberOfEmployeesWhoMetTarget(*[[27], 21]) == 1
assert my_solution.numberOfEmployeesWhoMetTarget(*[[36], 22]) == 1
assert my_solution.numberOfEmployeesWhoMetTarget(*[[42], 25]) == 1
assert my_solution.numberOfEmployeesWhoMetTarget(*[[70], 27]) == 1
assert my_solution.numberOfEmployeesWhoMetTarget(*[[2], 28]) == 0
assert my_solution.numberOfEmployeesWhoMetTarget(*[[14], 31]) == 0
assert my_solution.numberOfEmployeesWhoMetTarget(*[[45], 34]) == 1
assert my_solution.numberOfEmployeesWhoMetTarget(*[[44], 35]) == 1
assert my_solution.numberOfEmployeesWhoMetTarget(*[[11], 39]) == 0
assert my_solution.numberOfEmployeesWhoMetTarget(*[[71], 39]) == 1
assert my_solution.numberOfEmployeesWhoMetTarget(*[[91], 45]) == 1
