class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        if not digits:
            return []
        
        add: int = 1
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += add
            if digits[i] == 10:
                digits[i] = 0
                add = 1
            else:
                add = 0

        if digits[0] == 0:
            digits.insert(0, 1)

        return digits

        
def main() -> None:
    print('66. Plus One')

    solution = Solution()
    digits: list[int] = [9,9]
    result: list[int] = solution.plusOne(digits)
    
    print(f'Output: {result}')


if __name__ == '__main__':
    main()