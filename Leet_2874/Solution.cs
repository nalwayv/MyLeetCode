using System;


namespace Leet 
{
    public class Solution 
    {
        public long MaximumTripletValue(int[] nums) 
        {
            long a = 0;
            long b = 0;
            long c = 0;
            long[] values = new long[3];
            
            foreach(var num in nums)
            {
                c = long.Max(c, b * num);
                b = long.Max(a - num, b);
                a = long.Max(a, num);
            }
            
            return c;
        }
    }
}


public class Program
{
	public static void Main()
	{
		Console.WriteLine("2874. Maximum Value of an Ordered Triplet II");
		
		Leet.Solution sol = new();
		
		long testA = sol.MaximumTripletValue([12,6,1,2,7]);
		Console.WriteLine($"{testA} = 77");
		
		long testB = sol.MaximumTripletValue([1, 10, 3, 4, 19]);
		Console.WriteLine($"{testB} = 133");
		
		long testC = sol.MaximumTripletValue([1, 2, 3]);
		Console.WriteLine($"{testC} = 0");	
	}
}