def rotate_list(nums: list[int], k: int) -> None:
    def reverse_list(nums: list[int], left: int, right: int) -> None:
        if not nums or len(nums) == 1:
            return

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    length: int = len(nums)
    n: int = length
    m: int = n - (k % length)

    reverse_list(nums, 0, m - 1)  # rotate left half
    reverse_list(nums, m, n - 1)  # rotate right half
    reverse_list(nums, 0, n - 1)  # rotate whole


def create_grid(rows: int, cols: int, default_value: int = 0) -> list[list[int]]:
    """Create a 2D grid of size rows * cols with default_value.

    Args:
        rows: number of rows
        cols: number of columns
        default_value: value to fill grid with

    Returns:
        list[list[int]]: 2D grid of size rows * cols with default_value
    """
    return [[default_value for _ in range(cols)] for _ in range(rows)]


def shift_grid(grid: list[list[int]], k: int) -> list[list[int]]:
    """Rotate a 2D grid of size m * n by k

    Args:
        grid: 2D grid of size m * n
        k: number of positions to rotate by

    Returns:
        list[list[int]]: rotated grid
    """
    rows: int = len(grid)
    cols: int = len(grid[0])

    # convert to 1d
    one: list[int] = []
    for r in range(rows):
        for c in range(cols):
            one.append(grid[r][c])

    # shift by k
    rotate_list(one, k)

    result: list[list[int]] = create_grid(rows, cols)
    for r in range(rows):
        for c in range(cols):
            result[r][c] = one[r * cols + c]

    return result


def print_grid(grid: list[list[int]]) -> None:
    for row in grid:
        print("[", end="")
        for val in row:
            print(f" {val} ", end="")
        print("]")


def main() -> None:
    print("1260. Shift 2D Grid")

    grid: list[list[int]] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    result: list[list[int]] = shift_grid(grid, k=1)
    print_grid(result)


if __name__ == "__main__":
    main()
