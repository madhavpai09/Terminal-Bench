
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.canMakePalindromeQueries(*['abcabc', [[1, 1, 3, 5], [0, 2, 5, 5]]]) == [True, True]
assert my_solution.canMakePalindromeQueries(*['abbcdecbba', [[0, 2, 7, 9]]]) == [False]
assert my_solution.canMakePalindromeQueries(*['acbcab', [[1, 2, 4, 5]]]) == [True]
assert my_solution.canMakePalindromeQueries(*['bb', [[0, 0, 1, 1]]]) == [True]
assert my_solution.canMakePalindromeQueries(*['dd', [[0, 0, 1, 1]]]) == [True]
assert my_solution.canMakePalindromeQueries(*['bdbd', [[0, 0, 2, 3]]]) == [True]
assert my_solution.canMakePalindromeQueries(*['eeee', [[0, 1, 2, 3]]]) == [True]
assert my_solution.canMakePalindromeQueries(*['bbccbb', [[0, 1, 4, 5]]]) == [True]
assert my_solution.canMakePalindromeQueries(*['bcdbdc', [[1, 2, 3, 3]]]) == [False]
assert my_solution.canMakePalindromeQueries(*['cababc', [[1, 2, 3, 4]]]) == [True]
assert my_solution.canMakePalindromeQueries(*['cbbbbc', [[1, 1, 5, 5]]]) == [True]
assert my_solution.canMakePalindromeQueries(*['cdbdbc', [[1, 2, 3, 3]]]) == [True]
assert my_solution.canMakePalindromeQueries(*['ceacea', [[0, 2, 3, 5]]]) == [True]
assert my_solution.canMakePalindromeQueries(*['daeaed', [[0, 2, 3, 3]]]) == [True]
assert my_solution.canMakePalindromeQueries(*['ddaadd', [[0, 2, 3, 4]]]) == [True]
assert my_solution.canMakePalindromeQueries(*['ddedde', [[0, 2, 4, 5]]]) == [True]
assert my_solution.canMakePalindromeQueries(*['ecbbce', [[0, 1, 3, 5]]]) == [True]
assert my_solution.canMakePalindromeQueries(*['eczecz', [[0, 0, 3, 5]]]) == [True]
assert my_solution.canMakePalindromeQueries(*['mpepem', [[0, 2, 3, 4]]]) == [True]
assert my_solution.canMakePalindromeQueries(*['bccacacb', [[3, 3, 4, 7]]]) == [True]
