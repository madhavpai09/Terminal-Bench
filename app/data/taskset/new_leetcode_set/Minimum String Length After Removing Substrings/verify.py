
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.minLength(*['ABFCACDB']) == 2
assert my_solution.minLength(*['ACBBD']) == 5
assert my_solution.minLength(*['A']) == 1
assert my_solution.minLength(*['D']) == 1
assert my_solution.minLength(*['Z']) == 1
assert my_solution.minLength(*['CCCCDDDD']) == 0
assert my_solution.minLength(*['AATQCABDCBE']) == 7
assert my_solution.minLength(*['ZKPT']) == 4
assert my_solution.minLength(*['CCDDACDB']) == 0
assert my_solution.minLength(*['EUO']) == 3
assert my_solution.minLength(*['ABG']) == 1
assert my_solution.minLength(*['FACDHM']) == 4
assert my_solution.minLength(*['WCCDD']) == 1
assert my_solution.minLength(*['CCDDLLDW']) == 4
assert my_solution.minLength(*['GYCD']) == 2
assert my_solution.minLength(*['CABDCABDAB']) == 0
assert my_solution.minLength(*['ZCABDRIL']) == 4
assert my_solution.minLength(*['P']) == 1
assert my_solution.minLength(*['L']) == 1
assert my_solution.minLength(*['BQHSABE']) == 5
