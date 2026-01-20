
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.findValueOfPartition(*[[1, 3, 2, 4]]) == 1
assert my_solution.findValueOfPartition(*[[100, 1, 10]]) == 9
assert my_solution.findValueOfPartition(*[[59, 51, 1, 98, 73]]) == 8
assert my_solution.findValueOfPartition(*[[84, 11, 100, 100, 75]]) == 0
assert my_solution.findValueOfPartition(*[[59, 76, 2, 26, 49]]) == 10
assert my_solution.findValueOfPartition(*[[78, 36, 2, 70, 64, 24, 34, 63, 21, 49]]) == 1
assert my_solution.findValueOfPartition(*[[43, 35, 19, 1, 21, 11, 59, 38, 47, 1]]) == 0
assert my_solution.findValueOfPartition(*[[35, 74, 58, 56]]) == 2
assert my_solution.findValueOfPartition(*[[54, 75, 6, 20, 49, 94, 97, 20, 97]]) == 0
assert my_solution.findValueOfPartition(*[[92, 13, 30, 32, 89]]) == 2
assert my_solution.findValueOfPartition(*[[49, 10, 36]]) == 13
assert my_solution.findValueOfPartition(*[[37, 50, 25, 65, 41, 31]]) == 4
assert my_solution.findValueOfPartition(*[[14, 20, 59, 42]]) == 6
assert my_solution.findValueOfPartition(*[[43, 57, 73, 45, 30, 77, 17, 38, 20]]) == 2
assert my_solution.findValueOfPartition(*[[11, 17, 65, 55, 85, 74, 32]]) == 6
assert my_solution.findValueOfPartition(*[[84, 93]]) == 9
assert my_solution.findValueOfPartition(*[[31, 61, 78, 15, 52]]) == 9
assert my_solution.findValueOfPartition(*[[100, 65, 64, 8, 61, 17]]) == 1
assert my_solution.findValueOfPartition(*[[3, 72, 8, 90]]) == 5
assert my_solution.findValueOfPartition(*[[55, 55, 23]]) == 0
