
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.maximumTripletValue(*[[12, 6, 1, 2, 7]]) == 77
assert my_solution.maximumTripletValue(*[[1, 10, 3, 4, 19]]) == 133
assert my_solution.maximumTripletValue(*[[1, 2, 3]]) == 0
assert my_solution.maximumTripletValue(*[[2, 3, 1]]) == 0
assert my_solution.maximumTripletValue(*[[5, 7, 8, 4]]) == 0
assert my_solution.maximumTripletValue(*[[1000000, 1, 1000000]]) == 999999000000
assert my_solution.maximumTripletValue(*[[18, 15, 8, 13, 10, 9, 17, 10, 2, 16, 17]]) == 272
assert my_solution.maximumTripletValue(*[[8, 6, 3, 13, 2, 12, 19, 5, 19, 6, 10, 11, 9]]) == 266
assert my_solution.maximumTripletValue(*[[6, 11, 12, 12, 7, 9, 2, 11, 12, 4, 19, 14, 16, 8, 16]]) == 190
assert my_solution.maximumTripletValue(*[[15, 14, 17, 13, 18, 17, 10, 19, 2, 20, 12, 9]]) == 340
assert my_solution.maximumTripletValue(*[[6, 14, 20, 19, 19, 10, 3, 15, 12, 13, 8, 1, 2, 15, 3]]) == 285
assert my_solution.maximumTripletValue(*[[2, 7, 19, 4, 8, 20]]) == 300
assert my_solution.maximumTripletValue(*[[10, 13, 6, 2]]) == 14
assert my_solution.maximumTripletValue(*[[1, 19, 1, 3, 18, 10, 16, 9, 3, 17, 8, 9]]) == 324
assert my_solution.maximumTripletValue(*[[16, 2, 10, 20, 16, 2, 13, 8, 19]]) == 342
assert my_solution.maximumTripletValue(*[[19, 11, 12, 4, 17, 1, 7, 20, 13, 10, 14, 20, 11, 19, 3]]) == 360
assert my_solution.maximumTripletValue(*[[16, 15, 12, 5, 4, 12, 15, 17, 5, 18, 6, 16, 1, 17, 4]]) == 289
assert my_solution.maximumTripletValue(*[[8, 10, 17, 11, 2, 8, 13]]) == 195
assert my_solution.maximumTripletValue(*[[13, 4, 3, 19, 16, 14, 17, 6, 20, 6, 16, 4]]) == 260
assert my_solution.maximumTripletValue(*[[1, 8, 9, 18, 4, 10, 3, 13, 9]]) == 195
