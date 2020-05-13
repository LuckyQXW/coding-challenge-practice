/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
 
// Between O(nlogn) best case and O(n^2) worst case
class Solution {
    public int pathSum(TreeNode root, int sum) {
        if (root == null) {
            return 0;
        }
        int self = helper(root, sum);
        int left = pathSum(root.left, sum);  // Defer to next recursive call
        int right = pathSum(root.right, sum);  // Defer to next recursive call
        return self + left + right;
    }
    
    private int helper(TreeNode root, int sum) {
        if (root == null) {
            return 0;
        } else {
            int l = helper(root.left, sum - root.val);
            int r = helper(root.right, sum - root.val);
            // Need to check this, otherwise it doesn't count all the
            // paths add up to sum. Can't return early because we will
            // miss the paths that possibly goes deeper in the tree
            int reachedSum = sum == root.val ? 1 : 0;
            return l + r + reachedSum;
        }
    }
}

// Use a hashtable, O(n) space and O(n) solution
class Solution {
    public int pathSum(TreeNode root, int sum) {
        Map<Integer, Integer> m = new HashMap<>();
        return helper(root, 0, sum, m);
    }
    
    private int helper(TreeNode root, int acc, int sum, Map<Integer, Integer> m) {
        if (root == null) {
            return 0;
        }
        acc += root.val;
        int count = 0;
        // Current 
        if (acc == sum) {
            count++;
        }
        // Can remove some nodes from the top and get to 0, so
        // add that to the count
        if (m.containsKey(acc - sum)) {
            count += m.get(acc - sum);
        }
        // Add 1 to signify the possibility of having a sum,
        // if any subsequent accumulative sum can subtract
        // this and get to 0. If there is already a sum somewhere
        // keep accumulating since there can be multiple options
        if (!m.containsKey(acc)) {
            m.put(acc, 0);
        }
        m.put(acc, m.get(acc) + 1);
        
        int l = helper(root.left, acc, sum, m);
        int r = helper(root.right, acc, sum, m);
        
        // Remove the current accumulation from the map because
        // we are done processing the current node
        // Similar to unchoose in backtracking
        m.put(acc, m.get(acc) - 1);
        return count + l + r;
    }
}