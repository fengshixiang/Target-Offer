# class Solution:
#     def myPow(self, x: float, n: int) -> float:
#         if n == 0:
#             return 1
#         if n < 0:
#             return 1 / self.myPow(x, -n)
#         if n & 1:   # 等价于 n % 2 == 1
#             return x * self.myPow(x, n-1)
#         else:
#             return  self.myPow(x*x, n>>1)


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/ x
            n = -n
        res = 1
        while n:
            if n & 1:
                res = res * x
            x = x * x
            n = n >> 1
        return res