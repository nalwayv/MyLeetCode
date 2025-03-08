class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n: int = len(blocks)
        result: int = 0
        normal: str = blocks.lower()

        for i in range(k):
            if normal[i] == "w":
                result += 1
        
        count: int = result
        for i in range(k, n):
            a: int = 1 if normal[i] == "w" else 0
            b: int = 1 if normal[i-k] == "w" else 0
            count += a - b
            result = min(result, count)

        return result


def test_case(sol: Solution, blocks: str, k: int, result: int) -> None:
    print(f"Test Case: '{blocks}' == {result}")
    print(f"{"":>2}pass" if sol.minimumRecolors(blocks, k) == result else "fail")


def main() -> None:
    print("2379. Minimum Recolors to Get K Consecutive Black Blocks")

    sol = Solution()
    test_case(sol, "WBBWWBBWBW", 7, 3)
    test_case(sol, "WBWBBBW", 2, 0)
    test_case(sol, "W", 1, 1)
    test_case(sol, "B", 1, 0)


if __name__ == "__main__":
    main()