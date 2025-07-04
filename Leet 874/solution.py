import math

class Coord:
    def __init__(self, x: int = 0, y: int = 0) -> None:
        self.x: int = x
        self.y: int = y
    
    def length_squared(self) -> int:
        return self.x * self.x + self.y * self.y
    

class Solution:
    def _to_hash(self, x: int, y: int) -> str:
        return f"({x},{y})"

    def _move_to(self, coord: Coord, length: int, angle: int) -> Coord:
        r: float = math.radians(angle)
        x: int = coord.x + length * int(math.cos(r))
        y: int = coord.y + length * int(math.sin(r))

        return Coord(x, y)

    def robotSim(self, commands: list[int], obstacles: list[list[int]]) -> int:
        blocked: set[str] = set()
        for obs in obstacles:
            blocked.add(self._to_hash(obs[0], obs[1]))

        coord = Coord()
        direction: int = 90
        furthest: int = 0

        for move in commands:
            if move in [-1, -2]:
                if move == -1:
                    direction -= 90

                if move == -2:
                    direction += 90

                direction %= 360
                if direction < 0:
                    direction += 360

            else:
                for _ in range(move):
                    step: Coord = self._move_to(coord, 1, direction)
                    
                    if self._to_hash(step.x, step.y) in blocked:
                        break
                    
                    coord = step

                furthest = max(furthest, coord.length_squared())

        return furthest


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