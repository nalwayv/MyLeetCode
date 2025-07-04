class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        till: dict[str, int] = {"five": 0, "ten": 0, "twenty": 0}

        for bill in bills:
            if bill == 5:
                till["five"] += 1

            if bill == 10: 
                till["ten"] += 1
                if till["five"] > 0:
                    till["five"] -= 1
                else:
                    return False      
                    
            if bill == 20:
                # change could be 3 fives or 1 five and a ten
                till["twenty"] += 1

                if till["five"] > 0 and till["ten"] > 0:
                    till["five"] -= 1
                    till["ten"] -= 1
                elif till["five"] >= 3:
                    till["five"] -= 3
                else:
                    return False

        return True
    

def main() -> None:
    sol = Solution()

    input1: list[int] = [5,5,5,10,20]
    print("pass" if sol.lemonadeChange(input1) else "fail")

    input2: list[int] = [5,5,10,10,20]
    print("pass" if not sol.lemonadeChange(input2) else "fail")


if __name__ == "__main__":
    main()