/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest obj = new KthLargest(k, nums);
 * int param_1 = obj.Add(val);
 */

namespace Leet_703;

public class KthLargestException : Exception
{
    public KthLargestException(string message) : base(message)
    {
    }
}

public class KthLargest
{
    private readonly List<int> _nums;
    private readonly int _k;

    public KthLargest(int k, int[] nums)
    {
        if (nums.Length < k)
        {
            throw new KthLargestException("k size is too small and needs to be equal to or more then nums.Count");
        }

        _nums = [];
        _k = k;

        foreach (int n in nums)
        {
            if (_nums.Count == 0)
            {
                _nums.Add(n);
            }
            else
            {
                _nums.Insert(BisectLeft(n), n);
            }
        }
    }

    public int Add(int val)
    {
        _nums.Insert(BisectLeft(val), val);
        return _nums[^_k];
    }

    private int BisectLeft(int target)
    {
        int lo = 0;
        int hi = _nums.Count;

        while (lo < hi)
        {
            int mid = lo + (hi - lo) / 2;
            if (_nums[mid] < target)
            {
                lo = mid + 1;
            }
            else
            {
                hi = mid;
            }
        }
        return lo;
    }
}

internal class Program
{
    private static void Main()
    {
        Console.WriteLine("703. Kth Largest Element in a Stream");

        int[] nums = [4, 5, 8, 2];
        int k = 3;
        KthLargest kth = new(k, nums);

        int[] add = [3, 5, 10, 9, 4];
        foreach (int ad in add)
        {
            Console.WriteLine(kth.Add(ad));
        }
    }
}