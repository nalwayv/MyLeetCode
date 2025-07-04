class Solution:
    def findComplement(self, num: int) -> int:
        power: int = 1
        n: int = 0
        while power <= num:
            power *= 2
            n += 1

        for i in range(n):
            num = (num ^ (1 << i))

        return num
    

def main() -> None:
    print("476. Number Complement")

    sol = Solution()
    
    print(sol.findComplement(5) == 2)
    print(sol.findComplement(1) == 0)


if __name__ == "__main__":
    main()