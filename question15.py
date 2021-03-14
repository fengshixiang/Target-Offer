class Solution:
    def hammingWeight(self, n: int) -> int:
        a = 1
        total = 0
        for i in range(32):
            if n & a != 0:
                total += 1
            a = a << 1
        
        return total
