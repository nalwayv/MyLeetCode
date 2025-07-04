class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        """
        Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
        Return the array in the form [x1,y1,x2,y2,...,xn,yn].
        """
        result: list[int] = []

        p1: int = 0
        for p2 in range(n, n*2):
            result.append(nums[p1])
            result.append(nums[p2])
            p1 += 1

        return result


def test_case(sol: Solution, nums: list[int], expected: list[int], n: int) -> None:
    result: list[int] = sol.shuffle(nums, n)
    test: str = "pass" if result == expected else "fail"
    print(f"Test Case nums: {nums}, n: {n} = {test}")


def main() -> None:
    print("1470. Shuffle the Array")

    sol = Solution()

    nums_1: list[int] = [2,5,1,3,4,7]
    expect_1: list[int] = [2,3,5,4,1,7] 
    test_case(sol, nums_1, expect_1, 3)

    nums_2: list[int] = [1,2,3,4,4,3,2,1]
    expect_2: list[int] = [1,4,2,3,3,2,4,1]
    test_case(sol, nums_2, expect_2, 4)


if __name__ == "__main__":
    main()

        