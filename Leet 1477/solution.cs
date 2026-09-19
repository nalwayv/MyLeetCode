Console.WriteLine("1477. Find Two Non-overlapping Sub-arrays Each With Target Sum");
Console.WriteLine();

int result = Solution.MinSumOfLengths([3,2,2,4,3], 3);
Console.WriteLine($"MinSumOfLengths([3,2,2,4,3], 3) should equal 2 ? {result}");

class Solution 
{
    public static int MinSumOfLengths(int[] arr, int target) 
    {
        int[] dp = new int[arr.Length + 1];
        for(int i = 0; i <= arr.Length; i++)
        {
            dp[i] = arr.Length + 1;
        }

        int result = arr.Length + 1;
        int total = 0;

        int left = 0;
        for(int right = 0; right < arr.Length; right++)
        {
            total += arr[right];
            while(total > target)
            {
                total -= arr[left++];
            }

            dp[right + 1] = dp[right];

            if (total == target)
            {
                int currentWindow = right - left + 1;

                dp[right + 1] = Math.Min(dp[right + 1], currentWindow);
                result = Math.Min(result, dp[left] + currentWindow);
            }
        }

        return result == arr.Length + 1 ? -1 : result;
    }
}