# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # Basecase: Check for an empty input list. If it is empty, return None (an empty BST)
        if not nums:
            return None

        # Recursively: Get the index of the root node from the list (this will be the element at the center of the input list)
        mid = len(nums) // 2
        root = TreeNode(nums[mid])

        # Recursively: Build the left and right subtrees of the tree by recursively calling the function on each remaining half of the input list
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])

        # Return the root of the tree
        return root
        