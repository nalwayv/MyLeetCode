Console.WriteLine("836. Rectangle Overlap");

var case1 = Solution.IsRectangleOverlap([0,0,2,2], [1,1,3,3])? "Overlep" : "Dont Overlap";
Console.WriteLine($"[0,0,2,2] and [1,1,3,3] {case1}");

var case2 = Solution.IsRectangleOverlap([0,0,1,1], [1,0,2,1])? "Overlep" : "Dont Overlap";
Console.WriteLine($"[0,0,1,1] and [1,0,2,1] {case2}");

var case3 = Solution.IsRectangleOverlap([0,0,1,1], [2,2,3,3])? "Overlep" : "Dont Overlap";
Console.WriteLine($"[0,0,1,1] and [2,2,3,3] {case3}");


class Solution
{
    public static bool IsRectangleOverlap(int[] rec1, int[] rec2)
    {
        if(rec1.Length != 4 || rec2.Length != 4)
        {
            return false;
        }

        // aMaxX <= bMinX or aMinX >= bMaxX
        if (rec1[2] <= rec2[0] || rec1[0] >= rec2[2])
        {
            return false;
        }

        // aMaxY <= bMinY or aMinY >= bMaxY
        if (rec1[3] <= rec2[1] || rec1[1] >= rec2[3])
        {
            return false;
        }

        return true;
    }
}