Console.WriteLine("2472. Maximum Number of Non-overlapping Palindrome Substrings");

TestCase("abaccdbbd", 3, 2);
TestCase("adbcda", 2, 0);
TestCase("abab", 2, 1);


static void TestCase(string s, int k, int expected)
{
    var result = Solution.MaxPalindromes(s, k) == expected ? "pass" : "fail";
    Console.WriteLine($"test case for MaxPalindromes({s}) should equal {expected}? {result}");
}


static class Solution
{
    private static bool InRange(string s, int start, int end)
    {
        if (start < 0 || start >= s.Length) return false;
        if (end < 0 || end >= s.Length) return false;
        if (start > end) return false;
        return true;
    }

    private static bool IsPalindrome(string s, int start, int end)
    {
        while (start < end)
        {
            if (s[start] != s[end])
            {
                return false;
            }

            start++;
            end--;
        }

        return true;
    }

    public static int MaxPalindromes(string s, int k)
    {
        int count = 0;
        int i = 0;

        while (i + k <= s.Length)
        {
            // check k else k + 1
            if (IsPalindrome(s, i, i + k - 1) || (InRange(s, i, i + k) && IsPalindrome(s, i, i + k)))
            {
                count++;
                i += k;
            }
            else
            {
                i++;
            }
        }

        return count;
    }
}