# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Traverse the tree starting from the root node
        while root:
            # If both p and q are smaller than the current node's value, move to the left child
            if p.val < root.val and q.val < root.val:
                root = root.left
            # If both p and q are greater than the current node's value, move to the right child
            elif p.val > root.val and q.val > root.val:
                root = root.right
            # If the current node's value lies between p and q, or equal to p or q, then we have found the LCA
            else:
                return root