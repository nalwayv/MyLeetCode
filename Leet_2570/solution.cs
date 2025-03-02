namespace Solution
{
    public class Solution
    {
        /*
         NOTE:
         You are given two 2D integer arrays nums1 and nums2.
                
         nums1[i] = [idi, vali] indicate that the number with the id idi has a value equal to vali.
         nums2[i] = [idi, vali] indicate that the number with the id idi has a value equal to vali.
         Each array contains unique ids and is sorted in ascending order by id.
                
         Merge the two arrays into one array that is sorted in ascending order by id, respecting the following conditions:
                
         Only ids that appear in at least one of the two arrays should be included in the resulting array.
         Each id should be included only once and its value should be the sum of the values of this id in the two arrays. If the id does not exist in one of the two arrays, then assume its value in that array to be 0.
         Return the resulting array. The returned array must be sorted in ascending order by id.
        */
        public int[][] MergeArrays(int[][] nums1, int[][] nums2)
        {
            // Build table
            Dictionary<int, int> table = [];
            int maxId = int.MinValue;
            int count = 0;
            foreach (var pair in nums1)
            {
                if (pair.Length != 2)
                {
                    break;
                }
                
                if (table.ContainsKey(pair[0]))
                {
                    table[pair[0]] += pair[1];
                }
                else
                {
                    table[pair[0]] = pair[1];
                    count++;
                    maxId = int.Max(maxId, pair[0]);
                }
            }

            foreach (var pair in nums2)
            {
                if (pair.Length != 2)
                {
                    break;
                }
                
                if (table.ContainsKey(pair[0]))
                {
                    table[pair[0]] += pair[1];
                }
                else
                {
                    table[pair[0]] = pair[1];
                    count++;
                    maxId = int.Max(maxId, pair[0]);
                }
            }
            
            // Build result
            int[][] result = new int[count][];
            int j = 0;
            for (int i = 0; i <= maxId; i++)
            {
                if (j >= count)
                {
                    break;
                }
                
                if (table.TryGetValue(i, out int value))
                {
                    result[j] = [i, value];
                    j++;
                }
            }
            return result;
        }
    }
}


// ---------------------------------------------------------------------------------------------------------------------
// Main


public class Program
{
    private static void TestCase1(Solution.Solution solution)
    {
        Console.WriteLine("Test Case 1");
        int[][] nums1 = [[1, 2], [2, 3], [4, 5]];
        int[][] nums2 = [[1, 4], [3, 2], [4, 1]];
        
        int[][] result = solution.MergeArrays(nums1, nums2);
        for (int i = 0; i < result.Length; i++) 
        {
            Console.Write($"At {i}: ");
            foreach(int num in result[i])
            {
                Console.Write($" {num} ");
            }
            Console.WriteLine("");
        }
    }
    
    private static void TestCase2(Solution.Solution solution)
    {
        Console.WriteLine("Test Case 2");

        int[][] nums1 = [[2, 4],[3, 6],[5, 5]];
        int[][] nums2 = [[1, 3], [4, 3]];
        
        int[][] result = solution.MergeArrays(nums1, nums2);
        for (int i = 0; i < result.Length; i++) 
        {
            Console.Write($"At {i}: ");
            foreach(int num in result[i])
            {
                Console.Write($" {num} ");
            }
            Console.WriteLine("");
        }
    }
    
    public static void Main()
    {
        Console.WriteLine("2570. Merge Two 2D Arrays by Summing Values");

        Solution.Solution solution = new();
        TestCase1(solution);
        TestCase2(solution);
    }
}
