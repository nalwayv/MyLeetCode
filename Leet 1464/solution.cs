public class Solution {
    public int MaxProduct(int[] nums) {
        int num1 = -1;
        int num2 = -1;
        foreach(int num in nums) {
            if (num > num1) {
                num2 = num1;
                num1 = num;
            } else if(num > num2) {
                num2 = num;
            }
        }
        return (num1 - 1) * (num2 - 1);
    }
}
