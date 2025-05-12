namespace Lee677;

public class MapSum 
{
    private readonly Dictionary<string, int> _map;
    
    public MapSum() 
    {
        _map = new Dictionary<string, int>();
    }
    
    public void Insert(string key, int val)
    {
        _map[key] = val;
    }
    
    public int Sum(string prefix) 
    {
        int result = 0;
        foreach (var value in _map)
        {
            if (value.Key.StartsWith(prefix))
            {
                result += value.Value;
            }
        }
        return result;
    }
}

static class Program
{
    static void Main()
    {
        Console.WriteLine("677. Map Sum Pairs");
        
        MapSum mapSum = new MapSum();
        
        mapSum.Insert("apple", 3);
        mapSum.Insert("apple", 2);
        Console.WriteLine(mapSum.Sum("ap"));
        
        mapSum.Insert("app", 2);
        Console.WriteLine(mapSum.Sum("ap"));
    }
}