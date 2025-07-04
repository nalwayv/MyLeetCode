# running sum
# example:
#   data = [1, 2, 3, 4]
#   pass1: 1
#   pass2: 1 + 2 
#   pass3: 1 + 2 + 3
#   pass4: 1 + 2 + 3 + 4

def running_sum_a(nums: list[int]) -> list[int]:
    """
    """
    end: int = len(nums)
    result: list[int] = []

    i: int = end - 1
    while i >= 0:
        sum: int = 0

        j: int = 0
        while j < end - i:
            sum += nums[j]
            j += 1

        result.append(sum)

        i -= 1

    return result


def running_sum_b(nums: list[int]) -> list[int]:
    """leet code version
    """
    result: list[int] = [0] * len(nums)
    result[0] = nums[0]
    end: int = len(nums)

    for i in range(1, end):
        result[i] = nums[i] + result[i - 1]

    return result


def running_sum_c(nums: list[int]) -> list[int]:
    result: list[int] = []
    
    end: int = len(nums)
    for i in range(end):
        p1: int = (end - i) - 1

        s: int = 0
        for j in range(end - p1):
            s += nums[j]

        result.append(s)

    return result


def test_list(a: list[int], b: list[int]) -> bool:
    if len(a) != len(b):
        return False
    
    for i in range(max(len(a), len(b))):
        if a[i] != b[i]:
            return False

    return True


def main():
    case1: list[int] = [1, 2, 3, 4, 5]
    case2: list[int] = [1,1,1,1,1]
    case3: list[int] = [3, 1, 2, 10, 1]

    result1: list[int] = [1,3,6,10,15]
    result2: list[int] = [1,2,3,4,5]
    result3: list[int] = [3,4,6,16,17]
    
    print("A")

    print("CASE1: ", test_list(running_sum_a(case1), result1))
    print("CASE2: ", test_list(running_sum_a(case2), result2))
    print("CASE3: ", test_list(running_sum_a(case3), result3))

    print("B")

    print("CASE1: ", test_list(running_sum_b(case1), result1))
    print("CASE2: ", test_list(running_sum_b(case2), result2))
    print("CASE3: ", test_list(running_sum_b(case3), result3))

    print("C")

    print("CASE1: ", test_list(running_sum_c(case1), result1))
    print("CASE2: ", test_list(running_sum_c(case2), result2))
    print("CASE3: ", test_list(running_sum_c(case3), result3))

if __name__ == "__main__":
    main()