public class ListNode 
{
    int val;
    ListNode next;
    
    ListNode(int val) 
    { 
        this.val = val; 
    }
}

public class Solution 
{
    private ListNode fromArrayList(ArrayList<Integer> values) 
    {
        ListNode head = null;
        ListNode tail = null;

        for (var value : values) 
        {
            if (head == null) 
            {
                head = new ListNode(value);
                tail = head;
            } 
            else 
            {
                tail.next = new ListNode(value);
                tail = tail.next;
            }
        }
        return head;
    }

    public ListNode reverseKGroup(ListNode head, int k) 
    {
        if (head == null) 
        {
            return null;
        }

        var values = new ArrayList<Integer>();
        var current = head;
        while (current != null) 
        {
            values.add(current.val);
            current = current.next;
        }

        for(int i = 0; i < values.size(); i += k)
        {
            if (i + k <= values.size())
            {
                var sub = values.subList(i, i + k);
                Collections.reverse(sub);

                for(int j = 0; j < sub.size(); j++)
                {
                    values.set(i + j, sub.get(j));
                }
            }
        }

        return fromArrayList(values);
    }
}