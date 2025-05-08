namespace Leet341;

public interface INestedInteger 
{
    // @return true if this NestedInteger holds a single integer, rather than a nested list.
    bool IsInteger();
    // @return the single integer that this NestedInteger holds, if it holds a single integer
    // Return null if this NestedInteger holds a nested list
    int GetInteger();
    // @return the nested list that this NestedInteger holds, if it holds a nested list
    // Return null if this NestedInteger holds a single integer
    IList<INestedInteger> GetList();
}

public class NestedIterator
{
    private readonly Queue<int> _queue;

    private void Flatten(IList<INestedInteger> nestedList)
    {
        foreach (var nestedInteger in nestedList)
        {
            if (nestedInteger.IsInteger())
            {
                _queue.Enqueue(nestedInteger.GetInteger());
            }
            else
            {
                Flatten(nestedInteger.GetList());
            }
        }
    }
    
    public NestedIterator(IList<INestedInteger> nestedList) 
    {
        _queue = new Queue<int>();
        Flatten(nestedList);
    }

    public bool HasNext() 
    {
        return _queue.Count > 0;
    }

    public int Next() 
    {
        return _queue.Dequeue();
    }
}

static class Program
{
    static void Main()
    {
        Console.WriteLine("341. Flatten Nested List Iterator");
    }
}