// Key observation here is that since the string only
// has a's and b's, there will be at most 2 removals given
// that s is not a palindrome. If s is a palindrome, there
// will only be 1 removal. The special case is empty string
// in which case there will be 0 removals.
class Solution {
    public int removePalindromeSub(String s) {
        if (s.length() == 0) {
            return 0;
        }
        int i = 0;
        int j = s.length() - 1;
        int count = 0;
        while (i < j && s.charAt(i) == s.charAt(j)) {
            i++;
            j--;
        }
        if (s.charAt(i) != s.charAt(j)) {
            return 2;
        }
        return 1;
    }
}

// Test cases:
// ""
// "abba"
// "ababa"
// "a bbb"
// "a bbabb ba"