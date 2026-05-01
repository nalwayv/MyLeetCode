Console.WriteLine("2452. Words Within Two Edits of Dictionary");

Leet.Solution solution = new();

string[] queries1 = ["word","note","ants","wood"];
string[] dictionary1 = ["wood","joke","moat"];
IList<string> result1 = solution.TwoEditWords(queries1, dictionary1);
Console.WriteLine($"[{string.Join(", ", result1)}]");

string[] queries2 = ["yes"];
string[] dictionary2 = ["not"];
IList<string> result2 = solution.TwoEditWords(queries2, dictionary2);
Console.WriteLine($"[{string.Join(", ", result2)}]");


namespace Leet
{
    public class Solution 
    {
        public IList<string> TwoEditWords(string[] queries, string[] dictionary) 
        {
            List<string> result = [];
            foreach(var q in queries)
            {
                foreach(var d in dictionary)
                {
                    var diff = 0;
                    for(int i = 0; i < q.Length; i++)
                    {
                        if (diff > 2) 
                            break;
                        
                        if (q[i] != d[i])
                            diff++;
                    }

                    if(diff <= 2)
                    {
                        result.Add(q);
                        break;
                    }
                }
            }

            return result;
        }
    }
}