# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def addTwoNumbers(self, l1, l2 ):
        for i in l1:
            print(i)


print(Solution.addTwoNumbers(Solution,[2,4,3],[5,6,4])," --> ", 807)