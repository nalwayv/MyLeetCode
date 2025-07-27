class Solution:
    def countHillValley(self, nums: list[int]) -> int:
        # remove repeating
        arr: list[int] = []
        for n in nums:
            if not arr:
                arr.append(n)
            elif arr[-1] != n:
                arr.append(n)
        
        count: int = 0
        for i in range(1, len(arr) - 1):
            a: int = arr[i - 1]
            b: int = arr[i]
            c: int = arr[i + 1]

            if b > a and b > c or b < a and b < c:
                count += 1

        return count


def main() -> None:
    print("2210. Count Hills and Valleys in an Array")

    sol = Solution()
    print("case 1")
    print(sol.countHillValley(nums=[2,4,1,1,6,5]), 3, sep= " == ")

    print("case 2")
    print(sol.countHillValley(nums=[6,6,5,5,4,1]), 0, sep=" == ")

    print("case 3")
    print(sol.countHillValley(nums=[1,1,2,2,2,2,2,1]), 1, sep= " == ")


if __name__ == "__main__":
    main()