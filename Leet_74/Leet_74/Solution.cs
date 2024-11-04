namespace Leet_74;

public class Solution
{
    /// <summary>
    /// A Binary search
    /// </summary>
    /// <returns><c>True</c> if nums contains target</returns>
    private bool Contains(int[] nums, int target)
    {
        int lo = 0;
        int hi = nums.Length - 1;

        while (lo <= hi)
        {
            int mid = lo + (hi - lo) / 2;

            if (nums[mid] == target)
            {
                return true;
            }

            if (nums[mid] > target)
            {
                hi = mid - 1;
            }
            else
            {
                lo = mid + 1;
            }
        }

        return false;
    }

    /// <summary>
    /// Search matrix for target value
    /// </summary>
    /// <returns><c>True</c> if matrix contains target</returns>
    private bool Search(int[][] matrix, int target)
    {
        foreach (var row in matrix)
        {
            // each level is sorted so if last value is less than target goto next
            if (row[^1] < target)
            {
                continue;
            }

            // search for target on current level
            if (Contains(row, target))
            {
                return true;
            }
        }

        return false;
    }

    public bool SearchMatrix(int[][] matrix, int target)
    {
        return Search(matrix, target);
    }
}