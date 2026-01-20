
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.maximumCostSubstring(*['adaa', 'd', [-1000]]) == 2
assert my_solution.maximumCostSubstring(*['abc', 'abc', [-1, -1, -1]]) == 0
assert my_solution.maximumCostSubstring(*['hghhghgghh', 'hg', [2, 3]]) == 24
assert my_solution.maximumCostSubstring(*['ddzddzd', 'zfd', [-4, 2, -2]]) == 0
assert my_solution.maximumCostSubstring(*['kqqqqqkkkq', 'kq', [-6, 6]]) == 30
assert my_solution.maximumCostSubstring(*['pprpf', 'frep', [-5, -4, -4, 3]]) == 6
assert my_solution.maximumCostSubstring(*['eggggeee', 'ge', [5, 3]]) == 32
assert my_solution.maximumCostSubstring(*['ssss', 's', [3]]) == 12
assert my_solution.maximumCostSubstring(*['ffff', 'f', [1]]) == 4
assert my_solution.maximumCostSubstring(*['xuusmmums', 'sxmu', [-6, 5, 0, 5]]) == 15
assert my_solution.maximumCostSubstring(*['axaaxxaxa', 'ax', [-6, 1]]) == 2
assert my_solution.maximumCostSubstring(*['ffkfuft', 'utkf', [3, -6, 3, 6]]) == 30
assert my_solution.maximumCostSubstring(*['ll', 'il', [3, -6]]) == 0
assert my_solution.maximumCostSubstring(*['hwwqwwqqqh', 'wihq', [-2, -5, -4, 4]]) == 12
assert my_solution.maximumCostSubstring(*['qjjjqqq', 'zqj', [-4, 3, 4]]) == 24
assert my_solution.maximumCostSubstring(*['talaqlt', 'tqla', [4, 3, 3, -2]]) == 13
assert my_solution.maximumCostSubstring(*['qqqqqqqqqq', 'q', [0]]) == 0
assert my_solution.maximumCostSubstring(*['tt', 't', [-2]]) == 0
assert my_solution.maximumCostSubstring(*['zox', 'zoxr', [2, -5, -4, -5]]) == 2
assert my_solution.maximumCostSubstring(*['ddddddd', 'd', [-3]]) == 0
