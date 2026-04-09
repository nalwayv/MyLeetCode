class Solution
{
    public int XorAfterQueries(int[] nums, int[][] queries)
    {
        if(nums.Length == 0)
        {
            return 0;
        }

        long m = 1000000007;
        long[] lnums = nums.Select(i => (long)i).ToArray();

        foreach (var query in queries)
        {
            if (query.Length != 4)
            {
                return 0;
            }

            int l = query[0];
            int r = query[1];
            int k = query[2];
            int v = query[3];

            if(r > lnums.Length)
            {
                continue;
            }

            int idx = l;
            while (idx <= r)
            {
                lnums[idx] = lnums[idx] * v % m;
                idx += k;
            }
        }

        long result = lnums[0];
        for(int i = 1; i < lnums.Length; i++)
        {
            result ^= lnums[i];
        }
        return (int)result;
    }
}

class Program
{
    private static void Main()
    {
        Console.WriteLine("3653. XOR After Range Multiplication Queries I");

        var solution = new Solution();


        int[] numsA = [1,1,1];
        int[][] queriesA = [[0,2,1,4]];
        int result = solution.XorAfterQueries(numsA, queriesA);
        Console.WriteLine(result);

        int[] numsB = [2,3,1,5,4];
        int[][] queriesB = [[1,4,2,3],[0,2,1,2]];
        result = solution.XorAfterQueries(numsB, queriesB);
        Console.WriteLine(result);


    }
}