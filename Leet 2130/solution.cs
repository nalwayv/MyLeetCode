namespace Leet 
{
    public class ListNode(int val = 0, ListNode? next = null)
    {
        public int val = val;
        public ListNode? next = next;
    }

    public class Solution
    {
        private static List<ListNode> ToList(ListNode head)
        {
            List<ListNode> result = [];
            for (var current = head; current != null; current = current.next)
            {
                result.Add(current);
            }
            return result;
        }
        
        /// <summary>
        /// Return the max pair sum from listNode
        /// </summary>
        public int PairSum(ListNode head)
        {
            List<ListNode> nodes = ToList(head);

            int maxPair = -1;
            int p1 = 0;
            int p2 = nodes.Count - 1;

            while (p1 < p2)
            {
                var p1Value = nodes[p1++].val;
                var p2Value = nodes[p2--].val;

                maxPair = int.Max(maxPair, p1Value + p2Value);
            }

            return maxPair;
        }
    }
}

class Program
{
    /// <summary>
    /// Create a list from an array of ints
    /// </summary>
    private static Leet.ListNode CreateList(int[] nums)
    {
        Leet.ListNode head = new(nums[0]);
        Leet.ListNode tail = head;

        for (int i = 1; i < nums.Length; i++)
        {
            tail.next = new(nums[i]);
            tail = tail.next;
        }

        return head;
    }

    private static void Main()
    {
        Console.WriteLine("2130. Maximum Twin Sum of a Linked List");

        int[] nums = [4, 2, 2, 3];
        var head = CreateList(nums);

        Leet.Solution solution = new();
        Console.WriteLine($"MaxPair: {solution.PairSum(head)}");
    }
}