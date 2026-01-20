
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.findTheString(*[[[4, 0, 2, 0], [0, 3, 0, 1], [2, 0, 2, 0], [0, 1, 0, 1]]]) == abab
assert my_solution.findTheString(*[[[4, 3, 2, 1], [3, 3, 2, 1], [2, 2, 2, 1], [1, 1, 1, 1]]]) == aaaa
assert my_solution.findTheString(*[[[4, 3, 2, 1], [3, 3, 2, 1], [2, 2, 2, 1], [1, 1, 1, 3]]]) == 
assert my_solution.findTheString(*[[[1]]]) == a
assert my_solution.findTheString(*[[[0]]]) == 
assert my_solution.findTheString(*[[[2, 0], [0, 1]]]) == ab
assert my_solution.findTheString(*[[[2, 0], [1, 1]]]) == 
assert my_solution.findTheString(*[[[2, 0], [2, 1]]]) == 
assert my_solution.findTheString(*[[[2, 1], [0, 1]]]) == 
assert my_solution.findTheString(*[[[2, 1], [1, 1]]]) == aa
assert my_solution.findTheString(*[[[2, 1], [2, 1]]]) == 
assert my_solution.findTheString(*[[[2, 2], [0, 1]]]) == 
assert my_solution.findTheString(*[[[2, 2], [1, 1]]]) == 
assert my_solution.findTheString(*[[[2, 2], [2, 1]]]) == 
assert my_solution.findTheString(*[[[4, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]]) == 
assert my_solution.findTheString(*[[[4, 1, 1, 1], [1, 3, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]]) == 
assert my_solution.findTheString(*[[[4, 1, 1, 1], [1, 3, 1, 1], [1, 1, 2, 1], [1, 1, 1, 1]]]) == 
assert my_solution.findTheString(*[[[8, 0, 0, 0, 0, 1, 2, 0], [0, 7, 0, 1, 1, 0, 0, 1], [0, 0, 6, 0, 0, 0, 0, 0], [0, 1, 0, 5, 1, 0, 0, 1], [0, 1, 0, 1, 4, 0, 0, 1], [1, 0, 0, 0, 0, 3, 1, 0], [2, 0, 0, 0, 0, 1, 2, 0], [0, 1, 0, 1, 1, 0, 0, 1]]]) == abcbbaab
assert my_solution.findTheString(*[[[9, 1, 0, 1, 0, 1, 0, 0, 1], [1, 8, 0, 4, 0, 2, 0, 0, 1], [0, 0, 7, 0, 3, 0, 1, 2, 0], [1, 4, 0, 6, 0, 2, 0, 0, 1], [0, 0, 3, 0, 5, 0, 1, 2, 0], [1, 2, 0, 2, 0, 4, 0, 0, 1], [0, 0, 1, 0, 1, 0, 3, 1, 0], [0, 0, 2, 0, 2, 0, 1, 2, 0], [1, 1, 0, 1, 0, 1, 0, 0, 1]]]) == aabababba
assert my_solution.findTheString(*[[[14, 2, 1, 0, 0, 0, 1, 0, 0, 0, 2, 1, 0, 0], [2, 13, 1, 0, 0, 0, 1, 0, 0, 0, 4, 1, 0, 0], [1, 1, 12, 0, 0, 0, 1, 0, 0, 0, 1, 3, 0, 0], [0, 0, 0, 11, 1, 0, 0, 0, 2, 1, 0, 0, 2, 1], [0, 0, 0, 1, 10, 0, 0, 0, 1, 1, 0, 0, 1, 1], [0, 0, 0, 0, 0, 9, 0, 1, 0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 8, 0, 0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 7, 0, 0, 0, 0, 0, 0], [0, 0, 0, 2, 1, 0, 0, 0, 6, 1, 0, 0, 2, 1], [0, 0, 0, 1, 1, 0, 0, 0, 1, 5, 0, 0, 1, 1], [2, 4, 1, 0, 0, 0, 1, 0, 0, 0, 4, 1, 0, 0], [1, 1, 3, 0, 0, 0, 1, 0, 0, 0, 1, 3, 0, 0], [0, 0, 0, 2, 1, 0, 0, 0, 2, 1, 0, 0, 2, 1], [0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1]]]) == aaabbcacbbaabb
