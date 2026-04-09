class Solution:
    def robotSim(self, commands: list[int], obstacles: list[list[int]]) -> int:
        blocked: set[tuple[int, int]] = set()
        for obs in obstacles:
            blocked.add((obs[0], obs[1]))

        directions: list[tuple[int, int]] = [(0, 1),(1, 0),(0, -1),(-1, 0)]

        x: int = 0
        y: int = 0
        current_dir: int = 0
        max_dist: int = 0

        for command in commands:
            if command == -1:
                current_dir = (current_dir + 1) % 4
            elif command == -2:
                current_dir = (current_dir - 1) % 4
            else:
                dir_x, dir_y = directions[current_dir]

                for _ in range(command):
                    next_x = x + dir_x
                    next_y = y + dir_y

                    if (next_x, next_y) in blocked:
                        break
                        
                    x = next_x
                    y = next_y
                    max_dist = max(max_dist, x*x + y*y)
                    
        return max_dist


def case1(sol: Solution) -> None:
    commands: list[int] = [4,-1, 3]
    obstacles: list[list[int]] = []
    result: int = sol.robotSim(commands, obstacles)
    print(f"case 1 {'pass' if result == 25 else 'fail'}")


def case2(sol: Solution) -> None:
    commands: list[int] = [4, -1, 4, -2, 4]
    obstacles: list[list[int]] = [[2, 4]]
    result: int = sol.robotSim(commands, obstacles)
    print(f"case 2 {'pass' if result == 65 else 'fail'}")


def case3(sol: Solution) -> None:
    commands: list[int] = [-2,-1,8,9,6]
    obstacles: list[list[int]] = [[-1,3],[0,1],[-1,5],[-2,-4],[5,4],[-2,-3],[5,-1],[1,-1],[5,5],[5,2]]
    result: int = sol.robotSim(commands, obstacles)
    print(f"case 3 {'pass' if result == 0 else 'fail'}")


def main() -> None:
    print("874. Walking Robot Simulation")

    sol = Solution()
    case1(sol)
    case2(sol)
    case3(sol)


if __name__ == "__main__":
    main()