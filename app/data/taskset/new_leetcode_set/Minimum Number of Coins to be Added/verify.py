
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.minimumAddedCoins(*[[1, 4, 10], 19]) == 2
assert my_solution.minimumAddedCoins(*[[1, 4, 10, 5, 7, 19], 19]) == 1
assert my_solution.minimumAddedCoins(*[[1, 1, 1], 20]) == 3
assert my_solution.minimumAddedCoins(*[[1], 100000]) == 16
assert my_solution.minimumAddedCoins(*[[100000], 100000]) == 17
assert my_solution.minimumAddedCoins(*[[2], 5]) == 2
assert my_solution.minimumAddedCoins(*[[5, 6, 7], 10]) == 3
assert my_solution.minimumAddedCoins(*[[5, 6, 7], 15]) == 3
assert my_solution.minimumAddedCoins(*[[4, 11, 13, 15, 7, 5, 12, 11, 5, 9], 34]) == 2
assert my_solution.minimumAddedCoins(*[[8, 12, 9], 27]) == 3
assert my_solution.minimumAddedCoins(*[[2, 13, 7, 1, 11], 35]) == 1
assert my_solution.minimumAddedCoins(*[[10, 3, 5, 11, 6], 27]) == 2
assert my_solution.minimumAddedCoins(*[[6, 6, 6, 15, 4], 31]) == 2
assert my_solution.minimumAddedCoins(*[[6, 15, 6], 22]) == 3
assert my_solution.minimumAddedCoins(*[[8, 14, 15, 4, 14, 15, 8, 10, 8], 42]) == 2
assert my_solution.minimumAddedCoins(*[[9, 14, 14, 9, 14, 5, 12, 10, 11], 17]) == 3
assert my_solution.minimumAddedCoins(*[[14, 5, 13, 3, 7, 10, 10, 10], 32]) == 2
assert my_solution.minimumAddedCoins(*[[8, 6, 7, 12], 26]) == 3
assert my_solution.minimumAddedCoins(*[[15, 1, 12], 43]) == 4
assert my_solution.minimumAddedCoins(*[[4, 1, 4, 10], 16]) == 1
