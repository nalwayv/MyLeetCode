namespace Leet2336;

public class SmallestInfiniteSet
{
    private int _smallest = 1;
    private readonly PriorityQueue<int, int> _pq = new();
    private readonly HashSet<int> _seen = [];
    
    public SmallestInfiniteSet() 
    {
    }
    
    public int PopSmallest() 
    {
        if (_pq.Count > 0 && _pq.Peek() < _smallest)
        {
            int value = _pq.Dequeue();
            _seen.Remove(value);
            return value;
        }

        int result = _smallest;
        _smallest++;
        return result;   
    }
    
    public void AddBack(int num)
    {
        if (num >= _smallest || _seen.Contains(num))
        {
            return;
        }

        _pq.Enqueue(num, num);
        _seen.Add(num);
    }
}

static class Program
{
    private static void Main()
    {
        Console.WriteLine("2336. Smallest Number in Infinite Set");
        Console.WriteLine("_____ Case 1 _____");
        var s = new SmallestInfiniteSet();
        s.AddBack(2);
        Console.WriteLine($"{s.PopSmallest()} == 1");
        Console.WriteLine($"{s.PopSmallest()} == 2");
        Console.WriteLine($"{s.PopSmallest()} == 3");
        s.AddBack(1);
        Console.WriteLine($"{s.PopSmallest()} == 1");
        Console.WriteLine($"{s.PopSmallest()} == 4");
        Console.WriteLine($"{s.PopSmallest()} == 5");
    }
}