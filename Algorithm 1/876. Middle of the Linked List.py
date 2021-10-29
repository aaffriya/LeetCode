# https://leetcode.com/problems/middle-of-the-linked-list/
# Day 5
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        X1 = X2 = head
        
        while X2 and X2.next:
            X2 =X2.next.next
            X1 = X1.next
        else:
            return X1
        
