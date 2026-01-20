
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.sumDistance(*[[-2, 0, 2], 'RLL', 3]) == 8
assert my_solution.sumDistance(*[[1, 0], 'RL', 2]) == 5
assert my_solution.sumDistance(*[[-10, -13, 10, 14, 11], 'LRLLR', 2]) == 146
assert my_solution.sumDistance(*[[1, -67, 68, -26, -13, -40, -56, 62, 21], 'LLLRLLRRR', 4]) == 2106
assert my_solution.sumDistance(*[[-36, -72, -41, 69, -14, 44, 58, -47, 45], 'LLLRRRLRL', 2]) == 2284
assert my_solution.sumDistance(*[[-16, 20, 11, 6, 0], 'LLLLR', 5]) == 154
assert my_solution.sumDistance(*[[-16, -84, 49, 51, -52, 90, -9, 68, -64, -43], 'LLLRLLRLLR', 9]) == 3344
assert my_solution.sumDistance(*[[-59, 39, -11, 53, 48, -54, 27, 17], 'RRLLLLRL', 7]) == 1440
assert my_solution.sumDistance(*[[-16, 11, 6, -15], 'RLRR', 2]) == 90
assert my_solution.sumDistance(*[[2, 3], 'RR', 7]) == 1
assert my_solution.sumDistance(*[[5, 7, -5], 'LRR', 9]) == 40
assert my_solution.sumDistance(*[[-3, 0], 'RR', 4]) == 3
assert my_solution.sumDistance(*[[8, -8, -21, -17, 15], 'RLLRL', 10]) == 242
assert my_solution.sumDistance(*[[4, 5, 3], 'RRR', 2]) == 4
assert my_solution.sumDistance(*[[12, 31, 24, 49, 37, -61, 3, 43], 'LRRRLRLL', 8]) == 1086
assert my_solution.sumDistance(*[[3, -47, -25, 15, 8, -27, -33, -16], 'RLRLRLRR', 8]) == 832
assert my_solution.sumDistance(*[[-73, -53, -75, -59, 99, -66, 66, -28, -98, -76], 'LRLRRRLRRR', 3]) == 3091
assert my_solution.sumDistance(*[[21, -27, -11, -42, 11, 42, 46, -26], 'RLLLLLLL', 6]) == 1160
assert my_solution.sumDistance(*[[-3, 1], 'RR', 7]) == 4
assert my_solution.sumDistance(*[[-59, 45, 15, 8, -4, -3, 9, 51], 'RLRLRRRR', 10]) == 1024
