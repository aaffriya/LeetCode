# https://leetcode.com/contest/weekly-contest-270/problems/delete-the-middle-node-of-a-linked-list/
class Solution(object):
  def deleteMiddle(self, head):
    
    try:    
      slow, fast = head, head.next.next
    
      while fast and fast.next:
        slow, fast = slow.next, fast.next.next

      slow.next = slow.next.next

      return head
  
    except:
      head = None
      
      return head
