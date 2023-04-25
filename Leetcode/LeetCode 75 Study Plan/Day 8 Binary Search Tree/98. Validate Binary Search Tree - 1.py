class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # Define a recursive function to validate a BST
        def validate(node, low=-math.inf, high=math.inf):
            # Base case: if the node is None, return True
            if not node:
                return True
            # Check if the node's value is between the low and high bounds
            if node.val <= low or node.val >= high:
                return False
            
            # Recursively check if the left and right subtrees are valid BSTs
            return (validate(node.right, node.val, high) and
                   validate(node.left, low, node.val))
        
        # Call the validate function starting from the root, with the low and high bounds initialized to negative and positive infinity, respectively
        return validate(root)

