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
class Solution {
    public TreeNode invertTree(TreeNode root) {
        if (root != null) {
            root.left = invertTree(root.left);
            root.right = invertTree(root.right);
            TreeNode temp = root.left;
            root.left = root.right;
            root.right = temp;
        }
        return root;
    }
}

// Iterative solution, use a Stack to simulate the recursive
// process, whether we invert first and recurse or recurse first
// then invert doesn't matter
// Usually better if the tree is tall, prevent stack overflow
class Solution {
    public TreeNode invertTree(TreeNode root) {
        if (root != null) {
            Stack<TreeNode> s = new Stack<>();
            s.push(root);
            while (!s.isEmpty()) {
                TreeNode curr = s.pop();
                TreeNode temp = curr.left;
                curr.left = curr.right;
                curr.right = temp;
                if (curr.left != null) {
                    s.push(curr.left);
                }
                if (curr.right != null) {
                    s.push(curr.right);
                }
            }
        }
        return root;
    }
}