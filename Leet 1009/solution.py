class Solution:
    def bitwiseComplement(self, n: int) -> int:
        result: int = 0
        for i, val in enumerate(bin(n)[2:][::-1]):
            if val == '0':
                result += pow(2, i)
        return result


def main() -> None:
    print('1009. Complement of Base 10 Integer')

    sol = Solution()
    
    case1: int = sol.bitwiseComplement(5)
    result: str = 'pass' if case1 == 2 else 'fail'
    print(f'bitwiseComplement(5) should equal 2?: {result}')


if __name__ == '__main__':
    main()