public class ListNode
{
    public int val;
    public ListNode? next;
    public ListNode(int val = 0, ListNode? next = null)
    {
        this.val = val;
        this.next = next;
    }
}

public class Solution {
    public ListNode? DeleteDuplicate(ListNode? head) {
        if (head == null)
        {
            return head;
        }

        // current list 
        ListNode? prev = head;
        ListNode? curr = head.next;

        // build new list
        ListNode? result = new(head.val);
        ListNode? next = result;

        while (curr != null)
        {
            if (curr.val != prev.val)
            {
                next.next = new(curr.val);
                next = next.next;
            }

            prev = curr;
            curr = curr.next;
        }
        
        return result;
    }
}

internal class Program
{
    private static ListNode? FromArray(int[] numbers)
    {
        ListNode? root = null;
        ListNode? next = null;

        foreach(int num in numbers)
        {
            if(root == null)
            {
                root = new(num);
                next = root;
            }
            else
            {
                if(next != null)
                {
                    next.next = new(num);
                    next = next.next;
                }
            }
        }

        return root;
    }

    private static void PrintList(ListNode? root)
    {
        if(root == null)
        {
            return;
        }
        Console.Write("[");
        ListNode? current = root;
        while(current != null)
        {
            Console.Write($" {current.val} ");
            current = current.next;
        }
        Console.WriteLine("]");
    }

    private static void Main(string[] args)
    {
        Console.WriteLine("Leet 83. Remove Duplicates from Sorted List");

        int[] numbers = [1,1,2,3,3];
        ListNode? root = FromArray(numbers);

        Solution solution = new();
        ListNode? result = solution.DeleteDuplicate(root);
        PrintList(result);
    }
}