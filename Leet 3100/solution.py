class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        full_bottles: int = 0
        empty_bottles: int = numBottles
        num_exchange: int = numExchange
        bottles_drunk: int = numBottles

        # Simulate
        while empty_bottles - num_exchange >= 0 or full_bottles != 0:
            if empty_bottles - num_exchange >= 0:
                # Exchange
                full_bottles += 1
                empty_bottles -= num_exchange
                num_exchange += 1
            else:
                # Drink
                empty_bottles += full_bottles
                bottles_drunk += full_bottles
                full_bottles = 0

        return bottles_drunk


def main() -> None:
    print('3100. Water Bottles II')

    solution = Solution()
    
    case1: int = solution.maxBottlesDrunk(numBottles= 13, numExchange= 6)
    print(f'case 1 should equal 15? {'pass' if case1 == 15 else 'fail'}')

    case2: int = solution.maxBottlesDrunk(numBottles= 10, numExchange= 3)
    print(f'case 2 should equal 13? {'pass' if case2 == 13 else 'fail'}')


if __name__ == '__main__':
    main()