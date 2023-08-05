# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        q = [[root, float('-inf'), float('inf')]]

        while q:
            for i in range(len(q)):
                node, lower, upper = q.pop(0)
                if lower >= node.val or upper <= node.val:
                    return False
                if node.left:
                    q.append([node.left, lower, node.val])
                if node.right:
                    q.append([node.right, node.val, upper])
        return True