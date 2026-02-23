class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        max_size: int = pow(2, k)
        
        seen: set[str] = set()
        
        for i in range(len(s) - k + 1):
            seen.add(s[i:i+k])

            if len(seen) == max_size:
                return True

        return False