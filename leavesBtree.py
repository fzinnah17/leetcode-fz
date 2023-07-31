"""

Given the root of a binary tree, collect a tree's nodes as if you were doing this:

Collect all the leaf nodes.
Remove all the leaf nodes.
Repeat until the tree is empty.

Input = 
     1
    / \
   2   3
  / \   \
 4   5   6
    / \   \
   7   8   9
      / \   \
     10 11   12

Output = [[10, 11, 12], [7, 8, 9], [4, 5, 6], [2, 3], [1]]

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Pseudocode:
        output = []
        helper(node, currLeaves):
            if node doesn't exist:
                return None
            if node is a leaf node:
               currLeaves.append(node.val)
                remove it from the tree so that we can have a new tree without those leaf nodes return None
            #in all cases perform DFS on both sides
            node.left = helper(node.left, currLeaves)
            node.right = helper(node.right, currLeaves)
            return node #update the binary tree structure after removing the nodes
        while root: #loop is used to find and remove leaves from the binary tree one level at a time until there are no more leaves left in the tree. The loop is executed as long as the root variable is not None, there are still nodes in the tree to be processed.
            currLeaves = []
            update the root value from the helper function root = helper(root,currL)
            output.append(currLeaves)
        return output
        TC: O(N) N is the number of nodes in the binary tree. This is because we visit each node once during the tree traversal to find and remove the leaves.
        SC: O(N) because output stores the leaves at each level of the tree, and its size can be at most N (in the case of a balanced binary tree). Additionally, we use the currLeaves to temporarily store the leaves at each level, but its size is bounded by the number of leaves, which is also at most N for a balanced binary tree.
            """
        output = []
        def helper(node, currLeaves):
            if not node:
                return None
            if not node.left and not node.right:
                currLeaves.append(node.val)
                return None
            node.left = helper(node.left, currLeaves)
            node.right = helper(node.right, currLeaves)
            return node

        while root: #until the tree is empty we will keep on calling the helper function
            currLeaves = []
            root = helper(root, currLeaves)
            output.append(currLeaves)
        return output
