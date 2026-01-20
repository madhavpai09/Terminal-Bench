
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.minimumBeautifulSubstrings(*['1011']) == 2
assert my_solution.minimumBeautifulSubstrings(*['111']) == 3
assert my_solution.minimumBeautifulSubstrings(*['0']) == -1
assert my_solution.minimumBeautifulSubstrings(*['100111000110111']) == 4
assert my_solution.minimumBeautifulSubstrings(*['100111000111']) == 3
assert my_solution.minimumBeautifulSubstrings(*['1001110001111']) == 4
assert my_solution.minimumBeautifulSubstrings(*['100111000111101']) == 4
assert my_solution.minimumBeautifulSubstrings(*['10110011100011']) == 3
assert my_solution.minimumBeautifulSubstrings(*['101101']) == 2
assert my_solution.minimumBeautifulSubstrings(*['101101101']) == 3
assert my_solution.minimumBeautifulSubstrings(*['101101101101101']) == 5
assert my_solution.minimumBeautifulSubstrings(*['1011011011101']) == 5
assert my_solution.minimumBeautifulSubstrings(*['10110110111011']) == 6
assert my_solution.minimumBeautifulSubstrings(*['101101101111001']) == 5
assert my_solution.minimumBeautifulSubstrings(*['1011011011111']) == 7
assert my_solution.minimumBeautifulSubstrings(*['101101110011101']) == 5
assert my_solution.minimumBeautifulSubstrings(*['10110111001111']) == 6
assert my_solution.minimumBeautifulSubstrings(*['1011011101101']) == 5
assert my_solution.minimumBeautifulSubstrings(*['101101110110111']) == 7
assert my_solution.minimumBeautifulSubstrings(*['101101110111011']) == 7
