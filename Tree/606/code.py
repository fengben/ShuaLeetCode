# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if t is None:
            return ''
        if t.left or t.right:
            left = '(' + self.tree2str(t.left) + ')'
        else:
            left = ''
        if t.right:
            right = '(' + self.tree2str(t.right) + ')'
        else:
            right = ''
        return '' + str(t.val) + left + right
