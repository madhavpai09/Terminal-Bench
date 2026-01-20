
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.countBeautifulPairs(*[[2, 5, 1, 4]]) == 5
assert my_solution.countBeautifulPairs(*[[11, 21, 12]]) == 2
assert my_solution.countBeautifulPairs(*[[31, 25, 72, 79, 74]]) == 7
assert my_solution.countBeautifulPairs(*[[84, 91, 18, 59, 27, 9, 81, 33, 17, 58]]) == 37
assert my_solution.countBeautifulPairs(*[[8, 75, 28, 35, 21, 13, 21]]) == 19
assert my_solution.countBeautifulPairs(*[[35, 52, 74, 92, 25, 65, 77, 1, 73, 32]]) == 37
assert my_solution.countBeautifulPairs(*[[68, 8, 84, 14, 88, 42, 53]]) == 7
assert my_solution.countBeautifulPairs(*[[64, 23, 99, 83, 5, 21, 76, 34, 99, 63]]) == 25
assert my_solution.countBeautifulPairs(*[[18, 64, 12, 21]]) == 5
assert my_solution.countBeautifulPairs(*[[78, 36, 58, 88]]) == 6
assert my_solution.countBeautifulPairs(*[[99, 26, 92, 91, 53, 24, 25, 92, 73]]) == 22
assert my_solution.countBeautifulPairs(*[[51, 65, 87, 6, 17, 32, 14, 42, 46]]) == 19
assert my_solution.countBeautifulPairs(*[[43, 9, 75, 76, 25, 96, 46, 85, 19, 29]]) == 32
assert my_solution.countBeautifulPairs(*[[5, 24]]) == 1
assert my_solution.countBeautifulPairs(*[[26, 76, 24, 96, 82, 97, 97, 72, 35]]) == 25
assert my_solution.countBeautifulPairs(*[[77, 82, 94, 55]]) == 5
assert my_solution.countBeautifulPairs(*[[82, 3, 89, 52, 96, 72, 27, 59]]) == 17
assert my_solution.countBeautifulPairs(*[[97, 6, 46, 88, 41, 52, 46, 4, 17]]) == 17
assert my_solution.countBeautifulPairs(*[[95, 6]]) == 0
assert my_solution.countBeautifulPairs(*[[69, 63, 24, 1, 71, 55, 46, 4, 61]]) == 26
