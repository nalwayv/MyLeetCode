class Solution 
{
public:
    int maxCoins(std::vector<int>& piles) 
    {
        std::sort(piles.begin(), piles.end());
        int p1 = 0;
        int p2 = piles.size() - 2;
        int result = 0;

        while (p1 < p2)
        {
            result += piles[p2];
            p1 += 1;
            p2 -= 2;
        }
        
        return result;
    }
};