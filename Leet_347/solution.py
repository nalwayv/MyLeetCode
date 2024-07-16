class Solution:
    """
    Given an integer array nums and an integer k, 
    
    return the k most frequent elements. 
    
    You may return the answer in any order.

    Example 1:
        Input: nums = [1,1,1,2,2,3], k = 2
        Output: [1,2]
    """
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        table: dict[int, int] = {}
        for n in nums:
            if n in table:
                table[n] += 1
            else:
                table[n] = 1

        result: list[int] = []
        for _ in range(k):
            hi: int = -1
            num: int = 0
            for key, val in table.items():
                if val > hi:
                    hi = val
                    num = key

            result.append(num)
            table.pop(num)
            
        return result


def test_1(solution: Solution) -> None:
    # [1, 2]
    nums: list[int] = [1,1,1,2,2,3]
    k: int = 2
    result: list[int] = solution.topKFrequent(nums, k)
    print(f"Output: {result}")


def test_2(solution: Solution) -> None:
    # [1]
    nums: list[int] = [1]
    k: int = 1
    result: list[int] = solution.topKFrequent(nums, k)
    print(f"Output: {result}")


def test_3(solution: Solution) -> None:
    # [1, 2]
    nums: list[int] = [1,2]
    k: int = 2
    result: list[int] = solution.topKFrequent(nums, k)
    print(f"Output: {result}")


def test_4(solution: Solution) -> None:
    # [0]
    nums: list[int] = [3,0,1,0]
    k: int = 1
    result: list[int] = solution.topKFrequent(nums, k)
    print(f"Output: {result}")


def test_5(solution: Solution) -> None:
    # [-1, 2]
    nums: list[int] = [4,1,-1,2,-1,2,3]
    k: int = 2
    result: list[int] = solution.topKFrequent(nums, k)
    print(f"Output: {result}")


def main() -> None:
    solution = Solution()

    test_1(solution)
    test_2(solution)
    test_3(solution)
    test_4(solution)
    test_5(solution)


if __name__ == "__main__":
    main()