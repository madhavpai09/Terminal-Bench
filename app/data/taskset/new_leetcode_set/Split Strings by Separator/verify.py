
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.splitWordsBySeparator(*[['one.two.three', 'four.five', 'six'], '.']) == ['one', 'two', 'three', 'four', 'five', 'six']
assert my_solution.splitWordsBySeparator(*[['$easy$', '$problem$'], '$']) == ['easy', 'problem']
assert my_solution.splitWordsBySeparator(*[['|||'], '|']) == []
assert my_solution.splitWordsBySeparator(*[['stars.bars.$'], '.']) == ['stars', 'bars', '$']
assert my_solution.splitWordsBySeparator(*[['###x#i@f'], '#']) == ['x', 'i@f']
assert my_solution.splitWordsBySeparator(*[['##q@t#'], '#']) == ['q@t']
assert my_solution.splitWordsBySeparator(*[['#,'], '#']) == [',']
assert my_solution.splitWordsBySeparator(*[['#@'], '@']) == ['#']
assert my_solution.splitWordsBySeparator(*[['#a$f$nwgq#vw'], '$']) == ['#a', 'f', 'nwgq#vw']
assert my_solution.splitWordsBySeparator(*[['#uyddd,trxiwfv'], ',']) == ['#uyddd', 'trxiwfv']
assert my_solution.splitWordsBySeparator(*[['#x'], '$']) == ['#x']
assert my_solution.splitWordsBySeparator(*[['#x#,'], ',']) == ['#x#']
assert my_solution.splitWordsBySeparator(*[['#|'], '#']) == ['|']
assert my_solution.splitWordsBySeparator(*[['#|a|b|##|#|#g#u|'], '|']) == ['#', 'a', 'b', '##', '#', '#g#u']
assert my_solution.splitWordsBySeparator(*[['$$.o.$$.'], '$']) == ['.o.', '.']
assert my_solution.splitWordsBySeparator(*[['$,,'], ',']) == ['$']
assert my_solution.splitWordsBySeparator(*[['$j@@@'], '@']) == ['$j']
assert my_solution.splitWordsBySeparator(*[[',$$'], '$']) == [',']
assert my_solution.splitWordsBySeparator(*[[',,'], '|']) == [',,']
assert my_solution.splitWordsBySeparator(*[[',,,@@n'], ',']) == ['@@n']
