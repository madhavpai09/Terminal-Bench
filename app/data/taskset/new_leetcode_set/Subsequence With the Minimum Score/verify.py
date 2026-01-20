
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.minimumScore(*['abacaba', 'bzaa']) == 1
assert my_solution.minimumScore(*['cde', 'xyz']) == 3
assert my_solution.minimumScore(*['abecdebe', 'eaebceae']) == 6
assert my_solution.minimumScore(*['acdedcdbabecdbebda', 'bbecddb']) == 1
assert my_solution.minimumScore(*['dabbbeddeabbaccecaee', 'bcbbaabdbebecbebded']) == 16
assert my_solution.minimumScore(*['adebddaccdcabaade', 'adbae']) == 0
assert my_solution.minimumScore(*['dcadebdecbeaedd', 'dcdadeb']) == 1
assert my_solution.minimumScore(*['bcceaaccd', 'cbe']) == 1
assert my_solution.minimumScore(*['cabecaeadeaeadd', 'edcce']) == 2
assert my_solution.minimumScore(*['cbedceeeccd', 'ed']) == 0
assert my_solution.minimumScore(*['eeecaeecdeeadcdbcaa', 'edecabe']) == 2
assert my_solution.minimumScore(*['eceecbabe', 'bdeaec']) == 4
assert my_solution.minimumScore(*['caaa', 'aaa']) == 0
assert my_solution.minimumScore(*['cbaa', 'a']) == 0
assert my_solution.minimumScore(*['bcabcbcccbacccc', 'cbcbb']) == 0
assert my_solution.minimumScore(*['eddbeedbbaaaaadaacccddadccbbcdc', 'aecbddcedaaced']) == 12
assert my_solution.minimumScore(*['ccecdeccaebcdaeaccdceadbaabeddacaeacbaabaec', 'bdadc']) == 0
assert my_solution.minimumScore(*['eaedcdbdeededbcdcbedddbccbaebbdbadbdadccaddacbbcbabadbacbdcbeaebecbacacbadaadedcadcdcdaceaaad', 'cadedebbcabecbcbd']) == 1
assert my_solution.minimumScore(*['aacecebcbbcbacddbdcbaddeadd', 'cab']) == 0
assert my_solution.minimumScore(*['adcdaedbeeecbbaecebceaebcbcddecddcedecddbbdaabcbdbcbbabbddaeaedeabdecaedbcdbdccb', 'abadccaced']) == 0
