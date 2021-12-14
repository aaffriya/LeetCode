# https://leetcode.com/problems/merge-k-sorted-lists/discuss/1628465/Python-100-ms-Faster-Solution

class Solution:
    def mergeKLists(self, lists):
        
        res = []

        for node in lists:
            try:
                res.append(node.val)
                while node.next:
                    node = node.next
                    res.append(node.val)
            except: continue
        
        res.sort()
        
        class Node:
            def __init__(self, val):
                self.val = val
                self.next = None
                
        class LinkedList:
            def __init__(self, array):
                self.head = None
                if array:
                    self.head = Node(array[0])
                    temp = self.head
                    for x in array[1:]:
                        newNode = Node(x)
                        temp.next = newNode
                        temp = temp.next
                    
            def listNode(self):
                return self.head
                
        listObject = LinkedList(res)
        
        finalRes = listObject.listNode()
        
        return finalRes
    
                    
                    
                    
                    
        
