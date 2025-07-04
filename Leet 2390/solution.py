class Solution:
    def removeStars(self, s: str) -> str:
        stk: list[str] = [] 
        for c in s:
            if c == "*" and len(stk) > 0:
                stk.pop()
            else:
                stk.append(c)
        return "".join(stk)
    

def main() -> None:
    print("2390. Removing Stars From a String")
    
    sol = Solution()

    result: str = sol.removeStars("leet**cod*e")
    expect: str = "lecoe"
    print(result == expect)


if __name__ == "__main__":
    main()