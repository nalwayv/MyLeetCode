def maximumElementAfterDecrementingAndRearranging(arr: list[int]) -> int:
    # RULES:
    # The value of the first element in arr must be 1.
    # The absolute difference between any 2 adjacent elements must be less than or equal to 1
    
    arr_copy: list[int] = sorted(arr)
    
    # first value has to be 1
    arr_copy[0] = 1

    max_value: int = 1
    for i in range(1, len(arr_copy)):
        # if out of range set to previous + 1
        if abs(arr_copy[i] - arr_copy[i-1]) > 1:
            arr_copy[i] = arr_copy[i-1] + 1
            
        max_value = max(max_value, arr_copy[i])
    
    return max_value
    

def main() -> None:
    print("1846. Maximum Element After Decreasing and Rearranging")
    
    nums: list[int] = [2,2,1,2,1]
    result: int = maximumElementAfterDecrementingAndRearranging(nums)
    print(f"Result: {result}")


if __name__ == "__main__":
    main()