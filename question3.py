#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param numbers int整型一维数组 
# @return int整型
#

class Solution:
    def duplicate(self , numbers):
        # write code here
        d = dict()
        for n in numbers:
            if n in d:
                return n
            else:
                d[n] = 0
        return -1 