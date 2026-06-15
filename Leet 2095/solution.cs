namespace Leet
{
    public class ListNode(int val = 0, ListNode? next = null)
    {
        public int val = val;
        public ListNode? next = next;
    }

    public class Solution
    {
        public ListNode? DeleteMiddle(ListNode? head)
        {
            if (head == null || head.next == null)
            {
                return null;
            }

            var middle = head;
            var prev = head;
            int length = 1;

            for (var current = head; current.next != null; current = current.next)
            {
                // update middle
                if (++length % 2 == 0)
                {
                    prev = middle;
                    middle = middle?.next;
                }
            }

            // remove middle
            prev?.next = middle?.next;

            return head;
        }
    }
}

class Program
{
    private static Leet.ListNode CreateList(int[] nums)
    {
        if (nums.Length == 0)
        {
            return null;
        }

        Leet.ListNode head = new(nums[0]);
        Leet.ListNode tail = head;
        for (int i = 1; i < nums.Length; i++)
        {
            tail.next = new(nums[i]);
            tail = tail.next;
        }
        return head;
    }

    private static void PrintList(Leet.ListNode head)
    {
        Console.Write("[");
        for (var current = head; current != null; current = current.next)
        {
            Console.Write($" {current.val} ");
        }
        Console.WriteLine("]");
    }

    private static void Main()
    {
        Console.WriteLine("2095. Delete the Middle Node of a Linked List");

        int[] nums = [1, 3, 4, 7, 1, 2, 6];
        Leet.Solution solution = new();
        var head = CreateList(nums);

        Console.WriteLine("Before:");
        PrintList(head);
        head = solution.DeleteMiddle(head);
        Console.WriteLine("After:");
        PrintList(head);
    }
}