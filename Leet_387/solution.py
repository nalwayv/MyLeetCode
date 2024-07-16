class Solution:
    """
    Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
    """
    def firstUniqChar(self, s: str) -> int:
        table: dict[str, int] = {}
        for ch in s:
            if ch in table:
                table[ch] += 1
            else:
                table[ch] = 0

        for idx, val in enumerate(s):
            if val in table and table[val] == 0:
                return idx
        return -1


def main() -> None:
    solution = Solution()

    print(f"Output: {solution.firstUniqChar("leetcode")}") #0
    print(f"Output: {solution.firstUniqChar("loveleetcode")}") #2
    print(f"Output: {solution.firstUniqChar("aabb")}")#-1
    print(f"Output: {solution.firstUniqChar("aadadaad")}")#-1


if __name__ == "__main__":
    main()