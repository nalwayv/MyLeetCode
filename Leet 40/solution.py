class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()

        result: list[list[int]] = []
        current: list[int] = []

        def helper(target: int, start: int = 0):
            if target == 0:
                result.append(current[:])
                return
            
            if target < 0:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue

                current.append(candidates[i])
                helper(target - candidates[i], i + 1)
                current.pop()

        helper(target)

        return result


def main() -> None:
    print('40. Combination Sum II')

    solution = Solution()
    
    print(solution.combinationSum2([10, 1, 2, 7,6,1,5], 8))
    print(solution.combinationSum2([2,5,2,1,2], 5))


if __name__ == '__main__':
    main()