// Loop through the whole integer and count all the
// 1's
public class Solution {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
        int count = 0;
        for (int i = 0; i < 32; i++) {
            // use n & 1 as a mask to extract the
            // last bit
            if ((n & 1) == 1) {
                count++;
            }
            n = n >>> 1;
        }
        return count;
    }
}

// Faster bit maniputation solution, key trick is that
// n & (n - 1) flips the least significant 1 bit to 0,
// repeat until n becomes 0
public class Solution {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
        int count = 0;
        while (n != 0) {
            count++;
            n = n & (n - 1);
        }
        return count;
    }
}