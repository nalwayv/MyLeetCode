class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        result: int = numBottles

        while numBottles >= numExchange:
            d, m = divmod(numBottles, numExchange)
            result += d
            numBottles = d + m

        return result
    

def main() -> None:
    print('1518. Water Bottles')

    solution = Solution()
    
    print(solution.numWaterBottles(9, 3))#13
    print(solution.numWaterBottles(15, 4))#19


if __name__ == '__main__':
    main()