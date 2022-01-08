#https://leetcode.com/contest/biweekly-contest-69/problems/maximum-twin-sum-of-a-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        half = []
        
        slow = fast = head
        
        while fast:
            half.append(slow.val)
            slow = slow.next
            fast = fast.next.next
            
        ans, i = 0, len(half) - 1
        
        for x in reversed(half):
            ans = max(ans, x + slow.val)
            slow = slow.next
            
        return ans

# Basic Solution

# class Solution:
#     def pairSum(self, head: Optional[ListNode]) -> int:
        
#         res = []
        
#         while head:
#             res.append(head.val)
#             head = head.next
            
#         i, j, ans = 0, len(res) - 1, 0
        
#         while i < j:
#             ans = max(ans, res[i] + res[j])
#             i += 1
#             j -= 1
            
#         return ans
