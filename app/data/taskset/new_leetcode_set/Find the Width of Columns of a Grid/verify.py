
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.findColumnWidth(*[[[1], [22], [333]]]) == [3]
assert my_solution.findColumnWidth(*[[[-15, 1, 3], [15, 7, 12], [5, 6, -2]]]) == [3, 1, 2]
assert my_solution.findColumnWidth(*[[[0]]]) == [1]
assert my_solution.findColumnWidth(*[[[0], [0], [0]]]) == [1]
assert my_solution.findColumnWidth(*[[[0, 0, 0], [0, 0, 0], [0, 0, 0]]]) == [1, 1, 1]
assert my_solution.findColumnWidth(*[[[0, 3, 0], [2, 3, 0], [1, 3, 0]]]) == [1, 1, 1]
assert my_solution.findColumnWidth(*[[[-39, -5, -93], [-87, -69, 28], [-88, 25, 23]]]) == [3, 3, 3]
assert my_solution.findColumnWidth(*[[[37, 86, -11], [85, -65, 83], [69, -93, 52]]]) == [2, 3, 3]
assert my_solution.findColumnWidth(*[[[93, -20, -4], [6, -20, -19]]]) == [2, 3, 3]
assert my_solution.findColumnWidth(*[[[-19, -67, -92], [38, -47, -1]]]) == [3, 3, 3]
assert my_solution.findColumnWidth(*[[[-90, -89, -51]]]) == [3, 3, 3]
assert my_solution.findColumnWidth(*[[[31, 100, -6], [10, 0, 68], [-42, -37, -36]]]) == [3, 3, 3]
assert my_solution.findColumnWidth(*[[[73, -24, 41], [-23, 44, -88], [91, -22, 19]]]) == [3, 3, 3]
assert my_solution.findColumnWidth(*[[[-22, -77, 76], [48, -46, 81]]]) == [3, 3, 2]
assert my_solution.findColumnWidth(*[[[-34, -87, -54], [46, 98, 82], [-3, -99, -64]]]) == [3, 3, 3]
assert my_solution.findColumnWidth(*[[[-92, 24, 81], [-20, -20, -14]]]) == [3, 3, 3]
assert my_solution.findColumnWidth(*[[[-4, 0, -1, 3, 9, 8, 6], [-2, 5, -5, -7, -2, -6, 7], [4, -4, 1, 7, 0, 6, 8], [-6, 2, -5, 0, 9, 1, -6]]]) == [2, 2, 2, 2, 2, 2, 2]
assert my_solution.findColumnWidth(*[[[51, 84, 31, 44, -22, -70], [71, -37, -33, -48, -97, -32], [18, 95, -62, -63, 5, 63], [-18, -41, -58, -25, -17, -26], [67, -96, -77, 80, 59, -71], [-15, 20, -72, -27, 3, -97], [66, -1, 5, 80, 57, -58]]]) == [3, 3, 3, 3, 3, 3]
assert my_solution.findColumnWidth(*[[[325, -483, 796, 121], [-757, -920, -928, 783], [73, -136, 628, -724], [979, 224, -39, -884], [-612, -304, 259, 378], [7, 335, -650, -131], [-351, -104, 640, -258]]]) == [4, 4, 4, 4]
assert my_solution.findColumnWidth(*[[[2911, -805, 5477, -3349, 163, -6644], [4851, 2990, 2578, 1124, 2897, -1781], [-2153, 1774, -8238, -2894, 4845, 9608]]]) == [5, 4, 5, 5, 4, 5]
