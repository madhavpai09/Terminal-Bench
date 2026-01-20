
from typing import *

#<INSERT>

my_solution = Solution()

assert my_solution.minExtraChar(*['leetscode', ['leet', 'code', 'leetcode']]) == 1
assert my_solution.minExtraChar(*['sayhelloworld', ['hello', 'world']]) == 3
assert my_solution.minExtraChar(*['dwmodizxvvbosxxw', ['ox', 'lb', 'diz', 'gu', 'v', 'ksv', 'o', 'nuq', 'r', 'txhe', 'e', 'wmo', 'cehy', 'tskz', 'ds', 'kzbu']]) == 7
assert my_solution.minExtraChar(*['ecolloycollotkvzqpdaumuqgs', ['flbri', 'uaaz', 'numy', 'laper', 'ioqyt', 'tkvz', 'ndjb', 'gmg', 'gdpbo', 'x', 'collo', 'vuh', 'qhozp', 'iwk', 'paqgn', 'm', 'mhx', 'jgren', 'qqshd', 'qr', 'qpdau', 'oeeuq', 'c', 'qkot', 'uxqvx', 'lhgid', 'vchsk', 'drqx', 'keaua', 'yaru', 'mla', 'shz', 'lby', 'vdxlv', 'xyai', 'lxtgl', 'inz', 'brhi', 'iukt', 'f', 'lbjou', 'vb', 'sz', 'ilkra', 'izwk', 'muqgs', 'gom', 'je']]) == 2
assert my_solution.minExtraChar(*['eglglxa', ['rs', 'j', 'h', 'g', 'fy', 'l', 'fc', 's', 'zf', 'i', 'k', 'x', 'gl', 'qr', 'qj', 'b', 'm', 'cm', 'pe', 'y', 'ei', 'wg', 'e', 'c', 'll', 'u', 'lb', 'kc', 'r', 'gs', 'p', 'ga', 'pq', 'o', 'wq', 'mp', 'ms', 'vp', 'kg', 'cu']]) == 1
assert my_solution.minExtraChar(*['kngmktvcxrwubjzk', ['ktvc', 'pajp', 'x', 'emye', 'hde', 'haol', 'ubjz', 'tc', 'rb', 'kng', 'li', 'fph', 'd', 'rgrg']]) == 4
assert my_solution.minExtraChar(*['voctvochpgutoywpnafylzelqsnzsbandjcqdciyoefi', ['tf', 'v', 'wadrya', 'a', 'cqdci', 'uqfg', 'voc', 'zelqsn', 'band', 'b', 'yoefi', 'utoywp', 'herqqn', 'umra', 'frfuyj', 'vczatj', 'sdww']]) == 11
assert my_solution.minExtraChar(*['nwlztjn', ['a', 'f', 'v', 'me', 'm', 'bv', 'g', 'ss', 'tu', 'jm', 'z', 'kg', 'l', 'go', 'cn', 'uj', 'kx', 'w', 'qz', 'e', 'ut', 'tf', 'zn', 'ha', 'ke', 'af', 'aj', 'ls', 'r', 'no', 'pm', 'qn', 'yw', 'cs', 'oz', 'b']]) == 4
assert my_solution.minExtraChar(*['smsvy', ['j', 'p', 'y', 'r', 't', 'nj', 'k', 'xj', 'vg', 'da', 'm', 'u', 'yq', 'as', 'wh', 'b', 'vo', 'h', 'wb', 'z', 'np', 'uy', 'i', 'f', 'w', 'wg', 's', 'ls', 'xf', 'ou', 'mj', 'pf']]) == 1
assert my_solution.minExtraChar(*['azchrwjli', ['nrd', 'ulh', 'r', 'u', 'm', 'ue', 'jzd', 'zch', 'pbl', 'op', 'mw', 'wjl', 'wv', 'e']]) == 2
assert my_solution.minExtraChar(*['octncmdbgnxapjoqlofuzypthlytkmchayflwky', ['m', 'its', 'imaby', 'pa', 'ijmnvj', 'k', 'mhka', 'n', 'y', 'nc', 'wq', 'p', 'mjqqa', 'ht', 'dfoa', 'yqa', 'kk', 'pixq', 'ixsdln', 'rh', 'dwl', 'dbgnxa', 'kmpfz', 'nhxjm', 'wg', 'wky', 'oct', 'og', 'uhin', 'zxb', 'qz', 'tpf', 'hlrc', 'j', 'l', 'tew', 'xbn', 'a', 'uzypt', 'uvln', 'mchay', 'onnbi', 'hlytk', 'pjoqlo', 'dxsjr', 'u', 'uj']]) == 2
assert my_solution.minExtraChar(*['rqdrlfpthqkevauuks', ['pt', 'r', 'luet', 'hn', 'djj', 'nqk', 'yztb', 'yvrm', 'hjw', 'fon', 'hqke', 'btr', 'fg', 'guo', 'un', 'eyl', 'x', 'b', 'wj', 'yzy', 'dpj', 'z', 'oj', 'uu', 'fmp', 'ypmv', 'qd', 'rz', 'efj', 'sfc']]) == 6
assert my_solution.minExtraChar(*['etzdfxoxyajiothfsxxcxoxhfsxxcbvfmtcibmjkhniq', ['nio', 'y', 'jkhni', 'bu', 'hfsxxc', 'iacjvr', 'xox', 'vrslt', 'bvfm', 'gi', 'tjazf', 'ipfexh', 'tcib', 'crx', 'umxvs', 'q', 'e', 'rlpgq']]) == 10
assert my_solution.minExtraChar(*['t', ['q', 'f', 'b', 's', 'k', 't', 'p', 'i', 'o', 'v', 'l', 'u', 'c', 'm', 'r', 'd', 'g', 'e', 'j', 'h', 'y']]) == 0
assert my_solution.minExtraChar(*['cmizgedmufhbnqge', ['yid', 'u', 'jii', 'rdg', 'zcy', 'uo', 'buy', 's', 'vhn', 'ae', 'fygs', 'vlw', 'hv', 'nqge', 'fhb', 'oh', 'm', 'z', 't', 'rqwf', 'iqp', 'xan', 'ir', 'cmi', 'bim', 'bbd', 'jf', 'gs', 'vj']]) == 3
assert my_solution.minExtraChar(*['ybo', ['k', 'w', 'n', 's', 'v', 'i', 'q', 'j', 'h', 'o', 't', 'y', 'g', 'e', 'z', 'a', 'c', 'x', 'd', 'l', 'f']]) == 1
assert my_solution.minExtraChar(*['msgaxldzkgi', ['ax', 'ms', 'hvb', 'w', 'z', 'ajc', 'ti', 'cn', 'x', 'j', 'gi', 'r', 'nj', 'f', 'xr', 'iuz', 'ya', 'gty', 'hgs', 'ug', 'mfv', 'bw', 'vr', 'oe', 'xv', 'jf', 'vy', 'q', 'qf', 'oo', 'iq', 't', 'v', 'htx', 'g', 'gjp', 'dis', 'gt', 'gv', 'wu', 'vtx', 'cmo', 'wdl', 'b']]) == 3
assert my_solution.minExtraChar(*['jztkzefkuhgldeuxumtecjfhwkumklktbvoefjzgbvoebvoeo', ['tkzef', 'teq', 'idx', 'czset', 'jfh', 'fjz', 'nij', 'hpr', 'rhijyw', 'bvoe', 'k', 'umklkt', 'szbescz', 'pyiri', 'bc', 'fzyzcgc', 'lf', 's', 'kxalcws', 'w', 'euxumt', 'hlroawe', 'yvoyx', 'ucvzmc', 'blr', 'piasks', 'fblc']]) == 11
assert my_solution.minExtraChar(*['pkfydgpkffmfam', ['pk', 'f', 'kdy', 'tw', 'm']]) == 4
assert my_solution.minExtraChar(*['pucblaexghipwhcfkhwawsuszagdlajctwevqiccnqpyt', ['pyvu', 'vt', 'it', 'jc', 'ex', 'zmn', 'qahtts', 'c', 'q', 'jlui', 'zx', 'gt', 'djb', 'ywdyt', 'dc', 'fhw', 'ninhz', 'vqic', 'ern', 'dwzyiq', 'cvh', 'ualv', 'jgmal', 'soj', 'khwaw', 'zejzs', 'cjqrt', 'la', 'pucb', 'uc', 'ezqcsl', 'uxx', 'pvz', 'uownow', 'f', 'ipwhcf', 'us', 'cx', 'k']]) == 14
