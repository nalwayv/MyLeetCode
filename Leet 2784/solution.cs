public class Solution 
{
    public bool IsGood(int[] nums) 
    {
        // An aray is good if
        // starting from 1 to max twice 
        // [1,2,3,3] is good
        // [1,2,2,3,3] is not good
        if(nums.Length == 0)
        {
            return false;
        }

        Dictionary<int, int> frequency = [];
        int maxNumber = -1;
        foreach(int num in nums)
        {
            maxNumber = int.Max(maxNumber, num);
            if(frequency.TryGetValue(num, out int value))
                frequency[num] = value + 1;
            else
                frequency[num] = 1;
        }

        for(int i = 1; i < maxNumber; i++)
        {
            if( !frequency.ContainsKey(i) || frequency[i] > 1)
            {
                return false;
            }
        }

        return frequency[maxNumber] == 2;
    }
}
class Program
{
    private static void Main()
    {
        Console.WriteLine("2784. Check if Array is Good");

        Solution solution = new();
        int[] nums = [3,4,4,1,2,1];
        string passed = solution.IsGood(nums) == false ? "Pass" : "Fail";
        Console.WriteLine($"[3,4,4,1,2,1] should not be a good array? {passed}");
    }
}

