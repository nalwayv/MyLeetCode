class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        Simplifies a given Unix-style file path.
        Args:
            path (str): The input file path as a string.
        Returns:
            str: The simplified path.
        """
        stk: list[str] = []
        for value in path.split("/"):
            if value == "..":
                if stk:
                    stk.pop()
            else:
                if value in [".", ""]:
                    continue
                stk.append(value)

        return "/" + "/".join(stk)


def case1(sol : Solution) -> None:
    path: str = "/home/"
    result: str = sol.simplifyPath(path)
    print(f"case 1: {result}")


def case2(sol : Solution) -> None:
    path: str = "/home//foo/"
    result: str = sol.simplifyPath(path)
    print(f"case 2: {result}")


def case3(sol : Solution) -> None:
    path: str = "/home/user/Documents/../Pictures"
    result: str = sol.simplifyPath(path)
    print(f"case 3: {result}")


def case4(sol : Solution) -> None:
    path: str = "/../"
    result: str = sol.simplifyPath(path)
    print(f"case 4: {result}")


def case5(sol : Solution) -> None:
    path: str = "/.../a/../b/c/../d/./"
    result: str = sol.simplifyPath(path)
    print(f"case 5: {result}")


def case6(sol : Solution) -> None:
    path: str = "/a/../../b/../c//.//"
    result: str = sol.simplifyPath(path)
    print(f"case 6: {result}")


def main() -> None:
    print("71. Simplify Path")

    sol = Solution()

    case1(sol)
    case2(sol)
    case3(sol)
    case4(sol)
    case5(sol)
    case6(sol)
    

if __name__ == "__main__":
    main()