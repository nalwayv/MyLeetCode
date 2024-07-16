class Solution:
    """
    Given an array arr, replace every element in that array with the greatest element among the elements to its right, 
    
    and replace the last element with -1.

    After doing so, return the array.
    

    Input: arr = [17,18,5,4,6,1]

    Output: [18,6,6,6,1,-1]

    Explanation: 
    - index 0 --> the greatest element to the right of index 0 is index 1 (18).
    - index 1 --> the greatest element to the right of index 1 is index 4 (6).
    - index 2 --> the greatest element to the right of index 2 is index 4 (6).
    - index 3 --> the greatest element to the right of index 3 is index 4 (6).
    - index 4 --> the greatest element to the right of index 4 is index 5 (1).
    - index 5 --> there are no elements to the right of index 5, so we put -1

    """
    def replace_elements(self, arr: list[int]) -> list[int]:
        n: int = len(arr)
        if n <= 1:
            arr[0] = -1
            return arr
        
        for i in range(0, n - 1):

            max_value: int = -1
            for j in range(i + 1, n):
                max_value = max(max_value, arr[j])

            arr[i] = max_value

        arr[n - 1] = -1

        return arr


    def leet_code_version(self, arr: list[int]) -> list[int]:
        """
        leet code

        
         0  1  2 3 4 5
        [17,18,5,4,6,1] -> [1,6,4,5,18,17]
        

        p = -1
        c = max[-1, 1] -> 1
        [0] = -1
        p = c

        p = 1
        c = max[1, 6] -> 6
        [1] = 1
        p = c

        ...
        """
        n: int = len(arr);
        if n <= 1:
            arr[0] = -1
            return arr

        previous_max: int = -1
        for i in reversed(range(n)):
            current_max: int = max(previous_max, arr[i])
            arr[i] = previous_max
            previous_max = current_max

        return arr
    
def main() -> None:
    solution = Solution()
    arr: list[int] = [17,18,5,4,6,1]
    solution.replace_elements(arr)
    print(f"Output: {arr}")


if __name__ == "__main__":
    main()