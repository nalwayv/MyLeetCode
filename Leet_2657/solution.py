class Solution:
    def findThePrefixCommonArray(self, A: list[int], B: list[int]) -> list[int]:
        if len(A) != len(B):
            return []

        a_nums: set[int] = {num for num in A}
        result: list[int] = []

        length: int = len(B)
        i: int = length
        while i > 0:
            count: int = 0
            for j in range(i):
                if B[j] in a_nums:
                    count += 1

            result.insert(0, count)

            i -= 1
            a_nums.remove(A[i])

        return result


def main() -> None:
    print("2657. Find the Prefix Common Array of Two Arrays")

    sol = Solution()
    print(sol.findThePrefixCommonArray([1,3,2,4], [3,1,2,4]))
    print(sol.findThePrefixCommonArray([2,3,1], [3,1,2]))


if __name__ == "__main__":
    main()
