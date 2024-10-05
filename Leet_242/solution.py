from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count: Counter[str] = Counter(t)
        for ch in s:
            if ch in count and count[ch] > 0:
                count[ch] -= 1
            else:
                return False
            
        # make sure all letters have been used
        
        for v in count.values():
            if v > 0:
                return False
            
        return True
    

def main() -> None:
    print("242. Valid Anagram")
    
    sol = Solution()
    is_anagram: bool = sol.isAnagram("nagaram", "nagaram")
    print(f"case1 {"pass" if is_anagram else "fail"}")


if __name__ == "__main__":
    main()

