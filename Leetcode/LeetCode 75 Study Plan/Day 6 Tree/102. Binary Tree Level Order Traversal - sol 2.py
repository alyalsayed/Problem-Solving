# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
     def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # Initialize a dictionary to hold the nodes at each level of the tree
        levels = {}
        
        # Define a helper function to traverse the tree in a level order manner
        def traverse(node, level):
            if not node:
                return
            
            # If the current level is not in the levels dictionary, add it
            if level not in levels:
                levels[level] = []
            
            # Add the value of the node to the list of nodes at the current level
            levels[level].append(node.val)
            
            # Recursively traverse the left and right subtrees with the next level
            traverse(node.left, level+1)
            traverse(node.right, level+1)
        
        # Traverse the binary tree starting from the root node at level 0
        traverse(root, 0)
        
        # Return the values of the nodes at each level as a list of lists
        return list(levels.values())