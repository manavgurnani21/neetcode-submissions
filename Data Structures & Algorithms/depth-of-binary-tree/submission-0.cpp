/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    int dive(TreeNode* node, int depth) {
        if(!node) {
            return depth - 1;
        }
        return max(dive(node->left, depth + 1), dive(node->right, depth + 1));
    }

    int maxDepth(TreeNode* root) {
        if (!root) {
            return 0;
        }
        return dive(root, 1);
    }
};
