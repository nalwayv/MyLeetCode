class Solution:
    """
    You're given strings jewels representing the types of stones that are jewels, 
    
    and stones representing the stones you have. Each character in stones is a type of stone you have. 
    
    You want to know how many of the stones you have are also jewels.

    Letters are case sensitive, so "a" is considered a different type of stone from "A".

    Example 1:
        Input: jewels = "aA", stones = "aAAbbbb"
        Output: 3
    
    Example 2:
        Input: jewels = "z", stones = "ZZ"
        Output: 0
    """
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        table: dict[str, int] = {}

        for s in stones:
            if s in table:
                table[s] += 1
            else:
                table[s] = 1

        # sum from available stones
        result: int = 0
        for s in jewels:
            if s in table:
                result += table[s]

        return result


def main() -> None:
    solution = Solution()

    print(f"Output {solution.numJewelsInStones("aA", "aAAbbbb")}")
    print(f"Output {solution.numJewelsInStones("z", "ZZ")}")


if __name__ == "__main__":
    main()