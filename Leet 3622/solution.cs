public class Solution
{
    public bool CheckDivisibility(int n)
    {
        int number = n;
        int sum = 0;
        int product = 1;

        while (n > 0)
        {
            int digit = n % 10;

            sum += digit;
            product *= digit;

            n /= 10;
        }

        return number % (sum + product) == 0;
    }
}
