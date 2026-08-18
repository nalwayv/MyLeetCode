public class Solution {
    public bool StoneGameIX(int[] stones) {
        int[] remainders = [0,0,0];
        foreach(var s in stones) {
            remainders[s % 3]++;
        }

        if (remainders[0] % 2 == 0) {
            return remainders[1] > 0 && 0 < remainders[2];
        }

        return Math.Abs(remainders[1] - remainders[2]) > 2;
    }
}
