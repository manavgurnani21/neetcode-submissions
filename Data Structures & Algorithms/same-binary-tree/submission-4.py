# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if q is None and p is None:
            return True

        def different(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            return imbalanced(p, q) or ((p and q) and (p.val != q.val))

        def imbalanced(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            return (p is None and q is not None) or (q is None and p is not None)

        # None-type cases
        if imbalanced(p, q):
            return False

        p_queue = [p]
        q_queue = [q]

        if different(p, q):
            return False

        while len(p_queue) > 0 and len(q_queue) > 0:
            p_current = p_queue.pop()
            q_current = q_queue.pop()
            p_l_c = p_current.left
            p_r_c = p_current.right
            q_l_c = q_current.left
            q_r_c = q_current.right

            if different(p_l_c, q_l_c) or different(p_r_c, q_r_c):
                return False

            if p_l_c:
                p_queue.append(p_l_c)
            if p_r_c:
                p_queue.append(p_r_c)
            if q_l_c:
                q_queue.append(q_l_c)
            if q_r_c:
                q_queue.append(q_r_c)
        
        return True
        

