Console.WriteLine("2833. Furthest Point From Origin");

Leet.Solution solution = new();
var distance = solution.FurthestDistanceFromOrigin("L_RL__R");

Console.WriteLine($"Furthest distance: {distance}");


namespace Leet
{
    public class Solution 
    {
        public int FurthestDistanceFromOrigin(string moves) {
            int left = 0;
            int right = 0;
            int blank = 0;
            
            foreach(var move in moves)
            {
                if (move == 'L')
                    left++;

                if (move == 'R')
                    right++;

                if (move == '_')
                    blank++;
            }
            
            if (left > right)
                return left + blank - right;
            
            return right + blank - left;
        }
    }
}