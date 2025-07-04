from typing import NamedTuple


class TripData(NamedTuple):
    start_station: str
    time: int


class TripMean():
    def __init__(self) -> None:
        self.sum_total: int = 0
        self.length: int = 0

    def add(self, amount: int):
        self.sum_total += amount
        self.length += 1

    def mean(self) -> float:
        if self.length == 0:
            return 0.0
        return self.sum_total / self.length


class UndergroundSystem:
    def __init__(self):
        self.customers: dict[int, TripData] = {}
        self.trips: dict[str, TripMean] = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customers[id] = TripData(stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id not in self.customers:
            return
        
        if customer := self.customers.pop(id, None):
            trip_name: str = f"{customer.start_station}-{stationName}"

            if trip_name not in self.trips:
                self.trips[trip_name] = TripMean()

            self.trips[trip_name].add(abs(customer.time - t))

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        if trip := self.trips.get(f"{startStation}-{endStation}", None):
            return trip.mean()
        return 0.0
    

def main() -> None:
    print("1396. Design Underground System")

    undergroundSystem = UndergroundSystem()
    
    undergroundSystem.checkIn(45, "Leyton", 3)
    undergroundSystem.checkIn(32, "Paradise", 8)
    undergroundSystem.checkIn(27, "Leyton", 10)
    undergroundSystem.checkOut(45, "Waterloo", 15)
    undergroundSystem.checkOut(27, "Waterloo", 20)
    undergroundSystem.checkOut(32, "Cambridge", 22)
    print(undergroundSystem.getAverageTime("Paradise", "Cambridge"))    # return 14.00000. One trip "Paradise" -> "Cambridge", (14) / 1 = 14
    print(undergroundSystem.getAverageTime("Leyton", "Waterloo"))       # return 11.00000. Two trips "Leyton" -> "Waterloo", (10 + 12) / 2 = 11
    undergroundSystem.checkIn(10, "Leyton", 24)
    print(undergroundSystem.getAverageTime("Leyton", "Waterloo"))       # return 11.00000
    undergroundSystem.checkOut(10, "Waterloo", 38)
    print(undergroundSystem.getAverageTime("Leyton", "Waterloo"))       # return 12.00000. Three trips "Leyton" -> "Waterloo", (10 + 12 + 14) / 3 = 12


if __name__ == "__main__":
    main()