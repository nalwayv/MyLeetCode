public class ListNode 
{
    public int val;
    public ListNode? next;
    public ListNode(int val=0, ListNode? next=null) 
    {
        this.val = val;
        this.next = next;
    }
}

public class Solution 
{
    public ListNode? MergeKLists(ListNode?[] lists) 
    {
        List<int> values = [];
        foreach(var list in lists)
        {
            var current = list;
            while(current != null)
            {
                values.Add(current.val);
                current = current.next;
            }
        }
        values.Sort();

        ListNode? head = null;
        ListNode? tail = null;
        foreach(var value in values)
        {
            if(head == null)
            {
                head = new ListNode(value);
                tail = head;
            }
            else if(tail != null)
            {
                tail.next = new ListNode(value);
                tail = tail.next;
            }
        }
        return head;
    }
}

static class Program
{
    private static ListNode? ArrayToListNode(int[] values)
    {
        ListNode? head = null;
        ListNode? tail = null;
        foreach(var value in values)
        {
            if(head == null)
            {
                head = new ListNode(value);
                tail = head;
            }
            else if(tail != null)
            {
                tail.next = new ListNode(value);
                tail = tail.next;
            }
        }
        return head;
    }

    private static void Main()
    {
        Solution solution = new();
        ListNode?[] lists = [
            ArrayToListNode([1,4,5]),
            ArrayToListNode([1,3,4]),
            ArrayToListNode([2,6]),
        ];
        var head = solution.MergeKLists(lists);
        Console.Write("[ ");
        while(head != null)
        {
            Console.Write($" {head.val} ");
            head = head.next;
        }
        Console.WriteLine(" ]");
    }
}