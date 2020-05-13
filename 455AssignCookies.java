// First sort the array, then start from the back of the arrays and
// assign cookies only if the current cookie can feed the children. 
// If not, save the cookie then move on
class Solution {
    public int findContentChildren(int[] g, int[] s) {
        Arrays.sort(g);
        Arrays.sort(s);
        int i = s.length - 1;  // pointer to cookies
        int j = g.length - 1;  // pointer to greedy children
        int feedCount = 0;
        while (i >= 0 && j >= 0) {
            if (g[j] > s[i]) {  // current child has bigger appetite than cookie
                j--; // move on to next child
            } else {  // current cookie can feed the child
                i--; // consume this cookie and move on to next cookie and child
                j--;
                feedCount++;
            }
        }
        return feedCount;
    }
}

// Test cases:
// g=[1,2,3], s=[3] - cannot give same cookie to more than one children
// g=[1,2], s=[1,2,3] - can feed all children
// g=[1,2], s=[3] - can only feed one child
// g=[10,9,8,7], s=[5,6,7,8] - feed 2 of the children with smallest appetite
// g=[], s=[]
// g=[1], s=[]
// g=[], s=[1]
// g=[3], s=[1,1,1] - each child has at most one cookie