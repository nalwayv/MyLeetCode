namespace Leet1352;

class ProductOfNumbers
{
    private readonly List<int> _nums = [];

    public void Add(int num)
    {
        if (num == 0)
        {
            _nums.Clear();
            return;
        }

        if (_nums.Count > 0)
        {
            _nums.Add(num * _nums.Last());
        }
        else
        {
            _nums.Add(num);
        }
    }

    public int GetProduct(int k)
    {
        if (k > _nums.Count)
        {
            return 0;
        }

        int lastIndex = _nums.Count - 1;

        if (k == _nums.Count)
        {
            return _nums[lastIndex];
        }

        return _nums[lastIndex] / _nums[lastIndex - k];
    }
}

class Program
{
    private static void Main()
    {
        Console.WriteLine("1352. Product of the Last K Numbers");

        var productOfNumbers = new ProductOfNumbers();
        productOfNumbers.Add(3);
        productOfNumbers.Add(0);
        productOfNumbers.Add(2);
        productOfNumbers.Add(5);
        productOfNumbers.Add(4);
        Console.WriteLine($"GetProduct(2) = 20 ? {productOfNumbers.GetProduct(2)}");
        Console.WriteLine($"GetProduct(3) = 40 ? {productOfNumbers.GetProduct(3)}");
        Console.WriteLine($"GetProduct(4) =  0 ? {productOfNumbers.GetProduct(4)}");
        productOfNumbers.Add(8);
        Console.WriteLine($"GetProduct(2) = 32 ? {productOfNumbers.GetProduct(2)}");
    }
}