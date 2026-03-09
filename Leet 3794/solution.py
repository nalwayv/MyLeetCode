class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        str_to_k = s[:k]
        str_after_k = s[k:]
        str_to_k = str_to_k[::-1]
        
        return str_to_k + str_after_k
