# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        main_queue = []
        sub_queue = [root]

        while sub_queue:
            for_queue = []
            for i in range(len(sub_queue)):
                node = sub_queue.pop(0)
                if node.left:
                    sub_queue.append(node.left)
                if node.right:
                    sub_queue.append(node.right)
                for_queue.append(node.val)
            main_queue.append(for_queue)
        return main_queue
