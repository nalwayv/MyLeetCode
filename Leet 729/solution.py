from bisect import bisect_left

class MyCalendar:
    def __init__(self):
        self.bookings: list[tuple[int, int]] = []

    def bookings_overlap(self, booking_1: tuple[int, int], booking_2: tuple[int, int]) -> bool:
        return (booking_2[0] < booking_1[1]) and (booking_1[0] < booking_2[1])

    def book(self, startTime: int, endTime: int) -> bool:
        booking: tuple[int, int] = (startTime, endTime)

        if not self.bookings:
            self.bookings.append(booking)
        else:
            at: int = bisect_left(self.bookings, booking)
            n: int = len(self.bookings)

            if (at - 1) >= 0 and self.bookings_overlap(self.bookings[at-1], booking):
                return False

            if at < n and self.bookings_overlap(self.bookings[at], booking):
                return False
                
            self.bookings.insert(at, booking)

        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)


def main() -> None:
    print("729. My Calendar I")

    calendar = MyCalendar()
    
    for time_range in [(10, 20), (15, 25), (20, 30)]:
        print(f"{time_range}, {"pass" if calendar.book(*time_range) else "fail"}")


if __name__ == "__main__":
    main()