class Solution:
    def check(self, nums: list[int]) -> bool:
        n: int = len(nums)
        for i in range(1, n):
            if nums[i-1] > nums[i]:
                for j in range(1, n):
                    if nums[(i + j - 1) % n] > nums[(i + j) % n]:
                        return False

        return True


def main() -> None:
    print("1752. Check if Array Is Sorted and Rotated")

    sol = Solution()
    
    print(f"{sol.check([3,4,5,1,2])} = True")
    print(f"{sol.check([2,1,3,4])} = False")
    print(f"{sol.check([1,2,3])} = True")
    print(f"{sol.check([4,4,1,1,2,2,3,3])} = True")
    print(f"{sol.check([6,10,6])} = True")


if __name__ == "__main__":
    main()
        