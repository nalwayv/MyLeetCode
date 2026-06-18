class RideSharingSystem
{
    private readonly Queue<int> _drivers = new();
    private readonly Queue<int> _riders = new();
    private readonly HashSet<int> _cancelled = [];
    private readonly HashSet<int> _booked = [];

    public void AddRider(int riderId)
    {
        _riders.Enqueue(riderId);
        _booked.Add(riderId);
    }

    public void AddDriver(int driverId)
    {
        _drivers.Enqueue(driverId);
    }

    public int[] MatchDriverWithRider()
    {
        if (_drivers.Count == 0)
        {
            return [-1, -1];
        }

        // if rider has cancelled then move on to next
        while (_riders.Count > 0 && _cancelled.Contains(_riders.Peek()))
        {
            _cancelled.Remove(_riders.Dequeue());            
        }

        // there might be no riders after removing cancelled
        if (_riders.Count == 0)
        {
            return [-1, -1];
        }

        // dispatch
        int driver = _drivers.Dequeue();
        int rider = _riders.Dequeue();
        _booked.Remove(rider);

        return [driver, rider];
    }

    public void CancelRider(int riderId)
    {
        if (!_booked.Contains(riderId))
        {
            return;
        }

        _booked.Remove(riderId);
        _cancelled.Add(riderId);
    }
}

class Program
{
    private static void PrintResult(int[] values)
    {
        Console.Write("[");
        foreach(int v in values)
        {
            Console.Write($" {v} ");
        }
        Console.WriteLine("]");
    }
    private static void Main()
    {
        Console.WriteLine("3829. Design Ride Sharing System");

        var rs = new RideSharingSystem();
        
        rs.AddRider(3);
        rs.AddDriver(2);
        rs.AddRider(1);

        PrintResult(rs.MatchDriverWithRider());

        rs.CancelRider(3);
        rs.AddDriver(5);

        PrintResult(rs.MatchDriverWithRider());
        PrintResult(rs.MatchDriverWithRider());
    }
}