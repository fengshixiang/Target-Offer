class Solution:
    def cuttingRope(self, n: int) -> int:
        if n <= 1:
            return n
        if n == 2:
            return 1
        if n == 3:
            return 2
        
        products = [0, 1, 2, 3]
        for i in range(4, n+1):
            max = 0
            for j in range(1, i//2 + 1):
                if products[j] * products[i-j] > max:
                    max = products[j] * products[i-j]
                
            products.append(max)

        return products[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.cuttingRope(4))