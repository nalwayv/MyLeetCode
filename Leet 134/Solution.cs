namespace Leet_134;

public static class Solution
{
    public static int CanCompleteCircuit(IList<int> gas, IList<int> cost)
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