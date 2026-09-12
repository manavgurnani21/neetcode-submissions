# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.max_diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            else:
                leftHeight = dfs(node.left)
                rightHeight = dfs(node.right)
                height_node = 1 + max(leftHeight, rightHeight)
                print("height node ", height_node)
                self.max_diameter = max(self.max_diameter, leftHeight + rightHeight)
                print("max diam ", self.max_diameter)
                return height_node
        
        dfs(root)

        return self.max_diameter