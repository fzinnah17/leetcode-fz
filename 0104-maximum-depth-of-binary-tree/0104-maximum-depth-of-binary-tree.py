# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        #always to remember if we are hitting going deeper in nodes that means we have to implement dfs. [Either iterative/recursive DFS]
        #also 'preorder' is best to use because after checking root, I am checking the left side nodes first to see how deep it is, if not then I return back to root and check right nodes. 
        
        #plan:
        #1. check the root node depth, then remove it if left node is there and right node is there
        #2. check left side and go as deep node as possible and repeat step 1 by making left node as root, keep track of the node depth
        #3. return back to root
        #4. check right side and go as deep node as possible and repeat step 1 by making left node as root, keep track of node depth
        #5. compare both depths and return the output with max
        
        
        #iterative dfs uses stack[it has list] and preorder
        #What about removing items from the Stack? For this, we first of all need to check that the Stack isn’t empty as you can’t remove items from an empty Stack right? If the stack is empty then we can simply return none so that we do actually return something, but if it is not empty then we can remove the final item and return it. Since we are using Python’s inbuilt list class, we can use the .pop() method
        
        stack = [[root, 1]] #prevent edge case
        output = 0
        
        while stack:
            currNode, currDepth = stack.pop()
            if currNode:
                output = max(output, currDepth)
                stack.append([currNode.left, currDepth+1])
                stack.append([currNode.right, currDepth+1])
        return output
                
        
        
        
        
        