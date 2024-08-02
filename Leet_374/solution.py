PICK: int = 13 # just a random number


def guess( guess: int) -> int:
    if guess > PICK:
        return -1
    
    if guess < PICK:
        return 1
    
    return 0


class Solution:
    def guessNumber(self, n: int) -> int:
        lo: int = 1
        hi: int = n

        while lo <= hi:
            mi: int = (lo + hi) // 2

            g: int = guess(mi)

            if g == 0:
                return mi
            
            if g < 0:
                hi = mi - 1
            else:
                lo = mi + 1


        return -1


def main() -> None:
    print("374. Guess Number Higher or Lower")
    
    sol = Solution()

    print(sol.guessNumber(1))
    print(sol.guessNumber(25))
    print(sol.guessNumber(50))


if __name__ == "__main__":
    main()