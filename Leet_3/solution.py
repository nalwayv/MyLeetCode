class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        values: set[str] = set()
        
        result: int = 0
        p1: int = 0
        end: int = len(s)
        
        while p1 < end:
            p2: int = p1
            
            count: int = 0
            while p2 < end and s[p2] not in values:
                values.add(s[p2])
                p2 += 1
                count += 1

            result = max(result, count)
            values.clear()

            p1 += 1
    
        return result


def main() -> None:
    solution = Solution()
    print(f"Output {solution.lengthOfLongestSubstring("abcabcbb")}") # 3
    print(f"Output {solution.lengthOfLongestSubstring("bbbbb")}") # 1
    print(f"Output {solution.lengthOfLongestSubstring("pwwkew")}") # 3
    print(f"Output {solution.lengthOfLongestSubstring(" ")}") # 1
    print(f"Output {solution.lengthOfLongestSubstring("dvdf")}") # 3


if __name__ == "__main__":
    main()