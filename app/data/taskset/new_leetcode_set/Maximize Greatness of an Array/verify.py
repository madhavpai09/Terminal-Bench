
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.maximizeGreatness(*[[1, 3, 5, 2, 1, 3, 1]]) == 4
assert my_solution.maximizeGreatness(*[[1, 2, 3, 4]]) == 3
assert my_solution.maximizeGreatness(*[[31, 25, 72, 79]]) == 3
assert my_solution.maximizeGreatness(*[[65, 84, 91, 18, 59, 27, 9, 81, 33, 17]]) == 9
assert my_solution.maximizeGreatness(*[[42, 8, 75, 28, 35, 21, 13, 21]]) == 6
assert my_solution.maximizeGreatness(*[[35, 52, 74, 92, 25, 65, 77, 1, 73]]) == 8
assert my_solution.maximizeGreatness(*[[43, 68, 8, 100]]) == 3
assert my_solution.maximizeGreatness(*[[14, 88, 42, 53, 98, 69, 64, 40, 60, 23]]) == 9
assert my_solution.maximizeGreatness(*[[21]]) == 0
assert my_solution.maximizeGreatness(*[[34, 99, 63, 23, 70, 18, 64, 12, 21, 21]]) == 8
assert my_solution.maximizeGreatness(*[[36, 58, 88, 58, 99, 26, 92, 91, 53, 10]]) == 8
assert my_solution.maximizeGreatness(*[[25, 20, 92]]) == 2
assert my_solution.maximizeGreatness(*[[63, 51, 65, 87, 6, 17, 32, 14, 42, 46]]) == 9
assert my_solution.maximizeGreatness(*[[43, 9, 75, 76, 25, 96, 46, 85, 19]]) == 8
assert my_solution.maximizeGreatness(*[[88, 2, 5, 24]]) == 3
assert my_solution.maximizeGreatness(*[[26, 76, 24, 96, 82, 97, 97, 72]]) == 6
assert my_solution.maximizeGreatness(*[[21, 77, 82, 30, 94]]) == 4
assert my_solution.maximizeGreatness(*[[76, 94, 51, 82, 3, 89, 52]]) == 6
assert my_solution.maximizeGreatness(*[[27, 59, 57, 97, 6, 46, 88, 41, 52]]) == 8
assert my_solution.maximizeGreatness(*[[4, 17, 2, 95, 6, 62]]) == 5
