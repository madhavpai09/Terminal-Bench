
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.getWordsInLongestSubsequence(*[3, ['bab', 'dab', 'cab'], [1, 2, 2]]) == ['bab', 'cab']
assert my_solution.getWordsInLongestSubsequence(*[4, ['a', 'b', 'c', 'd'], [1, 2, 3, 4]]) == ['a', 'b', 'c', 'd']
assert my_solution.getWordsInLongestSubsequence(*[1, ['abbbb'], [1]]) == ['abbbb']
assert my_solution.getWordsInLongestSubsequence(*[1, ['ad'], [1]]) == ['ad']
assert my_solution.getWordsInLongestSubsequence(*[1, ['baaccb'], [1]]) == ['baaccb']
assert my_solution.getWordsInLongestSubsequence(*[1, ['bc'], [1]]) == ['bc']
assert my_solution.getWordsInLongestSubsequence(*[1, ['bdb'], [1]]) == ['bdb']
assert my_solution.getWordsInLongestSubsequence(*[1, ['cc'], [1]]) == ['cc']
assert my_solution.getWordsInLongestSubsequence(*[1, ['cd'], [1]]) == ['cd']
assert my_solution.getWordsInLongestSubsequence(*[1, ['cdb'], [1]]) == ['cdb']
assert my_solution.getWordsInLongestSubsequence(*[1, ['cea'], [1]]) == ['cea']
assert my_solution.getWordsInLongestSubsequence(*[1, ['cebbbb'], [1]]) == ['cebbbb']
assert my_solution.getWordsInLongestSubsequence(*[1, ['da'], [1]]) == ['da']
assert my_solution.getWordsInLongestSubsequence(*[1, ['daab'], [1]]) == ['daab']
assert my_solution.getWordsInLongestSubsequence(*[2, ['adbe', 'acace'], [2, 2]]) == ['acace']
assert my_solution.getWordsInLongestSubsequence(*[2, ['ba', 'dc'], [1, 1]]) == ['dc']
assert my_solution.getWordsInLongestSubsequence(*[2, ['baa', 'ada'], [1, 2]]) == ['ada']
assert my_solution.getWordsInLongestSubsequence(*[2, ['bebea', 'ddecc'], [1, 1]]) == ['ddecc']
assert my_solution.getWordsInLongestSubsequence(*[2, ['cedbca', 'db'], [1, 1]]) == ['db']
assert my_solution.getWordsInLongestSubsequence(*[2, ['dbcdd', 'baba'], [2, 1]]) == ['baba']
