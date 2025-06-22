class Solution:
    def divideString(self, s: str, k: int, fill: str) -> list[str]:
        """
        Divides the input string `s` into groups of size `k`. If the last group is smaller than `k`, it is filled with the specified `fill` character.
        Args:
            s (str): The input string to be divided.
            k (int): The size of each group.
            fill (str): The character used to fill the last group if it is smaller than `k`.
        Returns:
            list[str]: A list of string groups, each of length `k`. The last group is padded with `fill` if necessary.
        """
        result: list[str] = []
        n: int = len(s)
        p1: int = 0
        p2: int = 0

        while p1 < n:
            step: int = k
            while p2 < n and step > 0:
                step -= 1
                p2 += 1

            diff: int = p2 - p1
            if diff != k:
                result.append(f"{s[p1:p2]}{fill * (k - diff)}")
            else:
                result.append(s[p1:p2])
            p1 = p2

        return result
        

def main() -> None:
    print("2138. Divide a String Into Groups of Size k")

    sol = Solution()

    print(sol.divideString("abcdefghi", 3, "x"))
    print(sol.divideString("abcdefghij", 3, "x"))
    print(sol.divideString("abcdefg", 2, "x"))


if __name__ == "__main__":
    main()
        