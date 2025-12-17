class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.upper().replace('-','')
        result: list[str] = []
        
        n: int = len(s)
        m: int = n % k

        if m == 0:
            for i in range(0, n, k):
                result.append(s[i : i + k])
        else:
            result.append(s[: m])
            for i in range(m, n, k):
                result.append(s[i : i + k])

        return '-'.join(result)
    

def main() -> None:
    print('482. License Key Formatting')

    solution = Solution()
    case1: str = solution.licenseKeyFormatting(s = '5F3Z-2e-9-w', k = 4)
    case2: str = solution.licenseKeyFormatting(s = '2-5g-3-J', k = 2)
    case3: str = solution.licenseKeyFormatting(s = '1a1-11-1a', k = 3)

    print(case1)
    print(case2)
    print(case3)


if __name__ == '__main__':
    main()