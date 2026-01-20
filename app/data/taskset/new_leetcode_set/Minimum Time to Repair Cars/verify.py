
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.repairCars(*[[4, 2, 3, 1], 10]) == 16
assert my_solution.repairCars(*[[5, 1, 8], 6]) == 16
assert my_solution.repairCars(*[[1, 1, 3, 3], 74]) == 576
assert my_solution.repairCars(*[[3, 3, 1, 2, 1, 1, 3, 2, 1], 58]) == 75
assert my_solution.repairCars(*[[1, 3, 1, 2, 1, 1], 21]) == 18
assert my_solution.repairCars(*[[2, 2, 3, 3, 1, 3, 3, 1, 3], 32]) == 32
assert my_solution.repairCars(*[[3, 1, 3, 3, 1, 3], 42]) == 108
assert my_solution.repairCars(*[[3, 2, 2, 2, 1, 3, 1], 21]) == 18
assert my_solution.repairCars(*[[2, 2, 1, 3, 1, 2, 1, 1, 1, 3], 36]) == 25
assert my_solution.repairCars(*[[3, 2, 1, 3, 3, 2, 1, 1], 25]) == 25
assert my_solution.repairCars(*[[3, 3, 2], 51]) == 768
assert my_solution.repairCars(*[[3, 1, 1, 1, 1, 2, 2, 3, 2], 9]) == 3
assert my_solution.repairCars(*[[3, 1, 3, 2, 3, 1, 1, 3, 1, 1], 24]) == 12
assert my_solution.repairCars(*[[1, 3, 1, 3, 3, 3, 2, 1], 77]) == 192
assert my_solution.repairCars(*[[3, 2, 3, 3], 51]) == 450
assert my_solution.repairCars(*[[3], 52]) == 8112
assert my_solution.repairCars(*[[1, 2, 2, 1, 2, 3, 2, 2, 2], 4]) == 2
assert my_solution.repairCars(*[[1, 3, 1], 62]) == 588
assert my_solution.repairCars(*[[1, 2, 1, 1, 3, 2, 2, 1, 2], 78]) == 121
assert my_solution.repairCars(*[[3, 2, 3], 77]) == 1728
