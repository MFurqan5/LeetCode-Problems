public class Solution {
    public int FurthestDistanceFromOrigin(string moves) {
        int left = 0, right = 0, blank = 0;
        
        foreach (char c in moves) {
            if (c == 'L') left++;
            else if (c == 'R') right++;
            else blank++;
        }
        
        return Math.Abs(left - right) + blank;
    }
}