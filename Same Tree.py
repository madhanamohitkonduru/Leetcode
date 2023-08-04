#MY Solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (p and not q) or (q and not p):
            return False
        elif not p and not q:
            return True

        p_queue = [p]
        q_queue = [q]

        while p_queue or q_queue:
            for i in range(len(p_queue)):
                p_pop, q_pop = p_queue.pop(0), q_queue.pop(0)
                if p_pop.val != q_pop.val:
                    return False
                if p_pop.left and q_pop.left:
                    p_queue.append(p_pop.left)
                    q_queue.append(q_pop.left)
                elif (not p_pop.left and q_pop.left) or (p_pop.left and not q_pop.left):
                    return False

                if p_pop.right and q_pop.right:
                    p_queue.append(p_pop.right)
                    q_queue.append(q_pop.right)
                elif (not p_pop.right and q_pop.right) or (p_pop.right and not q_pop.right):
                    return False

        return True

#Opt Sol
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False
