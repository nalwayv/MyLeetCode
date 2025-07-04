namespace Leet2349;
public class NumberContainers
{
    private const int NotFoundValue = -1;
    private readonly Dictionary<int, int> _indexToNumberMap;
    private readonly Dictionary<int, PriorityQueue<int, int>> _numberToIndexesMap;

    public NumberContainers()
    {
        _indexToNumberMap = new Dictionary<int, int>();
        _numberToIndexesMap = new Dictionary<int, PriorityQueue<int, int>>();
    }

    public void Change(int index, int number)
    {
        _indexToNumberMap[index] = number;
        if (!_numberToIndexesMap.TryGetValue(number, out var indexQueue))
        {
            indexQueue = new PriorityQueue<int, int>();
            _numberToIndexesMap[number] = indexQueue;
        }

        indexQueue.Enqueue(index, index);
    }

    public int Find(int number)
    {
        if (!_numberToIndexesMap.TryGetValue(number, out var value))
        {
            return NotFoundValue;
        }

        while (value.Count > 0)
        {
            int currentIndex = value.Peek();
            if (_indexToNumberMap[currentIndex] == number)
            {
                return currentIndex;
            }

            value.Dequeue();
        }

        return NotFoundValue;
    }
}

static class Program
{
    static void Main()
    {
        Console.WriteLine("2349. Design a Number Container System");

        var numberContainers = new NumberContainers();

        numberContainers.Change(3, 10);
        numberContainers.Change(2, 10);
        numberContainers.Change(4, 10);
        numberContainers.Change(1, 10);

        numberContainers.Change(1, 20);
        numberContainers.Change(2, 20);

        numberContainers.Change(1, 30);

        int find10 = numberContainers.Find(10);
        Console.WriteLine($"Find(10) result: {find10}");

        int find20 = numberContainers.Find(20);
        Console.WriteLine($"Find(20) result: {find20}");
    }
}