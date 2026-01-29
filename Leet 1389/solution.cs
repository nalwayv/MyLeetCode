namespace Leet
{
    public class Solution {
        public int[] CreateTargetArray(int[] nums, int[] index) 
        {
            List<int> result = [];
            foreach(var (num, idx) in nums.Zip(index, (x, y) => (x, y)))
            {
                if(idx > result.Count)
                {
                    result.Add(num);
                }
                else
                {
                    result.Insert(idx, num);
                }
            }
            return result.ToArray();
        }
    }

    class Program
    {
        static void PrintArray(int[] nums)
        {
            Console.Write("[");
            foreach(int n in nums)
            {
                Console.Write($" {n} ");
            }
            Console.WriteLine("]");
        }

        static void Main()
        {
            Console.WriteLine("1389. Create Target Array in the Given Order");
            Solution solution = new();

            var case1 = solution.CreateTargetArray([0,1,2,3,4], [0,1,2,2,1]);
            PrintArray(case1);
        }
    }
}