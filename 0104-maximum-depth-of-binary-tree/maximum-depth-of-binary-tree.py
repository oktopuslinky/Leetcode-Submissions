# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root is None:
            return 0
        max_len = 0
        stack = [(root, 0)]
        while stack:
            node, depth = stack.pop()
            if node.left is not None:
                stack.append((node.left, depth+1))
            else:
                max_len = max(max_len, depth+1)

            if node.right is not None:
                stack.append((node.right, depth+1))
            else:
                max_len = max(max_len, depth+1)
        
        return max_len