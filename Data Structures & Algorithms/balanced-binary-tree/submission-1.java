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
    public boolean isBalanced(TreeNode root) {
        if (root == null) return true;

        return depth(root) != -1;
    }

    static int depth(TreeNode root) {
        if(root == null) return 0;
        int left_height = depth(root.left);
        int right_height = depth(root.right);
        int max_height = 1 + Math.max(left_height, right_height);
        if((left_height == -1) || (right_height == -1) || (Math.abs(right_height - left_height) > 1)) return -1;
        else return max_height;
    }
}
