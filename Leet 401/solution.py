class Solution:
    def count_bits(self, n: int) -> int:
        count: int = 0
        while n > 0:
            count += (n & 1)
            n >>= 1
        return count

    def readBinaryWatch(self, turnedOn: int) -> list[str]:
        result: list[str] = []

        for i in range(12):
            for j in range(60):
                if self.count_bits(i << 6 | j) == turnedOn:
                    if j < 10:
                        result.append(f'{i}:0{j}')
                    else:
                        result.append(f'{i}:{j}')

        return result