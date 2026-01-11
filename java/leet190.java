// File: leet190.java
public class leet190 {

    // Main method for testing
    public static void main(String[] args) {
        Solution solution = new Solution();

        int n = 43261596;
        int reversed = solution.reverseBits(n);
        System.out.println("Input: " + n);
        System.out.println("Reversed: " + reversed);
    }
}
// solution class
class Solution {
    public int reverseBits(int n) {
        int result = 0;
        for (int i = 0; i < 32; i++) {
            result <<= 1;
            result |= (n & 1);
            n >>>= 1;
        }
        return result;
    }
}
