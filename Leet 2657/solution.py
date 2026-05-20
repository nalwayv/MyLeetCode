class Solution:
    def findThePrefixCommonArray(self, A: list[int], B: list[int]) -> list[int]:
        length: int = min(len(A), len(B))
        tally: dict[int, int] = {}
        result: list[int] = []

        count: int = 0

        for i in range(length):
            if A[i] not in tally:
                tally[A[i]] = 0

            tally[A[i]] += 1
            if tally[A[i]] == 2:
                count += 1
            
            if B[i] not in tally:
                tally[B[i]] = 0

            tally[B[i]] += 1
            if tally[B[i]] == 2:
                count += 1
                
            result.append(count)

        return result


def main() -> None:
    print("2657. Find the Prefix Common Array of Two Arrays")

    sol = Solution()
    print(sol.findThePrefixCommonArray([1,3,2,4], [3,1,2,4]))
    print(sol.findThePrefixCommonArray([2,3,1], [3,1,2]))


if __name__ == "__main__":
    main()
