class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.slots: list[int] = [big, medium, small]

    def _is_empty(self, carType: int) -> bool:
        if carType >= 1 and carType <= 3:
            return self.slots[carType - 1] <= 0
        return False

    def addCar(self, carType: int) -> bool:
        if self._is_empty(carType):
            return False

        self.slots[carType - 1] -= 1
        
        return True
        

def add_car(p: ParkingSystem, cartype: int):
    if p.addCar(cartype):
        print(f"car was added")
    else:
        print("car was not added")


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)


def main() -> None:
    print("1603. Design Parking System")

    parking_system = ParkingSystem(1,1,0)
    
    add_car(parking_system, 1)
    add_car(parking_system, 2)
    add_car(parking_system, 3)
    add_car(parking_system, 1)


if __name__ == "__main__":
    main()