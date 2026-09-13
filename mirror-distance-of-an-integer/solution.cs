public class Solution {
    public int MirrorDistance(int n) {
        int original = n;
        int reversed = 0;
        while (n > 0) {
            reversed = reversed * 10 + n % 10;
            n /= 10;
        }
        return Math.Abs(original - reversed);
    }
}