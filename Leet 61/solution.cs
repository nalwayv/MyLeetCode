public class ListNode(int val = 0, ListNode next = null)
{
    public int val = val;
    public ListNode next = next;
}

public class Solution
{
    private static void ReverseList(List<int> nums, int left, int right)
    {
        if (nums.Count <= 1)
        {
            return;
        }

        while (left < right)
        {
            (nums[right], nums[left]) = (nums[left], nums[right]);
            left++;
            right--;
        }
    }

    private static void RotateList(List<int> nums, int k)
    {
        k %= nums.Count;
        var n = nums.Count;
        var m = n - k;

        ReverseList(nums, 0, m - 1);
        ReverseList(nums, m, n - 1);
        ReverseList(nums, 0, n - 1);
    }

    public ListNode RotateRight(ListNode head, int k)
    {
        if (head == null || k <= 0)
        {
            return head;
        }

        List<int> values = [];

        var current = head;
        while (current != null)
        {
            values.Add(current.val);
            current = current.next;
        }

        RotateList(values, k);

        current = head;
        int i = 0;
        while (current != null && i < values.Count)
        {
            current.val = values[i++];
            current = current.next;
        }
        return head;
    }
}

class Program
{
    private static void PrintListNode(ListNode head)
    {
        if (head == null)
        {
            return;
        }

        var current = head;
        Console.Write("[");
        while (current != null)
        {
            Console.Write($" {current.val} ");
            current = current.next;
        }
        Console.WriteLine("]");
    }

    private static void Main()
    {
        Solution solution = new();
        var head = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5)))));
        PrintListNode(head);
        PrintListNode(solution.RotateRight(head, 2));

    }
}