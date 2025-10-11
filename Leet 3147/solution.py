class Solution:
    def maximumEnergy(self, energy: list[int], k: int) -> int:
        length: int = len(energy)
        max_energy: float = -float('inf')

        for i in range(length - k, length):
            curr_energy: int = 0
            for j in range(i, -1, -k):
                curr_energy += energy[j]
                max_energy = max(max_energy, curr_energy)

        return int(max_energy)


def main() -> None:
    print('3147. Taking Maximum Energy From the Mystic Dungeon')

    sol = Solution()

    print(f'Case 1 should equal 3? {sol.maximumEnergy([5,2,-10,-5,1], 3)}')
    print(f'Case 2 should equal -1? {sol.maximumEnergy([-2,-3,-1], 2)}')


if __name__ == '__main__':
    main()