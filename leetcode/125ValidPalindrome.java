// Use two pointers, one from beginning of string and the other
// from end of string. O(n) solution
class Solution {
    public boolean isPalindrome(String s) {
        int i = 0;           // i start from beginning of string
        int j = s.length() - 1;  // j start from end of string
        s = s.toLowerCase();  // Handle ignore case
        while (i < j) {
            // Handle non-alphanumeric characters
            while (i < j && !Character.isLetterOrDigit(s.charAt(i))) {
                i++;
            }
            while(i < j && !Character.isLetterOrDigit(s.charAt(j))) {
                j--;
            }
            if (s.charAt(i) != s.charAt(j)) {
                return false;
            }
            i++;
            j--;
        }
        return true;
    }
}

// Test cases:
// a
// aba
// ab?!ba
// a  b a
// A 123 b 3:21a
// A man, a plan, a canal: Panama - true
// race a car - false
// racecar- true