class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        sum_total: int = 0
        i: int = 1
        
        while i*i <= num:
            if num % i == 0 :
                sum_total += i

                if i*i != num:
                    sum_total += num//i
            i += 1

        return sum_total - num == num


def main():
    print("507. Perfect Number")
    sol = Solution()
    
    print(sol.checkPerfectNumber(6))
    print(sol.checkPerfectNumber(28))
    print(sol.checkPerfectNumber(496))


if __name__ == "__main__":
    main()