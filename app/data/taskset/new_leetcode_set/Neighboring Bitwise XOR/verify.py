
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.doesValidArrayExist(*[[1, 1, 0]]) == True
assert my_solution.doesValidArrayExist(*[[1, 1]]) == True
assert my_solution.doesValidArrayExist(*[[1, 0]]) == False
assert my_solution.doesValidArrayExist(*[[0]]) == True
assert my_solution.doesValidArrayExist(*[[1]]) == False
assert my_solution.doesValidArrayExist(*[[0, 0]]) == True
assert my_solution.doesValidArrayExist(*[[0, 1]]) == False
assert my_solution.doesValidArrayExist(*[[0, 0, 0]]) == True
assert my_solution.doesValidArrayExist(*[[0, 0, 1]]) == False
assert my_solution.doesValidArrayExist(*[[0, 1, 0]]) == False
assert my_solution.doesValidArrayExist(*[[0, 1, 1]]) == True
assert my_solution.doesValidArrayExist(*[[1, 0, 0]]) == False
assert my_solution.doesValidArrayExist(*[[1, 0, 1]]) == True
assert my_solution.doesValidArrayExist(*[[1, 1, 1]]) == False
assert my_solution.doesValidArrayExist(*[[0, 0, 0, 0]]) == True
assert my_solution.doesValidArrayExist(*[[0, 0, 0, 1]]) == False
assert my_solution.doesValidArrayExist(*[[0, 0, 1, 0]]) == False
assert my_solution.doesValidArrayExist(*[[0, 0, 1, 1]]) == True
assert my_solution.doesValidArrayExist(*[[0, 1, 0, 0]]) == False
assert my_solution.doesValidArrayExist(*[[0, 1, 0, 1]]) == True
