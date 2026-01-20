
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.maxPartitionsAfterOperations(*['accca', 2]) == 3
assert my_solution.maxPartitionsAfterOperations(*['aabaab', 3]) == 1
assert my_solution.maxPartitionsAfterOperations(*['xxyz', 1]) == 4
assert my_solution.maxPartitionsAfterOperations(*['c', 3]) == 1
assert my_solution.maxPartitionsAfterOperations(*['c', 5]) == 1
assert my_solution.maxPartitionsAfterOperations(*['h', 17]) == 1
assert my_solution.maxPartitionsAfterOperations(*['p', 13]) == 1
assert my_solution.maxPartitionsAfterOperations(*['ab', 5]) == 1
assert my_solution.maxPartitionsAfterOperations(*['ba', 1]) == 2
assert my_solution.maxPartitionsAfterOperations(*['ba', 3]) == 1
assert my_solution.maxPartitionsAfterOperations(*['ca', 1]) == 2
assert my_solution.maxPartitionsAfterOperations(*['fh', 8]) == 1
assert my_solution.maxPartitionsAfterOperations(*['abb', 1]) == 3
assert my_solution.maxPartitionsAfterOperations(*['aca', 2]) == 2
assert my_solution.maxPartitionsAfterOperations(*['acb', 2]) == 2
assert my_solution.maxPartitionsAfterOperations(*['acb', 4]) == 1
assert my_solution.maxPartitionsAfterOperations(*['bab', 3]) == 1
assert my_solution.maxPartitionsAfterOperations(*['cba', 1]) == 3
assert my_solution.maxPartitionsAfterOperations(*['cbb', 5]) == 1
assert my_solution.maxPartitionsAfterOperations(*['cca', 5]) == 1
