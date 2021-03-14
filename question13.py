class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        visited = [[False]*n for i in range(m)]
        count = self.count_path(m ,n, k, 0, 0, visited)
        
        return count

    def count_path(self, m, n, k, row, col, visited):
        count = 0
        if row >= 0 and row < m and col >= 0 and col < n and not visited[row][col]\
            and self._sum(row) + self._sum(col) <= k:
            visited[row][col] = True
            count = 1
            count += self.count_path(m, n, k, row, col+1, visited) +\
                    self.count_path(m, n, k, row, col-1, visited) +\
                    self.count_path(m, n, k, row+1, col, visited) +\
                    self.count_path(m, n, k, row-1, col, visited)

        return count

    def _sum(self, num):
        total = 0
        while num >= 10:
            total += num % 10
            num = num // 10
        total += num

        return total

if __name__ == '__main__':
    m = 1
    n = 2
    k = 1

    s = Solution()
    print(s.movingCount(m, n, k))
    # print(s._sum(2))