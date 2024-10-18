class Solution:
    def hIndex(self, citations: list[int]) -> int:
        """
        Given a list of numbers return the h-index

        Example: 
        >>> hIndex([1,3,1])
        1
        """
        h: int = 0
        i: int = 1
        for num in reversed(sorted(citations)):
            if num >= i:
                h = i
                i += 1
        return h


def main() -> None:
    print("274. H-Index")
    
    solution: Solution = Solution()

    print(solution.hIndex([3,0,6,1,5]))
    print(solution.hIndex([1,3,1]))


if __name__ == "__main__":
    main()