# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None: return True
        if p == None or q == None: return False
        return q.val == p.val and self.isSameTree(p.left,q.left) and self.isSameTree(q.right,p.right)

