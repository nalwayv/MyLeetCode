class Solution:
    def compress(self, chars: list[str]) -> int:
        p1: int = 0
        n: int = len(chars)
        chars2: list[str] = []

        while p1 < n:
            p2: int = p1

            while p2 < n and chars[p1] == chars[p2]:
                p2 += 1

            diff: int = p2 - p1

            if diff <= 1:
                chars2.append(chars[p1])
            elif diff < 9:
                chars2.append(chars[p1])
                chars2.append(str(diff))
            else:
                # deconstruct int
                base: int = 10
                nums: list[str] = []
                while diff > 0:
                    a: int = diff % base
                    nums.append(str(a))
                    diff //= base
                
                chars2.append(chars[p1])
                for num in reversed(nums):
                    chars2.append(num)

            p1 = p2

        for i,v in enumerate(chars2):
            chars[i] = v
        
        return len(chars2)
    

def main() -> None:
    print("443. String Compression")
    sol = Solution()
    chars: list[str] = ["a","a","b","b","c","c","c"]
    result: int = sol.compress(chars)
    print(f"Result: {result}, chars: {chars}")


if __name__ == "__main__":
    main()