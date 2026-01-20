
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.maximumSumQueries(*[[4, 3, 1, 2], [2, 4, 9, 5], [[4, 1], [1, 3], [2, 5]]]) == [6, 10, 7]
assert my_solution.maximumSumQueries(*[[3, 2, 5], [2, 3, 4], [[4, 4], [3, 2], [1, 1]]]) == [9, 9, 9]
assert my_solution.maximumSumQueries(*[[2, 1], [2, 3], [[3, 3]]]) == [-1]
assert my_solution.maximumSumQueries(*[[6], [50], [[79, 91]]]) == [-1]
assert my_solution.maximumSumQueries(*[[23], [38], [[68, 22]]]) == [-1]
assert my_solution.maximumSumQueries(*[[25], [29], [[66, 65]]]) == [-1]
assert my_solution.maximumSumQueries(*[[31], [17], [[1, 79]]]) == [-1]
assert my_solution.maximumSumQueries(*[[39], [30], [[94, 84]]]) == [-1]
assert my_solution.maximumSumQueries(*[[40], [81], [[71, 45]]]) == [-1]
assert my_solution.maximumSumQueries(*[[76], [14], [[54, 41]]]) == [-1]
assert my_solution.maximumSumQueries(*[[95], [75], [[17, 57]]]) == [170]
assert my_solution.maximumSumQueries(*[[6, 36], [5, 4], [[39, 5]]]) == [-1]
assert my_solution.maximumSumQueries(*[[9, 17], [37, 10], [[68, 97]]]) == [-1]
assert my_solution.maximumSumQueries(*[[17], [42], [[9, 60], [94, 22]]]) == [-1, -1]
assert my_solution.maximumSumQueries(*[[18], [40], [[40, 26], [89, 31]]]) == [-1, -1]
assert my_solution.maximumSumQueries(*[[24, 50], [62, 62], [[39, 98]]]) == [-1]
assert my_solution.maximumSumQueries(*[[37], [5], [[23, 63], [12, 89]]]) == [-1, -1]
assert my_solution.maximumSumQueries(*[[39], [75], [[30, 57], [46, 33]]]) == [114, -1]
assert my_solution.maximumSumQueries(*[[41], [2], [[15, 60], [30, 17]]]) == [-1, -1]
assert my_solution.maximumSumQueries(*[[44, 55], [77, 95], [[41, 60]]]) == [150]
