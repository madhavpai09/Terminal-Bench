
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.numberOfWays(*['abcd', 'cdab', 2]) == 2
assert my_solution.numberOfWays(*['ababab', 'ababab', 1]) == 2
assert my_solution.numberOfWays(*['goxoq', 'dfqgl', 244326024901249]) == 0
assert my_solution.numberOfWays(*['ceoceo', 'eoceoc', 4]) == 208
assert my_solution.numberOfWays(*['ib', 'ib', 10]) == 1
assert my_solution.numberOfWays(*['ttttttt', 'ttttttt', 5]) == 7776
assert my_solution.numberOfWays(*['aaaa', 'aaaa', 8]) == 6561
assert my_solution.numberOfWays(*['meplrmeplr', 'eplrmeplrm', 7]) == 956594
assert my_solution.numberOfWays(*['dsmn', 'smnd', 3]) == 7
assert my_solution.numberOfWays(*['jjj', 'jjj', 10]) == 1024
assert my_solution.numberOfWays(*['rrrrr', 'rrrrr', 1]) == 4
assert my_solution.numberOfWays(*['fefe', 'fefe', 9]) == 9841
assert my_solution.numberOfWays(*['pfly', 'wvqr', 840550364246523]) == 0
assert my_solution.numberOfWays(*['ltjwwltjww', 'jwwltjwwlt', 1]) == 2
assert my_solution.numberOfWays(*['mb', 'mb', 3]) == 0
assert my_solution.numberOfWays(*['jjjjjjjjjj', 'jjjjjjjjjj', 3]) == 729
assert my_solution.numberOfWays(*['oqytlmi', 'lmioqyt', 8]) == 239945
assert my_solution.numberOfWays(*['hpcg', 'pcgh', 5]) == 61
assert my_solution.numberOfWays(*['bqbqbqbqbq', 'bqbqbqbqbq', 9]) == 193710244
assert my_solution.numberOfWays(*['ccccccccc', 'ccccccccc', 7]) == 2097152
