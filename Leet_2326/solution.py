class ListNode:
    def __init__(self, val: int =0):
        self.val = val
        self.next: ListNode|None = None


class Solution:
    def _create_matrix(self, m: int, n:int) -> list[list[int]]:
        mat: list[list[int]] = []
        for _ in range(m):
            mat.append([-1 for _ in range(n)])
        return mat
    
    def _in_range(self, x:int, y:int, row:int, col:int) -> bool:
        return (x >= 0 and x < row) and (y >= 0 and y < col)

    def spiralMatrix(self, m: int, n: int, head: ListNode|None) -> list[list[int]]:
        """
        """
        matrix: list[list[int]] = self._create_matrix(m, n)

        if not head:
            return matrix

        left: int = 0
        right: int = 1
        up: int = 2
        down: int = 3

        x: int = 0
        y: int = 0

        empty: int = -1
        direction: int = right

        length: int = pow(m * n, 2)
        matrix[x][y] = head.val
        current: ListNode|None = head.next

        while current and length > 0:
            if direction == right:
                if self._in_range(x, y+1, m, n) and matrix[x][y+1] == empty:
                    y += 1
                    matrix[x][y] = current.val

                    current = current.next
                else:
                    direction = down

            elif direction == down:
                if self._in_range(x+1, y, m, n) and matrix[x+1][y] == empty:
                    x += 1
                    matrix[x][y] = current.val

                    current = current.next
                else:
                    direction = left

            elif direction == left:
                if self._in_range(x, y-1, m, n) and matrix[x][y-1] == empty:
                    y -= 1
                    matrix[x][y] = current.val

                    current = current.next
                else:
                    direction = up

            elif direction == up:
                if self._in_range(x-1, y, m, n) and matrix[x-1][y] == empty:
                    x -= 1
                    matrix[x][y] = current.val

                    current = current.next
                else:
                    direction = right

            length -= 1

        return matrix


def print_matrix(matrix: list[list[int]], m: int, n: int) -> None:
     for i in range(m):
        print("[",end="")
        for j in range(n):
            print(f" {matrix[i][j]:>02d} ",end="")
        print("]")   


def create_linked_list(values: list[int]) -> ListNode|None:
    head: ListNode|None = None
    tail: ListNode|None = None

    for val in values:
        if not head:
            head = ListNode(val)
            tail = head
        elif tail:
            tail.next = ListNode(val)
            tail = tail.next
    return head


def print_linked_list(head: ListNode|None) -> None:
    print("[",end="")
    current: ListNode|None = head
    while current:
        print(f" {current.val} ",end="")
        current = current.next
    print("]")


def case_1(sol: Solution) -> None:
    print("case 1")
    
    values: list[int] = [3,0,2,6,8,1,7,9,4,2,5,5,0]
    head: ListNode|None = create_linked_list(values)
    print_linked_list(head)

    m: int = 3
    n: int = 5
    matrix: list[list[int]] = sol.spiralMatrix(m, n, head)
    print_matrix(matrix, m, n)  


def main() -> None:
    print("2326. Spiral Matrix IV")

    sol = Solution()
    case_1(sol)
        

if __name__ == "__main__":
    main()