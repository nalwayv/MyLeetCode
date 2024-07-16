class Solution:
    """
    Write a function to find the longest common prefix string amongst an array of strings.

    If there is no common prefix, return an empty string "".

    Example 1:

        Input: strs = ["flower","flow","flight"]
        Output: "fl"
    """
    def longestCommonPrefix(self, strs: list[str]) -> str:
        strs_n: int = len(strs)
        pre: str = strs[0]
        pre_n: int = len(pre)
        
        for i in range(1, strs_n):
            while pre_n != 0 and strs[i][:pre_n] != pre[:pre_n]:
                pre_n -= 1
                
            if pre_n == 0:
                return ""

        return pre[:pre_n]

def main() -> None:
    solution = Solution()

    input1: list[str] = ["flower", "flow", "flight"]
    print(f"Output: {solution.longestCommonPrefix(input1)}")

    input2: list[str] = ["aa","aab","aabc"]
    print(f"Output: {solution.longestCommonPrefix(input2)}")


if __name__ == "__main__":
    main()