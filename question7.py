# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        

        if len(preorder) == 0:
            return None

        new_tree = TreeNode(preorder[0])

        # 在中序遍历中找根节点的值
        root_index = inorder.index(preorder[0])
        new_tree.left = self.buildTree(preorder=preorder[1:(root_index+1)], inorder=inorder[:root_index])
        new_tree.right = self.buildTree(preorder=preorder[root_index+1:], inorder=inorder[root_index+1:])

        return new_tree