#!usr/bin/env python3
# coding: utf-8
# @time :2021/1/26 12:48

"""
1128. 等价多米诺骨牌对的数量

"""
from typing import List


class MySolution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:

        count = 0
        countDict = {}
        for d in dominoes:
            if d[0] <= d[1]:
                x = str(d[0]*10 + d[1])
            else:
                x = str(d[1]*10 + d[0])
            if x not in countDict:
                countDict[x] = 1
            else:
                countDict[x] += 1

        for v in countDict.values():
            count += (v - 1) * v // 2

        return count


class OfficialSolution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        num = [0] * 100
        ret = 0
        for x, y in dominoes:
            val = (x * 10 + y if x <= y else y * 10 + x)
            ret += num[val]
            num[val] += 1
        return ret


# 作者：LeetCode - Solution
# 链接：https: // leetcode - cn.com / problems / number - of - equivalent - domino - pairs / solution / deng - jie - duo - mi - nuo - gu - pai - dui - de - shu - li - yjlz /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

s = MySolution()
s2 = OfficialSolution()
a = s.numEquivDominoPairs([[1, 2], [2, 1], [1, 2]])
b = s2.numEquivDominoPairs([[1, 2], [2, 1], [1, 2]])
print(a, b)