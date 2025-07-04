namespace Leet895;

public class FreqStack
{
    private readonly Dictionary<int, int> _frequency = [];
    private readonly Dictionary<int, Stack<int>> _stack = [];
    private int _top = -1;

    public FreqStack()
    { }

    public void Push(int val)
    {
        _frequency.TryAdd(val, 0);
        _frequency[val]++;
        _top = int.Max(_top, _frequency[val]);

        if (!_stack.ContainsKey(_frequency[val]))
        {
            _stack[_frequency[val]] = [];
        }
        _stack[_frequency[val]].Push(val);
    }

    public int Pop()
    {
        if (!_stack.TryGetValue(_top, out var stack) || stack.Count == 0)
        {
            return -1;
        }

        var value = stack.Pop();
        _frequency[value]--;
        if (stack.Count == 0)
        {
            _top--;
        }
        return value;
    }
}

class Program
{
    private static void Main()
    {
        Console.WriteLine("895. Maximum Frequency Stack");

        FreqStack obj = new();
        obj.Push(5);
        obj.Push(7);
        obj.Push(5);
        obj.Push(7);
        obj.Push(4);
        obj.Push(5);

        Console.WriteLine($"Pop = 5 ? {obj.Pop()}");
        Console.WriteLine($"Pop = 7 ? {obj.Pop()}");
        Console.WriteLine($"Pop = 5 ? {obj.Pop()}");
    }
}