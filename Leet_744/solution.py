class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        target_i: int = ord(target)

        lo: int = 0
        hi: int = len(letters) - 1

        idx: int = -1

        while lo <= hi:
            mid: int = (lo + hi) // 2
            letter_i: int = ord(letters[mid])
            diff: int = letter_i - target_i

            if diff <= 0:
                lo = mid + 1
            else:
                hi = mid - 1

            idx = lo % len(letters)

        return letters[idx]