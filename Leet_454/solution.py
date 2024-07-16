class Solution:
    def fourSumCount(self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
        table: dict[int, int] = {}
        n: int = len(nums1)
        result: int = 0

        for i in range(n):
            for j in range(n):
                k1: int = nums1[i] + nums2[j]
                if k1 in table:
                    table[k1] += 1
                else:
                    table[k1] = 1

        for i in range(n):
            for j in range(n):
                k1: int = 0 - (nums3[i] + nums4[j])
                if k1 in table:
                    result += table[k1]

        return result

def test_1(solution: Solution) -> None:
    nums1: list[int] = [1, 2]
    nums2: list[int] = [-2, -1]
    nums3: list[int] = [-1, 2]
    nums4: list[int] = [0, 2]
    result: int = solution.fourSumCount(nums1, nums2, nums3, nums4)
    print(f"Output: {result}")


def test_2(solution: Solution) -> None:
    nums1: list[int] = [0]
    nums2: list[int] = [0]
    nums3: list[int] = [0]
    nums4: list[int] = [0]
    result: int = solution.fourSumCount(nums1, nums2, nums3, nums4)
    print(f"Output: {result}")


def main() -> None:
    solution = Solution()

    test_1(solution)
    test_2(solution)


if __name__ == "__main__":
    main()