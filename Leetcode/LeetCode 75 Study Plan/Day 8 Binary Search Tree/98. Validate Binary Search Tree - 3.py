# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # Define a recursive function to perform inorder traversal of the binary tree
        def inorder(root):
            # Base case: if the node is None, return True
            if not root:
                return True
            
            # Recursively visit the left subtree
            if not inorder(root.left):
                return False
            
            # Check if the current node's value is greater than the previous node's value
            if root.val <= self.prev:
                return False
            
            # Update the previous node's value to be the current node's value
            self.prev = root.val
            
            # Recursively visit the right subtree
            return inorder(root.right)
        
        # Initialize the previous node's value to negative infinity
        self.prev = -math.inf
        
        # Call the inorder function starting from the root
        return inorder(root)