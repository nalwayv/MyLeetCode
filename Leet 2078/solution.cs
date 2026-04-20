public class Solution 
{
    public int MaxDistance(int[] colors) 
    {
        var end = colors.Length - 1;
        var start = 0;

        while (start < end)
        {
            if (colors[0] != colors[end] || colors[start] != colors[end])
            {
                break;
            }

            start += 1;
            end -= 1;
        }

        return end;
    }
}

class Program
{
    static void Main()
    {
        Console.WriteLine("2078. Two Furthest Houses With Different Colors");
        Solution solution = new();

        Console.WriteLine(solution.MaxDistance([1,1,1,6,1,1,1]));   // 3
        Console.WriteLine(solution.MaxDistance([1,8,3,8,3]));       // 4
        Console.WriteLine(solution.MaxDistance([0,1]));             // 1
        Console.WriteLine(solution.MaxDistance([1,6,1,1,1,1,1]));   // 5
        Console.WriteLine(solution.MaxDistance([1,1,1,1,1,6,1]));   // 5
        Console.WriteLine(solution.MaxDistance([0,1,1,0]));         // 2
    }
}