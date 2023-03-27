# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        In order: left, root, and right
        Pseudocode:
        1. EDGE CASE: no root value means return []
        Outer function(necessary variables, sets up the recursion, and returns the result)
        Inner function(current node processed, performs the recursion, accepts variables to update the state of the algorithm)
        2. Inside the helper function:
            Recursively call left child, if it exists, then add it to the list. 
            Add the current node value
            Recursively call the right child
        3. Come out of the helper function after recursion is performed
        4. Call the helper function with the outer function's root value
        5. return result
        I AM ALLOWED TO HAVE AS MANY ARGUMENTS INSIDE HELPER FUNCTION AS LONG AS I CALL IT IN THE OUTER FUNCTION. THOSE PARAMETERS SHOULD BE INITIALIZED FOR OUTER FUNCTION AS WELL
        TC: O(n) we traverse all the nodes exactly once
        SC: O(n) for recursion stack
        Maximum number of function calls on the call stack at any point in time is equal to the height of the binary tree, which is O(n) in the worst case for an unbalanced tree.
        """
        output = []
        if not root:
            return output
        def dfs(node, output):
            if not node:
                return
            if node.left:
                dfs(node.left, output)
            output.append(node.val)
            if node.right:
                dfs(node.right,output)
        dfs(root, output)
        return output
            
        
        
        