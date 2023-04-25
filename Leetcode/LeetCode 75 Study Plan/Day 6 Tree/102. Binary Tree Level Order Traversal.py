# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # If the root is None, return an empty list
        if not root:
            return []
        
        # Initialize a queue to hold the nodes to be processed and a result list
        queue, result = [root], []
        
        # While the queue is not empty
        while queue:
            # Get the number of nodes in the current level
            level_size = len(queue)
            # Initialize a list to hold the values of the nodes in the current level
            level_values = []
            
            # Process all the nodes in the current level
            for i in range(level_size):
                # Dequeue a node from the queue
                node = queue.pop(0)
                # Add the value of the node to the level_values list
                level_values.append(node.val)
                # Enqueue the left and right children of the node if they exist
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Add the level_values list to the result list
            result.append(level_values)
        
        # Return the result list representing the level order traversal of the binary tree
        return result