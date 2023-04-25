"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    
      def preorder(self, root: 'Node') -> List[int]:
        # If the root node is None, return an empty list
        if not root:
            return []
        
        # Initialize a stack to keep track of the nodes to be visited and a result list
        stack, result = [root], []
        
        # Iterate over the stack until it becomes empty
        while stack:
            # Pop a node from the stack
            node = stack.pop()
            # Add the value of the node to the result list
            result.append(node.val)
            # Add the children of the node to the stack in reverse order
            stack.extend(node.children[::-1])
        
        # Return the result list representing the preorder traversal of the n-ary tree
        return result