
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.lengthOfLongestSubsequence(*[[1, 2, 3, 4, 5], 9]) == 3
assert my_solution.lengthOfLongestSubsequence(*[[4, 1, 3, 2, 1, 5], 7]) == 4
assert my_solution.lengthOfLongestSubsequence(*[[1, 1, 5, 4, 5], 3]) == -1
assert my_solution.lengthOfLongestSubsequence(*[[1000], 12]) == -1
assert my_solution.lengthOfLongestSubsequence(*[[1000], 1000]) == 1
assert my_solution.lengthOfLongestSubsequence(*[[1, 2], 10]) == -1
assert my_solution.lengthOfLongestSubsequence(*[[1, 1000], 5]) == -1
assert my_solution.lengthOfLongestSubsequence(*[[2, 3], 3]) == 1
assert my_solution.lengthOfLongestSubsequence(*[[2, 3], 5]) == 2
assert my_solution.lengthOfLongestSubsequence(*[[2, 3, 5], 5]) == 2
assert my_solution.lengthOfLongestSubsequence(*[[1, 3, 3, 7], 1000]) == -1
assert my_solution.lengthOfLongestSubsequence(*[[1, 3, 3, 7], 2]) == -1
assert my_solution.lengthOfLongestSubsequence(*[[1, 3, 3, 8], 7]) == 3
assert my_solution.lengthOfLongestSubsequence(*[[1, 1, 2, 1], 2]) == 2
assert my_solution.lengthOfLongestSubsequence(*[[1, 1, 1, 1], 5]) == -1
assert my_solution.lengthOfLongestSubsequence(*[[1, 1, 1, 2], 3]) == 3
assert my_solution.lengthOfLongestSubsequence(*[[9, 12, 8, 4, 11, 13, 15, 7, 5], 84]) == 9
assert my_solution.lengthOfLongestSubsequence(*[[11, 5, 9, 11, 12, 13, 12, 5, 1, 8], 87]) == 10
assert my_solution.lengthOfLongestSubsequence(*[[9, 11, 11, 15, 4, 14, 3, 2, 13, 7], 89]) == 10
assert my_solution.lengthOfLongestSubsequence(*[[11, 13, 6, 13, 10], 53]) == 5
