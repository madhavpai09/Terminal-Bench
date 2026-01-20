
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.primeSubOperation(*[[4, 9, 6, 10]]) == True
assert my_solution.primeSubOperation(*[[6, 8, 11, 12]]) == True
assert my_solution.primeSubOperation(*[[5, 8, 3]]) == False
assert my_solution.primeSubOperation(*[[2, 2]]) == False
assert my_solution.primeSubOperation(*[[998, 2]]) == True
assert my_solution.primeSubOperation(*[[1, 20, 7, 12, 4]]) == False
assert my_solution.primeSubOperation(*[[17, 20, 5, 15, 6]]) == False
assert my_solution.primeSubOperation(*[[17, 2]]) == False
assert my_solution.primeSubOperation(*[[18, 12, 14, 6]]) == False
assert my_solution.primeSubOperation(*[[11, 2, 10, 15, 19]]) == False
assert my_solution.primeSubOperation(*[[12]]) == True
assert my_solution.primeSubOperation(*[[4, 3, 7, 4]]) == False
assert my_solution.primeSubOperation(*[[6, 17, 2, 9, 20]]) == False
assert my_solution.primeSubOperation(*[[20, 18, 2]]) == False
assert my_solution.primeSubOperation(*[[10, 18, 14, 3, 11]]) == False
assert my_solution.primeSubOperation(*[[19, 10]]) == True
assert my_solution.primeSubOperation(*[[4, 18, 10, 16, 3]]) == False
assert my_solution.primeSubOperation(*[[17, 2, 15]]) == False
assert my_solution.primeSubOperation(*[[9]]) == True
assert my_solution.primeSubOperation(*[[15, 20, 17, 7, 16]]) == True
