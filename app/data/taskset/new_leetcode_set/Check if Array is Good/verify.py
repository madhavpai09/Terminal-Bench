
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.isGood(*[[2, 1, 3]]) == False
assert my_solution.isGood(*[[1, 3, 3, 2]]) == True
assert my_solution.isGood(*[[1, 1]]) == True
assert my_solution.isGood(*[[3, 4, 4, 1, 2, 1]]) == False
assert my_solution.isGood(*[[1]]) == False
assert my_solution.isGood(*[[2]]) == False
assert my_solution.isGood(*[[3]]) == False
assert my_solution.isGood(*[[4]]) == False
assert my_solution.isGood(*[[5]]) == False
assert my_solution.isGood(*[[6]]) == False
assert my_solution.isGood(*[[8]]) == False
assert my_solution.isGood(*[[9]]) == False
assert my_solution.isGood(*[[10]]) == False
assert my_solution.isGood(*[[12]]) == False
assert my_solution.isGood(*[[13]]) == False
assert my_solution.isGood(*[[14]]) == False
assert my_solution.isGood(*[[15]]) == False
assert my_solution.isGood(*[[82]]) == False
assert my_solution.isGood(*[[1, 8]]) == False
assert my_solution.isGood(*[[1, 13]]) == False
