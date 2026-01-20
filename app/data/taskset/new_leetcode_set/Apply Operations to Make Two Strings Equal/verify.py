
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.minOperations(*['1100011000', '0101001010', 2]) == 4
assert my_solution.minOperations(*['10110', '00011', 4]) == -1
assert my_solution.minOperations(*['101101', '000000', 6]) == 4
assert my_solution.minOperations(*['0', '1', 2]) == -1
assert my_solution.minOperations(*['1011100100111000', '1001010001011100', 19]) == -1
assert my_solution.minOperations(*['00101101100010', '00001010001111', 30]) == 8
assert my_solution.minOperations(*['1011000', '0001101', 30]) == 4
assert my_solution.minOperations(*['1111110101010110', '1000100111100101', 19]) == -1
assert my_solution.minOperations(*['1011100000100100101', '1110001001110000011', 14]) == -1
assert my_solution.minOperations(*['0', '1', 17]) == -1
assert my_solution.minOperations(*['0', '1', 3]) == -1
assert my_solution.minOperations(*['0001110010', '0110100111', 29]) == 5
assert my_solution.minOperations(*['01111101010100110100', '10010011011001011000', 21]) == 7
assert my_solution.minOperations(*['00000101', '01001010', 10]) == -1
assert my_solution.minOperations(*['01', '00', 30]) == -1
assert my_solution.minOperations(*['11111', '01011', 4]) == 2
assert my_solution.minOperations(*['001010101011001', '110111000101110', 14]) == 7
assert my_solution.minOperations(*['010011101', '101111000', 17]) == 4
assert my_solution.minOperations(*['11110111', '10011111', 16]) == -1
assert my_solution.minOperations(*['0011', '1100', 14]) == 2
