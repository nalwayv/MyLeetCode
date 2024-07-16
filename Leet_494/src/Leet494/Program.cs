namespace Leet494;
public class Solution
{
    // private struct Node
    // {
    //     public int index;
    //     public int target;
    // }

    public static int Count(int[] nums, int target, int current, int depth)
    {   
        if (depth == nums.Length)
        {
            if (current == target)
            {
                return 1;
            }
        }
        else
        {
            int add = Count(nums, target, current + nums[depth], depth + 1);
            int sub = Count(nums, target, current - nums[depth], depth + 1);
            return add + sub;
        }

        return 0;
    }

    public static int FindTargetSumWays(int[] nums, int target)
    {
        return Count(nums, target, 0, 0);

        // Stack<Node> stack = new();
        // Node root = new() { index = 0, target = 0 };
        // stack.Push(root);
        // int count = 0;
        // while (stack.Count != 0)
        // {
        //     Node current = stack.Pop();

        //     if (current.index == nums.Length)
        //     {
        //         if (current.target == target)
        //         {
        //             count += 1;
        //         }
        //     }
        //     else
        //     {
        //         stack.Push(new Node
        //         {
        //             index = current.index + 1,
        //             target = current.target + nums[current.index]
        //         });

        //         stack.Push(new Node
        //         {
        //             index = current.index + 1,
        //             target = current.target - nums[current.index]
        //         });
        //     }
        // }
        // return count;
    }
}

internal class Program
{
    private static void Input1()
    {
        int[] nums = [1, 1, 1, 1, 1];
        int target = 3;
        int result = Solution.FindTargetSumWays(nums, target);
        Console.WriteLine($"Input [1,1,1,1,1], Target: 3, Expect: 5, Ouput: {result}");
    }

    private static void Input2()
    {
        int[] nums = [1];
        int target = 1;
        int result = Solution.FindTargetSumWays(nums, target);
        Console.WriteLine($"Input [1], Target: 1, Expect: 1, Ouput: {result}");
    }

    private static void Input3()
    {
        int[] nums = [1];
        int target = 2;
        int result = Solution.FindTargetSumWays(nums, target);
        Console.WriteLine($"Input [1], Target: 2, Expect: 0, Ouput: {result}");
    }

    private static void Input4()
    {
        int[] nums = [1000];
        int target = -1000;
        int result = Solution.FindTargetSumWays(nums, target);
        Console.WriteLine($"Input [1000], Target: 1, Expect: 1, Ouput: {result}");
    }

    private static void Main()
    {
        Console.WriteLine("Hello, World!");
        Input1();
        Input2();
        Input3();
        Input4();
    }
}