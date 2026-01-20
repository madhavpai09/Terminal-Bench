
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.minimumCost(*['abcd', 'acbe', ['a', 'b', 'c', 'c', 'e', 'd'], ['b', 'c', 'b', 'e', 'b', 'e'], [2, 5, 5, 1, 2, 20]]) == 28
assert my_solution.minimumCost(*['aaaa', 'bbbb', ['a', 'c'], ['c', 'b'], [1, 2]]) == 12
assert my_solution.minimumCost(*['abcd', 'abce', ['a'], ['e'], [10000]]) == -1
assert my_solution.minimumCost(*['aaaabadaaa', 'dbdadddbad', ['c', 'a', 'c', 'a', 'a', 'b', 'b', 'b', 'd', 'd', 'c'], ['a', 'c', 'b', 'd', 'b', 'c', 'a', 'd', 'c', 'b', 'd'], [7, 8, 11, 9, 7, 6, 4, 6, 9, 5, 9]]) == 56
assert my_solution.minimumCost(*['aaadbdcdac', 'cdbabaddba', ['a', 'c', 'b', 'd', 'b', 'a', 'c'], ['c', 'a', 'd', 'b', 'c', 'b', 'd'], [7, 2, 1, 3, 6, 1, 7]]) == 39
assert my_solution.minimumCost(*['aababdaacb', 'bcdcdcbdcb', ['a', 'd', 'd', 'a', 'c', 'b', 'c', 'a', 'c', 'd', 'b', 'b'], ['b', 'c', 'b', 'd', 'a', 'a', 'b', 'c', 'd', 'a', 'c', 'd'], [11, 4, 3, 2, 7, 11, 7, 6, 9, 2, 1, 7]]) == 42
assert my_solution.minimumCost(*['aababdbddc', 'adcbbbcdba', ['a', 'd', 'b', 'a', 'd', 'c', 'd', 'b'], ['b', 'a', 'd', 'c', 'c', 'a', 'b', 'a'], [10, 6, 8, 3, 6, 10, 8, 6]]) == 72
assert my_solution.minimumCost(*['aabbcabbdb', 'acddbabbdd', ['c', 'd', 'c', 'a', 'd', 'c', 'a', 'd', 'b', 'a', 'b'], ['d', 'b', 'a', 'c', 'c', 'b', 'b', 'a', 'd', 'd', 'c'], [5, 3, 8, 10, 9, 7, 8, 7, 5, 1, 10]]) == 32
assert my_solution.minimumCost(*['aabbddccbc', 'abbbaabaca', ['a', 'b', 'c', 'b', 'a', 'd'], ['d', 'c', 'b', 'd', 'b', 'b'], [3, 8, 7, 6, 7, 10]]) == -1
assert my_solution.minimumCost(*['aabdbaabaa', 'bdaacabcab', ['b', 'd', 'd', 'a', 'c', 'c', 'a', 'd', 'a', 'b'], ['c', 'c', 'b', 'd', 'b', 'd', 'b', 'a', 'c', 'a'], [9, 1, 7, 9, 2, 1, 3, 8, 8, 2]]) == 43
assert my_solution.minimumCost(*['aacacaaccd', 'dadaacaabd', ['c', 'c', 'a', 'a', 'd', 'b', 'd', 'd'], ['b', 'd', 'd', 'b', 'b', 'c', 'c', 'a'], [7, 8, 9, 11, 4, 6, 9, 10]]) == 77
assert my_solution.minimumCost(*['aacbabbacc', 'adbdbcbdaa', ['c', 'b', 'a', 'b', 'a', 'c', 'd', 'c', 'd'], ['b', 'c', 'b', 'd', 'd', 'a', 'b', 'd', 'c'], [2, 6, 7, 4, 7, 4, 3, 5, 6]]) == 41
assert my_solution.minimumCost(*['aacbbabdad', 'ddadcababd', ['d', 'b', 'c', 'a', 'b', 'c', 'd', 'c', 'b', 'a', 'a'], ['c', 'd', 'd', 'b', 'c', 'b', 'b', 'a', 'a', 'c', 'd'], [7, 10, 4, 2, 7, 4, 4, 4, 6, 2, 8]]) == 45
assert my_solution.minimumCost(*['aacbbbbcab', 'cdacdcddac', ['b', 'd', 'c', 'c', 'b', 'a'], ['c', 'c', 'b', 'a', 'a', 'd'], [4, 7, 9, 11, 3, 4]]) == 67
assert my_solution.minimumCost(*['aacbcabcad', 'bbcadddcdd', ['b', 'a', 'd', 'a', 'b', 'c', 'a', 'd', 'd', 'b'], ['d', 'b', 'b', 'd', 'c', 'a', 'c', 'c', 'a', 'a'], [7, 7, 9, 8, 6, 3, 8, 2, 1, 5]]) == 53
assert my_solution.minimumCost(*['aacbdbcdca', 'bbbdbcaacd', ['a', 'c', 'b', 'd', 'd', 'a', 'c', 'd'], ['c', 'b', 'c', 'c', 'b', 'd', 'd', 'a'], [9, 5, 4, 1, 2, 4, 7, 1]]) == 47
assert my_solution.minimumCost(*['aadbbcdbbd', 'badddbdbac', ['c', 'd', 'c', 'd', 'b', 'a'], ['b', 'b', 'a', 'a', 'a', 'd'], [11, 4, 7, 8, 5, 2]]) == -1
assert my_solution.minimumCost(*['aadbccbddd', 'cacdbabadc', ['d', 'b', 'c', 'd', 'a', 'a', 'c', 'b'], ['c', 'c', 'b', 'b', 'b', 'd', 'a', 'a'], [5, 8, 7, 2, 4, 7, 1, 5]]) == 46
assert my_solution.minimumCost(*['aadbddcabd', 'bdcdccbada', ['d', 'a', 'a', 'b', 'd', 'b'], ['b', 'c', 'd', 'c', 'a', 'd'], [6, 10, 5, 8, 11, 4]]) == -1
assert my_solution.minimumCost(*['aaddadccad', 'cbaaadbcba', ['c', 'a', 'a', 'd', 'c', 'c', 'b', 'b', 'a', 'd'], ['a', 'c', 'd', 'c', 'd', 'b', 'd', 'c', 'b', 'b'], [1, 10, 2, 8, 9, 1, 9, 10, 5, 1]]) == 44
