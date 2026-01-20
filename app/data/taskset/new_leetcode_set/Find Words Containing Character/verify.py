
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.findWordsContaining(*[['leet', 'code'], 'e']) == [0, 1]
assert my_solution.findWordsContaining(*[['abc', 'bcd', 'aaaa', 'cbc'], 'a']) == [0, 2]
assert my_solution.findWordsContaining(*[['abc', 'bcd', 'aaaa', 'cbc'], 'z']) == []
assert my_solution.findWordsContaining(*[['sgtkshnss', 'm', 'ryvbkyvuz', 'ezittyjwgb', 'wudlwg'], 'x']) == []
assert my_solution.findWordsContaining(*[['lkwnhpbj', 'tlohm', 'juazsb', 'f', 'rq'], 'v']) == []
assert my_solution.findWordsContaining(*[['aaa', 'imvtfjmxr', 'wbzfoovjnf', 'hqwrwmi'], 'c']) == []
assert my_solution.findWordsContaining(*[['utyeachht', 'bgpkcs', 'skeecqvvvw', 'nccrd'], 'i']) == []
assert my_solution.findWordsContaining(*[['alcpxexztg', 'r'], 'h']) == []
assert my_solution.findWordsContaining(*[['ekcpg', 'pdknua', 'fot', 'janppw', 'ofomkfvx'], 'g']) == [0]
assert my_solution.findWordsContaining(*[['dq', 'rlvopu'], 'd']) == [0]
assert my_solution.findWordsContaining(*[['wzppkd', 'jxvk', 'zaztizmwuv', 'hvcdtobr'], 'b']) == [3]
assert my_solution.findWordsContaining(*[['y', 'hs', 'qznrkpi'], 'v']) == []
assert my_solution.findWordsContaining(*[['pze', 'yojczsb', 'mjvyr', 'i', 'xsygks'], 'q']) == []
assert my_solution.findWordsContaining(*[['qsgtjagcu', 'm'], 'e']) == []
assert my_solution.findWordsContaining(*[['kidtwmw', 'ogh', 'trdedlh', 'wwbtlindg', 'naoylytpof', 'ujcbzwzkm', 'doamcoxdv'], 'o']) == [1, 4, 6]
assert my_solution.findWordsContaining(*[['tsmeupctki'], 't']) == [0]
assert my_solution.findWordsContaining(*[['dqxlbljmpf', 'uvdzfoiqg', 'jsnbnx', 'fbedae', 'nodewb', 'o', 'ivepktj'], 'g']) == [1]
assert my_solution.findWordsContaining(*[['fjlmmecm', 'sautsoorhl', 'n', 'hsyco', 'amlukrpjpv', 'rmhdnj', 'g'], 'e']) == [0]
assert my_solution.findWordsContaining(*[['khjchmeciv', 'vgx', 'xghr', 'bbufgegu', 'qyfxu'], 'r']) == [2]
assert my_solution.findWordsContaining(*[['jhtcugtcpl', 'bvhlgmmla', 'ntfkwzite', 'imbtzafaj', 'sdl', 't'], 'm']) == [1, 3]
