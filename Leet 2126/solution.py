def asteroids_destroyed(mass:int, asteroids: list[int]) -> bool:
    asteroids.sort()
    count: int = 0

    for asteroid in asteroids:
        if asteroid > mass:
            break
    
        mass += asteroid
        count += 1

    return len(asteroids) == count


def main() -> None:
    print("2126. Destroying Asteroids")

    print(f"Result: {asteroids_destroyed(mass= 10, asteroids= [3,9,19,5,21])}")
    print(f"Result: {asteroids_destroyed(mass= 5, asteroids= [4,9,23,4])}")


if __name__ == "__main__":
    main()