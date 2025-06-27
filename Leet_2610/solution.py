class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        # Conditions
        # - The 2D array should contain only the elements of the array nums.
        # - Each row in the 2D array contains distinct integers.
        # - The number of rows in the 2D array should be minimal.
        table: dict[int, int] = {}
        result: list[list[int]] = []

        for num in nums:
            if num not in table:
                table[num] = 0

            frequency = table[num]
            if frequency >= len(result):
                result.append([])

            result[frequency].append(num)
            table[num] += 1

        return result


def main() -> None:
    print("2610. Convert an Array Into a 2D Array With Conditions")
    
    sol = Solution()
    print(sol.findMatrix([1,3,4,1,2,3,1]))
    print(sol.findMatrix([1,2,3,4]))


if __name__ == "__main__":
    main()