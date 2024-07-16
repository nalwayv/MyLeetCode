class Solution:
    """
    Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

    Example:
        Input: haystack = "sadbutsad", needle = "sad"
        Output: 0
        
        Explanation: "sad" occurs at index 0 and 6.
        The first occurrence is at index 0, so we return 0.
    """
    def strStr(self, haystack: str, needle: str) -> int:
        haystack_len: int = len(haystack)
        needle_len: int = len(needle)

        if needle_len > haystack_len:
            # way to big
            return -1

        for p1 in range(haystack_len):
            if p1 < haystack_len and (p1 + needle_len) <= haystack_len:
                if haystack[p1:p1 + needle_len] == needle:
                    return p1
        return -1


def main() -> None:
    solution = Solution()
    print(f"Output: {solution.strStr("sadbutsad", "sad")}")
    print(f"Output: {solution.strStr("leetcode", "leeto")}")

if __name__ == "__main__":
    main()