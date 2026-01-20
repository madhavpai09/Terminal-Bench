
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.getWordsInLongestSubsequence(*[3, ['e', 'a', 'b'], [0, 0, 1]]) == ['e', 'b']
assert my_solution.getWordsInLongestSubsequence(*[4, ['a', 'b', 'c', 'd'], [1, 0, 1, 1]]) == ['a', 'b', 'c']
assert my_solution.getWordsInLongestSubsequence(*[1, ['c'], [0]]) == ['c']
assert my_solution.getWordsInLongestSubsequence(*[1, ['d'], [1]]) == ['d']
assert my_solution.getWordsInLongestSubsequence(*[1, ['e'], [0]]) == ['e']
assert my_solution.getWordsInLongestSubsequence(*[1, ['fe'], [0]]) == ['fe']
assert my_solution.getWordsInLongestSubsequence(*[1, ['frl'], [1]]) == ['frl']
assert my_solution.getWordsInLongestSubsequence(*[1, ['ha'], [1]]) == ['ha']
assert my_solution.getWordsInLongestSubsequence(*[1, ['l'], [0]]) == ['l']
assert my_solution.getWordsInLongestSubsequence(*[1, ['n'], [1]]) == ['n']
assert my_solution.getWordsInLongestSubsequence(*[1, ['s'], [1]]) == ['s']
assert my_solution.getWordsInLongestSubsequence(*[2, ['d', 'g'], [0, 1]]) == ['d', 'g']
assert my_solution.getWordsInLongestSubsequence(*[2, ['lr', 'h'], [0, 0]]) == ['lr']
assert my_solution.getWordsInLongestSubsequence(*[2, ['wx', 'h'], [0, 1]]) == ['wx', 'h']
assert my_solution.getWordsInLongestSubsequence(*[2, ['yw', 'n'], [0, 1]]) == ['yw', 'n']
assert my_solution.getWordsInLongestSubsequence(*[2, ['z', 'n'], [0, 0]]) == ['z']
assert my_solution.getWordsInLongestSubsequence(*[2, ['zr', 'a'], [0, 0]]) == ['zr']
assert my_solution.getWordsInLongestSubsequence(*[3, ['h', 'vv', 'kp'], [0, 1, 0]]) == ['h', 'vv', 'kp']
assert my_solution.getWordsInLongestSubsequence(*[3, ['m', 'v', 'y'], [0, 1, 0]]) == ['m', 'v', 'y']
assert my_solution.getWordsInLongestSubsequence(*[3, ['o', 'cfy', 'en'], [1, 0, 0]]) == ['o', 'cfy']
