class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        lo: int = 0
        hi: int = len(letters) - 1
        idx: int = -1

        while lo <= hi:
            mid: int = (lo + hi) // 2
            if letters[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1

            idx = lo % len(letters)

        return letters[idx]