# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode()
        current = head
        
        
        while current:
            prev = dummy
            next = current.next
            
            while prev.next and prev.next.val < current.val:
                prev = prev.next
            next = current.next
            current.next = prev.next
            prev.next = current
            
            current = next
            
        return dummy.next
        