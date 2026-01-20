
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.beautifulIndices(*['isawsquirrelnearmysquirrelhouseohmy', 'my', 'squirrel', 15]) == [16, 33]
assert my_solution.beautifulIndices(*['abcd', 'a', 'a', 4]) == [0]
assert my_solution.beautifulIndices(*['sqgrt', 'rt', 'sq', 3]) == [3]
assert my_solution.beautifulIndices(*['mquz', 'tklr', 'caz', 4]) == []
assert my_solution.beautifulIndices(*['wl', 'xjigt', 'wl', 2]) == []
assert my_solution.beautifulIndices(*['bavgoc', 'ba', 'c', 6]) == [0]
assert my_solution.beautifulIndices(*['xpcp', 'yxnod', 'xpc', 4]) == []
assert my_solution.beautifulIndices(*['lahhnlwx', 'hhnlw', 'ty', 6]) == []
assert my_solution.beautifulIndices(*['dexgscgecd', 'gscge', 'd', 6]) == [3]
assert my_solution.beautifulIndices(*['vjrao', 'vjr', 'yxpsw', 5]) == []
assert my_solution.beautifulIndices(*['oo', 'swhup', 'o', 1]) == []
assert my_solution.beautifulIndices(*['bxlzgxc', 'ducf', 'xlzgx', 3]) == []
assert my_solution.beautifulIndices(*['wetlgztzm', 'box', 'wetl', 4]) == []
assert my_solution.beautifulIndices(*['ocmm', 'm', 'oc', 3]) == [2, 3]
assert my_solution.beautifulIndices(*['goxmox', 'gibs', 'ox', 6]) == []
assert my_solution.beautifulIndices(*['kzlrqzldvy', 'zl', 'tfsr', 9]) == []
assert my_solution.beautifulIndices(*['qhd', 'hd', 'od', 1]) == []
assert my_solution.beautifulIndices(*['bozpeh', 'bozp', 'vrjn', 2]) == []
assert my_solution.beautifulIndices(*['ggfsg', 'gfsg', 'g', 4]) == [1]
assert my_solution.beautifulIndices(*['fape', 'vq', 'ap', 4]) == []
