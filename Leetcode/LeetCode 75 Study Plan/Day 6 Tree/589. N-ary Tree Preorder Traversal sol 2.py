"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    
    # Define the preorder method to traverse the n-ary tree in a preorder manner
    def preorder(self, root: 'Node') -> List[int]:
        # If the root node is None, return an empty list
        if not root:
            return []
        
        # Initialize the result list with the value of the root node
        result = [root.val]
        
        # Iterate over the children of the root node
        for child in root.children:
            # Recursively call the preorder method on each child and concatenate the results to the result list
            result.extend(self.preorder(child))
        
        # Return the result list representing the preorder traversal of the n-ary tree
        return result