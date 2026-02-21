class Solution:    
    def countPrimeSetBits(self, left: int, right: int) -> int:
        # constraints: 1 <= left <= right <= 10**6
        #   max length of bits is len(bin(10**6)) == 22
        #   biggest prime < 22 = 19
        primes: set[int] = {2, 3, 5, 7, 11, 13, 17, 19}
        count: int = 0
        for num in range(left, right + 1):
            if num.bit_count() in primes:
                count += 1
        return count
    

def main() -> None:
    print('762. Prime Number of Set Bits in Binary Representation')

    sol = Solution()
    
    case1 = sol.countPrimeSetBits(6,10)
    case1_result = 'pass' if case1 == 4 else 'fail'
    print(f'6-10 should equal 4? {case1_result}')

    case2 = sol.countPrimeSetBits(10,15)
    case2_result = 'pass' if case2 == 5 else 'fail'
    print(f'10-15 should equal 5? {case2_result}')


if __name__ == '__main__':
    main()