public class MyQueue
{
    private readonly Stack<int> _enque;
    private readonly Stack<int> _deque;

    public MyQueue()
    {
        _enque = [];
        _deque = [];
    }

    public void Push(int x)
    {
        _enque.Push(x);
    }

    public int Pop()
    {
        if (_deque.Count == 0)
        {
            while (_enque.Count != 0)
            {
                _deque.Push(_enque.Pop());
            }
        }
        return _deque.Pop();
    }

    public int Peek()
    {
        if (_deque.Count == 0)
        {
            while (_enque.Count != 0)
            {
                _deque.Push(_enque.Pop());
            }
        }
        return _deque.Peek();
    }

    public bool Empty()
    {
        return _deque.Count == 0 && _enque.Count == 0;
    }
}

public class MyQueueOneStack
{
    private readonly Stack<int> _que;

    public MyQueueOneStack()
    {
        _que = [];
    }

    public void Push(int x)
    {
        if (Empty()) {
            _que.Push(x);
        } 
        else {
            // rotate 
            Stack<int> tmp = [];
            while (_que.Count != 0)
            {
                tmp.Push(_que.Pop());
            }

            _que.Push(x);

            while (tmp.Count != 0)
            {
                _que.Push(tmp.Pop());
            }
        }
    }

    public int Pop()
    {
        return _que.Pop();
    }

    public int Peek()
    {
        return _que.Peek();
    }

    public bool Empty()
    {
        return _que.Count == 0;
    }
}

internal class Program
{
    private static void Main()
    {
        Console.WriteLine("Que using a stack!");

        MyQueue que = new();

        Console.WriteLine($"Push");
        Console.WriteLine($"Push");
        que.Push(1);
        que.Push(2);

        Console.WriteLine($"Pop: {que.Pop()}"); // 1
        Console.WriteLine($"Peek: {que.Peek()}"); // 2
        Console.WriteLine($"Is Empty: {que.Empty()}"); // false
        Console.WriteLine($"Pop: {que.Pop()}"); // 2
        Console.WriteLine($"Is Empty: {que.Empty()}"); // true

        Console.WriteLine($"Push");
        Console.WriteLine($"Push");
        que.Push(1);
        que.Push(2);
        Console.WriteLine($"Is Empty: {que.Empty()}"); // false
        Console.WriteLine($"Peek: {que.Peek()}"); // 1
        Console.WriteLine($"Pop: {que.Pop()}"); // 1
        Console.WriteLine($"Is Empty: {que.Empty()}"); // false
    }
}