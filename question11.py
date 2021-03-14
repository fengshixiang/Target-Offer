class Solution:
    def minArray(self, numbers: List[int]) -> int:
        if len(numbers) == 1:
            return numbers[0]
        a, b = 0, len(numbers) - 1
        mid = a
        while numbers[a] >= numbers[b]:
            if b - a == 1:
                mid = b
                break
            mid = (a + b) // 2
            if numbers[a] == numbers[mid] and numbers[mid] == numbers[b]:
                return self.min_in_order(numbers, a, b)
            if numbers[mid] >= numbers[a]:
                # mid在前半部分
                a = mid
            elif numbers[mid] <= numbers[b]:
                # mid在后半部分
                b = mid
        return numbers[mid]

    def min_in_order(self, numbers, index1, index2):
        m = numbers[index1]
        for i in range(index1+1, index2+1):
            if numbers[i] < m:
                m = numbers[i]
        return m