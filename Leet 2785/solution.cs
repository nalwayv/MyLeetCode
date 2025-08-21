public class Solution
{
    public string SortVowels(string s)
    {
        List<char> chars = [];
        List<int> index = [];

        const string vowels = "aeiouAEIOU";
        for (int i = 0; i < s.Length; i++)
        {
            if (vowels.Contains(s[i]))
            {
                chars.Add(s[i]);
                index.Add(i);
            }
        }

        chars.Sort();

        StringBuilder sb = new(s);
        for (int i = 0; i < chars.Count; i++)
        {
            sb[index[i]] = chars[i];
        }
        return sb.ToString();
    }
}