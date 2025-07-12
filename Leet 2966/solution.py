class Solution:
    def divideArray(self, nums: list[int], k: int) -> list[list[int]]:
        """
        Divides the input list `nums` into groups of three such that the maximum difference
        within each group does not exceed `k`.

        Parameters:
            nums (list[int]): The list of integers to be divided that has to have a length that is devisable by 3.
            k (int): The maximum allowed difference between the largest and smallest number in each group.
        
        Returns:
            list[list[int]]: A list of groups where the difference 
            between the maximum and minimum in each group is at most `k`.
        """
        n: int = len(nums)
        if n % 3 != 0:
            return []
        
        nums.sort()

        result: list[list[int]] = []

        size: int = n // 3

        i: int = 0
        while i < n:
            group: list[int] = nums[i : i + 3]
            if group[-1] - group[0] <= k:
                result.append(group)
            i += 3

        if len(result) != size:
            result.clear()
            return result
        return result


def main() -> None:
    print("2966. Divide Array Into Arrays With Max Difference")

    sol = Solution()

    print("case 1")
    print(sol.divideArray(nums=[1, 3, 4, 8, 7, 9, 3, 5, 1], k=2))

    print("case 2")
    print(sol.divideArray(nums=[2, 4, 2, 2, 5, 2], k=2))

    print("case 3")
    print(
        sol.divideArray(
            nums=[4, 2, 9, 8, 2, 12, 7, 12, 10, 5, 8, 5, 5, 7, 9, 2, 5, 11], k=14
        )
    )


if __name__ == "__main__":
    main()
