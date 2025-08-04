namespace Leet1791;

using System;
using System.Collections.Generic;
using System.Linq;

class Solution
{
    public int FindCenter(int[][] edges) 
    {
        if (edges.Length < 2)
        {
            return -1;
        }
        
        HashSet<int> edgeFirst = new(edges[0]);
        edgeFirst.IntersectWith(edges[1]);
        
        if (edgeFirst.Any())
        {
            return edgeFirst.First();
        }
        
        return -1;
    }
}


class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("1791. Find Center of Star Graph");
        Solution solution = new();
        int[][] edges = new int[][]
        {
            [1, 2],
            [2, 3],
            [4, 2]
        };
        int center = solution.FindCenter(edges);
        Console.WriteLine($"Center of the star graph should equal 2? {center}");
    }
}