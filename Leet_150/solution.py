class Solution:
    def is_int(self, val: str) -> bool:
        """ simple trick to get ints that are also negative
        """
        try:
            int(val)
            return True
        except ValueError:
            return False
        
    def evalRPN(self, tokens: list[str]) -> int:
        stk: list[int] = []
        nums: list[int] = [0, 0]

        for t in tokens:
            if self.is_int(t):
                stk.append(int(t))
            else:
                for i in range(2):
                    nums[i] = stk.pop()
                    
                result: int = 0
                match t:
                    case "+": result = nums[1] + nums[0]
                    case "-": result = nums[1] - nums[0]
                    case "*": result = nums[1] * nums[0]
                    case "/": result = int(nums[1] / nums[0])
                    case _: result = 0
                stk.append(result)

        return stk[-1]


def test1(solution: Solution) -> None:
    tokens = ["2","1","+","3","*"]
    # ((2 + 1) * 3) = 9
    result: int = solution.evalRPN(tokens)
    print(f"Output: {result}, Expected 9")


def test2(solution: Solution) -> None:
    tokens = ["4","13","5","/","+"]
    # (4 + (13 / 5)) = 6
    result: int = solution.evalRPN(tokens)
    print(f"Output: {result}, Expected 6")


def test3(solution: Solution) -> None:
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    # = 22
    result: int = solution.evalRPN(tokens)
    print(f"Output: {result}, Expected 22")


def main() -> None:
    solution = Solution()
    test1(solution)
    test2(solution)
    test3(solution)


if __name__ == "__main__":
    main()