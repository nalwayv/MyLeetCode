class Solution:
    def maxMatrixSum(self, matrix: list[list[int]]) -> int:
        negative_count = 0
        nums: list[int] = []

        for row in matrix:
            for val in row:
                nums.append(abs(val))
                if val < 0:
                    negative_count += 1

        nums.sort()
        if negative_count % 2 != 0:
            nums[0] *= -1
            return sum(nums)
        return sum(nums)


def main() -> None:
    print('1975. Maximum Matrix Sum')

    solution = Solution()

    case1 = solution.maxMatrixSum([[1,-1],[-1,1]])
    print(f'case 1 should equal 4: {case1}')
    
    case2 = solution.maxMatrixSum([[1,2,3],[-1,-2,-3],[1,2,3]])
    print(f'case 2 should equal 16: {case2}')


if __name__ == '__main__':
    main()
