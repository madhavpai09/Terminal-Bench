
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.canMakeSubsequence(*['abc', 'ad']) == True
assert my_solution.canMakeSubsequence(*['zc', 'ad']) == True
assert my_solution.canMakeSubsequence(*['ab', 'd']) == False
assert my_solution.canMakeSubsequence(*['a', 'd']) == False
assert my_solution.canMakeSubsequence(*['b', 'c']) == True
assert my_solution.canMakeSubsequence(*['b', 'v']) == False
assert my_solution.canMakeSubsequence(*['c', 'b']) == False
assert my_solution.canMakeSubsequence(*['c', 'k']) == False
assert my_solution.canMakeSubsequence(*['c', 'm']) == False
assert my_solution.canMakeSubsequence(*['d', 'h']) == False
assert my_solution.canMakeSubsequence(*['d', 'm']) == False
assert my_solution.canMakeSubsequence(*['d', 'x']) == False
assert my_solution.canMakeSubsequence(*['f', 'f']) == True
assert my_solution.canMakeSubsequence(*['f', 'g']) == True
assert my_solution.canMakeSubsequence(*['f', 's']) == False
assert my_solution.canMakeSubsequence(*['g', 'g']) == True
assert my_solution.canMakeSubsequence(*['h', 'i']) == True
assert my_solution.canMakeSubsequence(*['i', 'e']) == False
assert my_solution.canMakeSubsequence(*['i', 'j']) == True
assert my_solution.canMakeSubsequence(*['j', 'j']) == True
