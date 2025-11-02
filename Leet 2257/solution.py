class Solution:
    def countUnguarded(self, m: int, n: int, guards: list[list[int]], walls: list[list[int]]) -> int:
        OPEN = 0
        BLOCKED = 1

        blocked: list[list[int]] = [
            [OPEN for _ in range(n)]
            for _ in range(m)
        ]

        for wx, wy in walls:
            blocked[wx][wy] = BLOCKED

        for gx, gy in guards:
            blocked[gx][gy] = BLOCKED

        guarded: list[list[int]] = [
            [OPEN for _ in range(n)]
            for _ in range(m)
        ]

        for gx, gy in guards:
            guarded[gx][gy] = BLOCKED

            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                x: int = gx + dx
                y: int = gy + dy

                while 0 <= x < m and 0 <= y < n and blocked[x][y] != BLOCKED:
                    guarded[x][y] = BLOCKED
                    x += dx
                    y += dy

        count: int = 0
        for r in range(m):
            for c in range(n):
                if guarded[r][c] == OPEN and blocked[r][c] == OPEN:
                    count += 1

        return count


def main() -> None:
    print('2257. Count Unguarded Cells in the Grid')

    solution = Solution()

    case_1 = solution.countUnguarded(4, 6, [[0,0],[1,1],[2,3]], [[0,1],[2,2],[1,4]])
    print(f'{case_1} == 7')

    case_2 = solution.countUnguarded(3, 3,[[1,1]], [[0,1],[1,0],[2,1],[1,2]])
    print(f'{case_2} == 4')

    case_3 = solution.countUnguarded(2, 7,[[1,5],[1,1],[1,6],[0,2]], [[0,6],[0,3],[0,5]])
    print(f'{case_3} == 1')


if __name__ == '__main__':
    main()