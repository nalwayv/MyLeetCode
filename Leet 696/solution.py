class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # count substring of same type
        # [00100] -> [2,1,2]
        counts: list[int] = []
        i: int = 0
        while i < len(s):
            current: str = s[i]
            count: int = 0
            while i < len(s) and current == s[i]:
                count += 1
                i += 1
            counts.append(count)

        # sum min values
        # [2,1,2] -> 1, 1
        result: int = 0
        for c in range(len(counts) - 1):
            result += min(counts[c], counts[c+1])

        return result


def main() -> None:
    print('696. Count Binary Substrings')

    sol = Solution()
    
    test_cases: list[tuple[str, int]] = [('00110011', 6), ('10101', 4), ('00100', 2)]
    for value, expected in test_cases:
        result = sol.countBinarySubstrings(value)
        status = 'pass' if result == expected else 'fail'
        print(f'case {value}: {status}')


if __name__ == '__main__':
    main()