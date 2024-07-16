public class MyStack
{
    private readonly Queue<int> _stk;

    public MyStack()
    {
        _stk = [];
    }

    public void Push(int x)
    {
        _stk.Enqueue(x);

        // rotate n-1 to simulate a stack
        // will make push 0(n)
        if (_stk.Count > 1)
        {
            for (int i = 0; i < _stk.Count - 1; i++)
            {
                _stk.Enqueue(_stk.Dequeue());
            }
        }
    }

    public int Pop()
    {
        return _stk.Dequeue();
    }

    public int Top()
    {
        return _stk.Peek();
    }

    public bool Empty()
    {
        return _stk.Count == 0;
    }

    public void print()
    {
        Console.Write("[");
        foreach (int i in _stk)
        {
            Console.Write($" {i} ");
        }
        Console.WriteLine("]");
    }
}

internal class Program
{
    private static void Main()
    {
        Console.WriteLine("Que stack!");

        MyStack stk = new();
        for (int i = 1; i <= 5; i++)
        {
            stk.Push(i);
        }

        stk.print();

        while (!stk.Empty())
        {
            // 5 4 3 2 1
            Console.WriteLine($"Pop: {stk.Pop()}");
        }
        Console.WriteLine($"IsEmpty: {stk.Empty()}");
    }
}