public class Solution {
    public int MaxProduct(int n) {
        var mx1 = int.MinValue;
        var mx2 = int.MinValue;

        while (n > 0) {
            var current = n % 10;

            if (current > mx1) {
                mx2 = mx1;
                mx1 = current;
            } else if (current > mx2) {
                mx2 = current;
            }

            n /= 10;
        }

        return mx1 * mx2;
    }
}
