# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, pNode):
        # write code here
        if pNode.right:    # 如果有右节点，则右节点的最左子节点就是下一个节点
            pNode = pNode.right
            while pNode.left:
                pNode = pNode.left
            return pNode
        else:   # 一直往上找，直到是父节点的左子节点
            p_parent = pNode.next
            while p_parent and p_parent.right == pNode:
                pNode = p_parent
                p_parent = pNode.next
            pNode = p_parent
            return pNode