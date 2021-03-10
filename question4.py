# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        height = len(array)
        width = len(array[0])
        m, n = height-1, 0
        while m >= 0 and n < width:
            if array[m][n] == target:
                return True
            elif array[m][n] < target:
                n += 1
            else:
                m -= 1
        
        return False

if __name__ == '__main__':
    s = Solution()
    a = [[1,2,8,9], [2,4,9,2], [4,7,10, 13], [6,8,11,15]]
    print(s.Find(5, a))