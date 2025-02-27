class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        """
        """
        n: int = len(nums)
        elements: int = 3
        count: int = 0

        for i in range(n):
            for j in range(i+1, n+1):
                if j - i >= elements:

                    previous_diff: int = -1
                    first_pass: bool = True
                    passed_test: bool = True

                    for k in range(i, j-1):
                        current_diff: int = nums[k+1] - nums[k]

                        if first_pass:
                            first_pass = False
                            previous_diff = current_diff
                        else:
                            if previous_diff != current_diff:
                                passed_test = False
                                break

                    if passed_test:
                        count += 1

        return count

    
#-------------------------------------------------------------
# TEST CASES


def test_case_1(sol: Solution) -> None:
    print("Case 1")
    nums: list[int] = [1,3,5,7,9]
    expected: int = 6
    result: int = sol.numberOfArithmeticSlices(nums)
    test: str = "pass" if result == expected else "fail"
    print(f"{"":>2} {test}")


def test_case_2(sol: Solution) -> None:
    print("Case 2")
    nums: list[int] = [7,7,7,7]
    expected: int = 3

    result: int = sol.numberOfArithmeticSlices(nums)
    test: str = "pass" if result == expected else "fail"
    print(f"{"":>2} {test}")


def test_case_3(sol: Solution) -> None:
    print("Case 3")
    nums: list[int] = [3,-1,-5,-9]
    expected: int = 3

    result: int = sol.numberOfArithmeticSlices(nums)
    test: str = "pass" if result == expected else "fail"
    print(f"{"":>2} {test}")


#-------------------------------------------------------------
# MAIN


def main() -> None:
    print("413. Arithmetic Slices")

    sol = Solution()

    test_case_1(sol)
    test_case_2(sol)
    test_case_3(sol)


if __name__ == "__main__":
    main()