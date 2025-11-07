class Leet1578
{
    public int MinCost(string colors, int[] neededTime)
    {
        int total = 0;
        int currentMax = 0;
        int currentSum = 0;
        int i = 0;
        for (int j = 0; j < colors.Length; j++)
        {
            if (colors[j] != colors[i])
            {
                total += currentSum - currentMax;
                i = j;
                currentMax = 0;
                currentSum = 0;
            }
            
            currentSum += neededTime[j];
            currentMax = int.Max(currentMax, neededTime[j]);
        }

        // any remaining colors
        currentSum = 0;
        for (int j = i; j < colors.Length; j++)
        {
            currentSum += neededTime[j];
            currentMax = int.Max(currentMax, neededTime[j]);
        }
        total += currentSum - currentMax;
        
        return total;
    }
}

class Program
{
    static void Main()
    {
        Console.WriteLine("1578. Minimum Time to Make Rope Colorful");

        var leet1578 = new Leet1578();
        var case1 = leet1578.MinCost("abaac", [1, 2, 3, 4, 5]);
        Console.WriteLine(case1);
    }
}