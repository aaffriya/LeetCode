# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        fast = slow = ehead = head
        
        for j in range(n):
            fast = fast.next
            
        try:
            while fast.next:
                fast = fast.next
                slow = slow.next
            else:
                slow.next = slow.next.next
                return head
        except:
            return ehead.next
        
