namespace Leet_74;

public class Solution
{
    /// <summary>
    /// A Binary search
    /// </summary>
    /// <param name="nums">1d matrix</param>
    /// <param name="target">target to find</param>
    /// <returns>True if contains target</returns>
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
    /// Search each level of the matrix for target
    /// </summary>
    /// <param name="matrix">2D int matrix</param>
    /// <param name="target">value to look for</param>
    /// <param name="level">current layer of matrix to search</param>
    /// <returns>true if 2d matrix contains target</returns>
    private bool Search(int[][] matrix, int target, int level = 0)
    {
        if (level >= matrix.Length)
        {
            return false;
        }

        // each level is sorted so if last value is less than target goto next
        if (matrix[level][^1] < target)
        {
            return Search(matrix, target, level + 1);
        }

        // search for target on current level
        if (Contains(matrix[level], target))
        {
            return true;
        }

        return Search(matrix, target, level + 1);
    }

    public bool SearchMatrix(int[][] matrix, int target)
    {
        return Search(matrix, target);
    }
}