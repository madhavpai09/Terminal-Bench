
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.findPeaks(*[[2, 4, 4]]) == []
assert my_solution.findPeaks(*[[1, 4, 3, 8, 5]]) == [1, 3]
assert my_solution.findPeaks(*[[1, 1, 1]]) == []
assert my_solution.findPeaks(*[[1, 1, 3]]) == []
assert my_solution.findPeaks(*[[1, 1, 5]]) == []
assert my_solution.findPeaks(*[[1, 2, 5]]) == []
assert my_solution.findPeaks(*[[1, 4, 1]]) == [1]
assert my_solution.findPeaks(*[[1, 4, 3]]) == [1]
assert my_solution.findPeaks(*[[1, 5, 5]]) == []
assert my_solution.findPeaks(*[[1, 6, 4]]) == [1]
assert my_solution.findPeaks(*[[2, 1, 1]]) == []
assert my_solution.findPeaks(*[[2, 1, 2]]) == []
assert my_solution.findPeaks(*[[2, 2, 3]]) == []
assert my_solution.findPeaks(*[[2, 2, 5]]) == []
assert my_solution.findPeaks(*[[2, 3, 2]]) == [1]
assert my_solution.findPeaks(*[[2, 3, 6]]) == []
assert my_solution.findPeaks(*[[2, 4, 3]]) == [1]
assert my_solution.findPeaks(*[[2, 4, 5]]) == []
assert my_solution.findPeaks(*[[2, 6, 4]]) == [1]
assert my_solution.findPeaks(*[[3, 3, 3]]) == []
