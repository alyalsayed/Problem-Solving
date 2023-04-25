class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # Initialize an empty stack and the previous node's value to negative infinity
        stack, prev = [], -math.inf

        # Process the nodes in the stack or the root node
        while stack or root:
            # Traverse the left subtree of the current node and add the nodes to the stack
            while root:
                stack.append(root)
                root = root.left
            
            # Pop a node from the stack, check if its value is greater than the previous node's value
            # and update the previous node's value to be the current node's value
            root = stack.pop()
            if root.val <= prev:
                return False
            prev = root.val
            
            # Traverse the right subtree of the current node
            root = root.right
        
        # If all the nodes satisfy the conditions of a valid BST, return True
        return True
