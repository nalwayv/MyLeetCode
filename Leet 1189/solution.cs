public class Solution
{
    public int MaxNumberOfBalloons(string text)
    {
        int[] balloon = [0, 0, 0, 0, 0];
        foreach (char ch in text)
        {
            if (ch == 'b') balloon[0]++;
            if (ch == 'a') balloon[1]++;
            if (ch == 'l') balloon[2]++;
            if (ch == 'o') balloon[3]++;
            if (ch == 'n') balloon[4]++;
        }

        balloon[2] /= 2;
        balloon[3] /= 2;

        int result = balloon[0];
        for (int i = 1; i < balloon.Length; i++)
        {
            result = int.Min(result, balloon[i]);
        }
        return result;
    }
}

class Program
{
    private static void Main()
    {
        Console.WriteLine("1189. Maximum Number of Balloons");
        Solution solution = new();

        int case1 = solution.MaxNumberOfBalloons("nlaebolko");
        Console.WriteLine($"Max number of balloon's: {case1}");

        int case2 = solution.MaxNumberOfBalloons("loonbalxballpoon");
        Console.WriteLine($"Max number of balloon's: {case2}");
    }
}