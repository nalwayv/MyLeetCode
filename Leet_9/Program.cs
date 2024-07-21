public class Solution {
    public bool IsPalindrome(int x) {
        // check if number is negative
        if (x < 0)
        {
            return false;
        }

        // check if numbers is a single digit
        if (x / 10 == 0)
        {
            return true;
        }

        // check is number is a palindrom by breaking it down
        List<int> numbers = [];
        while (x > 0)
        {
            numbers.Add(x % 10);
            x /= 10;
        }

        int p1 = 0;
        int p2 = numbers.Count - 1;
        while (p1 < p2)
        {
            if (numbers[p1] != numbers[p2])
            {
                return false;
            }

            p1 += 1;
            p2 -= 1;
        }

        return true;        
    }
}


internal class Program
{
    private static void Main(string[] args)
    {
        Console.WriteLine("Leet 9. Palindrome Number");
        Solution solution = new();

        Console.WriteLine($"is 121 a palindrome ? {solution.IsPalindrome(121)}");
        Console.WriteLine($"is -121 a palindrome ? {solution.IsPalindrome(-121)}");
        Console.WriteLine($"is 10 a palindrome ? {solution.IsPalindrome(10)}");
        Console.WriteLine($"is 0 a palindrome ? {solution.IsPalindrome(0)}");
    }
}