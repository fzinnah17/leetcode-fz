# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def delNodes(self, root, to_delete):
        """
        TC: O(n) because we are traversing the entire binary tree once using a recursive depth-first search approach. Each node in the tree is visited once, and the time complexity depends on the number of nodes in the tree, which is n.
        SC: O(n)
        """
        output = []
        deleteSet = set(to_delete)
        def helper(node, stayasParent):
            if not node:
                return None
            if node.val in deleteSet:
                node.left = helper(node.left,stayasParent = False)
                node.right = helper(node.right,stayasParent = False)
                return None
            else:
                node.left = helper(node.left,stayasParent = True)
                node.right = helper(node.right,stayasParent = True)
            if not stayasParent: #stayasParent = True
                output.append(node)
            return node
        helper(root, stayasParent = False)
        return output
                
        
        
                
                
                
                
                
                
        