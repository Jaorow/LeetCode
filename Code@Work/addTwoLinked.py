from typing import Optional


# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1 = []
        while l1 != None:
            stack1.append(l1.val)
            l1 = l1.next
        
        stack2 = []
        while l2 != None:
            stack2.append(l2.val)
            l2 = l2.next
        print(stack1)

#tests for addTwoNumbers function

tests = {'1': 708}
print(f"\n GOT \t<---->\t WANT\n")
for test in tests:
    print(f" {Solution.addTwoNumbers(Solution,l1 = [2,4,3], l2 = [5,6,4])} \t<---->\t {tests[test]}")