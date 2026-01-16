namespace Leet
{
    public class Solution
    {
        public bool ArrayStringsAreEqual(string[] word1, string[] word2)
        {
            return string.Concat(word1) == string.Concat(word2);
        }
    }

    class Program
    {
        static void Main()
        {
            Console.WriteLine("1662. Check If Two String Arrays are Equivalent");

            Solution solution = new();

            string[] word1 = ["ab", "c"];
            string[] word2 = ["a", "bc"];

            var result = solution.ArrayStringsAreEqual(word1, word2) ? "pass" : "fail";
            Console.WriteLine($"case1 ([ab, c], [a bc]) should equal true: {result}");
        }
    }
}