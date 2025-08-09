class Solution:
    def memLeak(self, memory1: int, memory2: int) -> list[int]:
        bits: int = 1

        while True:
            if memory1 >= memory2 and memory1 - bits >= 0:
                print(f"{bits} bit of memory is allocated to stick 1")
                memory1 -= bits
            
            elif memory2 - bits >= 0:
                print(f"{bits} bit of memory is allocated to stick 2")
                memory2 -= bits
            
            else:
                print("crash")
                break

            bits += 1

        return [bits, memory1, memory2]


def main() -> None:
    print("1860. Incremental Memory Leak")

    sol = Solution()

    case1: list[int] = sol.memLeak(memory1=2, memory2=2)
    print(f"crashTime: {case1[0]}, memory1crash: {case1[1]}, memory2crash: {case1[2]}")

    case2: list[int] = sol.memLeak(memory1=8, memory2=11)
    print(f"crashTime: {case2[0]}, memory1crash: {case2[1]}, memory2crash: {case2[2]}")


if __name__ == "__main__":
    main()