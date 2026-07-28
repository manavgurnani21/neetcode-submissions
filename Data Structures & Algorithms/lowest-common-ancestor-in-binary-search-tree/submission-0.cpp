/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
public:
    TreeNode* minNode;
    TreeNode* maxNode;

    TreeNode* recursiveChecker(TreeNode* node) {
        if(node->val >= minNode->val && node->val <= maxNode->val) { // between min and max so it's an ancestor (base case)
            return node;
        }
        if(node->val > maxNode->val) { // overshot the max value, need to look in smaller tree
            return recursiveChecker(node->left);
        }
        return recursiveChecker(node->right); // in our problem, we only arrive here when we've undershot the min value, so need to look in the larger tree
    }

    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if(p->val > q->val) {
            minNode = q;
            maxNode = p;
        }
        else {
            minNode = p;
            maxNode = q;
        }

        return recursiveChecker(root);
    }
};