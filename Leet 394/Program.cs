
public class Solution
{
    // Given an encoded string, return its decoded string.
    // The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. 
    // Note that k is guaranteed to be a positive integer.
    // You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. 
    // Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, 
    // k. For example, there will not be input like 3a or 2[4].
    // The test cases are generated so that the length of the output will never exceed 105.
    
    public string DecodeString(string s)
    {
        Stack<char> stkIn = [];
        Stack<char> stkOut = [];

        foreach (char current in s)
        {
            if (current == ']')
            {
                while (stkIn.Count > 0 && stkIn.Peek() != '[')
                {
                    stkOut.Push(stkIn.Pop());
                }

                // pop should by '[' just get rid of it
                // as pattern shows a number should then follow popped '['
                // if not there is a problem with the input string so just exit
                char _ = stkIn.Pop();
                if (!char.IsNumber(stkIn.Peek()))
                {
                    return "";
                }

                // add number to out by keep track
                // then pop off and accumulat into single int
                int count = 0;
                int num = 0;
                while (stkIn.Count > 0 && char.IsNumber(stkIn.Peek()))
                {
                    stkOut.Push(stkIn.Pop());
                    count += 1;
                }

                for (int i = 0; i < count; i++)
                {
                    num *= 10;
                    num += stkOut.Pop() - '0';
                }

                // add pattern to result
                for (int i = 0; i < num; i++)
                {
                    foreach (char rune in stkOut)
                    {
                        stkIn.Push(rune);
                    }
                }

                stkOut.Clear();
            }
            else
            {
                stkIn.Push(current);
            }
        }

        // create string result
        char[] text = new char[stkIn.Count];
        for (int i = 0; i < text.Length; i++)
        {
            text[text.Length - i - 1] = stkIn.Pop();
        }
        return new string(text);
    }
}

internal class Program
{
    private static void Main()
    {
        Console.WriteLine("Leet 394");

        Solution solution = new();
        string case1 = solution.DecodeString("3[a]2[bc]");
        string outputCase1 = "aaabcbc";
        Console.WriteLine($"Input: 3[a]2[bc], Expect {outputCase1}, Output: {case1}, Equal? {case1.Equals(outputCase1)}");

        string case2 = solution.DecodeString("3[a2[c]]");
        string outputCase2 = "accaccacc";
        Console.WriteLine($"Input: 3[a2[c]], Expect: {outputCase2}, Output: {case2}, Equal? {case2.Equals(outputCase2)}");

        string case3 = solution.DecodeString("2[abc]3[cd]ef");
        string outputCase3 = "abcabccdcdcdef";
        Console.WriteLine($"Input: 2[abc]3[cd]ef, Expect: {outputCase3}, Output: {case3}, Equal? {case3.Equals(outputCase3)}");

        string case4 = solution.DecodeString("10[leetcode]");
        string outputCase4 = "leetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcode";
        Console.WriteLine($"Input: 100[leetcode], Expect: {outputCase4}, Output: {case4}, Equal? {case4.Equals(outputCase4)}");

        string case5 = solution.DecodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef");
        string outputCase5 = "zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef";
        Console.WriteLine($"Input: 3[z]2[2[y]pq4[2[jk]e1[f]]]ef, Expect: {outputCase5} , Output: {case5}, Equal? {case5.Equals(outputCase5)}");
    }
}