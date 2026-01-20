
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.maxFrequencyElements(*[[1, 2, 2, 3, 1, 4]]) == 4
assert my_solution.maxFrequencyElements(*[[1, 2, 3, 4, 5]]) == 5
assert my_solution.maxFrequencyElements(*[[15]]) == 1
assert my_solution.maxFrequencyElements(*[[10, 12, 11, 9, 6, 19, 11]]) == 2
assert my_solution.maxFrequencyElements(*[[2, 12, 17, 18, 11]]) == 5
assert my_solution.maxFrequencyElements(*[[19, 19, 19, 20, 19, 8, 19]]) == 5
assert my_solution.maxFrequencyElements(*[[1, 1, 1, 1]]) == 4
assert my_solution.maxFrequencyElements(*[[10, 1, 12, 10, 10, 19, 10]]) == 4
assert my_solution.maxFrequencyElements(*[[1, 1, 1, 20, 6, 1]]) == 4
assert my_solution.maxFrequencyElements(*[[17, 17]]) == 2
assert my_solution.maxFrequencyElements(*[[6, 13, 15, 15, 11, 6, 7, 12, 4, 11]]) == 6
assert my_solution.maxFrequencyElements(*[[1, 2]]) == 2
assert my_solution.maxFrequencyElements(*[[14, 14, 17]]) == 2
assert my_solution.maxFrequencyElements(*[[17, 17, 2, 12, 20, 17, 12]]) == 3
assert my_solution.maxFrequencyElements(*[[3, 9, 11, 11, 20]]) == 2
assert my_solution.maxFrequencyElements(*[[8, 15, 8, 11, 8, 13, 12, 11, 8]]) == 4
assert my_solution.maxFrequencyElements(*[[17, 8, 17, 19, 17, 13, 17, 17, 17, 5]]) == 6
assert my_solution.maxFrequencyElements(*[[11]]) == 1
assert my_solution.maxFrequencyElements(*[[5]]) == 1
assert my_solution.maxFrequencyElements(*[[4, 4, 10]]) == 2
