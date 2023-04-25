class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # Base case: if the root is None, return True
        if not root:
            return True

        # Initialize a stack with the root node and its lower and upper bounds
        stack = [(root, -math.inf, math.inf)]
        
        # Process the nodes in the stack
        while stack:
            # Pop a node, its lower and upper bounds from the stack
            root, lower, upper = stack.pop()
            
            # If the node is None, skip it and continue processing the stack
            if not root:
                continue
            
            # Check if the node's value is within its lower and upper bounds
            val = root.val
            if val <= lower or val >= upper:
                return False
            
            # Add the node's right child and its updated lower and upper bounds to the stack
            stack.append((root.right, val, upper))
            
            # Add the node's left child and its updated lower and upper bounds to the stack
            stack.append((root.left, lower, val))
        
        # If all the nodes satisfy the conditions of a valid BST, return True
        return True
