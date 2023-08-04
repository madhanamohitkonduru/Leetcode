#opt sol
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not t:
            return True
        if not s:
            return False

        if self.sameTree(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def sameTree(self, s, t):
        if not s and not t:
            return True
        if s and t and s.val == t.val:
            return self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right)
        return False


#My Sol
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def sameTree(self, s, t):
        if not s and not t:
            return True
        if s and t and s.val == t.val:
            return self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right)
        return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        elif root and not subRoot:
            return True
        elif not root and subRoot:
            return False

        q = [root]

        while q:
            for i in range(len(q)):
                node = q.pop(0)

                if node.val == subRoot.val:
                    if self.sameTree(node, subRoot):
                        return True

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return False



#my partially right sol
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        q = [root]
        print(root)

        while q:
            for i in range(len(q)):
                flag = 0
                node = q.pop(0)

                if node and subRoot:
                    if node.val == subRoot.val:
                        p_queue = [node]
                        q_queue = [subRoot]

                        while p_queue or q_queue:
                            for i in range(len(p_queue)):
                                p_pop, q_pop = p_queue.pop(0), q_queue.pop(0)

                                if p_pop.left and q_pop.left:
                                    p_queue.append(p_pop.left)
                                    q_queue.append(q_pop.left)
                                elif (not p_pop.left and q_pop.left) or (p_pop.left and not q_pop.left):
                                    flag = 1
                                    break

                                if p_pop.right and q_pop.right:
                                    p_queue.append(p_pop.right)
                                    q_queue.append(q_pop.right)
                                elif (not p_pop.right and q_pop.right) or (p_pop.right and not q_pop.right):
                                    flag = 1
                                    break
                            if flag == 1:
                                break
                        if flag == 0:
                            return True

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return False