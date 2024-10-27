namespace Leet_134;

internal abstract class Program
{
    private static void Case1()
    {
        List<int> gas = [1, 2, 3, 4, 5];
        List<int> cost = [3, 4, 5, 1, 2];

        string result = Solution.CanCompleteCircuit(gas, cost) == 3 ? "passed" : "failed";
        Console.WriteLine($"case 1: {result}");
    }
    
    private static void Case2()
    {
        List<int> gas = [2,3,4];
        List<int> cost = [3,4,3];

        string result = Solution.CanCompleteCircuit(gas, cost) == -1 ? "passed" : "failed";
        Console.WriteLine($"case 2: {result}");
    }
    
    private static void Case3()
    {
        List<int> gas = [5,1,2,3,4];
        List<int> cost = [4,4,1,5,1];

        string result = Solution.CanCompleteCircuit(gas, cost) == 4 ? "passed" : "failed";
        Console.WriteLine($"case 3: {result}");
    }

    public static void Main(string[] args)
    {
        Console.WriteLine("134. Gas Station");

        Case1();
        Case2();
        Case3();
    }
}