public class Solution {
    public bool CanReach(int[] arr, int start) {
        Stack<int> stack = new();
        HashSet<int> seen = new();

        stack.Push(start);

        while (stack.Count > 0)
        {
            var current = stack.Pop();

            if (seen.Contains(current)) 
                continue;

            seen.Add(current);

            if (0 <= current && current < arr.Length)
            {
                if (arr[current] == 0) 
                    return true;

                var add = current + arr[current];
                var sub = current - arr[current];

                stack.Push(add);
                stack.Push(sub);
            }
        }

        return false;
    }
}

class Program
{
    private static void Main()
    {
        Console.WriteLine("1306. Jump Game III");
        Solution solution = new();
        int[] arr = [4,2,3,0,3,1,2];
        int start = 5;
        Console.WriteLine(solution.CanReach(arr, start));
    }
}