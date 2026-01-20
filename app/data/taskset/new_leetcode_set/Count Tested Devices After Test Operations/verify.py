
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.countTestedDevices(*[[1, 1, 2, 1, 3]]) == 3
assert my_solution.countTestedDevices(*[[0, 1, 2]]) == 2
assert my_solution.countTestedDevices(*[[0]]) == 0
assert my_solution.countTestedDevices(*[[1]]) == 1
assert my_solution.countTestedDevices(*[[0, 0]]) == 0
assert my_solution.countTestedDevices(*[[0, 1]]) == 1
assert my_solution.countTestedDevices(*[[0, 2]]) == 1
assert my_solution.countTestedDevices(*[[1, 0]]) == 1
assert my_solution.countTestedDevices(*[[1, 2]]) == 2
assert my_solution.countTestedDevices(*[[2, 1]]) == 1
assert my_solution.countTestedDevices(*[[2, 2]]) == 2
assert my_solution.countTestedDevices(*[[0, 0, 1]]) == 1
assert my_solution.countTestedDevices(*[[0, 0, 2]]) == 1
assert my_solution.countTestedDevices(*[[1, 1, 0]]) == 1
assert my_solution.countTestedDevices(*[[1, 2, 0]]) == 2
assert my_solution.countTestedDevices(*[[1, 3, 1]]) == 2
assert my_solution.countTestedDevices(*[[2, 0, 1]]) == 1
assert my_solution.countTestedDevices(*[[2, 2, 0]]) == 2
assert my_solution.countTestedDevices(*[[2, 2, 2]]) == 2
assert my_solution.countTestedDevices(*[[3, 0, 3]]) == 2
