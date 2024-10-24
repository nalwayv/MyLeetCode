class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        Simplify a unix string path for use

        Example:
        >>> simplifyPath("/.../a/../b/c/../d/./")
        /.../b/d
        """

        stk: list[str] = ["/"]
        for p in path.split("/"):
            if p != "":

                # . ignore home path
                if p == ".":
                    continue

                # .. go back a directory
                if p == "..":
                    # dont remove first / from path
                    if len(stk) == 1 and stk[-1] == "/":
                        continue

                    # remove any / before last directory name
                    while len(stk) > 0 and stk[-1] == "/":
                        stk.pop()
                    
                    if len(stk) > 0:
                        stk.pop()
                else:
                    # add path seperator if needed
                    if len(stk) > 0 and stk[-1] != "/":
                        stk.append("/")

                    stk.append(p)
            else:
                if len(stk) > 0 and stk[-1] != "/":
                    stk.append("/")

        # remove end /
        if len(stk) > 0 and stk[-1] == "/":
            stk.pop()
            
        # default
        if len(stk) == 0:
            return "/"
        
        # str builder
        return "".join(stk)


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