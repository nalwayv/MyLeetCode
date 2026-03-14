class Solution {
    public String getHappyString(int n, int k) {
        var stk = new Stack<String>();
        stk.push("");
        int count = 0;
        var abc = new char[] {'c', 'b', 'a'};

        while(!stk.empty())
        {
            var current = stk.pop();
            if(current.length() == n)
            {
                count++;
                if(count == k)
                {
                    return current;
                }
                continue;
            }

            for(var val : abc)
            {
                if (current.isEmpty() || current.charAt(current.length() - 1) != val)
                {
                    stk.push(current + val);
                }
            }
        }

        return "";
    }
}