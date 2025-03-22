class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        """
        Given an integer array nums, 
        return the largest perimeter of a triangle with a non-zero area

        Args:
            nums (list[int]):
        Returns:
            int:
                max perimeter
        """
        # being sorted helps with one of the perimeter rules of 'a + b > c'
        sorted_arr = sorted(nums)

        result: int = 0
        for i in range(len(sorted_arr) - 2):
            a: int = sorted_arr[i + 0]
            b: int = sorted_arr[i + 1]
            c: int = sorted_arr[i + 2]
            
            # if pass store max perimeter
            if (a + b) > c:
                result = max(result, a+b+c)

        return result


def case1(sol: Solution) -> None:
    nums: list[int] = [2,1,2]
    expected: int = 5
    result: int = sol.largestPerimeter(nums)
    print(f"Case1: {"pass" if result == expected else "fail"}")


def case2(sol: Solution) -> None:
    nums: list[int] = [1,2,1,10]
    expected: int = 0
    result: int = sol.largestPerimeter(nums)
    print(f"Case1: {"pass" if result == expected else "fail"}")


def main() -> None:
    print("976. Largest Perimeter Triangle")

    sol = Solution()

    case1(sol)
    case2(sol)


if __name__ == "__main__":
    main()