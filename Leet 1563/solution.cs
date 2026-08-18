public class Solution 
{
    private static int RangeSum(int[] pre, int i, int j) 
    {
        return pre[j + 1] - pre[i];
    }
    
    public int StoneGameV(int[] stoneValue) 
    {
        int[] pre = new int[stoneValue.Length + 1];
        for(int i = 0; i < stoneValue.Length; i++) 
        {
            pre[i + 1] = pre[i] + stoneValue[i];
        }

        int[,] dp = new int[stoneValue.Length,stoneValue.Length];

        for(int l = 2; l <= stoneValue.Length; l++) 
        {
            for(int i = 0; i <= stoneValue.Length - l; i++) 
            {
                int j = i + l - 1;
                int result = 0;

                for(int k = i; k < j; k++) 
                {
                    int left = RangeSum(pre, i, k);
                    int right = RangeSum(pre, k + 1, j);
                
                    if (left < right) 
                    {
                        result = Math.Max(result, left + dp[i, k]);
                    } 
                    else if (left > right) 
                    {
                        result = Math.Max(result, right + dp[k + 1, j]);
                    } 
                    else 
                    {
                        result = Math.Max(
                            result, 
                            Math.Max(left + dp[i, k], right + dp[k + 1, j])
                        );
                    }
                }

                dp[i, j] = result;
            }
        }

        return dp[0, stoneValue.Length - 1];
    }
}


class Program
{
    private static void Main()
    {
        Console.WriteLine("1563. Stone Game V");

        Solution solution = new();
        int[] stoneValue = [6,2,3,4,5,5];
        int result = solution.StoneGameV(stoneValue);
        Console.WriteLine(result);
    }
}