import heapq


class SeatManager:
    def __init__(self, n: int):
        self._seats: list[int] = [i for i in range(1, n+1)]
        self._seat_numbers: set[int] = {i for i in range(1, n+1)}
        heapq.heapify(self._seats)

    def reserve(self) -> int:
        if not self._seats:
            return 0
        
        seat: int = heapq.heappop(self._seats)
        self._seat_numbers.remove(seat)
        return seat

    def unreserve(self, seatNumber: int) -> None:
        if seatNumber in self._seat_numbers:
            return
        
        self._seat_numbers.add(seatNumber)
        heapq.heappush(self._seats, seatNumber)


def main() -> None:
    print("--- 1845. Seat Reservation Manager ---")

    manager = SeatManager(5)

    print(f"reserve {manager.reserve():>3}")
    print(f"reserve {manager.reserve():>3}")

    print("unreserve 2")
    manager.unreserve(2)

    print(f"reserve {manager.reserve():>3}")
    print(f"reserve {manager.reserve():>3}")
    print(f"reserve {manager.reserve():>3}")
    print(f"reserve {manager.reserve():>3}")

    print("unreserve 5")
    manager.unreserve(5)

    print(f"reserve {manager.reserve():>3}")


if __name__ == "__main__":
    main()