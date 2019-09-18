# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class BST(object):
    def __init__(self, root):
        self.root = root

    def height(self, node=None, curr_ht=0):
        if not node:
            if not self.root:
                return curr_ht
            node = self.root
            curr_ht += 1
        left_ht, right_ht = curr_ht, curr_ht
        if node.left:
            left_ht = self.height(node.left, curr_ht + 1)
        if node.right:
            right_ht = self.height(node.right, curr_ht + 1)
        return max(left_ht, right_ht)


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return BST(root).height()