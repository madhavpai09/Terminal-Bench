
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.beautifulIndices(*['isawsquirrelnearmysquirrelhouseohmy', 'my', 'squirrel', 15]) == [16, 33]
assert my_solution.beautifulIndices(*['abcd', 'a', 'a', 4]) == [0]
assert my_solution.beautifulIndices(*['a', 'a', 'a', 1]) == [0]
assert my_solution.beautifulIndices(*['aba', 'a', 'a', 1]) == [0, 2]
assert my_solution.beautifulIndices(*['nvnvt', 'eq', 'nv', 1]) == []
assert my_solution.beautifulIndices(*['npearbvede', 'myqpb', 'pearb', 9]) == []
assert my_solution.beautifulIndices(*['vatevavakz', 'va', 'lbda', 1]) == []
assert my_solution.beautifulIndices(*['ithhi', 't', 'hhi', 1]) == [1]
assert my_solution.beautifulIndices(*['osuv', 'osuv', 'wrn', 1]) == []
assert my_solution.beautifulIndices(*['dc', 'dreec', 'dc', 2]) == []
assert my_solution.beautifulIndices(*['jajrfw', 'rf', 'j', 3]) == [3]
assert my_solution.beautifulIndices(*['zcvx', 'kfdvv', 'tru', 1]) == []
assert my_solution.beautifulIndices(*['wltmqbxt', 'mqbxt', 'lt', 7]) == [3]
assert my_solution.beautifulIndices(*['gggsytwgzg', 'sytwg', 'g', 4]) == [3]
assert my_solution.beautifulIndices(*['diive', 'viw', 'lqqdn', 4]) == []
assert my_solution.beautifulIndices(*['ss', 'omkdt', 's', 1]) == []
assert my_solution.beautifulIndices(*['hfzoxcm', 'hfzo', 'ipelr', 1]) == []
assert my_solution.beautifulIndices(*['xllimtmil', 'imt', 'iwqx', 5]) == []
assert my_solution.beautifulIndices(*['vdyl', 'i', 'ir', 4]) == []
assert my_solution.beautifulIndices(*['ouwpaz', 'mxre', 'pa', 5]) == []
