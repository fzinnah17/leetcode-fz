# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
        def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
            def dfs(node):  #get LCA
                if not node: return None
                if node.val in [startValue, destValue]:
                    return node
                left = dfs(node.left)
                right = dfs(node.right)
                if left and right:
                    return node
                return left or right

            root = dfs(root)
            temp, path = [], []

            def getPath(src,dst):
                if not src:
                    return
                if src.val == dst:
                    temp.append(path[:])
                    return
                path.append("L")
                getPath(src.left,dst)
                path.pop()
                path.append("R")
                getPath(src.right,dst)
                path.pop()

            getPath(root,startValue)
            getPath(root,destValue)

            return len(temp[0]) * "U" + "".join(temp[1])