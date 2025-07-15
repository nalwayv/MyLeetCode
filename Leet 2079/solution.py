class Solution:
    def wateringPlants(self, plants: list[int], capacity: int) -> int:
        steps: int = 0
        can: int = capacity

        for i, plant in enumerate(plants):
            # need refil
            if can < plant:
                steps += i * 2
                can = capacity

            steps += 1
            can -= plant

        return steps


def main() -> None:
    print("2079. Watering Plants")

    sol = Solution()
    
    print(sol.wateringPlants(plants=[2,2,3,3], capacity=5), "== 14")
    print(sol.wateringPlants(plants=[7,7,7,7,7,7,7], capacity=8), "== 49")
    print(sol.wateringPlants(plants=[3,2,4,2,1], capacity=6), "== 17")


if __name__ == "__main__":
    main()

        