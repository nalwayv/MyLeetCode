public class Solution {
    public bool HasAllCodes(string s, int k) {
        int maxSize = 1 << k;
        HashSet<string> seen = [];
        
        for(int i = 0; i <= s.Length - k; i++)
        {
			seen.Add(s.Substring(i, k));

			if (seen.Count == maxSize)
            {
                return true;
            }
        }

		return false;
    }
}