// basically get the last bit of n and add it to res, 
// then shift n to the right to get next bit. Repeat
// 32 times to build up the whole reversed pattern

public class Solution {
    // you need treat n as an unsigned value
    public int reverseBits(int n) {
        int res = 0;
        for (int i = 0; i < 32; i++) {
            res = (res << 1) + (n & 1);
            n = n >>> 1;
        }
        return res;
    }
}