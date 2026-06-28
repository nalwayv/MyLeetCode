public class Solution
{
    public int CanCompleteCircuit(IList<int> gas, IList<int> cost)
    {
        if (gas.Count != cost.Count)
        {
            return -1;
        }
        
        int startIndex = 0;
        int currentGas = 0;

        int n = gas.Count;
        
        // double length for circuit
        for (int i = 0; i < n * 2; i++)
        {
            // has completed a circuit
            if (i == startIndex + n)
            {
                return i % n;
            }

            int at = i % n;
            currentGas = currentGas + gas[at] - cost[at];
            
            // reset if out of gas and start from new position
            if (currentGas < 0)
            {
                currentGas = 0;
                startIndex = i + 1;
            }
        }

        return -1;
    }
}


internal abstract class Program
{
    private static void Case1(Solution solution)
    {
        List<int> gas = [1, 2, 3, 4, 5];
        List<int> cost = [3, 4, 5, 1, 2];

        string result = solution.CanCompleteCircuit(gas, cost) == 3 ? "passed" : "failed";
        Console.WriteLine($"case 1: {result}");
    }
    
    private static void Case2(Solution solution)
    {
        List<int> gas = [2,3,4];
        List<int> cost = [3,4,3];

        string result = solution.CanCompleteCircuit(gas, cost) == -1 ? "passed" : "failed";
        Console.WriteLine($"case 2: {result}");
    }
    
    private static void Case3(Solution solution)
    {
        List<int> gas = [5,1,2,3,4];
        List<int> cost = [4,4,1,5,1];

        string result = solution.CanCompleteCircuit(gas, cost) == 4 ? "passed" : "failed";
        Console.WriteLine($"case 3: {result}");
    }

    private  static void Main()
    {
        Console.WriteLine("134. Gas Station");
        Solution solution = new();
        Case1(solution);
        Case2(solution);
        Case3(solution);
    }
}