
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.minOperations(*[[2, 6, 3, 4]]) == 4
assert my_solution.minOperations(*[[2, 10, 6, 14]]) == -1
assert my_solution.minOperations(*[[410193, 229980, 600441]]) == -1
assert my_solution.minOperations(*[[6, 10, 15]]) == 4
assert my_solution.minOperations(*[[4, 2, 6, 3]]) == 5
assert my_solution.minOperations(*[[48841, 93382, 993143, 170438, 48860, 174356, 291531]]) == 7
assert my_solution.minOperations(*[[565053, 324050, 845500, 764459, 693331, 849602, 379407]]) == 7
assert my_solution.minOperations(*[[404514, 309109, 640464, 451473, 954489, 240704, 730484, 888313, 126885]]) == 9
assert my_solution.minOperations(*[[432320, 571622, 553142, 152985, 127988, 46098, 850399, 251987, 660091]]) == 9
assert my_solution.minOperations(*[[266354, 828118, 333704, 385834]]) == -1
assert my_solution.minOperations(*[[715086, 420033, 320095, 230175, 359910, 99010, 261428, 561978, 495675, 817898]]) == 10
assert my_solution.minOperations(*[[846237, 105643, 71480, 567494, 315367, 503911, 836510, 984966, 748650]]) == 9
assert my_solution.minOperations(*[[591723, 60746, 374246, 765639, 97358, 188339, 225788, 155868]]) == 8
assert my_solution.minOperations(*[[780304, 789919, 873587, 158393, 298420, 624934, 660252, 787804]]) == 8
assert my_solution.minOperations(*[[184432, 604193, 195562, 660134, 410026, 780971, 446702, 401480, 567049, 647296, 32815, 819020]]) == 12
assert my_solution.minOperations(*[[358771, 577201, 359849, 457987, 710497, 21300, 955067, 665670, 180408, 650137, 997097, 677290]]) == 12
assert my_solution.minOperations(*[[811340, 393975, 627577, 26811, 209797, 500958, 637753, 592871, 449081, 216228, 498803, 730546, 937075, 122352, 610619, 921594, 47754, 242342, 726157]]) == 19
assert my_solution.minOperations(*[[985732, 437182, 281370, 204922, 295879, 239067, 105852, 967432, 24512, 977516, 566875, 507422, 988409, 155892]]) == 14
assert my_solution.minOperations(*[[61934, 478887, 397567, 718200, 461668, 936276, 802169, 833144, 749931, 807386, 109400, 501586, 423875, 877463, 26894, 352687, 755053]]) == 17
assert my_solution.minOperations(*[[865937, 351065, 864096, 504664, 698592, 630262, 38706, 159959, 198626, 161672, 931247, 719751, 722377, 561747, 937783, 835190, 748284]]) == 17
