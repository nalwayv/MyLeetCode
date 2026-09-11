Console.WriteLine("3483. Unique 3-Digit Even Numbers");

TestCase([1,2,3,4], 12);
TestCase([0,2,2], 2);

static void TestCase(int[] digits, int expected)
{
    string result = Solution.TotalNumbers(digits) == expected ? "pass" : "fail";
    Console.WriteLine($"Test case should equal expected {expected} ? {result}");
}

class Solution
{
    private static int ToNumber(int[] digits, int k)
    {
        int result = 0;
        for(int i = 0; i < k; i++)
        {
            result = result * 10 + digits[i];
        }
        return result;
    }

    private static void PopulateSeen(HashSet<int> seen, int[] digits, int k = 0)
    {
        if (k == 3 && digits[0] != 0)
        {
            var number = ToNumber(digits, 3);
            var isEven = number % 2 == 0;
            var seenHasNumber = seen.Contains(number);
            
            if (isEven && !seenHasNumber)
            {
                seen.Add(number);
            }
        }
        else
        {
            for(int i = k; i < digits.Length; i++)
            {
                // swap
                (digits[k], digits[i]) = (digits[i], digits[k]);

                PopulateSeen(seen, digits, k + 1);
                
                // swap back
                (digits[k], digits[i]) = (digits[i], digits[k]);
            }
        }
    }

    public static int TotalNumbers(int[] digits)
    {
        var seen = new HashSet<int>();
        PopulateSeen(seen, digits);
        return seen.Count;
    }
}