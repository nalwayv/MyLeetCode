class Solution:
    def remove_duplicates(self, nums: list[int]) -> int:
        n: int = len(nums)

        p1: int = 0
        p2: int = 0
        p3: int = 0
        k: int = 0

        while p1 < n:
            p2 = p1
            while p2 < n and nums[p1] == nums[p2]:
                p2 += 1

            diff: int = p2 - p1
            if diff >= 2:
                nums[p3] = nums[p1]
                p3 += 1

                nums[p3] = nums[p1]
                p3 += 1

                k += (diff - 2)
            else:
                nums[p3] = nums[p1]
                p3 += 1

            p1 = p2

        return n - k


def case1(sol: Solution) -> None:
    print("case 1")
    nums: list[int] = [1,1,1,2,2,3]
    k: int = sol.remove_duplicates(nums)
    print(f"{nums[:k]} K: {k}")
    print("[1, 1, 2, 2, 3] < above should be the same")


def case2(sol: Solution) -> None:
    print("case 2")
    nums: list[int] = [0,0,1,1,1,1,2,3,3]
    k: int = sol.remove_duplicates(nums)
    print(f"{nums[:k]} K: {k}")
    print("[0, 0, 1, 1, 2, 3, 3] < above should be the same")


def case3(sol: Solution) -> None:
    print("case 3")
    nums: list[int] = [1,1,1,1,2,2,2,2,3,3,3,3]
    k: int = sol.remove_duplicates(nums)
    print(f"{nums[:k]} K: {k}")
    print("[1, 1, 2, 2, 3, 3] < above should be the same")


def main() -> None:
    print("80. Remove Duplicates from Sorted Array II")

    sol = Solution()
    
    case1(sol)
    case2(sol)
    case3(sol)


if __name__ == "__main__":
    main()