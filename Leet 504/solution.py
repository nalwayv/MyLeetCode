
class Solution:
    def convertToBase7(self, num: int) -> str:
        """Given an integer num, return a string of its base 7 representation.

        Args:
            num (int): integer to convert

        Returns:
            str: base 7 representation of num
        """
        if num == 0:
            return '0'

        sign = -1 if num < 0 else 1
        num = abs(num)

        result: str = ''
        while num > 0:
            r = num % 7
            result =  str(r) + result
            num //= 7
        
        if sign == -1:
            result = '-' + result

        return result


def test_case(sol: Solution, num: int, expected: str) -> None:
    result: str = sol.convertToBase7(num)
    test: str = "pass" if result == expected else "fail"    
    print(f'{num} should equal {expected}?: {test}')


def main() -> None:
    print("504. Base 7")
    
    sol = Solution()
    
    test_case(sol, 100, '202')
    test_case(sol, -7, '-10')


if __name__ == "__main__":
    main()  