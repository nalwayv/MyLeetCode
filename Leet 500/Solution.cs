bool ContainsWord(string word, HashSet<char> letters)
{
    foreach(char c in word)
    {
        if (!letters.Contains(c))
        {
            return false;
        }
    }
    return true;
}


string[] FindWords(string[] words)
{
    HashSet<char> row1 = new HashSet<char>("qwertyuiop");
    HashSet<char> row2 = new HashSet<char>("asdfghjkl");
    HashSet<char> row3 = new HashSet<char>("zxcvbnm");

    List<string> result = new List<string>();
    foreach (string word in words)
    {
        if (ContainsWord(word.ToLower(), row1) || ContainsWord(word.ToLower(), row2) || ContainsWord(word.ToLower(), row3))
        {
            result.Add(word);
        }
    }
    return result.ToArray();
}


Console.WriteLine("500. Keyboard Row");
Console.Write("[ ");
foreach (var word in FindWords(["Hello", "Alaska", "Dad", "Peace"]))
{
    Console.Write($" {word} ");
}
Console.WriteLine("]");