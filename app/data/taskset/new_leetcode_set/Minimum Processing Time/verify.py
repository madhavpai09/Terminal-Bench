
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.minProcessingTime(*[[8, 10], [2, 2, 3, 1, 8, 7, 4, 5]]) == 16
assert my_solution.minProcessingTime(*[[10, 20], [2, 3, 1, 2, 5, 8, 4, 3]]) == 23
assert my_solution.minProcessingTime(*[[121, 99], [287, 315, 293, 260, 333, 362, 69, 233]]) == 461
assert my_solution.minProcessingTime(*[[33, 320], [132, 68, 232, 166, 30, 300, 112, 138]]) == 452
assert my_solution.minProcessingTime(*[[50, 82], [288, 138, 205, 295, 367, 100, 258, 308]]) == 417
assert my_solution.minProcessingTime(*[[291], [125, 169, 269, 32]]) == 560
assert my_solution.minProcessingTime(*[[55, 350, 166, 210, 389], [276, 253, 157, 237, 92, 396, 331, 19, 82, 301, 136, 396, 251, 92, 280, 70, 253, 47, 81, 84]]) == 470
assert my_solution.minProcessingTime(*[[143, 228, 349, 231, 392], [102, 365, 363, 211, 38, 96, 98, 79, 365, 289, 252, 201, 259, 346, 21, 68, 128, 56, 167, 183]]) == 517
assert my_solution.minProcessingTime(*[[168, 32, 299, 303, 96], [382, 183, 337, 73, 115, 350, 6, 18, 93, 238, 102, 302, 96, 381, 327, 385, 387, 288, 138, 83]]) == 456
assert my_solution.minProcessingTime(*[[324, 117, 374, 219, 303], [374, 202, 328, 11, 353, 208, 383, 287, 107, 236, 226, 387, 21, 183, 352, 164, 207, 182, 15, 65]]) == 571
assert my_solution.minProcessingTime(*[[376], [21, 247, 274, 38]]) == 650
assert my_solution.minProcessingTime(*[[93, 3, 281, 218], [182, 16, 241, 312, 81, 339, 207, 330, 306, 166, 82, 290, 7, 317, 396, 389]]) == 459
assert my_solution.minProcessingTime(*[[374, 250, 197, 170], [247, 56, 330, 361, 240, 261, 67, 65, 138, 181, 308, 26, 59, 150, 137, 244]]) == 531
assert my_solution.minProcessingTime(*[[115, 271, 137], [34, 72, 328, 312, 159, 32, 283, 6, 234, 280, 46, 349]]) == 464
assert my_solution.minProcessingTime(*[[47, 217, 349, 233, 283], [195, 188, 181, 259, 145, 96, 298, 322, 213, 154, 278, 292, 315, 191, 177, 228, 291, 204, 310, 266]]) == 526
assert my_solution.minProcessingTime(*[[177, 6, 326, 318, 294], [136, 215, 260, 259, 35, 248, 340, 377, 144, 248, 83, 150, 63, 48, 269, 197, 317, 135, 36, 344]]) == 542
assert my_solution.minProcessingTime(*[[266, 372], [260, 325, 159, 316, 296, 366, 335, 146]]) == 668
assert my_solution.minProcessingTime(*[[63, 339], [79, 316, 98, 354, 220, 267, 333, 11]]) == 559
assert my_solution.minProcessingTime(*[[149, 60, 172, 5, 212], [230, 374, 276, 281, 55, 96, 52, 83, 56, 399, 69, 333, 145, 6, 50, 101, 216, 327, 120, 209]]) == 404
assert my_solution.minProcessingTime(*[[220, 375, 285, 267, 150], [53, 317, 367, 258, 337, 280, 232, 322, 153, 169, 121, 211, 171, 345, 76, 370, 265, 107, 45, 320]]) == 542
