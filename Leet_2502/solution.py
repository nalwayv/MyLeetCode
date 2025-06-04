class Allocator:
    def __init__(self, n: int):
        self.n: int = n
        self.block: list[int] = [0] * n

    def allocate(self, size: int, mID: int) -> int:
        """
        Allocates a contiguous block of memory of the given size and assigns it to the specified mID.
        
        Args:
            size (int): The number of contiguous memory units to allocate.
            mID (int): The ID to assign to the allocated memory units.

        Returns:
            int: The starting index of the allocated block if successful; otherwise, -1 if allocation fails.
        """
        left: int = 0
        for right in range(self.n):
            if self.block[right] == 0:
                if right - left + 1 == size:
                    for i in range(left, right + 1):
                        self.block[i] = mID
                    return left
            else:
                left = right + 1

        return -1

    def freeMemory(self, mID: int) -> int:
        """
        Frees all memory blocks allocated to the given memory ID (mID).

        Iterates through the memory blocks and resets any block assigned to mID to 0, 
        effectively freeing it. Returns the number of blocks that were freed.

        Args:
            mID (int): The memory ID to be freed.

        Returns:
            int: The number of memory blocks that were freed.
        """
        count: int = 0
        for i in range(self.n):
            if self.block[i] == mID:
                self.block[i] = 0
                count += 1
        return count


def main() -> None:
    print("2502. Design Memory Allocator")

    alloc = Allocator(10)

    print(f"alloc(1,1) = 0 ? {'pass' if alloc.allocate(1,1) == 0 else 'fail'}")
    print(f"alloc(1,2) = 1 ? {'pass' if alloc.allocate(1,2) == 1 else 'fail'}")
    print(f"alloc(1,3) = 2 ? {'pass' if alloc.allocate(1,3) == 2 else 'fail'}")
    print(f"free(2) = 1 ? {'pass' if alloc.freeMemory(2) == 1 else 'fail'}")
    print(f"alloc(3,4) = 3 ? {'pass' if alloc.allocate(3,4) == 3 else 'fail'}")
    print(f"alloc(1,1) = 1 ? {'pass' if alloc.allocate(1,1) == 1 else 'fail'}")
    print(f"alloc(1,1) = 6 ? {'pass' if alloc.allocate(1,1) == 6 else 'fail'}")
    print(f"free(1) = 3 ? {'pass' if alloc.freeMemory(1) == 3 else 'fail'}")
    print(f"alloc(10,2) = -1 ? {'pass' if alloc.allocate(10, 2) == -1 else 'fail'}")
    print(f"free(7) = 0 ? {'pass' if alloc.freeMemory(7) == 0 else 'fail'}")


if __name__ == "__main__":
    main()
