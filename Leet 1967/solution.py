from typing import List

class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        count: int = 0
        for p in patterns:
            if word.find(p) >= 0:
                count += 1
        return count