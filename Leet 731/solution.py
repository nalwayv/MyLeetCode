class MyCalendarTwo:
    def __init__(self):
        self.bookings: list[tuple[int, int]] = []
        self.overlaps: list[tuple[int, int]] = []

    def overlap(self, s1: int, e1:int, s2: int, e2: int) -> bool:
        return e1 > s2 and e2 > s1

    def book(self, startTime: int, endTime: int) -> bool:
        for s, e in self.overlaps:
            if self.overlap(startTime, endTime, s, e):
                return False
            
        for s, e in self.bookings:
            if self.overlap(startTime, endTime, s, e):
                overlap_duration: tuple[int, int] = (max(s, startTime), min(e, endTime))
                self.overlaps.append(overlap_duration)

        self.bookings.append((startTime, endTime))
        return True


def main() -> None:
    print("731. My Calendar II")

    myCalendarTwo = MyCalendarTwo()

    print("(10, 20)", myCalendarTwo.book(10, 20))   # return True, The event can be booked
    print("(50, 60)", myCalendarTwo.book(50, 60))   # return True, The event can be booked
    print("(10, 40)", myCalendarTwo.book(10, 40))   # return True, The event can be double booked 
    print("(5, 15)", myCalendarTwo.book(5, 15))     # return False, The event cannot be booked
    print("(5, 10)", myCalendarTwo.book(5, 10))     # return True, The event can be booked
    print("(25, 55)", myCalendarTwo.book(25, 55))   # return True, The event can be booked


if __name__ == "__main__":
    main()