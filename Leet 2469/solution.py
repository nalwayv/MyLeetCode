class Solution:
    def convertTemperature(self, celsius: float) -> list[float]:
        return [celsius + 273.15, celsius * 1.8 + 32.0]


def main() -> None:
    print('2469. Convert the Temperature')
    solution = Solution()
    case1 = solution.convertTemperature(36.50)
    print(case1)


if __name__ == '__main__':
    main()