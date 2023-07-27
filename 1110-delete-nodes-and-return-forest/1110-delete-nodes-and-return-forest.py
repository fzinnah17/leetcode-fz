# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def delNodes(self, root, to_delete):
        """
        Pseudocode:
        1. Variables: Output = [], to_delete = set([to_delete])
        2. Helper function(currNode, to_delete, stayasParent):
            Edge case:
            if not node:
                return None
            if node.val not in to_delete set:
                Helper function on left tree(currNode.left, to_delete, stayasParent = True)
                Helper function on right tree(currNode.right, to_delete, stayasParent = True)
                as long as stayasParent = True as there's nothing to remove:
                    add the values in the output list as it will not be removed
                return the node
            
            else:
                remove the node.val by referncing to None
        3. Helper function(root, to_delete, stayasParent = False)
        4. return output
        TC: O(n) SC: O(n)
        """
        output = []
        to_delete = set(to_delete)
        def helper(currNode, to_delete, stayasParent):
            if not currNode:
                return None
            if currNode.val not in to_delete:
                currNode.left = helper(currNode.left, to_delete, stayasParent = True)
                currNode.right = helper(currNode.right, to_delete, stayasParent = True)
                if not stayasParent:
                    output.append(currNode) #adding the values
                return currNode
            else:
                currNode.left = helper(currNode.left, to_delete, stayasParent = False)
                currNode.right = helper(currNode.right, to_delete, stayasParent = False)
                return None        
        helper(root, to_delete, stayasParent = False)
        return output